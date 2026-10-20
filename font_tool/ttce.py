#!/usr/bin/env python3
"""Telltale .ttarch2 (TTCE container) reader/repacker.

Reverse engineered from Lucas Saragosa's TelltaleToolLib
(TTArchive2.cpp / DataStream/DataStream.cpp / Blowfish.cpp / Compression.cpp).

TTCE container:
    u32 type = 0x54544345 ("ECTT", i.e. TTCE reversed)
    u32 windowSize (normally 0x10000)
    u32 numPages
    u64 pageOffsets[numPages + 1]        (relative to container start)
    each page: Blowfish(modified/"new" variant, game key) -> raw deflate -> windowSize bytes

Inner archive (TTA2/TTA3/TTA4):
    u32 version magic  (1414807858/59/60)
    [u32 unknown]      TTA2/TTA3 only
    u32 nameTableSize
    u32 numResources
    entries: u64 crc64(lowercase name), u64 offset, [u32 skip], u32 size, u32 skip, u16 page, u16 nameoff
    name table  (nameTableSize bytes)
    resource blocks (offset is relative to the end of the name table)
"""
import struct
import zlib
import re
import sys
import os

MAGIC_TTCE = 0x54544345            # "ECTT"
MAGIC_TTA4 = 1414807860
MAGIC_TTA3 = 1414807859
MAGIC_TTA2 = 1414807858
M32 = 0xffffffff


# ------------------------------------------------------------------ Blowfish
def load_constants(path):
    src = open(path, 'r', errors='ignore').read()

    def grab(name):
        m = re.search(r'static unsigned int %s\[\]\s*=\s*\{(.*?)\};' % name, src, re.S)
        body = re.sub(r'//.*', '', m.group(1))
        return [int(x, 16) for x in re.findall(r'0x[0-9a-fA-F]+', body)]

    bfp = grab('bfp')
    ks = [grab('ks%d' % i) for i in range(4)]
    assert len(bfp) == 18 and all(len(k) == 256 for k in ks)
    return bfp, ks


def load_game_key(path, game_name='Tales from the Borderlands'):
    """Pull the raw Blowfish key for a game out of TelltaleToolLib's Blowfish.h."""
    for line in open(path, 'r', errors='ignore'):
        if game_name in line and '\\x' in line:
            strs = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
            return bytes(int(x, 16) for x in re.findall(r'\\x([0-9a-fA-F]{2})', strs[-1]))
    raise KeyError(game_name)


def bs(num):
    return (((num & 0xff000000) >> 24) | ((num & 0x00ff0000) >> 8) |
            ((num & 0x0000ff00) << 8) | ((num & 0x000000ff) << 24))


class Blowfish:
    """modified=True -> the 'version 7' variant used by newer games."""

    def __init__(self, key, bfp, ks, modified=True):
        if isinstance(key, str):
            key = key.encode('latin-1')
        self.S = [list(k) for k in ks]
        self.P = list(bfp)
        self.modified = modified
        if modified:
            self.S[0][118] = bs(self.S[0][118])
        kb = len(key)
        j = 0
        for i in range(18):
            data = 0
            for _ in range(4):
                data = ((data << 8) | key[j]) & M32
                j = (j + 1) % kb
            self.P[i] ^= data
        dl = dr = 0
        for i in range(0, 18, 2):
            dl, dr = self.beo(dl, dr)
            self.P[i], self.P[i + 1] = dl, dr
        for i in range(4):
            for j in range(0, 256, 2):
                dl, dr = self.beo(dl, dr)
                self.S[i][j], self.S[i][j + 1] = dl, dr

    def bf(self, x):
        y = (self.S[0][(x >> 24) & 0xff] + self.S[1][(x >> 16) & 0xff]) & M32
        y = (y ^ self.S[2][(x >> 8) & 0xff]) & M32
        y = (y + self.S[3][x & 0xff]) & M32
        return y

    def beo(self, Xl, Xr):
        P = self.P
        for i in range(16):
            Xl ^= P[i]
            Xr = self.bf(Xl) ^ Xr
            Xl, Xr = Xr, Xl
        Xl, Xr = Xr, Xl
        return (Xl ^ P[17]) & M32, (Xr ^ P[16]) & M32

    def bdn(self, Xl, Xr):
        P = self.P
        for i in range(17, 1, -1):
            t = {2: P[4], 3: P[1], 4: P[2]}.get(i, P[i]) if self.modified else P[i]
            Xl ^= t
            Xr = self.bf(Xl) ^ Xr
            Xl, Xr = Xr, Xl
        Xl, Xr = Xr, Xl
        if self.modified:
            return (Xl ^ P[0]) & M32, (Xr ^ P[3]) & M32
        return (Xl ^ P[0]) & M32, (Xr ^ P[1]) & M32

    def _crypt(self, data, fn):
        buf = bytearray(data)
        n = len(buf) // 8
        v = struct.unpack('<%dI' % (n * 2), bytes(buf[:n * 8]))
        out = [0] * (n * 2)
        for i in range(n):
            a, b = fn(v[2 * i], v[2 * i + 1])
            out[2 * i], out[2 * i + 1] = a, b
        return struct.pack('<%dI' % (n * 2), *out) + bytes(buf[n * 8:])

    def decrypt(self, data):
        return self._crypt(data, self.bdn)

    def encrypt(self, data):
        return self._crypt(data, self.beo)


# ------------------------------------------------------------------ container
class TTContainer:
    def __init__(self, path, const_path=None, key=None, game='Tales from the Borderlands'):
        self.f = open(path, 'rb')
        const_path = const_path or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TTL_Blowfish.h')
        self.bfp, self.ks = load_constants(const_path)
        self.key = key if key is not None else load_game_key(const_path, game)
        self._cache = {}
        self._order = []
        f = self.f
        t, win, pages = struct.unpack('<III', f.read(12))
        if t != MAGIC_TTCE:
            raise ValueError('not a TTCE container: 0x%X' % t)
        self.window, self.num_pages = win, pages
        self.page_off = struct.unpack('<%dQ' % (pages + 1), f.read((pages + 1) * 8))
        self.header_end = f.tell()
        self._bc = None

    def page(self, i):
        if i in self._cache:
            return self._cache[i]
        o0, o1 = self.page_off[i], self.page_off[i + 1]
        self.f.seek(o0)
        raw = self.f.read(o1 - o0)
        if self._bc is None:
            self._bc = Blowfish(self.key, self.bfp, self.ks, modified=True)
        raw = self._bc.decrypt(raw)
        out = zlib.decompressobj(-15).decompress(raw)
        self._cache[i] = out
        self._order.append(i)
        if len(self._order) > 64:
            self._cache.pop(self._order.pop(0), None)
        return out

    def read(self, offset, size):
        out = bytearray()
        while size > 0:
            p = offset // self.window
            within = offset - p * self.window
            chunk = self.page(p)[within:within + size]
            if not chunk:
                break
            out += chunk
            size -= len(chunk)
            offset += len(chunk)
        return bytes(out)

    def dump(self, out_path, log=None):
        with open(out_path, 'wb') as o:
            for i in range(self.num_pages):
                o.write(self.page(i))
                if log and (i % 250 == 0 or i == self.num_pages - 1):
                    log('  page %d/%d' % (i + 1, self.num_pages))
        return self.num_pages * self.window


# ------------------------------------------------------------------ inner archive
class TTARCH2:
    def __init__(self, c, base=0):
        self.c = c
        self.base = base
        head = c.read(base, 24)
        ver, = struct.unpack_from('<I', head, 0)
        p = 4
        if ver in (MAGIC_TTA2, MAGIC_TTA3):
            self.version = 0 if ver == MAGIC_TTA2 else 1
            p += 4
        elif ver == MAGIC_TTA4:
            self.version = 2
        else:
            raise ValueError('bad TTA magic 0x%X' % ver)
        self.namesize, nres = struct.unpack_from('<II', head, p)
        p += 8
        self.count = nres
        self.entry_size = 32 if self.version < 1 else 28
        raw = c.read(base + p, nres * self.entry_size)
        self.entries = []
        q = 0
        for _ in range(nres):
            crc, off = struct.unpack_from('<QQ', raw, q)
            q += 16
            if self.version < 1:
                q += 4
            size, skip = struct.unpack_from('<II', raw, q)
            q += 8
            page, poff = struct.unpack_from('<HH', raw, q)
            q += 4
            self.entries.append({'crc': crc, 'offset': off, 'size': size,
                                 'page': page, 'nameoff': poff})
        self.names_pos = base + p + q
        self.data_pos = self.names_pos + self.namesize

    def name(self, e):
        if 'name' not in e:
            off = self.names_pos + e['page'] * 0x10000 + e['nameoff']
            e['name'] = self.c.read(off, 256).split(b'\0')[0].decode('utf-8', 'replace')
        return e['name']

    def data(self, e):
        return self.c.read(self.data_pos + e['offset'], e['size'])


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    const = os.path.join(here, 'TTL_Blowfish.h')
    path = sys.argv[1]
    c = TTContainer(path, const)
    print('%s: pages=%d window=%d size=%d' % (os.path.basename(path), c.num_pages, c.window, c.page_off[-1]))
    a = TTARCH2(c)
    print('TTA version=%d namesize=%d resources=%d data@%d' % (a.version, a.namesize, a.count, a.data_pos))
    for i, e in enumerate(a.entries):
        print('%5d %10d  %s' % (i, e['size'], a.name(e)))


# ------------------------------------------------------------------ packing
CRC64_POLY = 0x42F0E1EBA9EA3693


def crc64_ecma(name):
    """TTG resource name hash: CRC64/ECMA-182 over the LOWERCASE name."""
    if isinstance(name, str):
        name = name.lower().encode('utf-8')
    crc = 0
    for b in name:
        crc ^= b << 56
        for _ in range(8):
            crc = ((crc << 1) ^ CRC64_POLY) & 0xFFFFFFFFFFFFFFFF if crc >> 63 else (crc << 1) & 0xFFFFFFFFFFFFFFFF
    return crc


def _ben(self, Xl, Xr):
    """Modified ('version 7') Blowfish ENCRYPT - inverse of bdn."""
    P = self.P
    for i in range(16):
        t = {1: P[3], 2: P[4], 3: P[1], 4: P[2]}.get(i, P[i])
        Xl ^= t
        Xr = self.bf(Xl) ^ Xr
        Xl, Xr = Xr, Xl
    Xl, Xr = Xr, Xl
    return (Xl ^ P[17]) & M32, (Xr ^ P[16]) & M32


Blowfish.ben = _ben
Blowfish.encrypt = lambda self, data: self._crypt(data, self.ben)


def pack_ttarch2(files, out_path, bfp, ks, key, window=0x10000, version=2, log=None, level=1):
    """files: list of (name, bytes).  Writes an encrypted+compressed .ttarch2."""
    files = sorted(files, key=lambda kv: crc64_ecma(kv[0]))
    names, datas = [], []
    for n, b in files:
        names.append(n.encode('utf-8') + b'\0')
        datas.append(b)
    ntz = sum(len(x) for x in names)
    namesize = ntz + (window - (ntz % window))
    nameblob = b''.join(names) + b'\0' * (namesize - ntz)
    header = struct.pack('<III', MAGIC_TTA4, namesize, len(files))
    entries = b''
    off = 0
    noff = 0
    for i, (n, b) in enumerate(files):
        entries += struct.pack('<QQIIHH', crc64_ecma(n), off, len(b), 0,
                               noff // 0x10000, noff % 0x10000)
        noff += len(names[i])
        off += len(b)
    payload = header + entries + nameblob + b''.join(datas)

    bc = Blowfish(key, bfp, ks, modified=True)
    pages = [payload[i:i + window] for i in range(0, len(payload), window)]
    chunks = []
    for p in pages:
        if len(p) < window:
            p = p + b'\0' * (window - len(p))
        co = zlib.compressobj(level, zlib.DEFLATED, -15)
        c = co.compress(p) + co.flush()
        chunks.append(bc.encrypt(c + b'\0' * (-len(c) % 8)) if len(c) % 8 else bc.encrypt(c))
    hdr_size = 12 + 8 * (len(pages) + 1)
    poffs = [hdr_size]
    for c in chunks:
        poffs.append(poffs[-1] + len(c))
    out = struct.pack('<III', MAGIC_TTCE, window, len(pages))
    out += struct.pack('<%dQ' % len(poffs), *poffs)
    out += b''.join(chunks)
    open(out_path, 'wb').write(out)
    if log:
        log('%s: %d files, payload %d -> archive %d bytes' % (out_path, len(files), len(payload), len(out)))
    return out


def unpack_to_dir(path, out_dir, const_path, log=print):
    import os
    c = TTContainer(path, const_path)
    a = TTARCH2(c)
    os.makedirs(out_dir, exist_ok=True)
    for e in a.entries:
        n = a.name(e)
        p = os.path.join(out_dir, n)
        os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(n) else None
        open(p, 'wb').write(a.data(e))
        log('  %10d  %s' % (e['size'], n))
    return a
