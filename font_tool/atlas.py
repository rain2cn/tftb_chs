#!/usr/bin/env python3
"""Decode a Telltale glyph atlas (raw BC1/BC3 block data) into a grayscale PNG (alpha plane)."""
import struct, zlib, sys


def write_png_gray(path, w, h, pix):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        raw += pix[y * w:(y + 1) * w]
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 0, 0, 0, 0))
    png += chunk(b'IDAT', zlib.compress(bytes(raw), 9))
    png += chunk(b'IEND', b'')
    open(path, 'wb').write(png)


def bc3_alpha(data, w, h, out=None):
    """Decode the BC3 alpha block of every 16-byte block into a w*h bytearray."""
    res = bytearray(w * h) if out is None else out
    bw = w // 4
    n = len(data) // 16
    for i in range(n):
        o = i * 16
        a0 = data[o]
        a1 = data[o + 1]
        bits = int.from_bytes(data[o + 2:o + 8], 'little')
        pal = [a0, a1, 0, 0, 0, 0, 0, 0]
        if a0 > a1:
            for k in range(1, 7):
                pal[1 + k] = ((7 - k) * a0 + k * a1) // 7
        else:
            for k in range(1, 5):
                pal[1 + k] = ((5 - k) * a0 + k * a1) // 5
            pal[6] = 0
            pal[7] = 255
        bx = (i % bw) * 4
        by = (i // bw) * 4
        base = by * w + bx
        for j in range(16):
            res[base + (j // 4) * w + (j % 4)] = pal[(bits >> (3 * j)) & 7]
    return res


def bc1_rgb(data, w, h):
    res = bytearray(w * h)
    bw = w // 4
    for i in range(len(data) // 16):
        o = i * 16
        c0, c1 = struct.unpack_from('<HH', data, o + 8)
        idx = int.from_bytes(data[o + 12:o + 16], 'little')
        cols = [(c0 >> 11) & 31, (c0 >> 5) & 63, c0 & 31,
                (c1 >> 11) & 31, (c1 >> 5) & 63, c1 & 31]
        if c0 > c1:
            cols += [(2 * cols[0] + cols[3]) // 3, (2 * cols[1] + cols[4]) // 3, (2 * cols[2] + cols[5]) // 3,
                     (cols[0] + 2 * cols[3]) // 3, (cols[1] + 2 * cols[4]) // 3, (cols[2] + 2 * cols[5]) // 3]
        else:
            cols += [(cols[0] + cols[3]) // 2, (cols[1] + cols[4]) // 2, (cols[2] + cols[5]) // 2, 0, 0, 0]
        bx = (i % bw) * 4
        by = (i // bw) * 4
        base = by * w + bx
        for j in range(16):
            k = (idx >> (2 * j)) & 3
            v = (cols[k * 3] * 11 + cols[k * 3 + 1] * 16 + cols[k * 3 + 2] * 5) >> 5
            res[base + (j // 4) * w + (j % 4)] = v
    return res


if __name__ == '__main__':
    path = sys.argv[1]
    d = open(path, 'rb').read()
    size = None
    for p in (24, 23, 22, 21, 20):
        if len(d) > (1 << p):
            size = 1 << p
            break
    atlas = d[len(d) - size:]
    print('atlas bytes:', len(atlas))
    for (w, h) in [(1024, 2048), (2048, 1024), (4096, 4096), (2048, 4096), (512, 4096)]:
        if w * h != len(atlas):
            continue
        a = bc3_alpha(atlas, w, h)
        write_png_gray('atlas_alpha_%dx%d.png' % (w, h), w, h, a)
        print('wrote atlas_alpha_%dx%d.png' % (w, h))
        r = bc1_rgb(atlas, w, h)
        write_png_gray('atlas_rgb_%dx%d.png' % (w, h), w, h, r)
        print('wrote atlas_rgb_%dx%d.png' % (w, h))
