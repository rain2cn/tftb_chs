# 《无主之地传说》(Tales from the Borderlands) 重译汉化 · 工程总览

本目录是完整的汉化工程：**输入原件 → 翻译工程 → 汉化成品 → 交付包**。
源文本一律以**游戏原版英文归档**为准重新翻译（不继承旧汉化），全书 5 章已完成。

---

## 一、目录结构（先看这里）

```
archives/
├── README.md                  ← 本文件（总说明）
│
├── 原版英文档/                 【输入】游戏原版英文归档（11 个 *_data.ttarch2）—— **唯一来源**
│
├── 翻译工程/                   【工程】脚本 + 译文源文件 + 中间产物
│   ├── tr/                       ★ 译文源文件（*_zh.py，字典形式 英文→中文）
│   ├── _work/                    ★ 中间产物：每章 BRIEF.md（翻译规范）/ selfcheck.py（验收）/ 待译清单
│   ├── ttce.py / landb.py / tftb.py     归档与文本库解析（TTCE 容器 + .landb）
│   ├── apply_one.py                     套用译文并校验（标记/中文/制表符）
│   ├── build_overlay.py                 装配「覆盖包」ttarch2（★ 构建链的装配器）
│   ├── 一键重建.py                       ★ 一条命令重建全部 8 个归档
│   ├── 找译文.py                         给一段中文/英文，告诉你改哪个 tr 文件
│   ├── makedict.py                      合并 tr/*.py 为字典
│   ├── todo_lines.py / status.py        导出待译清单 / 统计进度
│   ├── fix_quotes.py                    语法与全角引号检查
│   ├── rebake.py / run_all.py / atlas.py / gen_small_files.py / gen_credits.py   字体相关
│   ├── *.md                             各阶段说明（重译_交付说明.md 为总交付文档）
│   └── .venv/                           Python 运行环境
│
├── 汉化成品/                   【成品】8 个 ttarch2（覆盖包）—— 直接覆盖游戏 archives/ 即完成汉化
├── 汉化成品_上一版备份/         【备份】早期版本的 5 个归档
├── 交付包/                     【交付】最终打包文件（zip）及其展开目录
├── 基底归档/                   【安装素材】原汉化包的 8 个 `_resdesc_50_*.lua` + 中文字体包
│                               （★ 构建链**不依赖**它，只在安装时需要它里面的 lua / 字体）
├── 汉化包原件/                 【参考】原始汉化包（与 基底归档/ 内容相同，可留作对照）
└── _归档_早期试验/             【历史】早期字体试验、旧版输出、弃用脚本等
```

> 说明：脚本内部按相对位置互相引用（`../原版英文档`、`../汉化成品`），
> **请保持这两个目录名不变**。构建链只需要「原版英文档 + tr/」两样东西。

### 构建模型：覆盖包（不依赖任何第三方汉化包）

`一键重建.py` 对每个归档做两件事：

1. 把 `tr/*.py` 合并出的字典套用到「原版英文档」里对应的 `*_english.landb`；
2. 只把**与英文原文不同**的资源打进一个「覆盖包」ttarch2，命名 `Borderlands_pc_chs_full_<归档名>.ttarch2`。

所以产物体积很小（例如 Menu 只有 **35 KB**，各章 0.3~1.1 MB），只覆盖我们真正译过的资源；
其余资源（含**演职员表**、其它语言槽位）不会被覆盖，游戏会用自己原有的版本。

---

## 二、安装方法

把 `汉化成品/` 里的 **8 个** `Borderlands_pc_chs_full_*.ttarch2`，**和** `基底归档/` 里的 **8 个**
`_resdesc_50_*.lua`，一起放进游戏的 `archives` 目录：

```
<Steam>\steamapps\common\Tales from the Borderlands\archives\
├── Borderlands_pc_chs_full_Project.ttarch2        ├── _resdesc_50_Project.lua
├── Borderlands_pc_chs_full_Menu.ttarch2           ├── _resdesc_50_Menu.lua
├── Borderlands_pc_chs_full_Boot.ttarch2           ├── _resdesc_50_Boot.lua
├── Borderlands_pc_chs_full_Borderlands101.ttarch2 ├── _resdesc_50_Borderlands101.lua
├── …（102~105 同理）                                └── …（102~105 同理）
```

> **`_resdesc_50_*.lua` 是必需的**（Telltale 的「资源描述脚本」resdesc）：游戏靠它知道要挂载哪个 `ttarch2`。
> 少了它，游戏不会加载汉化归档。它与同名 `ttarch2` **必须放在同一目录**。
> 这些 lua 取自原汉化包（放在 `基底归档/` 与交付包里），文件名与我们的归档**完全一致**，所以**无需改动**。
>
> ⚠️ **游戏语言请设为 English（英语）**。我们的覆盖包只替换 `*_english.landb`，
> 所以游戏语言是英语时显示中文；若把游戏语言改成法语/德语等，会显示**原版**那门语言的文案。
> （原汉化包是把中文塞进了全部 5 个语言槽才做到"随便选哪门语言都是中文"。需要这个效果的话告我，我可以补上镜像。）
>
> 这些 `.lua` 不是明文脚本，而是 Telltale 的加密/编译 Lua（文件头 `1b 4c 45 6f` = `LEo`，与归档内部 `.lua` 的 `LEn` 同族），
> 无法用普通文本编辑器改；本次汉化**不需要修改它们**，原样保留即可。
>
> 字体沿用原汉化包 `Borderlands_pc_chs_fonts_v6.ttarch2`（**不要删除**，中文靠它渲染），我们不修改它。

| 归档 | 内容 |
| --- | --- |
| `Borderlands_pc_chs_full_Project.ttarch2` | 系统界面文本（拾取/交互/物品栏…） |
| `Borderlands_pc_chs_full_Menu.ttarch2` | 主菜单、设置、存档、章节名、成就、各章演职员表 |
| `Borderlands_pc_chs_full_Boot.ttarch2` | 启动/登录/保存提示 |
| `Borderlands_pc_chs_full_Borderlands101.ttarch2` | 第 1 章（24 个文本文件） |
| `Borderlands_pc_chs_full_Borderlands102.ttarch2` | 第 2 章（16 个） |
| `Borderlands_pc_chs_full_Borderlands103.ttarch2` | 第 3 章（19 个） |
| `Borderlands_pc_chs_full_Borderlands104.ttarch2` | 第 4 章（21 个） |
| `Borderlands_pc_chs_full_Borderlands105.ttarch2` | 第 5 章 · 终章（19 个） |

---

## 三、完成度与质检

| 章节 | 文本文件 | 条目数 | 含中文 | 标记差异 | 制表符差 |
| --- | --- | --- | --- | --- | --- |
| 第 1 章 101 | 24 | 42,131 | 21,754 (51.6%) | 0 | 0 |
| 第 2 章 102 | 16 | 33,460 | 17,227 (51.5%) | 0 | 0 |
| 第 3 章 103 | 19 | 23,729 | 12,396 (52.2%) | 0 | 0 |
| 第 4 章 104 | 21 | 18,401 | 9,602 (52.2%) | 0 | 0 |
| 第 5 章 105 | 19 | 12,090 | 6,376 (52.7%) | 0 | 0 |
| **合计** | **99** | **129,811** | **67,355 (51.9%)** | **0** | **0** |

- 「含中文」以外的条目是**纯标记**（`[beat]`、`{AngryA}`）与**说话人名**（`RHYS`/`FIONA`…），按约定保留英文。
- 逐文件验收（`_work/eN/selfcheck.py <tag>`）：**未覆盖 0 / 标记差异 0 / 制表符差 0**。
- 产物再与**原版英文档**逐条独立比对：标记不一致 0、制表符不一致 0。
  唯一 1 处「标记差异」为误报——原文含转义尖括号 `\<last edited by user ~HJack69~ 342 days ago\>`，译文已正确保留。

### 翻译约定

- **人名 / 地名 / 组织保留英文**：Rhys、Fiona、Sasha、Vaughn、Scooter、Jack、Athena、August、Vallory、Felix、Vasquez、
  Yvette、Gortys、Hyperion、Helios、Pandora、Dahl、Jakobs…（全套 5 章已统一，无中文译名残留）。
- **术语统一**：Vault→秘藏、Old Haven→老避风港、Hollow Point→空心镇、Hub of Heroism→英雄殿堂、
  Handsome Jack→帅杰克、Loader Bot→装载机器人、Skag→斯凯格、Crystalisk→晶兽、Eridium→镒矿、Crimson Lance→猩红长枪、Atlas→阿特拉斯。
- **一律原样保留**：`[...]` 音效/语气标签、`{...}` 表情标签、`^color:^`/`^font:^`/`^imageScale:^` 等富文本标记、`<ui_…>`、`<<id:NN>>`、开发注释。
  （例外：整行只有方括号的玩家动作/选择提示会译成中文，如 `[Draw Pistol]`→`[掏出手枪]`。）
- **标点**：`...`→`……`、`--`→`——`，中文正文用全角引号 `“ ”`。

---

## 四、如何继续维护

### 要手改某句译文 / 纠错别字：改哪个文件？

**所有译文都在 `翻译工程/tr/*.py` 里**，每个文件是一个字典（英文原文键 → 中文译文值），例如：

```python
T = {
  "Catch a Ride": "搭个便车",
  "Hello, Pandora!": "你好，Pandora！",
}
```

不用自己翻文件找——用查找工具（**先搜再改**）：

```bash
cd 翻译工程
.venv/bin/python 找译文.py "打完收工"          # 按中文片段找
.venv/bin/python 找译文.py -e "Catch a Ride"   # 按英文原文找
```

它会告诉你三件事：**① 改哪个文件第几行（含键和当前译文）→ ② 这个键被哪些归档/资源用到 → ③ 改完要跑的重建命令**。

tr 目录的文件命名规律（方便你直接猜）：

| 文件 | 内容 |
| --- | --- |
| `ep1_env02_zh.py`、`ep2_env05_zh.py` … | 第 1~5 章对白（文件名对应该章的场景资源） |
| `ep1_ui_credits_zh.py` / `ep5_ui_episode_zh.py` | 各章的演职员表 / 章节标题卡 |
| `menu_zh_a.py`、`menu_zh_b.py`、`chap_ach_zh.py` | 主菜单、章节名、成就（早期批次译法） |
| `ui_text_zh.py` | 界面文本（Project 归档） |
| `aa_menu_credits105_zh.py`、`zz_fix_tags_zh.py` | 演职员表补译 / 标记写法回正（这两个前缀决定加载优先级） |

改的时候守住这几条（都是踩过坑换来的）：

- ⚠️ **只能改「值」，绝不要改「键」**——键必须与原文**逐字节相同**（大小写、空格、标点都不能变）。
- 保留 `^color:^`/`^font:^` 这类富文本标记、`{表情}` 标签、`<ui_…>`、`<<id:…>>`、`\t` 和 `\n`——**逐 token 对齐**。
- **只能用字体图集里有的字**（清单：`_work/font_coverage.txt`）；别用 `「」〔〕『』～／™©®` 和生僻字（否则那些字显示不出来，还可能拖慢加载）。
- **超长文本块（>3000 字符，就是整页演职员表）按约定保留英文**，不要去翻译它——翻了会让场景载入从数秒变 1 分钟。
- 某句中文在 `tr/` 里搜不到？说明它属于上面这类"保留英文"的块，或者本来就是纯人名/标记（按约定不译）。

改完的标准动作：

```bash
.venv/bin/python fix_quotes.py tr/ep1_env02_zh.py      # 语法/引号自检（只查你改的文件）
.venv/bin/python 一键重建.py Borderlands101           # 重建受影响的归档（找译文.py 会告诉你是哪个）
.venv/bin/python _work/key_integrity.py               # 键完整性检查（孤儿键变多 = 改坏键了）
```

### 怎么读 `一键重建.py` 的日志

```
· ui_credits105_english.landb  ⚠ 未覆盖 37 条  （超长块保留英文 1）
```

| 字段 | 含义 | 出现了怎么办 |
| --- | --- | --- |
| `未覆盖 N 条` | 这 N 条**英文原文在 tr 字典里找不到对应译文** → 会原样保留英文 | 正常应尽量为 0。若突然变多，多半是**某个 tr 文件被覆盖/移走了**（例如重跑 `gen_credits.py` 会覆盖 `tr/aa_menu_credits105_zh.py` 里手工补的内容）。用 `_work/list_untranslated.py` 列出具体条目，再从 `_work/tr_快照_*/` 恢复 |
| `超长块保留英文 N` | 这条资源里有 N 个 >3000 字符的块按约定**不翻译**（正常） | 无需处理 |
| `标记差异 / 制表符差` | 「必须逐字一致」的东西不一致 | **必须为 0**，不为 0 就是改坏标记了 |
| `演职员表` 资源 | `ui_credits*` 整份走英文原档（见下） | 不翻译、也不进 tr 字典 |
| `❌ 有 N 个问题` + 退出码 1 | 归档**仍然会正常生成**，但这些警告值得处理 | 先按上表逐项排查 |

### 改完译文后：一键重建（推荐）

```bash
cd 翻译工程
.venv/bin/python 一键重建.py            # 重建全部 8 个归档并自动核验
```

改动流程：**编辑 `翻译工程/tr/` 下的 `*_zh.py`（字典：英文键 → 中文值）→ 跑 `一键重建.py` → 完成**。

- 它会逐个归档：把字典套用到「原版英文档」对应资源 → 以「基底归档」同名归档为基底只替换 `_english.landb` → 输出到 `汉化成品/`；
- 每次都会逐条核验 **未覆盖 / 标记差异 / 制表符差**，三项必须为 0，否则**报错并非零退出**；
- 常用参数：

```bash
.venv/bin/python 一键重建.py --list             # 列出可用归档名
.venv/bin/python 一键重建.py Menu               # 只重建某个归档（可写多个）
.venv/bin/python 一键重建.py --check            # 只核验现有产物，不重建
```

> 改了哪个归档的译文，就必须重建哪个归档；**Grid 里改过的资源要整个归档一起重建**（否则其余资源会退回汉化包旧版）。
> 例如演职员表 `ui_credits*` 属于 `Menu` 归档，章节对白属于 `Borderlands101~105`。

### 单文件级操作（需要精确定位时）

```bash
cd 翻译工程
.venv/bin/python fix_quotes.py tr/ep5_env_01_jackoffice_escape_zh.py   # 语法 + 全角引号检查
.venv/bin/python _work/e5/selfcheck.py env_01_jackoffice_escape        # 单文件验收（三项须为 0）
.venv/bin/python apply_one.py ../原版英文档/Borderlands_pc_Borderlands105_data.ttarch2 env_01_jackoffice_escape_english
.venv/bin/python build_ep.py ../基底归档/Borderlands_pc_chs_full_Borderlands105.ttarch2 ../汉化成品
.venv/bin/python status.py ../原版英文档/Borderlands_pc_Borderlands105_data.ttarch2   # 整体进度统计
```

写译文的硬规则：**键必须与原文字节一致**（大小写、空格、标点、`\n` 全都要一样）；
原文换行写 `\n`（**不是** `\\n`）；制表符写 `\t`；`^color:^`/`{表情}`/`<ui_…>` 等标记要**逐 token 对齐**（`{...}` 内不要多写空格）。

> ⚠️ **只能改「值」，绝不要改「键」。** 任何全局替换（大小写、标点、术语统一）都会连键一起改，
> 改坏之后那些条目就永远匹配不上——重建时表现为「未覆盖 N 条」警告。
> 收尾请跑键完整性检查（只读）：
> ```bash
> .venv/bin/python _work/key_integrity.py     # 列出「归档里找不到的键」；新增孤儿键 = 出事了
> .venv/bin/python _work/list_untranslated.py # 列出未覆盖条目及原文
> ```
> 出事的救火办法：从 `交付包/无主之地传说_重译汉化_v1/翻译源文件/`（上一版快照）回滚受影响的 tr 文件。

> 💡 **译文只能用字体图集里有的字。** 字体包 `Borderlands_pc_chs_fonts_v6.ttarch2` 是固定字形集（3375 个码点），
> 用到图集外的字会导致**场景加载变慢 / UI 卡顿**，且那些字显示为空白。
> 清单见 `_work/font_coverage.txt`（由 `_work/font_cover.py` 导出）；体检用 `_work/missing_glyph.py`、
> `_work/glyph_report.py`（生成 `_work/缺字修复建议.md`）。**避免 `「」〔〕『』～／™©®` 与生僻字。**

新增章节的规范模板：复制 `_work/e5/` 为新目录，把 `selfcheck.py` 里的归档名改成目标章，并按 `BRIEF.md` 派发翻译。

---

## 五、版本

- 2026-10-14（构建链重构）：**构建链不再依赖任何第三方汉化包/基底归档** —— 只从「原版英文档 + tr/」出发，
  由 `build_overlay.py` 装配「只含译过资源」的覆盖包；归档体积大幅缩小（Menu 304 KB → **35 KB**、101 5.9 MB → **1.1 MB**），
  已逐归档核对：**覆盖资源的字节与旧构建完全一致**（译文没变，只是打包方式变了）。
  同时弃用 `build_ep.py` / `build_archive.py` 及一批一次性诊断脚本（移到 `_归档_早期试验/弃用脚本_20261014/`）。
  ⚠️ 新增注意：覆盖包只替换英语槽，**游戏语言需设为 English**。
- 2026-10-14：**演职员表整份不翻译**（`ui_credits*` 直接逐字节沿用英文原档，条目已从 tr 清出），
  新增流水线规则 `SKIP_AS_EN`；剧集名归拢到 `tr/episode_titles_zh.py`；全部归档重建通过。
- 2026-10-13：**修复载入卡顿（元凶：超长演职员表块被翻成中文）** —— `ui_credits*` 的整页演职员表原本是
  一条约 3.4 万字符的字符串，翻成中文后成为 2.8 万字的单条 CJK 字符串，引擎排版 O(n²) 导致切场景载入 1 分钟。
  现由流水线自动对 >3000 字符的块保留英文（`apply_one.py` 的 `LONG_KEEP`），全库 11 处巨块已还原；
  另按用户要求把显示文本里的 `HYPERION` 统一为 `Hyperion`（只改值、不碰键）。
- 2026-10-12：第 5 章完成；**全 5 章统一人名译法**（回正 101~105 共约 430 处中文译名残留），重建全部归档，输出交付包。
- 2026-10-12（追加）：**Menu 归档补齐** —— 修复 `ui_credits105` 整块错位（用 `gen_credits.py` 词表重建）、
  恢复 `ui_credits104` 被误替换成「帅哥杰克」的 56 处人名（`Xu Zhiyong` 等本地化团队成员），
  统一 `ui_credits101~105` 译法；`chapters`/`ui_menu`/`ui_achievements` 维持既有译法（仅修 1 处源码畸形标记）。
  Menu 归档复核：8 资源 / 1300 条 / 标记差异 0 / 制表符差 0 / 旧译名 0。
- 2026-10-12（追加2）：新增 **`翻译工程/一键重建.py`**（改完译文一键出全部 8 个归档，自带核验）；
  **清除 14 处「标记内混入空格」**（如 `{ SternA}` → `{SternA}`，否则游戏可能识别不到该表情标签），
  修复脚本 `_work/fix_tag_spaces.py`，覆盖文件 `tr/zz_fix_tags_zh.py`；全部归档已重建。
  验收口径同时补齐：标记比对现已包含 `[..]` 与 `{..}`（原先只查 `^color:^`/`<>`，存在盲区）。

### 已知问题 / 重要经验

- **【已改为】演职员表整份不翻译** ⚠️ 这条很关键：
  `ui_credits*`（那个「VIRTUOS 本地化团队」整页演职员表）**现在整份走英文原档**——流水线里由
  `apply_one.py` 的 `SKIP_AS_EN = ('ui_credits',)` 直接逐字节沿用英文原文，**不翻译、也不进 tr 字典**。
  原因：整页上千行姓名职务，翻成中文会得到**一条 2.8 万字的 CJK 字符串**，引擎逐字排版/换行是 O(n²) 量级，
  实测**切换场景载入会从数秒变成 1 分钟**；而且原汉化包在这一块是错位/串行的。
  > 被清出 tr 的演职员表条目备份在 `_归档_早期试验/tr_移除的演职员表/`；
  > 原本散落在其中的**剧集名**（`Zer0 Sum`→零和、`Atlas Mugged`…）已归拢到 `tr/episode_titles_zh.py`（菜单/标题卡仍在用）。
- **其他超长块（>3000 字符）也一律保留英文**：`apply_one.py` 的 `LONG_KEEP = 3000` 兜底（日志显示「超长块保留英文 N」）。
- **对白错位**：约 53 段（101:3、102:3、103:17、104:30、105:0）译文串到了相邻行——会显示错误台词。
  最重的是 `104/env_07_oldhaven_vasquezbody` 与 `103/env_02_atlasescape_nojack`。
  检测脚本 `_work/shift_all.py`；**修复需逐段人工重译**（区间边界无法靠算法可靠判定）。
- **多余表情标签**：约 528 处骨架差异，多为译者**多加了 `{表情}` 标签**（不破坏渲染，但偏离"逐 token 对齐"约定）。

## Credits 

- [TelltaleToolLib](https://github.com/LucasSaragosa/TelltaleToolLib)
- 3DM 汉化组
