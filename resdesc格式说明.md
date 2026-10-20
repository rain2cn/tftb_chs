# Telltale `_resdesc_*.lua` 加密文件解析说明

适用于 **Tales from the Borderlands（无主之地传说）** 及同代 Telltale Tool 引擎游戏
（ttarch2 / "version7" 加密体系，ttarchext 中 gamenum ≥ 58）。

## 文件格式

```
+0x00   4 字节   magic = "\x1bLEo"          ← 明文，不加密
+0x04   N-4 字节  Blowfish(version7, ECB) 密文
```

- 密文区按 **8 字节一块**、块内两个**小端 uint32**（`xl, xr`）处理，ECB 模式、无 IV。
- 密文长度**不要求是 8 的倍数**：ttarchext 用 `datalen / 8` 取整，
  **末尾不足 8 字节的块保持明文**（例如 904 字节文件：4 魔法 + 896 密文 + 4 明文 `t)\r\n`）。
- 这也是为什么同目录 8 个文件的前 28 字节密文完全相同——那只是各文件共同的头部字段
  （`local set = {}` + `set.name = ...` 之前的公共部分）在 ECB 下产生的相同密文块。

## version7 Blowfish 与标准 Blowfish 的两处差异

1. **密钥初始化**时 `S[0][118]` 先做 32 位字节序反转（bswap），之后是标准密钥编排。
2. **轮函数中 P 数组下标互换**：
   - 加密：`i=1→P[3]`，`i=2→P[4]`，`i=3→P[1]`，`i=4→P[2]`，其余轮用 `P[i]`
   - 解密：`i=2→P[4]`，`i=3→P[1]`，`i=4→P[2]`，其余轮用 `P[i]`
   - 收尾：加密 `Xr^=P[16], Xl^=P[17]`；解密 `Xr^=P[3], Xl^=P[0]`

## 密钥

Tales from the Borderlands 专用 55 字节 Blowfish 密钥（见 `tftb_resdesc.py` 内 `KEY`，
来源：ttarchext `gamekeys` 表 / Lucas Saragosa 的 TelltaleToolLib，保留署名）。
不同游戏的密钥不同，换游戏需查 ttarchext 的游戏号表。

## 工具用法

```bash
python3 tftb_resdesc.py d 输入.lua [输出.lua]   # 解密（默认输出 *.dec.lua）
python3 tftb_resdesc.py e 输入.lua [输出.lua]   # 重新加密（改完 lua 后打包回游戏）
python3 tftb_resdesc.py a 目录                  # 批量解密目录下全部 _resdesc_*.lua
```

已验证：解密结果 100% 可打印文本；重新加密后与原文件**逐字节一致**。

## 参考实现

- ttarchext（Luigi Auriemma）：`IS_LUA3` 分支即本格式，`blowfish_ttarch.c` 是权威算法实现
- Telltale-Resdesc-Viewer / TTDS-Resdesc（Telltale-Modding-Group）：解密后的同类文件样例
- Lucas Saragosa / TelltaleToolLib：Blowfish 变体与游戏密钥表
