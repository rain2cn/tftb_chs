# 标记写法回正（清除标记内多余空格，使 {..}/^..^/<..> 与原文逐 token 一致）
T = {
 '[all-business] {SmugC}We at the Hyperion Corporation have taken a keen interest in your Vault Key, and would love to purchase said Vault Key for an {SlyC}obscene amount of money.': '[all-business] {SmugC}我们 亥博龙公司对您的秘藏钥匙产生了浓厚兴趣，很想用{SlyC}一笔下流的巨款买下它。',
 "{SternB}Then I guess you ain't {SternA}seen enough.": '{SternB}那我想你{SternA}见得还不够多。',
 '[postpax] {WorryB}{Body-A}Huh, this is a funny {WorryA}story actually...': '[postpax] {WorryB}{Body-A}嗯，这其实是个{WorryA}挺好笑的故事……',
 "{SternA}Okay, {ShockD}okay, look, I don't know what {ThinkA}the Hell you think you're doing, {ThinkB}but... this is {RageA}not how I operate, {SmugB}alright? I expected {SternB}Vasquez, and I got {AngryA}you.": '{SternA}好，{ShockD}好，听着，我不知道{ThinkA}你以为你在干什么，{ThinkB}但……我{RageA}不是这么办事的，{SmugB}行吗？我期待的是{SternB}Vasquez，结果来了个{AngryA}你。',
 "{sternA}I'm the one who's {SternB}buying the key.": '{sternA}买钥匙的人是{SternB}我。',
 '[insulted] {InquireA}Well maybe I {AngryA}*am* going to open {SternA}the Vault.': '[insulted] {InquireA}也许我{AngryA}*真*打算打开{SternA}秘藏。',
 "{AngryA}Sit, Sasha. Nobody's going {SternA}anywhere until I say so.": '{AngryA}坐下，萨莎。我没发话谁也别想{SternA}走。',
 "{NeutralA}And you've got some {SternA}sap lined-up to buy it.": '{NeutralA}而你还{SternA}找好了冤大头来买。',
 "Or maybe you're {SlyB}secretly an alien?": '或者你其实{SlyB}是个外星人？',
 '{NeutralB}By putting all my time and money into it {SternA}for [beat] a while now.': '{NeutralB}把全部时间和钱都投进去{SternA}投了[beat] 好一阵子了。',
 "{SternA}We'll do the job, but we {SternB}want more money.": '{SternA}活我们干，但我们{SternB}要更多钱。',
 "{thinkingB}Mmhm. Mmhm. Discrete's good, Rhys. Nothing wrong with having a little {mockingA}work done under the hood.": '{thinkingB}嗯哼。嗯哼。低调挺好，瑞斯。在引擎盖下面{mockingA}做点活儿没什么不对。',
 "[pickup2] {MockingA}Ah. {ThinkingA}Yeah. {SarcasticB}Well, uh, I totally get what you're saying there. {ConfusedA}I too have found {ThinkingA}Handsome Jack to be... {HappyB}an eternal well {MockingA}of inspiration.": '[pickup2] {MockingA}啊。{ThinkingA}是啊。{SarcasticB}这个，呃，我完全懂你在说什么。{ConfusedA}我也发现{ThinkingA}帅杰克是……{HappyB}一口永不枯竭的{MockingA}灵感之井。',
 "[pickup2] {SmugA}That is {SmugB}so generous of you. {SmugC}I'll think about that when you {SternB}shoot me in the back.": '[pickup2] {SmugA}你可{SmugB}真大方。{SmugC}等你{SternB}背后开枪打我的时候，我会想起这句话的。',
}
