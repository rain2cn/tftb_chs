#!/usr/bin/env python3
"""
tftb_resdesc.py — Telltale 引擎 _resdesc_*.lua 加密文件 解密/加密工具
====================================================================

适用游戏: Tales from the Borderlands (无主之地传说) 及同代 Telltale Tool 游戏
          (gamenum >= 58, ttarch2/version7 加密体系)

文件格式 (参考 ttarchext 的 IS_LUA3 分支):
    +0x00  magic "\x1bLEo"                    (4 字节, 明文)
    +0x04  Blowfish(version7 变体, ECB) 密文   (长度 = 文件大小 - 4)
    注意: 密文长度不要求是 8 的倍数 —— ttarchext 用 datalen/8 取整,
          末尾不足 8 字节的块保持明文不加密 (本工具行为与其一致)

version7 Blowfish 变体 (与标准 Blowfish 的两处差异):
    1. 密钥初始化时 S[0][118] 先做 32 位字节序反转 (bswap)
    2. 轮函数中 P 数组下标互换:
       加密: i=1->P[3], i=2->P[4], i=3->P[1], i=4->P[2], 其余 P[i]
       解密: i=2->P[4], i=3->P[1], i=4->P[2], 其余 P[i]
    数据按小端 uint32 对 (xl, xr) 逐 8 字节块处理 (ECB, 无 IV)

密钥: Tales from the Borderlands 55 字节 Blowfish key
      (来源: ttarchext gamekeys 表 / TelltaleToolLib, 保留署名)

用法:
    python3 tftb_resdesc.py d 输入.lua [输出.lua]     # 解密 (默认行为)
    python3 tftb_resdesc.py e 输入.lua [输出.lua]     # 加密 (重打包)
    python3 tftb_resdesc.py a 目录                    # 批量处理目录下全部 _resdesc_*.lua
"""
import base64
import json
import os
import struct
import sys
import zlib

_BF_CONSTS_B64 = (
    "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"
)
M = 0xFFFFFFFF
MAGIC = b"\x1bLEo"

# Tales from the Borderlands Blowfish key (55 bytes)
KEY = bytes([
    0x81, 0xD8, 0x9F, 0x98, 0x89, 0xDE, 0x9F, 0xA4, 0xE0, 0xD0, 0xE8, 0x95,
    0x62, 0x95, 0x95, 0xC6, 0xDB, 0x8E, 0x92, 0xE9, 0xA9, 0xD6, 0xA4, 0xD3,
    0xD8, 0x52, 0x9F, 0x85, 0x7B, 0xDB, 0xD3, 0x98, 0xC4, 0xB7, 0x9E, 0xB0,
    0xCF, 0xC7, 0xAC, 0x9D, 0xA5, 0xA4, 0xBA, 0xDB, 0xA9, 0x96, 0xB7, 0xE1,
    0xB1, 0xC4, 0x94, 0x97, 0xE3, 0xA3, 0x6F,
])


def _bswap32(n):
    return (((n & 0xff000000) >> 24) | ((n & 0x00ff0000) >> 8) |
            ((n & 0x0000ff00) << 8) | ((n & 0x000000ff) << 24)) & M


class TelltaleBlowfish7:
    """Telltale version7 变体 Blowfish (blf_key7 / blf_enc7 / blf_dec7)"""

    def __init__(self, key=KEY):
        c = json.loads(zlib.decompress(base64.b64decode("".join(_BF_CONSTS_B64))))
        self.P = list(c["bfp"])
        self.S = [list(c["ks0"]), list(c["ks1"]), list(c["ks2"]), list(c["ks3"])]
        self.S[0][118] = _bswap32(self.S[0][118])          # version7
        j = 0
        for i in range(18):                                # 标准密钥编排
            data = 0
            for _ in range(4):
                data = ((data << 8) | key[j]) & M
                j += 1
                if j >= len(key):
                    j = 0
            self.P[i] ^= data
        dl = dr = 0
        for i in range(0, 18, 2):
            dl, dr = self._encipher(dl, dr)
            self.P[i], self.P[i + 1] = dl, dr
        for i in range(4):
            for jj in range(0, 256, 2):
                dl, dr = self._encipher(dl, dr)
                self.S[i][jj], self.S[i][jj + 1] = dl, dr

    def F(self, x):
        a, b, c, d = (x >> 24) & 0xff, (x >> 16) & 0xff, (x >> 8) & 0xff, x & 0xff
        y = (self.S[0][a] + self.S[1][b]) & M
        y ^= self.S[2][c]
        return (y + self.S[3][d]) & M

    def _encipher(self, xl, xr):                            # 标准 encipher (密钥编排用)
        for i in range(16):
            xl ^= self.P[i]
            xr = self.F(xl) ^ xr
            xl, xr = xr, xl
        xl, xr = xr, xl
        xr ^= self.P[16]
        xl ^= self.P[17]
        return xl, xr

    def _round_p(self, i, encrypt):
        # version7 的 P 下标互换
        if encrypt:
            return {1: 3, 2: 4, 3: 1, 4: 2}.get(i, i)
        return {2: 4, 3: 1, 4: 2}.get(i, i)

    def _crypt_blocks(self, data, encrypt):
        out = bytearray()
        for o in range(0, (len(data) // 8) * 8, 8):        # 尾部不足 8 字节的块不处理
            xl, xr = struct.unpack("<II", data[o:o + 8])
            if encrypt:
                for i in range(16):
                    xl ^= self.P[self._round_p(i, True)]
                    xr = self.F(xl) ^ xr
                    xl, xr = xr, xl
                xl, xr = xr, xl
                xr ^= self.P[16]
                xl ^= self.P[17]
            else:
                for i in range(17, 1, -1):
                    xl ^= self.P[self._round_p(i, False)]
                    xr = self.F(xl) ^ xr
                    xl, xr = xr, xl
                xl, xr = xr, xl
                xr ^= self.P[3]
                xl ^= self.P[0]
            out += struct.pack("<II", xl, xr)
        out += data[(len(data) // 8) * 8:]
        return bytes(out)

    def decrypt(self, blob):
        assert blob[:4] == MAGIC, "不是 \\x1bLEo 格式的加密 lua"
        return self._crypt_blocks(blob[4:], False)

    def encrypt(self, plain):
        return MAGIC + self._crypt_blocks(plain, True)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    mode, src = sys.argv[1].lower(), sys.argv[2]
    bf = TelltaleBlowfish7()
    if mode == "a":                                        # 批量
        for fn in sorted(os.listdir(src)):
            if fn.startswith("_resdesc_") and fn.endswith(".lua"):
                p = os.path.join(src, fn)
                blob = open(p, "rb").read()
                if blob[:4] == MAGIC:
                    open(p + ".dec.lua", "wb").write(bf.decrypt(blob))
                    print("decrypted:", fn)
        return
    dst = sys.argv[3] if len(sys.argv) > 3 else (
        src.replace(".lua", ".dec.lua") if mode == "d" else src + ".enc.lua")
    blob = open(src, "rb").read()
    if mode == "e":
        open(dst, "wb").write(bf.encrypt(blob))
        print("encrypted ->", dst)
    else:
        open(dst, "wb").write(bf.decrypt(blob))
        print("decrypted ->", dst)


if __name__ == "__main__":
    main()
