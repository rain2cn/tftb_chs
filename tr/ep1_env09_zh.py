# 批次3-10：第1章 env_09_hollowpoint_fiona_purpleskag（Fiona 在"紫斯凯格"酒吧找 Vallory 谈假秘藏钥匙的交易）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g'), ('ep1_env12_zh.py', '_h'), ('ep1_env01_zh.py', '_i')):
    T.update(_load(_f, _n))

# —— 说话人标记（保留原文）——
T.update({
 "FIONA": "FIONA",
 "GUY": "GUY",
 "BARTENDER": "BARTENDER",
 "DRUNKGUY": "DRUNKGUY",
 "CRAZYGUY": "CRAZYGUY",
 "FINCH": "FINCH",
 "CARD PLAYER": "CARD PLAYER",
 "TECTOR": "TECTOR",
 "KROGER": "KROGER",
 "VALLORY": "VALLORY",
 "AUGUST": "AUGUST",
 "SASHA": "SASHA",
 "FELIX": "FELIX",
 "DRUNK1": "DRUNK1",
 "TOMMY": "TOMMY",
 "MINIMIKE": "MINIMIKE",
 "Drinking Guy": "Drinking Guy",
})

# —— 内部 / 技术条目（刻意保留英文）——
T.update({
 "<<ID": "<<ID",
 "{11CB5877-75F6-4199-8FBF-4626447F0393}>>": "{11CB5877-75F6-4199-8FBF-4626447F0393}>>",
 "{33001949-0DB2-4327-B9FD-7528EF56480C}>>": "{33001949-0DB2-4327-B9FD-7528EF56480C}>>",
 "{917F89E9-6A1E-43C5-9BDB-D0F7BADAFCA6}>>": "{917F89E9-6A1E-43C5-9BDB-D0F7BADAFCA6}>>",
 "PLACEHOLDER": "PLACEHOLDER",
 "[SILENT REVEAL]": "[SILENT REVEAL]",
 "[whisper talk]": "[whisper talk]",
 "[Silence]": "[Silence]",
})

# —— 开场：酒吧里的混乱与选项 ——
T.update({
 "[sighs; muttering to herself] Why do Tuesdays always bring the worst crowds...":
    "[sighs; muttering to herself] 为什么星期二总是来最烂的一批客人……",
 "[being punched] Awwhgh!": "[being punched] 哎哟！",
 "[angry] I already told ya we was out of orange juice!": "[angry] 我早跟你说过我们橙汁卖完了！",
 "Hey, give me a, uh, Dirty Larry.": "嘿，给我来一杯，呃，脏拉里。",
 "[rubbing his face; hugely petulant, like a child] Well I'm *sorry*！":
    "[rubbing his face; hugely petulant, like a child] 好吧，我*很抱歉*！",
 "[rubbing his face; hugely petulant, like a child] Well I'm *sorry*!":
    "[rubbing his face; hugely petulant, like a child] 好吧，我*很抱歉*！",
 "Oh, sure, your *majesty*, coming right up.": "哦，当然，*陛下*，马上就来。",
 "Yeah, if sorries and buts were candies and nuts.": "是啊，要是“对不起”和“但是”能当糖豆吃就好了。",
 "[from across the room now] What does that even mean!": "[from across the room now] 那到底是什么意思！",
 "No, I don't think so.": "不，我不这么认为。",
 "Maybe we did, so what?": "也许我们做了，那又怎样？",
 "I'm in the middle of something...": "我这儿正忙着呢……",
 "I'm not who you think I am.": "我不是你以为的那个人。",
 "Go away, you're drunk.": "走开，你喝多了。",
 "[Smash him with bottle]": "[用酒瓶砸他]",
 "Cool.": "酷。",
 "This anybody's?": "这是谁的吗？",
 "He just left.": "他刚走。",
 "[thoughtful murmur]": "[thoughtful murmur]",
 "\"Birth, Work, Kill, Eat\" by Bloody Mama": "“生、劳作、杀、吃”—— Bloody Mama 演唱",
 "\"Gonna Cut You\" by That Scary Guy": "“要把你切开”—— That Scary Guy 演唱",
 "\"Suicide or Die Tryin\" by The Weekend Warriors": "“自杀或拼命而死”—— The Weekend Warriors 演唱",
 "[Leave]": "[离开]",
 "What? It's a good song.": "怎么？这是首好歌。",
 "That doesn't mean *you* get it for free.": "那不意味着*你*能白听。",
 "[Pay him]": "[付钱]",
 "Add it to my tab.": "记我账上。",
 "Too late.": "太迟了。",
 "[flat] You spoil me.": "[flat] 你太宠我了。",
 "Buy yourself something nice.": "给自己买点好东西吧。",
 "C'mon.[beat] It's big boned.": "拜托。[beat] 那是骨架大。",
 "That *tab's* gettin' kinda *fat*, don't you think.": "那笔*账*好像有点*厚*了，你觉得呢。",
 "Add it to my tab, alright?": "记我账上，行吗？",
 "[getting hit with bottle] Awwhgh!": "[getting hit with bottle] 哎哟！",
 "Just a bit of fun.": "就是玩玩而已。",
 "Yeah, where is she.": "是啊，她在哪儿。",
 "I'm not exactly hiding.": "我又没在躲。",
 "You didn't have to kill him.": "你不必杀他。",
 "Thanks, I hated that guy!": "谢了，我讨厌那家伙！",
 "He started it!": "是他先动手的！",
 "Where's Vallory?": "瓦洛里 在哪儿？",
 "So... how's August?": "那……August 怎么样？",
 "I'll have one of those.": "给我来一杯那个。",
 "I got a deal for you.": "我有个交易找你。",
 "[Sit down]": "[坐下]",
 "I'll stand.": "我站着。",
 "*Don't.*": "*别*。",
 "I'd prefer to stand, thanks.": "我更愿意站着，谢谢。",
 "This won't take long.": "不会很久。",
 "Don't sweat it. This won't take that long.": "别紧张。不会很久的。",
 "What.": "什么。",
 "[spitting noise]": "[吐唾沫的声音]",
 "I need a meeting with Vallory.": "我要见 瓦洛里。",
 "Can I get a drink?": "能给我杯酒吗？",
 "Anybody been looking for me?": "有人找过我吗？",
 "I have it, don't worry.": "钱我拿到了，别担心。",
 "I have something better than money.": "我有比钱更好的东西。",
 "I'm sorry about everything.": "所有事我都很抱歉。",
 "I just don't have it ALL yet.": "我只是还没凑*齐*。",
 "It's stashed away.": "藏起来了。",
 "I'm joking! I don't have it.": "我开玩笑的！我没有。",
 "A fake Vault Key.": "一把假的秘藏钥匙。",
 "A Vault Key!": "一把秘藏钥匙！",
 "My everlasting friendship.": "我永恒的友谊。",
 "...Yes?": "……怎么了？",
 "Just give me more time.": "再给我点时间。",
 "I have something else.": "我有别的东西。",
 "[Break his finger]": "[掰断他的手指]",
 "I need more time.": "我需要更多时间。",
 "That won't be necessary.": "没必要那样。",
 "Shut up!": "闭嘴！",
 "I was gonna cut you in, Vallory.": "我本来打算分你一份的，瓦洛里。",
 "How do you know about that?": "你怎么知道那件事的？",
 "Somewhere safe.": "在一个安全的地方。",
 "Let's set the terms first.": "我们先把条件谈好。",
 "Out back in my trailer.": "在后面我的拖车里。",
 "It wasn't my choice.": "那不是我的选择。",
 "Oh, just shut up.": "哦，闭嘴吧。",
 "Don't worry, it's fine.": "别担心，没事。",
 "We deserve the biggest share!": "我们该拿最大的一份！",
 "Half, at least.": "至少一半。",
 "I just want the debt erased.": "我只想把债抹掉。",
 "What? No deal!": "什么？不行！",
 "So I'm your servant, basically.": "所以基本上，我就是你的仆人了。",
 "You are such a dick.": "你这人真是混蛋。",
 "I think you're interrupting my deal.": "我觉得你在打断我的交易。",
 "I was thinking Business.": "我说的是公事。",
 "I was thinking of old friends.": "我说的是老朋友。",
 "I don't need a babysitter.": "我不需要保姆。",
 "Why are you making everything suck!": "你干嘛非要把一切都搞烂！",
 "We could use the muscle.": "我们能多个打手也不错。",
 "Why'd you say anything!": "你干嘛要说出来！",
 "[Punch him]": "[揍他]",
 "[Nudge him]": "[撞他一下]",
 "Hey. Asshead.": "嘿。蠢货。",
 "We can make a deal.": "我们可以做个交易。",
 "I have something you want!": "我有你想要的东西！",
 "Don't be stupid, Vallory.": "别犯蠢，瓦洛里。",
 "I have a Vault Key.": "我有一把秘藏钥匙。",
 "August couldn't handle it.": "August 搞不定这事。",
 "Because you love money.": "因为你爱钱。",
 "Because mommy says so.": "因为妈妈说可以。",
 "It is the deal of the century.": "这是世纪级的交易。",
 "Show 'em who's boss.": "让他们知道谁是老大。",
 "Maybe she's right.": "也许她说得对。",
 "[Look at]": "[查看]",
 "[Talk to]": "[交谈]",
 "Ugh, c'mon![beat] You're insane?": "呃，拜托！[beat] 你疯了？",
 "Right this way, madam.": "这边请，女士。",
 "I wasted my two drink cards on you, man. Couldn't you have told me that at the start?":
    "我把两张酒水券都浪费在你身上了，老兄。你早说不就得了？",
 "Alright? Sounds good?": "行吗？听着不错吧？",
 "*I'm* Vallory! [cackles with insane laughter]": "*我*才是 瓦洛里！[cackles with insane laughter]",
 "So all I'm sayin' is... you get me in to meet Vallory... and we'll tag-team this crap we call Life *together*.":
    "我就是说……你帮我引见 瓦洛里……然后我们一起联手对付这坨叫“人生”的破烂*一起*。",
 "You got problems, I know, and I mean... who doesn't in this life?":
    "你有你的麻烦，我知道，而且我是说……这辈子谁没有呢？",
 "Uh-huh! [more laughter]": "嗯哼！[more laughter]",
 "[muttering] Guess I'll have to do this some other way.": "[muttering] 看来我得换个办法了。",
 "But *you*, I can tell... by your kind eyes and your soft hands... *you* are one of the good eggs.":
    "但*你*，我一眼就看得出来……从你和善的眼睛和柔软的手……*你*是个好人。",
 "So... you seem to be a fine, upstanding young --[gets cut off] barfly.":
    "所以……你看起来是个正直优秀的年轻——[gets cut off] 泡吧常客。",
 "Nope! [insane laughter]": "不是！[insane laughter]",
 "Uhhhh anybody seen Vallory?": "呃……有人见到 瓦洛里 吗？",
 "Hello?[beat] Wanted woman here!": "喂？[beat] 通缉犯在这儿呢！",
 "Can't you read?": "你不识字吗？",
 "Hey, wait a minute! Seven isn't higher than eight!": "嘿，等等！七不比八大啊！",
 "Vallory's takin' her nap.[beat] So pipe down.": "瓦洛里 在睡午觉。[beat] 所以小声点。",
 "Sorry, Mr. Finch.": "抱歉，芬奇 先生。",
 "Excuse me, alewife?": "打扰一下，酒馆娘？",
 "[purposefully haughty] Do you perchance know how I'd... uh, perchance to get a meeting with Vallory?":
    "[purposefully haughty] 请问您是否碰巧知道，我该如何……呃，碰巧安排一次与 瓦洛里 的会面？",
 "I have no idea what you're talking about.": "我完全不知道你在说什么。",
 "Uh, alewife?": "呃，酒馆娘？",
 "[deep sigh] Okay.": "[deep sigh] 好。",
 "[takes a quick breath] That's enough.": "[takes a quick breath] 够了。",
 "[getting smashed into the bar] Arghgh!": "[getting smashed into the bar] 啊呃！",
 "You've an unnatural talent for screwing things up, Kroger.":
    "你在搞砸事情上有着非凡的天赋，克罗格。",
 "Don't look at me. It's the broad, alright!": "别看我。是那娘们，行吗！",
 "That true?": "真的吗？",
 "Yeah, did it work?": "是啊，成了吗？",
 "Vallory awake yet?": "瓦洛里 醒了吗？",
 "It's the woman, alright? She's buggin' the customers, I don't know what her *freakin'* problem is.":
    "就是那女人，行吗？她在骚扰客人，我不知道她他妈*有什么毛病。",
 "You wouldn't think it to look at her... but Vallory's an anxious sleeper.":
    "光看她那样你绝对想不到……但 瓦洛里 睡觉很不踏实。",
 "[annoyed] Yeah, it's true, I'm not makin' up stories.":
    "[annoyed] 对，是真的，我没编故事。",
 "[delirious] Hey, Kroger -- *This*... friggin' *fish* owes me for alllll the drinks she friggin' *spilled* -- [BLAM! he gets shot]":
    "[delirious] 嘿，克罗格——*这条*……该死的*鱼*还欠我她他妈*洒掉*的所有酒钱——[BLAM! he gets shot]",
 "Everybody out. Now.": "所有人都出去。马上。",
 "Why is that?": "为什么？",
 "Wednesdays always bring the worst crowds.": "星期三总是来最烂的客人。",
 "Because that's when they realize that the week is gonna be exactly the same as every other.":
    "因为那天他们才意识到，这一周跟其他每周一模一样。",
 "Makes sense.": "有道理。",
 "She probably shouldn't live in the back of a bar, but... life makes fools of us all, I guess.":
    "她大概不该住在酒吧后屋，但……我想生活让我们所有人都成了傻瓜。",
})

# —— Vallory 登场 + August / Sasha 插话 ——
T.update({
 "Was that Fiona I heard? That you, darlin'?": "我刚听到的是 Fiona 吗？是你吗，亲爱的？",
 "[sitting down] Ooof. Old knees.": "[sitting down] 哎哟。老膝盖了。",
 "She's buggin' the customers, buggin' me about Vallory -- she's got a bug up her hole.":
    "她在烦客人，又缠着我问 瓦洛里——她心里有只虫子卡着呢。",
 "Just a spot of fun. Nothin' broke.[beat] Or nothin', you know, *nice* broke.":
    "就是玩玩而已。没砸坏东西。[beat] 或者说，你知道，没砸坏什么*好*东西。",
 "Yeah, I got a problem!": "是啊，我有麻烦！",
 "Yeah, I got a problem, and if you had just *let* me talk to Vallory when I *wanted* to, I wouldn't have to go and mess up your nice *bar*!":
    "是啊，我有麻烦，要是你在我*想*见 瓦洛里 的时候就*让*我见，我也不至于来砸你的漂亮*酒吧*！",
 "Now why would you go and do something like that?": "你干嘛要去干那种事呢？",
 "She wanted to talk to Vallory?": "她想跟 瓦洛里 说话？",
 "I *guess*, but, I mean look at her, who cares!": "我*想*是吧，但你看看她那样，谁在乎啊！",
 "Yeah, I got a problem, I've been wantin' to talk to Vallory for like... five whole minutes and I got tired of waitin' around for people to notice!":
    "是啊，我有麻烦，我想跟 瓦洛里 说话大概……整整五分钟了，我实在等不及别人注意到我！",
 "How was I supposed to know that!": "我怎么知道会那样！",
 "Oh, don't gimme that crap, that Skaglick *started* it!": "哦，少来这套，是那个舔异犬的*先*动的手！",
 "[to Kroger] Who swung first?": "[to Kroger] 谁先挥的拳？",
 "The girl.": "那姑娘。",
 "Well, yeah, I mean... because I knew he was gonna!": "嗯，是啊，我是说……因为我知道他就要动手了！",
 "You lying sack -- [gets cut off] of": "你这撒谎的杂——[gets cut off] 种",
 "I dunno, probably the girl.": "不知道，大概是那姑娘。",
 "[flat] Oh.[beat] She's *that* girl.": "[flat] 哦。[beat] 她就是*那个*姑娘。",
 "Was that really necessary? He was just annoying.": "真有那个必要吗？他只是很烦人而已。",
 "That's a good enough reason as any.": "这理由已经够充分了。",
 "[breathes out] Thanks, man, I *hated* that guy. Two strikes and you're out. His mother won't miss him.":
    "[breathes out] 谢了，老兄，我*讨厌*那家伙。两次前科，你就出局了。他妈不会想他的。",
 "[cold] Just tell me where Vallory is.": "[cold] 告诉我 瓦洛里 在哪儿就行。",
 "Surprise, it's me!": "惊喜，是我！",
 "What took you so long.": "你怎么这么久。",
 "Who ELSE but your \"poster girl\"": "除了你的“海报女郎”，还能是谁",
 "Yes, ma'am, it's her.": "是的，女士，是她。",
 "If that's you, I'll say I'm surprised.": "如果真是你，那我得说我挺意外的。",
 "Whiskey sour. Rakk egg.": "威士忌酸酒。加一颗拉卡蛋。",
 "Thought you'd be halfway to the Sunken Sea by now.": "我以为你现在该到沉没之海的一半路了。",
 "She's the one.": "就是她。",
 "A shot of whiskey with a Rakk egg.": "一杯威士忌，加一颗拉卡蛋。",
 "And put a little, uh...[german] *zitrone*, in it.": "再加一点，呃……[german] *柠檬*。",
 "Learned that from Marshall.": "跟 Marshall 学的。",
 "Much appreciated.": "多谢。",
 "It's me, your old pal Fiona.[beat] Surprise!": "是我，你的老朋友 Fiona。[beat] 惊喜吧！",
 "Took you long enough to even notice I was here.": "你花了这么久才注意到我在这儿。",
 "[annoyed] Yeah, uh, who *else* would it be? I mean, I'm sure alot of losers around here owe you money.":
    "[annoyed] 是啊，呃，还能是*谁*呢？我是说，我敢说这附近不少废柴都欠你钱。",
 "To speak honestly, I thought you'd be a runner.": "说实话，我以为你会跑路。",
 "What'd you expect me to do?": "你以为我会怎么做？",
 "[flat] Yeah, no, I think I, uh, I think I read that somewhere.":
    "[flat] 是啊，不，我想我，呃，我想我在哪儿读到过。",
 "And then, ya know, as these things go... we probably woulda cooked and ate it.":
    "然后，你知道，按这种事的发展……我们大概会把它煮了吃掉。",
 "You had to *expect* me to come around soon enough, I mean, what did you think I'd do?":
    "你总该*料到*我迟早会来吧，我是说，你以为我会怎么做？",
 "So... how's August? [beat] I expected him to be here.":
    "那……August 怎么样？[beat] 我以为他会在这儿。",
 "Nah, if anythin' I've gotten fatter.": "没有，要说的话，我反而更胖了。",
 "Make two.": "来两杯。",
 "Make it two, actually.": "其实来两杯吧。",
 "[a light laugh]": "[轻轻一笑]",
 "So, I came here because [beat] I got a deal for you.":
    "所以，我来这儿是因为[beat] 我有个交易找你。",
 "Okay, okay, but before you get all hot and bothered... I *do* have somethin' to trade.":
    "好，好，但在你激动起来之前……我*确实*有东西可以交换。",
 "Did you now?": "是吗？",
 "This is for both.": "这是两杯的。",
 "Thank ya, angel.": "谢谢，天使。",
 "Thanks.": "谢谢。",
 "[unamused] Okay.": "[unamused] 好。",
 "[defensive] It sounds good.": "[defensive] 听起来不错。",
 "Sit down, Fiona. Take a breath.": "坐下，Fiona。喘口气。",
 "Sit. Now.": "坐下。马上。",
 "So... it appears we have some business to discuss.": "那么……看来我们有些事要谈。",
 "Now, I know what you done... was just your *way* of survivin', like... a lil' tiny beetle rollin' up a lil' drop of crap into a wee lil' ball until it can make it it's home.":
    "我知道你干的那些事……只是你的*生存方式*，就像……一只小甲虫把一小滴粪球滚成一个小球，直到能把它当窝。",
 "[menacing] So why should I prevent my friend, Mr. Finch here, from sending you to your land of sweetener?":
    "[menacing] 那我干嘛要拦住我的朋友 芬奇 先生，不让他送你去你的甜头之地？",
 "And I also know that my nephew's a true born and raised simpleton... but at the end of the page, family's family, business is business, and this -- this is a bit of both.":
    "我也知道我侄子是个土生土长的纯傻子……但翻到最后一页，家人就是家人，生意就是生意，而这件事——两者都算。",
 "Because you know a good deal when you see one.": "因为好交易你一眼就认得出来。",
 "Because I have something you want.": "因为我有你想要的东西。",
 "It's better than money.": "它比钱更好。",
 "If it's not my bread you can save your air.": "要不是我的生计，你就省点口水吧。",
 "Well...[colder] I'm not happy yet.": "这个……[colder] 我还没高兴起来。",
 "You shoot me, you don't get anything but a moment of satisfaction as fleeting as eating a bar of chocolate or... uh... watching your enemies get eaten by ants.":
    "你开枪打我，你除了片刻的满足什么都得不到，那种满足跟吃一块巧克力或者……呃……看着你的敌人被蚂蚁吃掉一样短暂。",
 "C'mon, Vallory, don't be stupid.": "拜托，瓦洛里，别犯蠢。",
 "[menacing] A little satisfaction can go a long way.": "[menacing] 一点点满足也能顶很久。",
 "Come on, ma. I'm in love.": "拜托，妈。我恋爱了。",
 "With ... *that*?": "跟……*那个*？",
 "[muttering to herself] Nobody respects that sign.": "[muttering to herself] 没人把那牌子当回事。",
 "What the Hell are you lookin' at?": "你他妈在看什么？",
 "Ma?": "妈？",
 "Yeah, yeah, Ma! Ma, where are ya?": "好，好，妈！妈，你在哪儿？",
 "[laughing] That won't-- oww, my stomach hurts.": "[laughing] 那不会——哎哟，我肚子疼。",
 "I'm in here.": "我在这儿。",
 "Probably a symbol of my shepherdin' nature.": "大概是我那种牧羊人本性的象征。",
 "You know, I was havin' a real nice dream.": "你知道，我刚做了个特别好的梦。",
 "I was as big as a mountain... and lived on the moon.": "我大得像座山……住在月亮上。",
 "[excited] Yeah.": "[excited] 是啊。",
 "Finally get the money?": "终于拿到钱了？",
 "What about a ring this big?": "那颗戒指有这么大怎么样？",
 "You wanna know what I'm looking at? Two drunk idiots maybe one year away from having a really ugly, really stupid baby.":
    "你想知道我在看什么吗？两个醉鬼，大概还有一年就要生一个特别丑、特别蠢的孩子。",
 "Okay, settle down.": "好了，冷静点。",
 "I care when you're givin' my girl, \"I wanna freak on you\" eyes!":
    "可你要是用那种“我想跟你搞”的眼神看我的姑娘，我就在意了！",
 "What the Hell do you care where I look?": "我往哪儿看你他妈管得着吗？",
 "Are you kiddin'?": "你开玩笑吧？",
 "Uhhh, little help?": "呃……搭把手？",
 "Yeah!": "对！",
 "Oh, frag off, like I-- like you even... you don't even *know* what-- just shut up!":
    "哦，滚开，好像我——好像你——你根本*不知道*什么——闭嘴！",
 "Or just got tired of living?": "还是只是活腻了？",
 "That's what I thought.": "我就知道。",
 "Wait. You're the girl who cheated Ralphie.": "等等。你就是骗了 Ralphie 的那个姑娘。",
 "[annoyed] *Fiona* was just sayin' something about... helpin' our little family business *be* all that it can be. Right, was that it?":
    "[annoyed] *Fiona* 刚说了些什么……帮我们这家小家族生意*做到*最好。对吧，是这么说的吧？",
 "[annoyed] Yes, *Fiona* was just gonna explain just where... *on her person at this very moment*... my money is.":
    "[annoyed] 对，*Fiona* 正要解释我的钱……*此刻在她身上什么地方*。",
 "[annoyed] Yes, *Fiona* was just saying that she had somethin' *better* than money?[beat] A unicorn that craps eridium, maybe?":
    "[annoyed] 对，*Fiona* 刚说她有比钱*更好*的东西？[beat] 也许是只会拉镒矿的独角兽？",
 "[annoyed] Yes, *Fiona* was just tellin' me not to be... *stupid*, I think was the phrasin' she chose.":
    "[annoyed] 对，*Fiona* 刚叫我别……*犯蠢*，我想她用的就是这个说法。",
 "August, jus' yesterday she tried to heat up a pizza still in its cardboard.":
    "August，就在昨天她还把还裹着纸板的披萨拿去加热。",
 "[ditz act] What's wrong with that! That's how it comes!": "[ditz act] 那有什么不对！本来就是那样送来的！",
 "Oh now that's going too far you stupid witch, that's my *son* you're talking about!":
    "哦，这说得太过分了，你这蠢巫婆，你说的可是我的*儿子*！",
 "Well.": "这个。",
 "That's what *they* want you to think, baby.  But one was just opened a little while ago by some Vault Hunters.":
    "那正是*他们*想让你相信的，宝贝。但前不久刚有一批秘藏猎人打开了一个。",
 "They have enough treasure to last a million friggin' life times.":
    "里面的宝藏够他妈的用一百万辈子。",
 "But aren't Vaults like, just, um, a *parable* or somethin'?":
    "但秘藏不就像，呃，是个*寓言*什么的吗？",
 "How would she even get one? Huh? What?  Have sex with a leprechaun?":
    "她怎么可能弄到一个？啊？什么？跟矮精灵上床？",
 "[laughing] A *Vault Key*! Gimme a freakin' break!": "[laughing] *秘藏钥匙*！饶了我吧！",
 "I'll play along for a spell.[beat] Where is it?": "我就陪你演一会儿。[beat] 在哪儿？",
 "Or else this gets shelved as a tall tale.": "不然这事就只能当吹牛皮搁下了。",
 "You understand I'm gonna need some sort of verifiable proof.":
    "你明白我需要某种可验证的证据吧。",
 "I tell you, you tell somebody else... pretty soon I'm a bed and breakfast for people who wanna slit my throat.":
    "我告诉你，你再告诉别人……很快我就成了那些想割我喉咙的人的落脚客栈了。",
 "We're gonna set the terms *first*. And *Then* you can see it.":
    "我们*先*把条件谈好。*然后*你才能看。",
 "I respect you, Vallory. So... I'm just gonna tell you.[beat] I have it out back in my trailer.":
    "我尊重你，瓦洛里。所以……我就直说了。[beat] 东西在我后面那辆拖车里。",
 "It's somewhere safe. Alright? That's all you need to know.":
    "在一个安全的地方。行吗？你知道这些就够了。",
 "Finch, go get it.": "芬奇，去拿来。",
 "Sasha says that she saw this chick and her weird old-guy pal carryin'  somethin' that looked like a blinkin' satellite into her Van the other day.":
    "萨莎 说她前几天看见这姑娘和她那个古怪的老年伙伴搬了个像闪烁卫星似的东西进她的货车。",
 "Alright, easy-- just... take it easy, now.[beat] I'm frail and I sunburn easily.":
    "好了，别急——就……别急。[beat] 我身子弱，还容易晒伤。",
 "Incredible.": "不可思议。",
 "Uhhhhh.....": "呃………………",
 "So, Fiona...": "那，Fiona……",
 "It does indeed lack credibility.": "它确实缺乏可信度。",
 "Uhhhhhhh.....": "呃………………",
 "Oh yeahhhhh, now I see it.": "哦对…………现在我看清了。",
 "He's cheating.": "他在出老千。",
 "[Hit him]": "[揍他]",
 "Seen Vallory?": "见到 瓦洛里 了？",
 "I need to see Vallory.": "我要见 瓦洛里。",
 "I'm the girl on the poster.": "我就是海报上那个姑娘。",
 "Let me through.": "让我过去。",
 "But every so often I'd... come down to one of these little ol' villages... and breathe fire over the landscape to cull the earth.":
    "但偶尔我会……降临到这些小小的村庄……朝大地喷火，把地表的生物清一遍。",
 "And when you hear what it is, trust me, you're gonna be *really* happy[lightly laughing] this *whole* misunderstanding thing, uh, happened.":
    "等你听说是怎么回事，相信我，你会*真的*高兴[lightly laughing] 发生了这*整件*误会，呃。",
 "Okay, but don't-- just don't aim it near me.": "好，但别——别朝我这边瞄准。",
 "[cold] Nothin's better than bread, sweetheart. That's why they call it bread.":
    "[cold] 没什么比面包更好，甜心。所以才管它叫面包。",
 "I don't see one yet.": "我还没看见什么面包。",
 "Vallory, after today, your family business is gonna be an intergalactic enterprise.":
    "瓦洛里，过了今天，你的家族生意就要变成星际企业了。",
 "Still.[beat] What exactly am I supposed to *do* with a Vault Key, Fiona?":
    "不过。[beat] 我拿一把秘藏钥匙到底能*干什么*，Fiona？",
 "There's somethin' about this not settlin'.": "这事有点让我不踏实。",
 "You make shady deals all the time, baby -- you must know *somebody* who'd want to buy a Vault Key...":
    "你成天做见不得光的交易，宝贝——你肯定认识*哪个*想买秘藏钥匙的人……",
 "Yeah, no. I mean, I know people, but... this whole thing's--[kinda fishy][gets cut off]":
    "是啊，不。我是说，我认识人，但……这整件事——[kinda fishy][gets cut off]",
 "[irritated with his hesitance] Well then just fence it to them and let them deal with the monster alien hassle, alright?":
    "[irritated with his hesitance] 那就把东西销给他们，让他们去应付外星怪物那些破事，行吗？",
 "[frustrated] You've got contacts, folks who'd have the  money to buy this thing, and the muscle to deal with the monsters. [beat] What's the problem?":
    "[frustrated] 你有门路，有钱买这东西的人，也有能对付怪物的打手。[beat] 问题在哪儿？",
 "[imitating him]\"Mmmm, what should I do?\"": "[imitating him]“嗯，我该怎么办呢？”",
 "Just call one of your guy": "给你的人打个电话就行",
 "*What's* not that simple?": "*什么*没那么简单？",
 "Sasha, it's *not* that simple.": "萨莎，这*没*那么简单。",
 "Look, no offense, buddy, but I think this type of thing's just a *bit* above your paygrade.":
    "听着，无意冒犯，老兄，但我觉得这种事有点超出你的层次了。",
 "[laughing] August?[beat] C'mon. He gets nervous at the dry cleaners.":
    "[laughing] August？[beat] 拜托。他进干洗店都会紧张。",
 "Oh, please. I can  *handle* it. My *people* can handle it.":
    "哦，拜托。我*搞得定*。我*的人*搞得定。",
 "What did you say?": "你说什么？",
 "[a little nervous] Ma, c'mon, this'll be an easy drop. One and done and then we all get paid.":
    "[a little nervous] 妈，别这样，这会是笔轻松的买卖。一次搞定，然后大家都拿钱。",
 "What, you're not *man* enough for this kind of thing?": "怎么，你不够*男人*干这种事？",
 "First you couldn't handle building that coffee table and *now* you can't handle selling this Key! What has gotten into you!":
    "先是你连那张咖啡桌都做不好，*现在*你连卖这把钥匙都搞不定！你最近是怎么了！",
 "[exasperated] Oh my *God*.": "[exasperated] 我的*天*。",
 "We'll take it, we're taking it. Be nice and be grateful.":
    "我们接了，我们接。客气点，感恩点。",
 "This is a *Vault Key*, okay? There's no guarantees with somethin' like that.":
    "这是*秘藏钥匙*，行吗？这种东西没有任何保证。",
 "[light laughter] August? This guy doesn't *know* anybody except for his loser drinking buddies.":
    "[light laughter] August？这家伙除了他那些废物酒友之外*谁都不认识*。",
 "You have *no* idea who I *know*, okay, shorty? I got *connections* you couldn't freakin' *dream* of.":
    "你*完全不知道*我认识谁，行吗，小个子？我有你他妈*做梦都想不到*的*人脉*。",
 "I don't know... would Vallory even *let* you?": "我不知道……瓦洛里 会*让*你去吗？",
 "Oh, c'mon! I haven't done that since I was five years ol": "哦，拜托！我五岁之后就没干过那种事了",
 "I *am* the friggin' *guarantee*, alright, honey? I do fifteen deals bigger than this before I eat breakfast.":
    "我他妈*就是*那个保证，行吗，亲爱的？我吃早饭前就能做成十五笔比这更大的买卖。",
 "I can handle it, alright! And I *wanted* that table to have three legs, okay, it was a *choice*.":
    "我搞得定，行吗！而且那张桌子*就是*我想做成三条腿的，行吧，那是个*选择*。",
 "This isn't goin' down to the market to get a pack of smokes when *Mommy's* too hung over to make the walk.":
    "这可不是*妈妈*宿醉走不动路时，让你去趟市场买包烟。",
 "My *Ma* is a scary judge of talent, alright, honey? Which is *why* she has me do all of the most *important* chores.[beat] I mean jobs.":
    "我*妈*看人准得吓人，行吗，亲爱的？所以她才把最重要的家务都交给我。[beat] 我是说活儿。",
 "This chick's a complete *psycho*, Val, I mean *Mom*. Like you  would just *gift* her a freakin' *Vault Key*.":
    "这姑娘是个彻底的*疯子*，Val，我是说*妈*。好像你会白送她一把该死的*秘藏钥匙*似的。",
 "And I dunno -- it doesn't even *look* like a Key! Keys are gold with that hoop thing at the end and a big pointy part, this is like the engine to a giant lawnmower or something.":
    "而且我也不知道——它看起来根本*不像*钥匙！钥匙是金色的，末端有个圆环，还有一大截尖的，这玩意儿就像巨型割草机的引擎什么的。",
 "My God, how do you handle this all day? That voice? I feel like I've dropped IQ points.":
    "天哪，你一天到晚怎么受得了？那副嗓子？我觉得我智商都掉了几点。",
 "How the Hell would you even *know* what a Vault Key *looks* like? Just two seconds ago you were saying it was impossible for anyone to even get one!":
    "你他妈怎么*知道*秘藏钥匙*长什么样*？两秒前你还在说根本不可能有人能拿到一把！",
 "But Mom...[gets cut off]": "但是妈……[gets cut off]",
 "Well... we all know that's not really true...": "这个……我们都知道那不是真的……",
 "You call me *Mom* one more time and I'm takin' that tongue for its impudence.[beat] You understand?":
    "你再叫我一声*妈*，我就把那条不知好歹的舌头割下来。[beat] 听明白了吗？",
})

# —— "钥匙是真的吗"：Vallory 的试探 ——
T.update({
 "It *is* impossible. *Nobody's* gotten a Vault Key, ever! Right, Mom?":
    "这*确实*不可能。*从来没人*拿到过秘藏钥匙！对吧，妈？",
 "I don't know what I think, it's just... *not*...[trails off]":
    "我不知道我怎么想，只是……*不*……[trails off]",
 "The Key is, in truth, a very nice and charming thing.": "这把钥匙，说实话，是个非常讨喜迷人的东西。",
 "[muttering] She can have that impression.": "[muttering] 她可以留着这个印象。",
 "You think I just pulled this crap outta my hat?": "你以为这是我从帽子里变出来的破烂？",
 "Quiet down now.": "现在安静点。",
 "Keep going.": "继续说。",
 "Give me a break!": "饶了我吧！",
 "That's how it happened.[beat] And now it's yours. If you want it.":
    "事情就是这样。[beat] 现在它是你的了。如果你想要的话。",
 "Vallory, c'mon, I swear on my life here, on my friends' lives, on their mothers' lives...":
    "瓦洛里，拜托，我以我的命发誓，以我朋友的命，以他们母亲的命发誓……",
 "Mom, really, my *gut* is telling me you should just walk away.":
    "妈，真的，我的*直觉*告诉我你该直接走人。",
 "Your *expertise* in this matter is not really necessary *or* desired.":
    "这事你的*专业意见*既不必要也*不*受欢迎。",
 "Your *gut* isn't necessary, either.": "你的*直觉*也不必要。",
 "Look, Val, I just go with my gut.": "听着，Val，我就是跟着直觉走。",
 "The day I care 'bout what your *gut* wants, I'll be sure to let you know, alright?":
    "等哪天我在乎你的*直觉*想要什么了，我一定会告诉你，行吗？",
 "{NeutralA}I can hardly keep track of the names, honey. {SmugA}That's why I have you do it.":
    "{NeutralA}我根本记不住那些名字，宝贝。{SmugA}所以我才让你来干。",
 "Pretty sure he'd definitely be interested.": "我很确定他一定会感兴趣。",
 "I suppose your whole idea, then, is that this deal clears your debt? Right?":
    "那我想你的整个想法就是，这笔交易能抹掉你的债？对吧？",
 "{ThinkB}You mean Vasquez?": "{ThinkB}你是说 Vasquez？",
 "You have that, uh, that *crony* of yours over at Hyperion, right?":
    "你在 亥博龙有那个，呃，那个*亲信*，对吧？",
 "If it's small enough.": "只要它够小。",
 "Well, could be.": "这个，可能吧。",
 "Well they sure as shit ain't gettin' a finder's fee.": "他们他妈肯定拿不到什么中介费。",
 "But no.": "但不是。",
 "You can take what I owe, first dollar out -- Felix, too -- but after that I deserve the biggest cut.":
    "你可以先扣掉我欠你的，从第一块钱开始扣——菲利克斯 的也一样——但之后我该拿最大的一份。",
 "[a little laugh] You might not have a dick, sweetie -- but you sure got some balls, I'll give ya that.":
    "[a little laugh] 你也许没长那玩意儿，甜心——但你确实有点胆，这我承认。",
 "'Round here the truth is what I decree it is, darlin'.": "在这地界，真相是我说了算，亲爱的。",
 "I found the friggin' thing, me and Felix risked our *lives* bringing it to you [beat] heck, even half is unfair if you want the truth.":
    "这破东西是我找到的，我和 菲利克斯 冒着*命*把它带到你面前[beat] 说实话，就算一半也不公平。",
 "[stern] *Half*. At least.": "[stern] *一半*。至少。",
 "Half?": "一半？",
 "All I want is the debt erased. That's it. You can keep whatever else you get.":
    "我只要债抹掉。就这样。你剩下的都留着。",
 "[laughs]": "[laughs]",
 "[sarcastic] Oh, can I now? Why thank you!": "[sarcastic] 哦，是吗？真是谢谢你了！",
 "But it's not up to you to offer me supper, let alone the primest cut.":
    "但轮不到你来请我吃饭，更别说给我最好的那块肉。",
 "I'll take your obedient silence as a \"yes, mistress, I'm too frightened to speak, mistress\".":
    "我就把你那顺从的沉默当作“是的，女主人，我害怕得说不出话，女主人”。",
 "Alright, I got it.": "好，我懂了。",
 "Looks like Vallory *wants* someone who looks *exactly* like me [beat] and has the same name.":
    "看来 瓦洛里*想*见一个长得*跟我一模一样*[beat] 而且同名的人。",
 "This is harder than I thought it'd be.": "这比我想的要难。",
 "What the Hell are you talkin' about?": "你到底在说什么？",
 "I'm just tryin' to protect you, August. This deal is too big --":
    "我只是想保护你，August。这笔交易太大了——",
 "Watch it.": "注意点。",
 "[sad] What?": "[sad] 什么？",
 "It's the accountant in me, wanting to make sure I understand all the terms of the arrangement.":
    "是我骨子里那个会计在作祟，想确认我完全理解这项安排的所有条款。",
 "Finder's fee?": "中介费？",
 "The Key for the money due.": "用钥匙抵欠款。",
 "Look, I'm gonna be straightforward with ya... I'm downright dazzled. I really am.":
    "听着，我跟你直说吧……我真是被震住了。真的。",
 "I haven't been this impressed by someone's ingenuity since Charlie chewed his own feet off to escape my Thresher pit.":
    "自从 Charlie 咬掉自己的脚从我的鞭尾兽坑里逃出来之后，我就没对谁的机灵这么佩服过。",
 "So here's *my* deal [beat] this and every day henceforth... consider yourself *part of the family*.":
    "所以这*就是我的*条件[beat] 从今天起，以后的每一天……就当你是*家里人*了。",
 "{HappyA}My sincerest congratulations on your new employment.":
    "{HappyA}衷心祝贺你找到新工作。",
 "{InquireA}There's no insurance but {SmugA}there's bagels on Fridays.":
    "{InquireA}没有保险，但{SmugA}周五有贝果。",
 "What! No way! That is *so* completely not what I-- that's-- this is just *so* uncool, Vallory, really.":
    "什么！不行！这完全不是我——这——这也太不地道了，瓦洛里，真的。",
 "I prefer the term \"family member\" [beat] But you're free to call it whatever you like.":
    "我更愿意叫“家庭成员”[beat] 但你爱怎么叫都行。",
 "So what you're saying is... I'm your servant, basically, right?":
    "所以你的意思是……基本上我就是你的仆人了，对吧？",
 "You're a dick, Vallory. A giant dick.": "你是个混蛋，瓦洛里。一个大混蛋。",
 "Naw, it's okay. She's earned the license to blow off a little steam.":
    "不不，没事。她有资格发发牢骚。",
 "Dear. I wouldn't.": "亲爱的。我不会那样。",
 "You are *such* a--[gets stopped]": "你真是*个*——[gets stopped]",
 "You work for me now.": "你现在替我干活了。",
 "I'm forgettin' the legal language, but... as I recall it's a fairly strict oath.":
    "我记不清那些法律用语了，但……我记得那是份相当严格的誓约。",
 "I'll have somebody forward it over to ya.": "我会让人转给你。",
 "August, get in touch with your boy.": "August，联系你的人。",
 "{AngryA}And get it set up *away* from here. {SternA}I don't want a bunch of goose-steppin' Hyperion goons anywhere near Hollow Point.":
    "{AngryA}而且安排在*远离*这儿的地方。{SternA}我不想让一群踢正步的 亥博龙打手靠近空心镇。",
 "{NeutralA}Firm it up with Shade down in Prosperity Junction.":
    "{NeutralA}去繁荣枢纽找 Shade 把这事敲定。",
 "And you'll go with Fiona and her old man to watch over this deal.":
    "你跟着 Fiona 和她那老头一起去盯着这笔交易。",
 "And what about them?": "那他们呢？",
 "{NeutralA}On it.": "{NeutralA}这就去。",
 "I don't care if it's a thirteen *day* drive.": "我不在乎是不是要开十三*天*的车。",
 "What? That's like a thirteen hour drive!": "什么？那大概要开十三个小时！",
 "I don't trust nobody else to handle a deal like this.": "这种买卖我不信别人能办。",
 "And don't talk back.": "别顶嘴。",
 "[super whiny] Ohhhhh man, *fine*.": "[super whiny] 哦……好吧，*行*。",
 "You *grift* people for a livin', girl.  This here's a straight-up cash deal, no fuss no muss.":
    "你靠*骗*人吃饭，姑娘。这单是干干净净的现金交易，不吵不闹。",
 "Come on, Val.  I don't *need* a babysitter. I do this sort of thing for a *living*.":
    "别这样，Val。我*不需要*保姆。我靠这种事*谋生*。",
 "Oh my God, why are you making everything *suck* right now!":
    "我的天，你干嘛非要把现在的一切都搞*烂*！",
 "That's not-- the twist ties get all weird sometimes!": "那不是——扎带有时候会变得很怪！",
 "August!? August will screw it all up! He needs *help* tying up the garbage!":
    "August？！August 会把一切都搞砸！他连捆垃圾都*需要帮忙*！",
 "Enough, both of ya.": "够了，你们两个。",
 "I am protectin' my own interests, girl. The gettin's not good until it's gottin'.":
    "我是在保护我自己的利益，姑娘。东西没到手之前都不算顺利。",
 "[sarcastic] I'm devastated.": "[sarcastic] 我心都碎了。",
 "I don't even know what that means.": "我根本不知道那是什么意思。",
 "Well,  then -- what's everybody waitin' for.": "那好——大家还在等什么。",
 "Understand the concept here, Fiona.": "把这里的道理搞清楚，Fiona。",
 "You and your little gray-haired chew-toy over there are gonna sit nice and quiet with your hands folded neatly in your laps -- and if *any* measure of this thing goes *slightly* amiss...":
    "你和你那边那个花白头发的小磨牙玩具要乖乖安静地坐着，双手整齐地叠在膝盖上——要是这件事有*任何*一点*稍微*出了岔……",
 "Gee, I'm getting that \"part of the family\" warm fuzzy feeling already.":
    "哎呀，我已经感受到那种“家里人”的暖融融的感觉了。",
 "Shoot ya!": "就毙了你！",
 "Is it now?": "是吗？",
 "Ughgh, God, August, that's not-- ugh!": "呃呃，天哪，August，那不是——呃！",
 "Ughhgh! No!": "呃啊！不！",
 "[muttering] It's kind of a hard rule to follow, to be honest.":
    "[muttering] 说实话，这条规矩挺难遵守的。",
 "[muttering to herself] I imagine the turnover for these guys is unusually high.":
    "[muttering to herself] 我看这些人的离职率高得不正常。",
 "Buzz off, you're buggin' me.": "滚开，你在烦我。",
 "I *really* *need* to talk to Vallory, Kroger.": "我*真的* *需要*跟 瓦洛里 谈谈，克罗格。",
 "You are gonna be in *so* much trouble when she finds out...": "等她知道了你会*倒大霉*的……",
 "I need a sit down with Vallory.": "我需要跟 瓦洛里 坐下来谈。",
 "[light laughter] Ain't gonna happen, sweetpea, sorry.":
    "[light laughter] 不会发生的，小甜豆，抱歉。",
 "{angryB}I don't believe this.": "{angryB}我简直不敢相信。",
 "That ain't you, kid.": "那画的不是你，孩子。",
 "Look, I have kind of a good eye for faces, alright? Never names, but... faces I do alright.":
    "听着，我认脸还挺准的，行吗？名字从来记不住，但……脸我认得还行。",
 "That girl has completely different hair!": "那姑娘的头发完全不一样！",
 "What? Are you kidding?": "什么？你开玩笑吧？",
 "See that poster over there? The one that says \"Wanted?\"": "看到那边那张海报了吗？写着“通缉”的那张。",
 "Will you just-- just let me through! Vallory needs to talk to me.":
    "你能不能——就让我过去！瓦洛里 要跟我说话。",
 "Not. Gonna. Happen.": "绝。对。不。会。",
 "That's *me*, so, in a sort of official capacity Vallory really wants to see me.":
    "那就是*我*，所以，以某种官方身份来说，瓦洛里 真的很想见我。",
 "Huh. [beat] Is seven Aces good or bad?": "嗯。[beat] 七个 A 是好还是坏？",
 "[enraged] What!": "[enraged] 什么！",
 "Hey. Anybody seen Vallory around? I really need a meeting.":
    "嘿。有人见到 瓦洛里 吗？我真的需要见一面。",
 "[flat] Thanks.": "[flat] 谢了。",
 "[being hit with a bottle] Arghghgh!": "[being hit with a bottle] 啊啊啊！",
 "[unamused] I'm a heavy sleeper.": "[unamused] 我睡得很沉。",
 "No, Fiona. It isn't. [beat, unamused] Just you.": "不，Fiona。不是。 [beat, unamused] 只有你。",
 "My friends Mr. Finch and Mr. Kroger will do what I should have done when you first walked in here.":
    "我的朋友 芬奇 先生和 克罗格 先生会去做你刚进门时我就该做的事。",
 "Go to hell.": "滚一边去。",
 "But I get most of my bakin' tips from magazines, so... who knows how that woulda turned out.":
    "但我的烘焙窍门大多是杂志上看来的，所以……谁知道会是什么结果。",
 "To *cleanse* the degradation or some such.": "去*洗净*那份屈辱什么的。",
 "Make one of my *boys* here track ya down, bring your heart back, in a little... black box all lady-like.":
    "让我这儿的一个*小子*把你找出来，把你的心带回来，装在一个小小的……淑女风格的黑盒子里。",
 "I, uh... I wouldn't want to leave you in suspense...":
    "我，呃……我可不想让你悬着心……",
 "Has a bit of a bite.": "有点冲。",
 "I know. That's why I laughed.": "我知道。所以我才笑。",
 "I'm not joking.": "我没开玩笑。",
 "I gotta say, honey, you're actin' like someone who just wants to cut your visit short, if you catch my meanin'.":
    "我得说，宝贝，你这副样子像是想早点结束这次拜访，如果你懂我意思的话。",
 "Bein' cool and collected is one thing but you're turnin'... *stillness* into an artform. And I just can't work with someone like that.":
    "冷静自持是一回事，但你是在把……*静止*变成一门艺术。我实在没法跟这样的人打交道。",
 "Bein' assertive is one thing but... don't act like this is your bar, girl, cause it most certainly ain't.":
    "有主见是一回事，但……别表现得这是你的酒吧，姑娘，因为它绝对不是。",
 "And this talk ain't gonna go well for you if you continue to cop a bum attitude.":
    "你要是继续摆出这副臭态度，这谈话对你不会有什么好处。",
 "You're actin' like someone who has to somethin' to live for, so... I'm sure this is gonna go finely well.":
    "你这副样子像是还有值得活下去的东西，所以……我相信这会谈得非常顺利。",
 "You're certainly puttin' your best foot forward, I can see that.":
    "你确实在努力拿出最好的一面，我看得出来。",
 "Though I surely acknowledge the attempt at flattery. Keep that up and this'll go finely well.":
    "不过我当然认可你这份讨好的努力。继续保持，这就会谈得非常顺利。",
 "Here's a little piece of advice for you, girl...": "给你一点小建议，姑娘……",
 "Don't cop an attitude when you first walk in and then tell somebody they've lost some weight.":
    "别一进门就摆臭脸，然后又跟人客套说人家瘦了。",
 "Don't act like this a Sunday picnic, and surely don't act like we're best of friends. We ain't, so... a little respect comin' from you is required, unfortunately.":
    "别表现得这像周日野餐，更别表现得我们是最好的朋友。我们不是，所以……很遗憾，你得拿出点尊重。",
 "You remember that and this'll go just fine.": "你记住这点，这事就会很顺利。",
 "So polite this evening. [beat] You must be up to something.":
    "今晚这么有礼貌。[beat] 你肯定在打什么主意。",
 "There. Bein' polite isn't so hard after all.": "看吧。讲礼貌其实也没那么难。",
 "Oh, and just when I thought we were gettin' off on the right foot.":
    "哦，偏偏在我以为我们开了个好头的时候。",
 "Remember what I said, girlie. [beat] Lose the attitude.":
    "记住我说的话，丫头。[beat] 把那副态度收起来。",
 "Fastly now.": "快点。",
 "[correcting him] No. *Bring* her *back* to *me* for a suitable... chastising.":
    "[correcting him] 不。把她*带*回*到*我这儿来，好好……训一顿。",
 "As in Vallory *wants* to see me.  [beat]That's it? I get nothin'? [...SIGH]":
    "也就是说 瓦洛里*想*见我。[beat]就这样？我什么都没有？[...SIGH]",
 "FIONA LOOKS TO THE SIDE... SITTING DAINTILY ON THE BAR IS A SMALL SIGN":
    "FIONA 向旁边望去……吧台上端端正正摆着一块小牌子",
 "BARTENDER DOES NOT GIVE ADVICE, CHIT-CHAT, OR HAVE A LARYNX.":
    "酒保不提供建议、不闲聊，也没长喉头。",
 "[SIGH]": "[SIGH]",
 "Shoo fly.": "走开，苍蝇。",
 "I don't know what her *freakin'* problem is.": "我不知道她他妈*有什么毛病。",
 "Those two guys exploded for no reason, I was just providing color commentary!":
    "那两个人无缘无故就炸了，我只是在旁边解说而已！",
 "Careful now.": "小心点。",
 "Don't much care for surprises.": "我可不太喜欢意外。",
 "And put a little [German] *zitrone*, in it.": "再加一点 [German] *柠檬*。",
 "[subtext: shut up, lackey] I know.": "[subtext: shut up, lackey] 我知道。",
 "But it's not *their* picture up all over town.": "但贴满全镇的可不是*他们*的照片。",
 "Now, I don't judge a woman's livlihood.": "我不评判一个女人靠什么谋生。",
 "Why did you dare come here, Fiona?": "你怎么敢来这儿，Fiona？",
 "He'll be back soon enough. \nVALLORY But right now I'd suggest worrying about yourself.":
    "他很快就会回来。\nVALLORY 但现在我建议你担心一下你自己。",
 "And I suppose... *don't* poison Fiona's.": "还有我想……*别*往 Fiona 的酒里下毒。",
 "Never know when it might be your last. [beat] It's a dangerous world we live in.":
    "谁知道哪杯会是最后一杯。[beat] 我们生活的世界很危险。",
 "Yeah [beat] I can't think of any reason, either.": "是啊[beat] 我也想不出任何理由。",
 "[ditz act] They were out of the chocolate things with the sprinkes.":
    "[ditz act] 他们那种撒糖屑的巧克力卖完了。",
 "August, I thought I told you to [gritted teeth] get rid of her.":
    "August，我以为我告诉过你[gritted teeth] 把她处理掉。",
 "Sure thing, ma.": "没问题，妈。",
 "Thanks, sweetheart.": "谢谢，甜心。",
 "I'm lookin' at my old pal August. Don't you remember me bud?":
    "我在看我的老朋友 August。你不记得我了吗，哥们？",
 "[to Fiona] What were you thinking, coming round here?":
    "[to Fiona] 你在想什么，跑这儿来？",
 "Hey, that's the girl that swindled cousin Ralph.": "嘿，就是那姑娘骗了 Ralph 表哥。",
 "Just stopped by for a nice drink with your mother.": "只是过来跟你妈喝杯好酒。",
 "Just stopped by to visit old friends.": "只是过来看看老朋友。",
 "I was thinking I have an incredible deal, and who else but Vallory and her boy August to broker it.":
    "我在想我手上有个绝佳的交易，能撮合它的除了 瓦洛里 和她的宝贝 August 还能有谁。",
 "I think you're interrupting this deal between me and *your mother*.":
    "我觉得你在打断我和*你妈*之间的这笔交易。",
 "Fiona's not really one for thinkin', August.": "Fiona 可不是爱思考的类型，August。",
 "So... [really directed at Sasha] glad you could join us.":
    "那……[really directed at Sasha] 很高兴你能加入我们。",
 "[really directed at Sasha] That we're already in the middle of.":
    "[really directed at Sasha] 我们已经在进行中了。",
 "Ain't that right, Fiona.": "对吧，Fiona。",
 "*I* have a Vault Key.": "*我*有一把秘藏钥匙。",
 "I can get a Vault Key.": "我能弄到一把秘藏钥匙。",
 "*I* have a Vault Key!": "*我*有一把秘藏钥匙！",
 "I HAVE a Vault Key!": "我*有*一把秘藏钥匙！",
 "I have a VAULT KEY!": "我有一把*秘藏钥匙*！",
})

# —— 亮出钥匙 + 编故事 ——
T.update({
 "Yeah... that kinda thingy.": "是啊……就那种玩意儿。",
 "A Vault Key?": "秘藏钥匙？",
 "I... I, uh, saw her with some glowing alien Vault Thingy.":
    "我……我，呃，看见她拿着个发光的、外星来的秘藏玩意儿。",
 "[incredulous] You?": "[incredulous] 你？",
 "I *have* a Vault Key.": "我*有*一把秘藏钥匙。",
 "[air quotes] \"Have\"?": "[air quotes] “有”？",
 "I have a *Vault Key*.": "我有一把*秘藏钥匙*。",
 "[incredulous] A Vault Key?": "[incredulous] 一把秘藏钥匙？",
 "But it being her and all it also coulda been ... uh... a really fancy lampshade.":
    "但考虑到是她，那也有可能……呃……是个特别华丽的灯罩。",
 "I don't. [turns to Finch] Finch does.": "我没有。[turns to Finch] 芬奇 有。",
 "You don't want to go anywhere near that smelly old dude in that smelly old van to get it.":
    "你不会想靠近那辆臭烘烘的破货车里那个臭烘烘的老家伙去拿它的。",
 "So, what's this great deal is it I shouldn't shoot you right now?":
    "那么，这个能让我现在不开枪打你的绝佳交易是什么？",
 "It's a funny story, that...": "这事说来挺有意思的……",
 "I found": "我找到的",
 "Well [beat] ain't that something.": "这个嘛[beat] 真不简单。",
 "We want that key, August.": "我们想要那把钥匙，August。",
 "I saw her put it in that van of hers -- her and that weird old guy she hangs out with.":
    "我看见她把它放进她那辆货车里——她和她那个古怪的老家伙。",
 "But you don't want to go in there to get it [beat] it smelled like wet dog and unwashed underpants.":
    "但你不会想进去拿的[beat] 那里面闻着像湿狗和没洗的内裤。",
 "I don't. [looks at Finch] But Finch does.": "我不想。[looks at Finch] 但 芬奇 想。",
 "Come on, August, let's get rich.": "来吧，August，我们一起发财。",
 "[whispered to August] She doesn't realize how much you could sell that thing for. Her offer is a steal.":
    "[whispered to August] 她不知道那东西能卖多少钱。她开的价简直是白送。",
 "[whispered to Vallory] She doesn't realize how much *I* could sell that thing for.  Her offer is a steal.":
    "[whispered to Vallory] 她不知道*我*能把它卖多少钱。她开的价简直是白送。",
 "Sasha, let ma work, will ya?": "萨莎，让妈干活，行吗？",
 "Oooh.  You should keep it and wear it as a crown.  It's so cute.":
    "哦哦。你该留着它当皇冠戴。太可爱了。",
 "August, keep your pet on its leash.": "August，把你的宠物拴好。",
 "So what did you have in mind?": "那你有什么打算？",
 "It's not exactly my usual line of work.": "这不太算是我平时的行当。",
 "A criminal mastermind of such reknown must know someone who knows a buyer for such a rare artifact.":
    "如此声名远扬的犯罪天才，肯定认识认识这种稀世珍品买家的人。",
 "Surely an organization such as yours has the muscle to make it into the vault.":
    "像你们这样的组织肯定有实力进入秘藏。",
 "You take it off my hands and it's yours to do with as you please. [beat] You could put it up on the bar as a decoration for all I care.":
    "你从我这拿走，就随你怎么处置了。[beat] 你把它摆在吧台上当装饰我都不管。",
 "I know a lot of people. [beat] Most of 'em dead.": "我认识很多人。[beat] 大多都死了。",
 "Mom, I -- [gets cut off] can do it.": "妈，我——[gets cut off] 能办到。",
 "Flattery will get you far in this town. [beat] But we certainly ain't got that kinda muscle.":
    "在这镇上拍马屁很有用。[beat] 但我们确实没有那种实力。",
 "This ain't the sort of thing to let pride get mixed-up in, darlin'.":
    "这种事可不能掺进什么自尊心，亲爱的。",
 "Right next to your pickled head, you keep up that attitude.":
    "就摆在你那颗腌渍脑袋旁边，你要是继续这态度的话。",
 "Because you're the best.": "因为你是最棒的。",
 "Come on, August...": "拜托，August……",
 "She is. [to Fiona] Why should I deal with you at all, Fiona?":
    "她确实是。[to Fiona] 我干嘛要跟你打交道，Fiona？",
 "[to Vallory] She's right. I am the best. [beat] And I know a guy.":
    "[to Vallory] 她说得对。我就是最棒的。[beat] 而且我认识一个人。",
 "Because' you're the best fence in town, August.  Nobody else can make this deal work but you.":
    "因为你是镇上最棒的销赃人，August。除了你没人能把这交易做成。",
 "[to Sasha] Sasha, baby, don't take this personally [beat,to Fiona] but yeah, okay, I'll do it for love.":
    "[to Sasha] 萨莎，宝贝，别往心里去[beat,to Fiona] 但好吧，行，我为爱而做。",
 "Because whatever you may think of *her* [indicates Sasha], your one true love is money. And this thing is worth a fortune.":
    "因为不管你怎么看*她*[indicates Sasha]，你唯一的真爱是钱。而这东西值一大笔钱。",
 "Because Vallory loves a big score.": "因为 瓦洛里 喜欢大买卖。",
 "Alright, August, if you do indeed know a guy...": "好吧，August，如果你真认识一个人……",
 "Which means mommy says so [beat] right, Val?": "也就是说妈妈批准了[beat] 对吧，Val？",
 "Look, Val, I mean *Mom*, even if the universe did just *gift* this crazy chick a freakin' *Vault Key*.":
    "听着，Val，我是说*妈*，就算宇宙真的*白送*了这疯姑娘一把该死的*秘藏钥匙*。",
 "Come on! I don't even know what that is. Keys are gold with that hoop thing at the end and a big pointy part. That's like an alien lawnmower engine or something.":
    "拜托！我根本不知道那是什么。钥匙是金色的，末端有个圆环，还有一大截尖的。那玩意儿就像外星割草机的引擎什么的。",
 "How'd she even get it?  Have sex with a lepreuchan.": "她怎么弄到的？跟矮精灵上床吗。",
 "August, would you look at that -- ain't it something.":
    "August，你瞧瞧这个——真不简单啊。",
 "August, would you look at that? It's -- [gets cut off] incredible.":
    "August，你瞧瞧这个？真是——[gets cut off] 不可思议。",
 "Ta-da!": "哒哒！",
 "My gut says we're in no position to handle a deal that -- [gets cut off] massive.":
    "我的直觉说我们没能力处理这么——[gets cut off] 庞大的交易。",
 "Ma, don't mind Sasha, she's just got a lot of thoughts [beat] that don't know enough to stay inside her head.":
    "妈，别理 萨莎，她就是想法太多[beat] 多到不知道该待在她脑子里。",
 "No such thing as a deal too big.": "没有什么交易是太大的。",
 "Well if *she* thinks it's a bad idea, it must be the deal of the century.":
    "既然*她*觉得是个坏主意，那这肯定是世纪级的交易。",
 "Alright, August, you know a guy... right?": "好吧，August，你认识一个人……对吧？",
 "I've been wrong before, right? [beat] But if I'm right, can you afford to pass this up?":
    "我以前也判断错过，对吧？[beat] 但要是我判断对了，你舍得放过这个机会吗？",
 "Hey, maybe she's right.  Maybe I am wrong about how valuable this thing is.":
    "嘿，也许她说得对。也许我对这东西的价值判断错了。",
 "You're the boss around here, right?": "这儿你是老大，对吧？",
 "Come on Vallory, who cares what this chickadee thinks?":
    "拜托 瓦洛里，谁在乎这小妞怎么想？",
 "This is the deal of the century, Val.  No, of the millennium.  Perhaps of the -- [gets cut off] eon.":
    "这是世纪级的交易，Val。不，是千年级的。也许是——[gets cut off] 亿万年级的。",
 "But a Hyperion stooge sounds like the right kind of sucker to me.":
    "但在我听来，亥博龙的走狗就是最合适的那种冤大头。",
 "After all, this was *my* whole *thing*!": "毕竟这*本来就是*我的*主意*！",
 "Hey! Don't you talk to my ma -- [gets cut off] like that.":
    "嘿！别那样跟我妈——[gets cut off] 说话。",
 "Welcome to the first day of the rest of your life, Fiona.":
    "欢迎来到你余生的第一天，Fiona。",
 "With Vault Hunters crawlin' up alien assholes to catch just a sniff of somethin' like this... just how did a lowlife grifter like you get your pretty lil' hands on a Vault Key?":
    "秘藏猎人为了闻一口这种东西都得钻进外星人的屁股里……像你这种下三滥的骗子，到底是怎么把那漂亮小手伸到一把秘藏钥匙上的？",
 "Take that one back to the truck.": "把那一个带回车上去。",
 "Alright, ma.  I'm on it.": "好，妈。我这就去。",
 "So everyone's in agreement, then? [beat] Good.": "那大家都同意了？[beat] 好。",
 "We'll need the muscle in case anything goes screwy.": "万一出岔子，我们需要打手。",
 "Thank you so much, that's fantastic.": "太感谢了，这太棒了。",
 "Quit whinin' and pay up.": "别哼哼了，付钱。",
 "Aigh! My eye! [beat] Damn you, I needed that eye!": "哎哟！我的眼睛！[beat] 你这该死的，我需要那只眼睛！",
 "WHEN FIONA WALKS PAST THE BAR, SHE GLANCES AT THE BARTENDER AND SMILES.  THEN SHE NOTICES":
    "FIONA 走过吧台时，朝酒保瞥了一眼并微微一笑。然后她注意到",
 "A SIGN on the bar reads:\tBARTENDER DOES NOT GIVE ADVICE, CHIT-CHAT, OR HAVE A LARYNX.":
    "吧台上的一块牌子写着：\t酒保不提供建议、不闲聊，也没长喉头。",
 "A SIGN on the bar reads:\tBARTENDER DOES NOT GIVE ADVICE, CHIT-CHAT, OR HAVE A LARYNX.  A moment later, as Sasha passes by a \"wall of fame\" covered with the same WANTED POSTERS as the pole outside, two GOONS step out in front of Fiona: FINCH & KROGER.  They point at her Wanted Poster.":
    "吧台上的一块牌子写着：\t酒保不提供建议、不闲聊，也没长喉头。片刻之后，萨莎 走过一面“名人墙”，上面贴满了跟外面柱子上一样的通缉海报，两个打手挡在 Fiona 面前：FINCH 和 KROGER。他们指着她的通缉海报。",
 "And we get an easy thirty-seven fifty. No fuss, no muss.":
    "我们还能轻松赚三十七块五。不吵不闹。",
 "You don't look like nothin' much, girlie. So just keep calm and soon you'll be getting free room and board from the Sheriff --":
    "你看起来也不像什么大人物，丫头。所以保持冷静，很快你就能从警长那儿领到免费的食宿——",
 "Oh come on, I already did this like five minutes ago.":
    "哦拜托，我大概五分钟前刚做过这套。",
 "I mean the part where Vallory holds you responsible for her losing forty grand.":
    "我是说 瓦洛里 要你为她损失四万块负责那部分。",
 "Forty grand? [scoffs] I should shoot you right here for having a smart mouth.":
    "四万？[scoffs] 就凭你嘴硬，我就该在这儿毙了你。",
 "Is it really worth it?": "真的值得吗？",
 "Ain't no trouble walking you across town.": "押你走一趟镇上也不算麻烦。",
 "Calm it, Kroger. If she's on the up-and-up, crossing Vallory ain't worth it for thirty-seven fifty.  [beat, to Fiona] So whatcha on about, kid?":
    "冷静点，克罗格。要是她说的是真的，为了三十七块五得罪 瓦洛里 可不划算。[beat, to Fiona] 那你想说什么，孩子？",
 "{HappyA}Oh, there you are. Come on, {NeutralA}Vallory's right over here.":
    "{HappyA}哦，你在这儿。来，{NeutralA}瓦洛里 就在那边。",
 "We're lucky, she's in an unusually good mood today.":
    "我们运气不错，她今天心情好得出奇。",
 "[low voice] {ThinkB}Sasha's sister Fiona is here to see you.":
    "[low voice] {ThinkB}萨莎 的姐姐 Fiona 来见你。",
 "{SternA}Alright, Tommy... since your father is my favorite cousin I'm {InquireA}gonna go ahead and -- [trails off] cut you a {SternA}break on this.":
    "{SternA}好吧，Tommy……既然你爸是我最喜欢的表弟，我就{InquireA}干脆——[trails off] 在这事上给你{SternA}打个折。",
 "[all business]As you can see, Fiona, I'm in the {InquireA}middle of something right now.":
    "[all business]如你所见，Fiona，我现在{InquireA}正忙着。",
 "[sweet-ish] {SmugA}Hollow Point's favorite little flim-flam gal, all grown up. How sweet.":
    "[sweet-ish] {SmugA}空心镇最爱耍花招的小姑娘，都长这么大了。真甜。",
 "{InquireA}And Tommy and I have some more things to discuss.":
    "{InquireA}而我和 Tommy 还有些事要谈。",
 "{ThinkA}My mom is a busy woman.": "{ThinkA}我妈是个大忙人。",
 "{InquireA}It's only the {SchemeA}deal of a lifetime for both of us.":
    "{InquireA}这对我们俩来说都是{SchemeA}一生一次的交易。",
 "{InquireA}Is it? Well now, that {SmugA}*does* sound important.":
    "{InquireA}是吗？那这{SmugA}*确实*听着挺重要。",
 "{SternB}It's definitely important {SternA}to *me*.":
    "{SternB}对我{SternA}来说*确实*很重要。",
 "{InquireA}Important enough for you {SternA}to interrupt my work?":
    "{InquireA}重要到{SternA}来打断我的工作？",
 "{DoubtfulA}If you're busy, I can certainly wait. [beat] {SmugA}I'll just sit right over there while you finish.":
    "{DoubtfulA}你要是忙，我当然可以等。[beat] {SmugA}我就坐那边等你忙完。",
 "{InquireA}Well, you've already interrupted me so we might as well {SternA}get on with it.":
    "{InquireA}既然你已经打断我了，那我们不如{SternA}直接开始。",
 "{SmugA}Well look what you've done now, Tommy.  {InquireA}You've gotten poor Fiona all flustered.":
    "{SmugA}看看你干的好事，Tommy。{InquireA}你把可怜的 Fiona 都弄慌了。",
 "Me?": "我？",
 "Aiiiiiiiiiiigh!": "啊啊啊啊啊！",
 "{NeutralA}Stick around, kiddo.": "{NeutralA}别走远，小家伙。",
 "[to the bartender] {AngryA}Get Tommy a glass of milk.":
    "[to the bartender] {AngryA}给 Tommy 来杯牛奶。",
 "[all business] So why are you here?": "[all business] 那你来这儿干什么？",
 "{NeutralA}Alright, Fiona, you've got my {SternA}full and undivided attention.":
    "{NeutralA}好吧，Fiona，你现在有{SternA}我全部的注意力。",
 "{SternA}Now let's hear about this deal of a lifetime.":
    "{SternA}现在说说这笔一生一次的交易吧。",
 "{SternA}Now what's {InquireA}so important to you that you've brought it {SternA}to *my* attention?":
    "{SternA}到底是什么对你{InquireA}这么重要，重要到要{SternA}来*找我*说？",
 "{SternA}And maybe you can wait, {NeutralA}but I'm not the patient type. So tell me, {SternA}what's the deal?":
    "{SternA}也许你能等，{NeutralA}但我不是有耐心的那种人。所以告诉我，{SternA}是什么交易？",
 "*I* am the proud owner of a Vault Key.": "*我*是这把秘藏钥匙的骄傲持有者。",
 "I have a Vault Key. Not a plan to get one in the future, but right here right now.":
    "我有一把秘藏钥匙。不是以后打算去弄一把，而是就在此刻、就在这儿。",
 "{SmugA}Only the most valuable thing I can {FearA}possibly think of [beat] {SchemeC}a *Vault Key*!":
    "{SmugA}我能{FearA}想到的最值钱的东西[beat] {SchemeC}一把*秘藏钥匙*！",
 "{ThinkB}So, Fiona, what do you want to talk {ThinkA}to my ma for, anyway?":
    "{ThinkB}那，Fiona，你到底想跟我妈{ThinkA}谈什么？",
 "{ThinkB}*We* did.  [points at Fiona] But {ThinkA}*we* didn't.":
    "{ThinkB}*我们*谈过了。[points at Fiona] 但{ThinkA}*我们*没谈过。",
 "[a little chastised, but still trying to be all business] Sasha, {WorryC}I'm working.":
    "[a little chastised, but still trying to be all business] 萨莎，{WorryC}我在工作。",
 "{SternC}Stop. [beat] Nobody approaches my ma without {SternA}my permission.":
    "{SternC}站住。[beat] 没有{SternA}我的允许，谁都不能接近我妈。",
 "We already {SternB}talked about this.": "我们{SternB}已经谈过这个了。",
 "{InquireA}Don't be ridiculous, August. {SternA}It's me.":
    "{InquireA}别荒唐了，August。{SternA}是我。",
 "I'm her gatekeeper, so": "我是她的守门人，所以",
 "{ThinkB}Oh, alright. Come on.": "{ThinkB}哦，好吧。来吧。",
 "{SternA}What I'm here to discuss doesn't {SternB}concern you, August. It's between {SternA}me and Vallory.":
    "{SternA}我来要谈的事{SternB}跟你无关，August。这是{SternA}我和 瓦洛里 之间的事。",
 "{SternC}Anything that concerns my ma  -- [trails off] {WorryA}concerns me...":
    "{SternC}任何跟我妈有关的事——[trails off] {WorryA}都跟我有关……",
 "{AngryA}Don't act all tough with me, August.": "{AngryA}别跟我装硬，August。",
 "Well... yeah. Of course I do.": "这个……是啊。我当然知道。",
 "{InquireA}I want to talk about something that could make us all a lot of money. [beat] {SchemeC}You do still like money, right?":
    "{InquireA}我想谈一件能让我们大家都赚一大笔的事。[beat] {SchemeC}你还是喜欢钱的吧？",
 "And so does your ma.": "你妈也是。",
 "{SternA}She just wants to talk to her about deal stuff. {AngryA}Why are you being {SternB}like this?":
    "{SternA}她只是想跟她谈交易的事。{AngryA}你这是{SternB}干什么？",
 "{SternB}I just want to talk to Vallory {SternA}about a deal.":
    "{SternB}我只是想跟 瓦洛里{SternA}谈一笔交易。",
 "{SternA}Don't leave me {NeutralA}guessing, Fiona.  Why have you {SternA}come to see me?":
    "{SternA}别让我{NeutralA}猜，Fiona。你{SternA}来见我是为了什么？",
 "Thank you for taking the time to see us -- [gets cut off] Ma Vallory.":
    "谢谢你抽时间见我们——[gets cut off] 瓦洛里 妈。",
 "Better not be a waste of our time.": "最好别浪费我们的时间。",
 "What do you have for me?": "你有什么要给我的？",
 "Well isn't that something.": "真不简单啊。",
 "{ShockB}I ain't never seen anything like it.": "{ShockB}我从没见过这种东西。",
 "{InquireA}Now Fiona... you don't really {SternA}expect me to believe that thing is real, {InquireA}do you?":
    "{InquireA}那么 Fiona……你不会真的{SternA}指望我相信那东西是真的{InquireA}吧？",
 "That *you*, of all small-time scoundrels, just happens to have one of the rarest things in the universe?":
    "你，在所有小打小闹的混混里，偏偏就有一件宇宙中最稀罕的东西？",
 "{NeutralB}I totally understand your skepticism, {InquireA}but trust me -- it's {SchemeC}definitely real.":
    "{NeutralB}我完全理解你的怀疑，{InquireA}但相信我——它{SchemeC}绝对是真的。",
 "{SmugC}Of course I don't expect a pro like {DoubtfulA}yourself to be gullible enough to think{SmugA} it's real.":
    "{SmugC}我当然不会指望像{DoubtfulA}你这样的老手会天真到{SmugA}相信它是真的。",
 "So... {SternA}Is this important?": "那……{SternA}这重要吗？",
 "So if this is just some kinda lark...": "所以如果这只是什么胡闹……",
 "Yeah, are you sure it's real? I mea": "是啊，你确定是真的吗？我是说",
 "{SmugA}A real Vault Key, huh?": "{SmugA}一把真的秘藏钥匙，是吧？",
 "{SternA}Come on, are you really {InquireB}sure it's real, Fiona?":
    "{SternA}得了吧，你真的{InquireB}确定它是真的吗，Fiona？",
 "After all, some {InquireA}*guy* just gave it to you.":
    "毕竟，是某个{InquireA}*男人*把它给了你。",
 "[to August] {AngryA}*You* better not go off and give anyone anything like {SternA}*that* as a courting gift.":
    "[to August] {AngryA}*你*最好别拿{SternA}*那种*东西当求爱礼物送人。",
 "After all, you did just {InquireA}find it in some {SternA}musty old cave.":
    "毕竟，你只是{InquireA}在某个{SternA}发霉的老山洞里找到的。",
 "{AngryA}Where else would {SternA}someone find a Vault key?":
    "{AngryA}不然{SternA}还能在哪儿找到秘藏钥匙？",
 "After all, you did just con some {InquireA}sucker out of it.":
    "毕竟，你只是从某个{InquireA}冤大头手里骗来的。",
 "{InquireA}How else would Fiona get her {SternA}hands on a Vault Key?":
    "{InquireA}不然 Fiona 还能怎么{SternA}弄到一把秘藏钥匙？",
 "{HappyA}Even better  -- {HappyC}*we* won't get gunned-down{HappyA} by a Vault Hunter.":
    "{HappyA}更好的是——{HappyC}*我们*不会被秘藏猎人{HappyA}开枪打死。",
 "{SmugC}We'll make out like bandits.": "{SmugC}我们会像土匪一样大赚一笔。",
 "{HappyC}Just think about it , August.  {HappyB}A real, genuine, honest-to-goodness {HappyC}Vault Key.":
    "{HappyC}你想想，August。{HappyB}一把货真价实、如假包换的{HappyC}秘藏钥匙。",
 "{ThinkA}Yeah, Fiona. This {ThinkB}isn't your usual {SmugA}\"let's sell a bunch of psychos some apples and convince them they're {ThinkB}grenades\" sort of deal.":
    "{ThinkA}是啊，Fiona。这{ThinkB}可不是你平时那种{SmugA}“卖给一群疯子几个苹果，然后让他们相信那是{ThinkB}手雷”的交易。",
 "Yeah, Fiona.  {SlyA}Did the Vault Key fairy just leave it under your pillow?":
    "是啊，Fiona。{SlyA}是秘藏钥匙仙子把它放在你枕头底下的吗？",
 "{DoubtfulA}I've been dating this Vault Hunter and he gave it to me as {SchemeA}an engagement present.":
    "{DoubtfulA}我一直在跟一个秘藏猎人交往，他把它当作{SchemeA}订婚礼物送给我了。",
 "{WorryA}Yes, ma'am.": "{WorryA}是的，女士。",
 "{HappyA}I found it in that abandoned {DoubtfulA}mine just outside of town.":
    "{HappyA}我在镇外那座废弃的{DoubtfulA}矿里找到的。",
 "{SmugA}I swindled it from some {SchemeA}Crimson Raider who'd been tasked with guarding it.":
    "{SmugA}我从一个负责看守它的{SchemeA}猩红掠夺者手里骗来的。",
 "[to Vallory] {NeutralB}Trade secret. {SmugB}You know how that goes.":
    "[to Vallory] {NeutralB}商业机密。{SmugB}你知道这一行的。",
 "[to August] {SternA}She can't really say.  {InquireA}It's a trade secret, and all that.":
    "[to August] {SternA}她不能说。{InquireA}这是商业机密，之类的。",
 "{HappyA}Oh, it's a {HappyC}great story.  You're gonna love it, Ma -- {SmugA}mind if I just call you Ma? -- it all started {SmugB}one day when Fiona was -- [gets cut off] running a con on some suckers...":
    "{HappyA}哦，这是个{HappyC}精彩的故事。你会喜欢的，妈——{SmugA}我可以直接叫你妈吗？——{SmugB}一切都始于有一天 Fiona——[gets cut off] 在骗几个冤大头的时候……",
 "[annoyed] {AngryA}Never mind. She got it, {SternA}here it is, that's that.":
    "[annoyed] {AngryA}算了。她弄到了，{SternA}就在这儿，就这样。",
 "[considering] {SternA}Well... a *Vault Hunter* {NeutralA}would have a real Vault Key...?":
    "[considering] {SternA}这个……一个*秘藏猎人*{NeutralA}确实会有一把真秘藏钥匙……？",
 "Makes sense, it being an Eridium mine and all.": "说得通，毕竟那是个镒矿矿场。",
 "You think they'd have sent someone smarter to guard something like that.":
    "我以为他们会派个更聪明的人去守那种东西。",
 "[considering] {InquireA}Well... those do-gooders {NeutralA}*are* all a bit dim.":
    "[considering] {InquireA}这个……那些行善的家伙{NeutralA}*确实*都有点迟钝。",
 "[considering] {InquireA}Well... that {NeutralA}*is* an old Eridium mine...":
    "[considering] {InquireA}这个……那{NeutralA}*确实*是个废弃的镒矿矿场……",
 "{InquireA}Let's say, for the sake of argument, you {NeutralA}do have a real Vault Key.":
    "{InquireA}我们姑且假设，你真的{NeutralA}有一把真秘藏钥匙。",
 "What are you gonna {SternA}do with it?": "你打算拿它{SternA}怎么办？",
 "{NeutralA}Okay, Fiona...": "{NeutralA}好吧，Fiona……",
 "{SternA}Hardly anyone has.": "{SternA}很少有人有。",
 "{SmugA}I mean... never mind the{SmugB} Vault Monster...":
    "{SmugA}我是说……先不提那个{SmugB}秘藏怪物……",
 "{SmugA}You're certainly not going to try to open a Vault.":
    "{SmugA}你肯定不会真去打开一个秘藏。",
 "The Vault {SlyC}*Janitor* would take *you* {SlyA}down, Fiona.":
    "秘藏里的{SlyC}*清洁工*就能把*你*{SlyA}收拾掉，Fiona。",
 "{InquireA}We already have a{SchemeA} buyer lined-up.":
    "{InquireA}我们已经找好{SchemeA}买家了。",
 "{DoubtfulA}Some wanna-be Vault Hunter {InquireA}chump in Sanctuary is willing to pay a {SmugA}hundred grand for it.":
    "{DoubtfulA}避风港有个想当秘藏猎人的{InquireA}蠢货愿意出{SmugA}十万买它。",
 "[considering] {InquireA}A hundred grand, huh?": "[considering] {InquireA}十万，是吗？",
 "{InquireA}And you just came here to brag about it, hoping to {SternA}impress us?":
    "{InquireA}你就跑来这儿炫耀一下，指望{SternA}震住我们？",
 "[insulted] {InquireA}Well maybe I {AngryA}*am* going to open {SternA}the Vault.":
    "[insulted] {InquireA}也许我{AngryA}*真*打算打开{ SternA}秘藏。",
 "{HappyA}So glad you asked.": "{HappyA}你问得真好。",
 "[considering] {InquireA}Well you wouldn't be here {SternA}otherwise.":
    "[considering] {InquireA}不然你也不会{SternA}来这儿。",
 "Because {SmugA}that's where you {SchemeA}come in.": "因为{SmugA}这就轮到{SchemeA}你出场了。",
 "[to August] {NeutralA}We brought this deal to {WorryA}*you* because we knew {SternA}nobody else could help us with {NeutralA}something this big.":
    "[to August] {NeutralA}我们把这笔交易带给{WorryA}*你*，是因为我们知道{SternA}这么大的事{NeutralA}没别人帮得了我们。",
 "[to Vallory] {SmugB}Whatever the deal is with the key, {NeutralA}we want in on it. {ShockA}This is big.":
    "[to Vallory] {SmugB}不管这把钥匙的交易是什么，{NeutralA}我们都要参与。{ShockA}这是大事。",
 "{SternA}See, Fiona, I {AngryA}told you Vallory wouldn't {SternB}be interested.  {SternA}Let's just take this deal somewhere else.":
    "{SternA}看吧，Fiona，我{AngryA}就跟你说过 瓦洛里 不会{SternB}感兴趣。{SternA}我们把这交易拿到别处去吧。",
 "{AngryA}Sit, Sasha. Nobody's going {SternA}anywhere until I say so.":
    "{AngryA}坐下，萨莎。我没发话谁也别想{ SternA}走。",
 "I think we should": "我觉得我们应该",
 "[to August] It's a great deal for all of us.": "[to August] 这对我们所有人都是笔好交易。",
 "{SmugA}We're gonna sell it.": "{SmugA}我们要把它卖掉。",
 "Would you look at that, August? It's amazing, isn't it.":
    "你瞧瞧，August？太惊人了，对吧。",
 "Nice try, sis. But I don't think Vallory is very impressed.":
    "试得不错，姐。但我觉得 瓦洛里 没什么被打动。",
 "But if you're {SternA}trying to piss me off, {AngryA}it's working.":
    "但你要是{SternA}想惹我发火，{AngryA}那确实成功了。",
 "{AngryA}Look, I don't know what you're up to, Sasha.":
    "{AngryA}听着，我不知道你在打什么主意，萨莎。",
 "{AngryA}Alright, I {SternA}see what you're up to.": "{AngryA}好吧，我{SternA}看出你在打什么主意了。",
 "{NeutralA}Sasha, you've had your claws in my {SternA}boy for a while now.":
    "{NeutralA}萨莎，你的爪子已经搭在{SternA}我儿子身上有一阵子了。",
 "But while {NeutralA}reverse psychology cons might work on most marks [a bit menacing] {AngryA}I'm not most marks.":
    "但虽然{NeutralA}反向心理骗术对大多数肥羊管用[a bit menacing] {AngryA}我可不是大多数肥羊。",
 "{WorryA}I am, and I {SternA}swear it won't {WorryA}happen again.":
    "{WorryA}我知道，我{SternA}发誓不会{WorryA}再发生了。",
 "{SternA}It better not.": "{SternA}最好不会。",
 "{AngryA}And don't think the silent treatment has you off the{SternA} hook here, Fiona.":
    "{AngryA}别以为不说话就能{SternA}躲过去，Fiona。",
 "I thought it'd help convince you.": "我以为那能帮你被说服。",
 "{NeutralA}It's not Sasha's fault, {WorryA}Vallory.  I told her to {SternA}work you like that.":
    "{NeutralA}这不是 萨莎 的错，{WorryA}瓦洛里。是我让她{SternA}那么套路你的。",
 "{NeutralA}Of course you did.": "{NeutralA}你当然会。",
 "{InquireA}And good on you for owning up to it. [beat] But don't {SternA}ever pull anything {AngryA}like that on me again.":
    "{InquireA}你能承认这点，不错。[beat] 但别{SternA}再对我玩{AngryA}那种把戏。",
 "You're just saying that because you *expect* me to con you.":
    "你这么说只是因为你*预料*我会骗你。",
 "{SmugA}Come on, Vallory, you're just reading-into what Sasha's saying because you {SmugC}*expect* us to be {SmugA}up to something.":
    "{SmugA}得了吧，瓦洛里，你只是在过度解读 萨莎 的话，因为你{SmugC}*预料*我们在{SmugA}打什么主意。",
 "{NeutralA}You're {SmugA}*always* up to something, {SternA}Fiona.":
    "{NeutralA}你{SmugA}*总是*在打什么主意，{SternA}Fiona。",
 "{SmugA}That's Sasha for you.  Never know what sort of {SmugC}crazy notions she'll get in her head.":
    "{SmugA}这就是 萨莎。你永远不知道她脑子里会冒出什么{SmugC}疯念头。",
 "And while may be able to get {InquireA}*him* to agree with everything you want [a bit menacing] {AngryA}that doesn't trickle up to me.":
    "就算你能让{InquireA}*他*什么都同意你[a bit menacing] {AngryA}那也影响不到我。",
 "You may be {InquireA}smarter than I gave you credit for, Sasha.":
    "你可能比{InquireA}我以为的要聪明，萨莎。",
 "Is that so?": "是吗？",
 "{NeutralA}So, then, what you're saying is she's a {InquireA}liability to this Vault Key deal you've {SternA}brought before me?":
    "{NeutralA}那么，你的意思是，她对你{SternA}带到我这儿的这笔秘藏钥匙交易是个{InquireA}隐患？",
 "{InquireA}A problem we have to solve before we can proceed?":
    "{InquireA}一个我们必须先解决才能继续的问题？",
 "{ShockA}Wait, what? No, ma, {WorryA}come on, don't say that.":
    "{ShockA}等等，什么？不，妈，{WorryA}别这样，别说那种话。",
 "{ShockA}No, no, {SternA}nothing like that.  I can {SmugA}keep her in line.":
    "{ShockA}不，不，{SternA}不是那样。我{SmugA}能管住她。",
 "[you're busted] {SternA}Yeah.  That's what I thought.":
    "[you're busted] {SternA}是啊。我就知道。",
 "What about him?": "那他呢？",
 "What about August? Is he a problem": "August 呢？他是个问题吗",
 "{ShockA}Sasha's no {SmugA}liability, she's an asset.":
    "{ShockA}萨莎 不是{SmugA}隐患，她是资产。",
 "{SchemeA}Wild or not, she always gets the job done.":
    "{SchemeA}不管多野，她总能把事办成。",
 "{InquireB}If there's any problem with Sasha, {SternA}it's *my* problem to deal with.":
    "{InquireB}萨莎 要是有任何问题，{SternA}那也是*我*要处理的问题。",
 "I": "我",
 "{WorryA}Sasha won't be any {NeutralA}problem, ma.  I vouch for her.":
    "{WorryA}萨莎 不会有任何{NeutralA}问题，妈。我替她担保。",
 "Alright then.": "那就好。",
 "{WorryA}Sasha's sorry, Ma.  {ThinkA}Right, Sasha?":
    "{WorryA}萨莎 道歉了，妈。{ThinkA}对吧，萨莎？",
 "{InquireA}I know. I just wanted to see what {SmugA}Fiona had to say about it. [scoffs] {NeutralA}Some sister.":
    "{InquireA}我知道。我只是想看看{SmugA}Fiona 会怎么说。[scoffs] {NeutralA}真是个姐姐。",
 "{NeutralA}Look, Fiona, you came here {InquireA}all excited to show off {NeutralA}your Vault Key.":
    "{NeutralA}听着，Fiona，你{InquireA}兴冲冲地跑来炫耀{NeutralA}你的秘藏钥匙。",
 "{NeutralA}And you've got some {SternA}sap lined-up to buy it.":
    "{NeutralA}而你还{ SternA}找好了冤大头来买。",
 "{NeutralA}And you've got some half-cocked scheme to {InquireA}profit off it, somehow.":
    "{NeutralA}你还有个半生不熟的计划，想{InquireA}从中捞一笔。",
 "You've got your Vault Key.": "你有你的秘藏钥匙。",
 "You've got your fake Vault Key.": "你有你的假秘藏钥匙。",
 "What do you want from {InquireA}me Fiona?": "你到底想从{InquireA}我这儿要什么，Fiona？",
 "{ThinkB}But you wouldn't have come to {ThinkA}*us* if you didn't need something.":
    "{ThinkB}但你要是不需要什么，就不会来找{ThinkA}*我们*。",
 "{AngryA}I was getting to that [beat] {SmugA}but yes.":
    "{AngryA}我正要说到那儿[beat] {SmugA}但没错。",
 "Remember, once you deal us in it's forty percent.": "记住，你把我们算进来，就是四成。",
 "It must be something {NeutralA}big, or you'd have just {SternA}asked the second you walked in the door.":
    "那一定是件{NeutralA}大事，不然你进门那一刻就{SternA}开口了。",
 "{NeutralA}Rather than trying to get me all excited about {SternA}your deal first.":
    "{NeutralA}而不是先想让我对{SternA}你的交易兴奋起来。",
 "{DoubtfulA}Just a small {SMugA}investment -- [gets cut off] of some of your...":
    "{DoubtfulA}只是一笔小小的{SMugA}投资——[gets cut off] 用你的一些……",
 "{SmugA}You mean a loan.": "{SmugA}你是说借款。",
 "{DoubtfulA}I was hoping you might {SmugA}give us -- [gets cut off] some of your...":
    "{DoubtfulA}我希望你能{SmugA}给我们——[gets cut off] 你的一些……",
 "{SmugA}Give you? [Laughs] I think you've got me {SchemeA}confused with somebody else.":
    "{SmugA}给你们？[Laughs] 我想你把我{SchemeA}跟别人搞混了。",
 "{SmugA}I'd like to make you a {SchemeA}partner in this deal.":
    "{SmugA}我想让你成为这笔交易的{SchemeA}合伙人。",
 "{SmugA}Well isn't it {SchemeA}mighty big of you to think of {SmugA}little ol' me.":
    "{SmugA}你还能想到{SmugA}我这么个小人物，真是{ SchemeA}太抬举了。",
 "{WorryA}We just want to {NeutralB}borrow some of your Eridium.":
    "{WorryA}我们只是想{NeutralB}借一点你的镒矿。",
 "{DoubtfulA}All we need to make this {SmugA}thing work is {SmugB}some of your Eridium.":
    "{DoubtfulA}要让这事{SmugA}成，我们只需要{SmugB}一点你的镒矿。",
 "{SmugA}Some of my Eridium, huh?": "{SmugA}我的一些镒矿，是吧？",
 "Spend my money, that is.": "也就是说，花我的钱。",
 "{SmugB}Gotta spend money to make money, {SmugA}right?":
    "{SmugB}要赚钱就得先花钱，{SmugA}对吧？",
 "{NeutralB}We need it to power the Vault Key. No {SternB}buyer will pay for it without knowing it {NeutralB}actually charges-up.":
    "{NeutralB}我们需要它给秘藏钥匙供电。要是{SternB}买家不知道它{NeutralB}真能充上电，没人会付钱。",
 "{NeutralB}We need it to make the {SternB}key appear real. {SmugA}Give it that Vault Key glow.":
    "{NeutralB}我们需要它让{SternB}钥匙看起来是真的。{SmugA}给它那种秘藏钥匙的光泽。",
 "They'll think it's fake just like {SternA}you did when we started talking.":
    "他们会像{SternA}我们刚开口时你那样，以为它是假的。",
 "{SchemeA}And make it look legit if someone scans it, too.":
    "{SchemeA}而且要是有人扫描它，也得看起来像真的。",
 "{InquireA}Makes sense. [beat] But {SternA}Eridium isn't so easy to come by.":
    "{InquireA}有道理。[beat] 但{SternA}镒矿可不好弄。",
 "We get that Eridium, we all make money off this deal.":
    "我们拿到那些镒矿，这笔交易大家都能赚钱。",
 "Trust me, Vallory, you give me that Eridium and I can pull-off this deal.":
    "相信我，瓦洛里，你把镒矿给我，我就能把这交易做成。",
 "Invest the Eridium in this deal for August's future, Vallory.":
    "为了 August 的前途，把镒矿投进这笔交易吧，瓦洛里。",
 "{NeutralA}Look, Fiona, you came here {InquireA}all excited about your clever little fake {NeutralA}Vault Key scheme.":
    "{NeutralA}听着，Fiona，你{InquireA}兴冲冲跑来，炫耀你那套机灵的假{NeutralA}秘藏钥匙把戏。",
 "{NeutralA{Alright, Fiona.": "{NeutralA{好吧，Fiona。",
 "And entrust it to you...": "然后把它托付给你……",
 "[considering] It *is* a pretty good deal... But put all my Eridium into it...":
    "[considering] 这*确实*是笔不错的交易……但把我所有的镒矿都投进去……",
 "{SternA}For starters, you're thinking {NeutralA}too small in terms {SternA}of value.":
    "{SternA}首先，你在价值上{NeutralA}想得太小了。",
 "{SternA}So we're setting a {InquireA}new price of {NeutralA}five hundred thousand.":
    "{SternA}所以我们定个{InquireA}新价格：{NeutralA}五十万。",
 "I'm in.": "我加入。",
 "But my investment means this is my deal now.": "但我的投资意味着现在这是我的交易了。",
 "{SternA}It's his contact after all.": "{SternA}毕竟那是他的联系人。",
 "{InquireA}And since you're so concerned with August's future.":
    "{InquireA}既然你这么关心 August 的前途。",
 "{NeutralA}August is going along to supervise the deal.":
    "{NeutralA}August 会跟着一起去监督这笔交易。",
 "{SmugA}I'm in.": "{SmugA}我加入。",
 "I know.": "我知道。",
 "Our buyer can't afford that much money.": "我们的买家出不起那么多钱。",
 "{SmugC}More money is {SmugA}always welcomed.": "{SmugC}钱多一点{SmugA}总是受欢迎的。",
 "{SternA}More risk isn't, so {NeutralA}my share increases.":
    "{SternA}风险多一点就不必了，所以{NeutralA}我的份要增加。",
 "{AngryA}Come on, Vallory -- this is {SternA}*my* deal.":
    "{AngryA}拜托，瓦洛里——这是{SternA}*我*的交易。",
 "{SternA}My investment means it's {SmugA}my deal now, sweetheart.":
    "{SternA}我投了钱，就意味着它现在是{SmugA}我的交易，亲爱的。",
 "{ShockA}What?": "{ShockA}什么？",
 "{NeutralA}You put this whole thing together {HappyA}yourselves, and I'm impressed.  {SmugA}I truly am.  So now {SchemeA}you work for me.":
    "{NeutralA}这整件事是你们{HappyA}自己攒起来的，我很佩服。{SmugA}真的。所以现在{SchemeA}你们替我干活。",
 "{NeutralA}Your cut will be ten percent.": "{NeutralA}你们拿一成。",
 "{AngryA}Come on.": "{AngryA}别这样。",
 "And I won't have you screwing-up something this big on my dime.":
    "我可不会让你们花着我的钱把这么大的事搞砸。",
 "{SternA}Not anymore.  You wanted to {InquireA}play in the big leagues? {SmugA}Welcome to the team.":
    "{SternA}不再是了。你想{InquireA}跟大人物玩？{SmugA}欢迎入队。",
 "{SternA}This isn't fair. {AngryA}I work alone.":
    "{SternA}这不公平。{AngryA}我向来单干。",
 "You pay attention and learn how to do things the right way from me, you might even impress one day.":
    "你留心学着点，跟我会做事，说不定哪天你也能让人刮目相看。",
 "{DoubtfulA}We won't disappoint,{SmugA} I promise.":
    "{DoubtfulA}我们不会让你失望的，{SmugA}我保证。",
 "{SmugA}Hey, it could be worse, {SternA}I could just kill you and do the deal myself. [beat] I guess I must really like you, Fiona.":
    "{SmugA}嘿，事情本可以更糟，{SternA}我也可以直接杀了你，自己做这笔交易。[beat] 看来我是真喜欢你，Fiona。",
 "I take it we don't have a choice?": "我猜我们没得选？",
 "Not in the least.": "完全没有。",
 "{NeutralA}But if you screw this up in any way... and I don't get that {InquireA}return on my investment?":
    "{NeutralA}但你要是以任何方式把这搞砸……我拿不到{InquireA}投资的回报？",
 "{AngryA}I'll fly your flayed hides at half mast to {SternA}mourn my lost Eridium.":
    "{AngryA}我就把你们剥了皮挂在半旗上，{SternA}悼念我损失的镒矿。",
 "{SternA}Today is not that day.": "{SternA}今天不是那一天。",
 "{InquireA}And while maybe someday I'll trust you, Fiona.":
    "{InquireA}也许哪天我会信任你，Fiona。",
})

# —— 敲定交易 + 编造身份（Livia Strauss）——
T.update({
 "{AngryB}This isn't fair, {AngryA}we -- [gets cut off] put this whole deal...":
    "{AngryB}这不公平，{AngryA}我们——[gets cut off] 把这整笔交易……",
 "{InquireA}And a higher price means a {NeutralA}new buyer. {SternA}August, get in touch with your contact up at Hyperion.":
    "{InquireA}价格更高就意味着{NeutralA}新买家。{SternA}August，联系你上面 亥博龙的人。",
 "I'm sure Vasquez will be interested.": "我相信 Vasquez 会感兴趣的。",
 "{NeutralA}Which is more in keeping with the {SmugA}true value of a Vault Key.":
    "{NeutralA}这才更符合一把秘藏钥匙的{SmugA}真实价值。",
 "Factoring out all the {NeutralA}mortal risk we're not {InquireA}taking, of course.":
    "当然，是把我们没打算{InquireA}承担的那些{NeutralA}致命风险排除在外。",
 "{ThinkB}Don't worry, {NeutralB}Vasquez is a loyal customer.":
    "{ThinkB}别担心，{NeutralB}Vasquez 是个忠实客户。",
 "We'll be one and {NeutralA}done, no problem.": "我们一次{NeutralA}搞定，没问题。",
 "{InquireA}If there are, you'd best deal with them and {SternA}bring me back my money.":
    "{InquireA}要是有，你最好处理掉，然后{SternA}把我的钱带回来。",
 "{SternA}Any more surprises waiting to spring on me?":
    "{SternA}还有什么意外等着砸到我头上吗？",
 "{SternB}I've never lost money on a deal, and I'm {SternA}not about to start now.":
    "{SternB}我做交易从没亏过钱，{SternA}现在也不打算开始。",
 "{SmugA}That's the \"I want to stay alive\" spirit that will {SchemeA}carry you far in this business.":
    "{SmugA}这就是那种“我想活命”的精神，会{SchemeA}让你在这行里走得很远。",
 "{SmugB}Glad to have the help with {SmugA}something this big.":
    "{SmugB}很高兴{SmugA}这么大的事能有帮手。",
 "{SternA}Just make sure August does his part.": "{SternA}只要确保 August 做好他那一份。",
 "{NeutralA}That fiesty attitude of yours will {InquireA}either take you far, or {SmugA}land you in your grave one day.":
    "{NeutralA}你这副泼辣态度{InquireA}要么让你走得很远，要么{SmugA}哪天把你送进坟墓。",
 "{ThinkA}Hey. I know what I'm doing.": "{ThinkA}嘿。我知道我在干什么。",
 "{SmugA}Good girl.": "{SmugA}好女孩。",
 "{SternA}Okay, August. Call your guy. Tell him what we've got, and that we won't take a penny less than five hundred grand for it.":
    "{SternA}好，August。给你的人打电话。告诉他我们手上有什么，少五十万一分都不卖。",
 "But if we're gonna {NeutralA}move this thing, {SternA}we do it right.":
    "但既然我们要{NeutralA}出手这东西，{SternA}就得办得漂亮。",
 "[to Fiona] {SmugA}Alright, Fiona -- {SchemeA}go make us rich.":
    "[to Fiona] {SmugA}好吧，Fiona——{SchemeA}去让我们发财吧。",
 "{InquireA}Passing off a fake Vault Key is a pretty {NeutralA}ambitious con, Fiona.":
    "{InquireA}把一把假秘藏钥匙卖出去，可是个相当{NeutralA}有野心的骗局，Fiona。",
 "WHEN FIONA WALKS PAST THE BAR, SHE NODS AT THE BARTENDER AND SMILES.  THEN SHE NOTICES":
    "FIONA 走过吧台时，朝酒保点了点头并微微一笑。然后她注意到",
 "That looks -- [gets cut off] like you.": "那看起来——[gets cut off] 像你。",
 "{NeutralA}And you want to find some some mythical Vault Hunter to {SternA}sucker into buying it.":
    "{NeutralA}而你想找个传说中的秘藏猎人{SternA}骗他买下来。",
 "[insulted] {InquireA}Walking up to a {SternA}*real* Vault Hunter and {InquireB}selling it is {SchemeA}*exactly* what I plan to do.":
    "[insulted] {InquireA}直接走到一个{SternA}*真*秘藏猎人面前{InquireB}把它卖了，就是{SchemeA}*我的*计划。",
 "{NeutralA}Because you know {SternA}so many Vault Hunters, right?":
    "{NeutralA}因为你认识{SternA}那么多秘藏猎人，对吧？",
 "{ThinkA}Or vice-versa.": "{ThinkA}或者反过来也一样。",
 "{SternA}I can't imagine why not.": "{SternA}我想不出为什么不行。",
 "{SternA}We just slapped it together.  I {SternB}told her it wasn't very convincing, but does she {WorryA}listen to me?  {InquireA}No.":
    "{SternA}我们就是随便拼起来的。我{SternB}跟她说过那不太能唬人，可她{WorryA}听我的吗？{InquireA}不听。",
 "How'd the likes of you get your hands on it?": "你这种人是怎么把它弄到手的？",
 "How'd you  of all {SternA}small-time operators manage to pull something like this {InquireA}together, anyway?":
    "在所有{SternA}小打小闹的混混里，你到底是怎么把这种事{InquireA}攒起来的？",
 "Or maybe you're {SlyB}secretly an alien?": "或者你其实{ SlyB}是个外星人？",
 "{NeutralB}By putting all my time and money into it {SternA}for [beat] a while now.":
    "{NeutralB}把全部时间和钱都投进去{ SternA}投了[beat] 好一阵子了。",
 "[considering] {NeutralA}I can imagine so.  It's {InquireA}definitely not one of your usual petty schemes, {NeutralA}that's for sure.":
    "[considering] {NeutralA}我能想象。这{InquireA}绝对不是你们平时那种小把戏，{NeutralA}这点可以肯定。",
 "But this is pretty convincing work.": "但这活儿做得相当有说服力。",
 "How did {InquireA}*you* of all petty scoundrels happen to get {SternA}your hands on one of the rarest things in the universe?":
    "在所有小混混里，{InquireA}*你*是怎么弄到{SternA}宇宙中最稀罕的东西之一的？",
 "[considering]\t{InquireA}Felix, huh?  And here I thought that {SternA}old degenerate was just your {NeutralA}driver.":
    "[considering]\t{InquireA}菲利克斯，是吗？我还以为那个{SternA}老废物只是你的{NeutralA}司机。",
 "{SmugA}By knowing the right people. [beat] My buddy {SchemeA}Felix made it.":
    "{SmugA}因为我认识对的人。[beat] 是我哥们{SchemeA}菲利克斯 做的。",
 "{SmugA}I made it myself.": "{SmugA}是我自己做的。",
 "{InquireA}You're what they call full of {SternA}crap, Fiona.":
    "{InquireA}你就是他们说的满嘴{SternA}放屁，Fiona。",
 "I'm what they call a {SchemeA}renaissance woman.": "我就是他们说的{SchemeA}文艺复兴式女性。",
 "{HappyA}Just think about it, August -- it's the {HappyC}swindle of a lifetime.":
    "{HappyA}你想想，August——这是{HappyC}一生一次的骗局。",
 "{SternA}Actually, that kind of investment {NeutralA}does show commitment.":
    "{SternA}其实，那种投入{NeutralA}确实说明了用心。",
 "{SternA}Come on, {AngryA}Vallory doesn't care how much it {SternA}cost to make it.":
    "{SternA}得了吧，{AngryA}瓦洛里 才不管做它{SternA}花了多少钱。",
 "{SternA}Come on, {WorryA}no mark is gonna believe that some piece of {SternB}junk Felix slapped together is a {SternA}Vault key.":
    "{SternA}得了吧，{WorryA}没有哪个冤大头会相信 菲利克斯 随便拼凑的{SternB}破烂是{SternA}秘藏钥匙。",
 "{SternA}Actually, it {NeutralA}is pretty convincing work.":
    "{SternA}其实，这活儿做得{NeutralA}相当有说服力。",
 "{SternA}Come on, {WorryA}no mark is  gonna believe that some piece of {SternB}junk you slapped together is a {SternA}Vault key.":
    "{SternA}得了吧，{WorryA}没有哪个冤大头会相信你随便拼凑的{SternB}破烂是{SternA}秘藏钥匙。",
 "{InquireA}What exactly do you intend to do with this {NeutralA}fake Vault Key you've {SternA}cobbled together?":
    "{InquireA}你到底打算拿你{SternA}草草拼凑出来的这把{NeutralA}假秘藏钥匙干什么？",
 "{ThinkB}It's not like you're gonna just walk up to some Vault Hunter {ThinkA}and sell it.":
    "{ThinkB}你总不会直接走到某个秘藏猎人面前{ThinkA}把它卖了吧。",
 "You obviously put a lot of thought into this plan.": "你显然在这计划上费了不少心思。",
 "{SmugB}They'd just blow your head off and take the key.":
    "{SmugB}他们只会一枪打爆你的头，然后把钥匙拿走。",
 "If you even got as {SmugA}far as finding one of 'em.":
    "前提是你能{SmugA}找得到一个。",
 "{AngryA}Fiona?!": "{AngryA}Fiona？！",
 "[considering] Still... it is good work.": "[considering] 不过……这活儿做得不错。",
 "[considering] Which I suppose can be a {NeutralA}valuable trait in a {SternA}con artist.":
    "[considering] 我想这在{SternA}骗子身上算是{NeutralA}很有价值的特质。",
 "Make it worth my while.": "让我觉得值。",
 "Thank you for seeing me, Ma Vallory.": "谢谢你见我，瓦洛里 妈。",
 "Uh...  I could've waited, you know.": "呃……其实我可以等的。",
 "You piqued my interested, and when I get interested I get impatient.":
    "你勾起了我的兴趣，而我一旦有了兴趣就没了耐心。",
 "Uh... Maybe this wasn't such a good idea after all.":
    "呃……也许这终究不是什么好主意。",
 "If it was a good idea when you interrupted me, it damn well still better be a good idea now.":
    "你打断我的时候这主意要是好，那它现在他妈最好还是个好主意。",
 "[more to herself than anyone else] Why would I do that?":
    "[more to herself than anyone else] 我干嘛要那样做？",
 "Well, me and {SternA}Sasha. And Felix.": "这个，还有我，加{SternA}萨莎。还有 菲利克斯。",
 "[off-screen] Bullseye!": "[off-screen] 正中靶心！",
 "{SmugA}Vasquez will {SmugC}*definitely* be interested in this.":
    "{SmugA}Vasquez{SmugC}*肯定*会感兴趣。",
 "{SternA}Don't sweat it -- {NeutralA}Hyperion ain't what they used to be.":
    "{SternA}别担心——{NeutralA}亥博龙已经不是从前的样子了。",
 "{WorryA}You sure it's a good idea to {ThinkA}screw-over Vasquez, ma?":
    "{WorryA}你确定坑 Vasquez 是个好主意吗，妈？",
 "{NeutralA}Fawning all over my boy, speaking on my behalf everything I {InquireA}*don't* wanna say....":
    "{NeutralA}对我儿子阿谀奉承，替我说出所有我{InquireA}*不想*说的话……",
 "[meekly] But... we still haven't finished... [gets cut off by scream] our discussion.":
    "[meekly] 但……我们还没谈完……[gets cut off by scream] 我们的讨论。",
 "{AngryA}I'll finish with you later.": "{AngryA}我回头再跟你算账。",
 "But don't ever pull anything like that on me again.":
    "但别再对我玩那种把戏。",
 "{InquireA}And [beat] you can find a {NeutralA}new contact up there after they grind him into {SmugA}chump patties when he tries to use that key.":
    "{InquireA}而且[beat] 等他拿着那把钥匙被人碾成{SmugA}肉饼之后，你可以在上面找个{NeutralA}新联系人。",
 "{SlyB}Hyperion is obsessed with vaults.  {SlyA}This will be his ticket straight to the top.":
    "{SlyB}亥博龙对秘藏痴迷得很。{SlyA}这会是他直通顶层的门票。",
 "{InquireA}Alright, Fiona...": "{InquireA}好吧，Fiona……",
 "You were right about what you said...": "你说的是对的……",
 "Get the kid a drink.": "给这孩子来杯酒。",
 "We meet again, tough girl.": "我们又见面了，硬骨头姑娘。",
 "I oughta blast ya right here for having a smart mouth.":
    "就凭你这张嘴，我就该在这儿崩了你。",
 "I'd prefer to stay at the bar [beat] 'cause you're not gonna shoot me, you're gonna buy me a drink.":
    "我更愿意待在吧台这儿[beat] 因为你不会开枪打我，你会请我喝一杯。",
 "I don't think Ma Vallory would appreciate us shooting up her bar, so why don't we take this outside.":
    "我觉得 瓦洛里 妈不会喜欢我们在她酒吧里开枪，所以我们不如到外面去。",
 "You put a gun in my friend's face. Nobody puts a gun in my friend's face.":
    "你把枪指到了我朋友脸上。没人能拿枪指着我朋友的脸。",
 "Oh, is that so?": "哦，是吗？",
 "{HappyB}Will you look at that, August. It's {HappyA}incredble, isn't it?":
    "{HappyB}你瞧瞧，August。真是{HappyA}不可思议，对吧？",
 "{InquireA}Come on, Fiona. I thought we {SternA}talked about this? Vallory's not {SternB}interested in something {InquireA}like that.":
    "{InquireA}得了吧，Fiona。我们{SternA}不是说过了吗？瓦洛里 对{InquireA}那种东西{SternB}不感兴趣。",
 "{SmugA}Maybe not in your world, Fiona.": "{SmugA}也许在你的世界里不会，Fiona。",
 "{ShockA}Five hundred grand? {SternB}Nobody can afford that.":
    "{ShockA}五十万？{SternB}谁付得起这个价。",
 "{SternA}We'll do the job, but we {SternB}want more money.":
    "{SternA}活我们干，但我们{ SternB}要更多钱。",
 "{ShockA}Ten percent isn't fair when we {SternA}came up with the whole thing.":
    "{ShockA}整个主意都是我们想出来的，一成可不公平。",
 "{SternC}Great, now we've got *jobs*, like all the other {SternA}criminals around here.":
    "{SternC}好极了，现在我们也有*活儿*了，跟这儿其他{SternA}罪犯一样。",
 "{SmugA}I guess I must {SternA}really like you, Fiona.":
    "{SmugA}看来我是{SternA}真喜欢你，Fiona。",
 "{SmugA}Nobody ever does [beat] {SternA}more than once.":
    "{SmugA}从来没人这样[beat] {SternA}超过一次。",
 "{SmugA}Life isn't fair, Fiona. But you do a {NeutralA}good job with this, then we {SternA}can talk pay raise.":
    "{SmugA}生活本就不公平，Fiona。但你要是把这{NeutralA}干得好，我们就{SternA}可以谈加薪。",
 "{NeutralA}Shows a keen business sense. I appreciate that.":
    "{NeutralA}这显示出敏锐的商业头脑。我很欣赏。",
 "{InquireA}Coming to me to to invest in your deal.":
    "{InquireA}来找我投资你的交易。",
 "You've got some {SchemeA}moxie, and {NeutralA}I can respect that.":
    "你有点{SchemeA}胆气，{NeutralA}我尊重这点。",
 "{NeutralA}Asking me to {SmugA}*give* you some Eridium. Hah.":
    "{NeutralA}还想要我{SmugA}*送*你一些镒矿。哈。",
 "{NeutralA}Bringing this deal to me as {InquireA}a partnership.":
    "{NeutralA}把这笔交易当作{InquireA}合伙来找我。",
 "{NeutralA}That shows respect.  Respect will get you far in this town.":
    "{NeutralA}这显示出尊重。尊重能让你在这镇上走得很远。",
 "{HappyA}This truly is the deal of a lifetime, Fiona.":
    "{HappyA}这真是一生一次的交易，Fiona。",
 "I think it's worth spending on, ma.": "我觉得值得投钱，妈。",
 "{NeutralA}Okay, this con {SchemeA}could work.": "{NeutralA}好吧，这个骗局{SchemeA}也许能成。",
 "{SternA}So what makes you think you are {InquireA}capable of handling a {SternA}deal like this?":
    "{SternA}那你凭什么觉得自己{InquireA}有能力处理{SternA}这样的交易？",
 "{SmugA}You're what we like to call a {SmugC}\"small fry\".  [beat] Because a {ShockA}fry is a {SmugA}baby fish.":
    "{SmugA}你就是我们说的{SmugC}“小鱼苗”。[beat] 因为{ShockA}苗就是{SmugA}小鱼。",
 "{NeutralA}But this whole thing is very {InquireA}ambitious, Fiona.  And you're not exactly a {SternA}big fish in this scummy little pond of ours.":
    "{NeutralA}但这整件事非常{InquireA}有野心，Fiona。而你在我们这个小脏水塘里并不算什么{SternA}大鱼。",
 "[to Vallory] {SmugB}She does look cooly confident, I'll give her that.":
    "[to Vallory] {SmugB}她看起来确实冷静自信，这我承认。",
 "[to August] {SmugA}Because of her cool confidence.": "[to August] {SmugA}因为她那份冷静自信。",
 "{WorryA}You're right Vallory, {SternA}we can't do it.  {SmugA}Thanks for taking the time.":
    "{WorryA}你说得对 瓦洛里，{SternA}我们做不了。{SmugA}谢谢抽时间见我们。",
 "{NeutralA}Of course {SchemeA}plenty of folks would love to buy a Vault Key.":
    "{NeutralA}当然，{SchemeA}很多人都想买一把秘藏钥匙。",
 "{InquireB}You couldn't find a better person to do this {SchemeC}deal than me.":
    "{InquireB}要做这笔{SchemeC}交易，你找不到比我更合适的人。",
 "{SmugA}Because I'm the best at {SchemeA}what I do.":
    "{SmugA}因为我干这行{SchemeA}是最棒的。",
 "{InquireA}Because you'll {SchemeA}help me.": "{InquireA}因为你会{SchemeA}帮我。",
 "{InquireB}That's why I came to you -- {SchemeC}to make it all possible.":
    "{InquireB}所以我才来找你——{SchemeC}让这事成真。",
 "The deal practically {SchemeC}makes itself.": "这交易几乎{SchemeC}自己就成了。",
 "{InquireB}Because it's a {SmugA}*Vault Key*.  Some people are {SchemeA}literally willing to kill for one.":
    "{InquireB}因为这是{SmugA}*秘藏钥匙*。有些人{SchemeA}真的愿意为它杀人。",
 "Maybe we are underestimating them, ma.": "也许我们低估他们了，妈。",
 "Come on August, you know Fiona and I can do this, right?":
    "得了吧 August，你知道我和 Fiona 能做到的，对吧？",
 "{InquireB}Maybe you're the best among the kinda folks {InquireA}we run with, but  you're pretty much {SternA}nothing compared to Vallory.":
    "{InquireB}也许在我们{InquireA}交往的那类人里你是最棒的，但跟 瓦洛里 比，你基本上{SternA}什么都不是。",
 "{SternA}She doesn't actually want to {SternB}help us, Fiona, {InquireA}she's just being polite.":
    "{SternA}她其实并不想{SternB}帮我们，Fiona，{InquireA}她只是客气一下。",
 "{SternA}There are {SternB}other things in life besides {InquireA}vault keys, Fiona.":
    "{SternA}除了{InquireA}秘藏钥匙，生活里{SternB}还有别的东西，Fiona。",
 "What's so important?": "什么事这么重要？",
 "{SchemeA}Don't disappoint me, Fiona.": "{SchemeA}别让我失望，Fiona。",
 "{SternA}You disappointed me, Tommy.": "{SternA}你让我失望了，Tommy。",
 "You just watch yourself, little missy.": "你自己当心点，小丫头。",
 "Yeah. Watch yourself. We ain't *nice*.": "是啊。当心点。我们可*不*客气。",
 "[pickup4]{FearA}Vallory... if we {ConcernedA}get in the way of...":
    "[pickup4]{FearA}瓦洛里……要是我们{ConcernedA}挡了谁的……",
 "[pickup4]Vallory?": "[pickup4]瓦洛里？",
 "[pickup4]Yeah. Sis and I have a{HappyA} *meeting* with her.":
    "[pickup4]是啊。我和我姐跟她有个{HappyA}*会面*。",
 "[pickup4]I know I know.": "[pickup4]我知道我知道。",
 "[apickup4]{DoubtfulA}One way above you goon's pay grade.":
    "[apickup4]{DoubtfulA}远远超出你这种打手的档次。",
 "[pickup4]You two have a... nice... day.": "[pickup4]你们俩……过得……愉快。",
 "[pickup4]{InquireA}Wasn't great.": "[pickup4]{InquireA}不太愉快。",
 "[pickup4]{SternB}That didn't look good.": "[pickup4]{SternB}那看着不妙。",
 "It doesn't concern you.": "跟你无关。",
 "Don't act all tough with me.": "别跟我装硬。",
 "Making a lot of money.": "赚一大笔钱。",
 "It's the deal of a lifetime.": "这是一生一次的交易。",
 "It's important to me.": "这对我很重要。",
 "I can wait if you're busy.": "你要是忙我可以等。",
 "Oh, it's real!": "哦，它是真的！",
 "Of course it's fake!": "当然是假的！",
 "I'm engaged to a Vault Hunter.": "我跟一个秘藏猎人订婚了。",
 "I found it in a mine.": "我在一个矿里找到的。",
 "I swindled somebody.": "我从某人手里骗来的。",
 "We have a buyer for it.": "我们给它找了买家。",
 "I could open a Vault...": "我可以打开一个秘藏……",
 "That's where you come in...": "这就轮到你出场了……",
 "It cost me a lot.": "它花了我很多钱。",
 "Felix made it.": "菲利克斯 做的。",
 "I made it myself.": "我自己做的。",
 "Sell it to some sucker.": "卖给某个冤大头。",
 "Sell it to a Vault Hunter.": "卖给一个秘藏猎人。",
 "I'm the best.": "我是最棒的。",
 "I'll have your help.": "我会有你帮忙。",
 "Because it's a Vault Key.": "因为这是秘藏钥匙。",
 "Don't blame her.": "别怪她。",
 "You're reading into it.": "你在过度解读。",
 "Sasha's a wildcard.": "萨莎 是个变数。",
 "I'll keep her in line.": "我能管住她。",
 "She gets the job done.": "她能把事办成。",
 "Sasha's my problem, not yours.": "萨莎 是我的问题，不是你的。",
 "I need a loan.": "我需要一笔借款。",
 "I need some Eridium.": "我需要一些镒矿。",
 "I need a partner.": "我需要一个合伙人。",
 "Nobody can afford that.": "没人付得起这个价。",
 "More money is better.": "钱多一点更好。",
 "Hey, this is my deal.": "嘿，这是我的交易。",
 "I work alone.": "我单干。",
 "We won't let you down.": "我们不会让你失望。",
 "We need more money.": "我们需要更多钱。",
 "He better deliver.": "他最好办到。",
 "Any more surprises?": "还有更多意外吗？",
 "Glad to have the help.": "很高兴能有帮手。",
})

# —— 会前串供 + 与 August / Vasquez 接头 ——
T.update({
 "[hushed, fast]{neutralA}August is with someone else so we got a second. {worryA}He has some... trust issues. He keeps asking about you so I'm just gonna tell you everything I told him. It's a lot.":
    "[hushed, fast]{neutralA}August 正跟别人在一起，所以我们有一秒空隙。{worryA}他有点……信任问题。他一直问起你，所以我干脆把跟他说的全告诉你。内容挺多。",
 "[not great] Great.": "[not great] 好极了。",
 "[hushed, fast]So here's the setup, you're Lidia Strauss. We're old friends. You're an archaeologist that stole the vault key from a dig site on Eden-6. But you're originally from Eden-5. You contacted me and we met at Pyro Pete's just after Mercenary's Day to talk about the deal. Then I set you up with August. You provide the key. August and I go make the deal, then then we split the money 3 ways. The rest of it, you're just gonna have to improvise. Did you get all that?":
    "[hushed, fast]设定是这样的：你叫 Lidia Strauss。我们是老朋友。你是考古学家，从 Eden-6 的一处发掘现场偷出了秘藏钥匙。但你原本来自 Eden-5。你联系了我，我们在雇佣兵节之后在火佬彼特酒吧见面谈了这笔交易。然后我把你介绍给 August。你提供钥匙。我和 August 去谈成交易，然后我们三个人分钱。剩下的你就只能随机应变了。都记住了吗？",
 "{worryB}but he just kept asking questions.": "{worryB}但他就是一直追问。",
 "You need to know all this, just in case.": "你得知道这些，以防万一。",
 "{worryB}I told you. It's a lot, I know...": "{worryB}我跟你说了。内容很多，我知道……",
 "One more time.": "再说一遍。",
 "{angryA}Uh, you're killing me, Fiona.  [jokingly slow] Okay, you are-":
    "{angryA}呃，你要我的命啊，Fiona。[jokingly slow] 好，你是——",
 "{inquireB}Give it to me one more time.": "{inquireB}再给我说一遍。",
 "{happyA}Good. Good. That's a relief.": "{happyA}好。很好。那我就放心了。",
 "{smugA}Yeah Sasha. I got it. This isn't my first rodeo.":
    "{smugA}是啊 萨莎。我记住了。这又不是我第一次干这个。",
 "Yeah, I got it.": "嗯，我记住了。",
 "Uh... no.": "呃……没有。",
 "You're Livia Strauss. You're an-": "你是 Livia Strauss。你是个——",
 "{sadB}Uh... no. {sternB}You need to slow down Sasha. You're talking a mile a minute.":
    "{sadB}呃……没有。{sternB}你得说慢点 萨莎。你一口气说得太快了。",
 "{inquireA}You get it? You don't get it? {inquireB}Just, use your words.":
    "{inquireA}你记住了？没记住？{inquireB}你就，用嘴说出来。",
 "{HappyA}Tommy, come on. How far do we go back?": "{HappyA}Tommy，别这样。我们认识多少年了？",
 "{happyB}[laughing]": "{happyB}[laughing]",
 "Thanks again.": "再次感谢。",
 "{HappyA}{body-X} Oh, hey. Sasha tells me you've got something really cool to show me.":
    "{HappyA}{body-X} 哦，嘿。萨莎 跟我说你有样特别酷的东西要给我看。",
 "I've known your family a real long time, August.": "我认识你们家很久了，August。",
 "{happyA}That's right. Which is why this is all gonna work out. Now you say hi to the missus for me, okay?":
    "{happyA}没错。所以这事肯定能成。替我跟你太太问好，行吗？",
 "Will do, August... heh, buddy.": "一定，August……嘿，哥们。",
 "{smugA}It's... Lidia, right?": "{smugA}你是……Lidia，对吧？",
 "and she speaks highly of you.": "她对你评价很高。",
 "{smugC}She ensures me you can be trusted.": "{smugC}她向我保证你信得过。",
 "It's Livia actually.": "其实是 Livia。",
 "Lidia... that's me.": "Lidia……就是我。",
 "It's Libia actually.": "其实是 Libia。",
 "[dubious/confused]Livia... huh. [beat] I could've swore-":
    "[dubious/confused]Livia……嗯。[beat] 我发誓我——",
 "{happyA}It's Livia actually. Livia Strauss.": "{happyA}其实是 Livia。Livia Strauss。",
 "{HappyA}{body-hips}That's me, Lidia Strauss.": "{HappyA}{body-hips}就是我，Lidia Strauss。",
 "[smiles] Likewise.": "[smiles] 幸会。",
 "{HappyA}{body-hips}It's Libia actually. Libia Strauss.":
    "{HappyA}{body-hips}其实是 Libia。Libia Strauss。",
 "Livia. Livia Strauss.": "Livia。Livia Strauss。",
 "{smugA}Which is the only reason I'm willing to do a deal{thinkA}{body-A} with someone I don't know.":
    "{smugA}这也是我唯一愿意{thinkA}{body-A}跟一个不认识的人做交易的理由。",
 "[smiles] Right. Livia.": "[smiles] 对。Livia。",
 "{thinkB}{body-hips}You are.": "{thinkB}{body-hips}你就是。",
 "[pleading, near tears] Please... please... August... please, I'll pay... I'll pay... I'll pay... I'll pay...":
    "[pleading, near tears] 求你……求你……August……求你了，我付钱……我付钱……我付钱……我付钱……",
 "[smooth] {smugA}{body-A}Well, that was exciting.": "[smooth] {smugA}{body-A}这倒挺精彩的。",
 "{happyA}Hon, bring us over a couple drinks then start moppin' up that blood. I don't wanna have to get the floors redone.":
    "{happyA}亲爱的，给我们端两杯酒来，然后开始擦那些血。我可不想重铺地板。",
 "Let's get to business.": "我们说正事吧。",
 "[screaming, frantic] No! No! Please!": "[screaming, frantic] 不！不！求你了！",
 "Sure thing, babe.": "没问题，宝贝。",
 "{angryA}The little bastard had a Maliwan shield on. Shocked me real good. {worriedA}Sorry about the mess, boss. Won't happen again.":
    "{angryA}那小杂种身上带着马利万的护盾。把我电得不轻。{worriedA}抱歉弄乱了，老大。不会再发生了。",
 "[background, offscreen] [to Finch, putting on a drunk voice] Skip out on his tab?":
    "[background, offscreen] [to Finch, putting on a drunk voice] 赖账跑路了？",
 "[background, offscreen] Yeah, somethin' like that.":
    "[background, offscreen] 是啊，差不多吧。",
 "I'll take that drink.": "那杯酒我要了。",
 "Do your deals always end like that?": "你的交易总是这么收场吗？",
 "I like your style.": "我喜欢你的风格。",
 "{happyA}Coming right up.": "{happyA}马上就来。",
 "{smugA}Sasha, make mine a double... whatever it is.":
    "{smugA}萨莎，给我来双份……不管是什么。",
 "{smugB}Nope... {smugC}I just like to drink.": "{smugB}不是……{smugC}我只是喜欢喝酒。",
 "{smugB}Hope the gunplay didn't set your nerves off.":
    "{smugB}希望刚才的枪战没让你神经紧绷。",
 "{ThinkA}He said he'd do something, then he didn't. [beat] {thinkA}I don't abide dishonest people.":
    "{ThinkA}他说他会做某件事，然后他没做。[beat] {thinkA}我看不惯不诚实的人。",
 "{SternA}Your business deals always go like that?":
    "{SternA}你的生意总是这么谈的？",
 "{worryB}Uh, yeah. Does the job. {smugA}It breaks about even which is about the most I can ask.":
    "{worryB}呃，是啊。管用就行。{smugA}差不多不赔不赚，这已经是我能要求的最好结果了。",
 "[it's not nice]{worryB}Nice... place you got here.":
    "[it's not nice]{worryB}你这地方……挺不错。",
 "{HappyA}Have a seat.": "{HappyA}坐吧。",
 "{smugA}Hey, where'd you say you found this again?": "{smugA}嘿，你刚才说这东西在哪儿找到的？",
 "Sasha mentioned it was one of the Eden's.": "萨莎 说是在某个 Eden 星上。",
 "{thinkB}Which one was it exactly?": "{thinkB}具体是哪一个？",
 "{neutralA}Refresh my memory.": "{neutralA}帮我回忆一下。",
 "It was on Eden-5.": "是在 Eden-5。",
 "I found it on Eden-6.": "我是在 Eden-6 找到的。",
 "It's here now, what does it matter?": "它现在就在这儿，有什么关系？",
 "{sternA}What does it matter where I found it? It's here now.":
    "{sternA}我在哪儿找到的有关系吗？它现在就在这儿。",
 "{smugA}I can see how you'd like to keep the details of how you acquired the key to yourself, {smugA}what with all the pesky vault hunters crawling all over the place these days...{sternA}but if we're gonna be partners...":
    "{smugA}我能理解你想把弄到钥匙的细节保密，{smugA}毕竟这年头到处都是烦人的秘藏猎人……{sternA}但既然我们要当合伙人……",
 "{HappyA}I already told him it was Eden-6. Don't worry, you can trust August.":
    "{HappyA}我已经跟他说过是 Eden-6 了。别担心，你可以信任 August。",
 "{HappyA}See? You can trust me.": "{HappyA}看吧？你可以信任我。",
 "{doubtfulA}I found it on Eden-5. {fearA}At a {smugA}dig site there.":
    "{doubtfulA}我是在 Eden-5 找到的。{fearA}在那儿一个{smugA}发掘现场。",
 "{thinkB}Hmm... now that I think about it... pretty sure Sasha said you were from Eden-5... {sternA}but you found the key on Eden-6.":
    "{thinkB}嗯……这么一想……我很确定 萨莎 说过你来自 Eden-5……{sternA}但你是在 Eden-6 找到钥匙的。",
 "{sternA}I mean...": "{sternA}我是说……",
 "{sternB}But I like to keep the minor details straight.":
    "{sternB}但我喜欢把细节弄清楚。",
 "It's a minor detail...": "这只是个细节……",
 "I know where I'm from.": "我知道我来自哪儿。",
 "I meant Eden-6.": "我说的是 Eden-6。",
 "Sasha got it wrong.": "萨莎 搞错了。",
 "{smugB}I think I know where I'm from, August.": "{smugB}我想我知道我来自哪儿，August。",
 "{slyC}Do you?": "{slyC}是吗？",
 "{happyA}That's my fault. I must've gotten them mixed up. Sorry about that.":
    "{happyA}是我的错。我肯定把它们搞混了。抱歉。",
 "{smugA}That's alright.": "{smugA}没关系。",
 "{smugC}Did I say Eden-5? Sorry, {schemeD}you're right. I meant Eden-6.":
    "{smugC}我说 Eden-5 了吗？抱歉，{schemeD}你说得对。我说的是 Eden-6。",
 "Yeah... I guess that must be it.": "是啊……我想就是这样。",
 "{happyA}Oh, give her a break, August. She's probably tired from the trip.":
    "{happyA}哦，别为难她，August。她大概是旅途劳顿。",
 "{inquireA}Sasha can get a little confused, sometimes. She's a drinker, that's what I mean by, uh, that.":
    "{inquireA}萨莎 有时候会有点糊涂。她爱喝酒，我说的，呃，就是这个。",
 "{happyA}Yup.": "{happyA}没错。",
 "{smugB}I found it on Eden-6. {worryA}At a {smugC}dig site there.":
    "{smugB}我是在 Eden-6 找到的。{worryA}在那儿一个{smugC}发掘现场。",
 "{happyA}It's nice when you find a vault key there.":
    "{happyA}在那儿能找到秘藏钥匙可真不错。",
 "{HappyA}Right. Eden-6. Marcus is always talking about that place. Says it's really nice.":
    "{HappyA}对。Eden-6。马库斯 总提起那地方。说那儿特别好。",
 "{HappyB}It most certainly is.": "{HappyB}确实很好。",
 "{happyA}I already told him it was Eden-6. Don't worry, you can trust August.":
    "{happyA}我已经跟他说过是 Eden-6 了。别担心，你可以信任 August。",
 "{smugA}I can see how you'd like to keep the details of how you acquired the key to yourself, what with all the pesky vault hunters crawling all over the place these days... {sternA}but if we're gonna be partners...":
    "{smugA}我能理解你想把弄到钥匙的细节保密，毕竟这年头到处都是烦人的秘藏猎人……{sternA}但既然我们要当合伙人……",
 "{happyA}See? You can trust me.": "{happyA}看吧？你可以信任我。",
 "{happyA}Thanks, hon.": "{happyA}谢谢，亲爱的。",
 "{smugC}Alright... {smugA}let's have a look.": "{smugC}好……{smugA}我们看看。",
 "{smugB}Of course.": "{smugB}当然。",
 "{shockB}Whoa... it's pretty.": "{shockB}哇……真漂亮。",
 "[Grab his hand]": "[抓住他的手]",
 "{HappyA}Sorry... {HappyB}I haven't touched anything this expensive before.":
    "{HappyA}抱歉……{HappyB}我以前没碰过这么贵的东西。",
 "{shockB}Wow... it's beautiful.": "{shockB}哇……真美。",
 "{happyA}Well, I'm sold.": "{happyA}好，我被说服了。",
 "{smugA}I'll call Vasquez and get this going.": "{smugA}我打电话给 Vasquez，开始办。",
 "[a pissed guy, playing it cool]{thinkB}You're grabbing{sternB} my hand.":
    "[a pissed guy, playing it cool]{thinkB}你抓着{sternB}我的手。",
 "{slyC}[a tense breath]": "{slyC}[a tense breath]",
 "{sternC}Why... are you doing that?": "{sternC}你……干嘛这样？",
 "It's not yours yet.": "它还不是你的。",
 "It's dangerous.": "很危险。",
 "Look. Don't touch.": "听着。别碰。",
 "{HappyA}Well, she's saving you from a couple of hours puking your guts out.":
    "{HappyA}这个嘛，她是在救你，不然你得吐上几个小时的苦胆。",
 "{HappyC}You never heard of Eridium poisoning?": "{HappyC}你没听说过镒矿中毒吗？",
 "{happyA}She's helping you out, August.": "{happyA}她是在帮你，August。",
 "How's that?": "怎么说？",
 "{worryA}Can't say I have.": "{worryA}我还真没听过。",
 "{fearA}Ah, well then, {happyA}thanks for that. {smugA}But just say something sooner next time.":
    "{fearA}啊，那……{happyA}谢了。{smugA}但下次早点说一声。",
 "[to Sasha] {sternA}Your friend here is making me nervous.":
    "[to Sasha] {sternA}你这朋友让我紧张。",
 "{neutralA}I'll call up Vasquez. He's been chomping at the bit for this thing.":
    "{neutralA}我打电话给 Vasquez。他对这东西早就急不可耐了。",
 "Come on Livia, quit messing with him.": "得了吧 Livia，别逗他了。",
 "{neutralA}How do you figure?": "{neutralA}你怎么看出来的？",
 "{sternC}It's not yours yet, {angryA}August.": "{sternC}它还不是你的，{angryA}August。",
 "{doubtfulA}It's radioactive.": "{doubtfulA}它带辐射。",
 "{smugB}You see with your eyes, August.": "{smugB}你用眼睛看东西，August。",
 "{sternB}What are you talking about?": "{sternB}你在说什么？",
 "Hey, Vasquez, man, it's your boy, August.": "嘿，Vasquez，老兄，是我，你的兄弟 August。",
 "[smalltime crook] {sternB}No, look... I don't even know {worryA}what [struggles]obstinate means, man. {sternA}What I know, is I gotta move this thing right now.":
    "[smalltime crook] {sternB}不，听着……我连 [struggles]固执 是什么意思都不知道，老兄。{sternA}我只知道，我现在必须把这东西出手。",
 "[hushed, cool guy voice] {slyA}I know what obstinate means. {smugA}These Hyperion guys get uncomfortable around people that sound too competent.":
    "[hushed, cool guy voice] {slyA}我知道固执是什么意思。{smugA}这些 亥博龙的人一遇到听起来太能干的人就不自在。",
 "[all business] Alright. Sasha will hold the key, since it's clear you don't trust me alone with it. And seeing as I just had a guy killed in front of you... I'm not even offended. Bring your gun, babe.":
    "[all business] 好吧。钥匙由 萨莎 拿着，既然你显然不放心让我一个人跟它待着。考虑到我刚在你面前让人杀了一个……我都不觉得被冒犯了。带上你的枪，宝贝。",
 "She'll let you know when it's done and where to get your money. Let's go.":
    "事成了她会通知你，也会告诉你到哪儿拿钱。我们走。",
 "Got it.": "明白。",
 "So, that's it?": "就这样？",
 "We'll follow in the caravan.": "我们开车队跟在后面。",
 "{HappyA}Tector!": "{HappyA}Tector！",
 "{neutralA}Yeah, boss?": "{neutralA}怎么了，老大？",
 "{HappyA}Make sure Tommy gets home alright.": "{HappyA}确保 Tommy 平安到家。",
 "{HappyA}{body-leanF}Hey, August this is-": "{HappyA}{body-leanF}嘿，August，这是——",
 "[big sigh]Ugh... Vasquez. It's August.": "[big sigh]呃……Vasquez。我是 August。",
 "Are you buyin' this Vault Key or what, 'cause I--": "你到底买不买这把秘藏钥匙，因为我——",
 "Hey wait, do you have me on speaker? Seriously?": "喂等等，你开免提了？真的假的？",
 "I'm not early! Check the comm!": "我没早到！你查通话记录！",
 "Yeah? You say \"Hi\" to your--[stops himself] He hung up.":
    "是吗？你替你跟他问——[stops himself] 他挂了。",
 "Look. Let me make it crystal clear. I want. A million. Dollars.":
    "听着。我把话说清楚。我要。一百万。美元。",
 "[processed: walking away] I don't-- I don't even know what... abstememous means.":
    "[processed: walking away] 我——我甚至不知道……abstememous 是什么意思。",
 "Ask for more money!": "多要点钱！",
 "Let's just rip 'em off.": "我们直接坑他们一把。",
 "[smalltime crook] {thinkB}I'm tryin' to do you a solid here.":
    "[smalltime crook] {thinkB}我这是在帮你个忙。",
 "[smalltime crook] [beat]{worryB}That ain't good enough, buddy boy.":
    "[smalltime crook] [beat]{worryB}这还不够，小子。",
 "[smalltime crook] I ain't that guy.": "[smalltime crook] 我不是那种人。",
 "[smalltime crook] {sternA}Don't go makin' things harder cause I'll walk.":
    "[smalltime crook] {sternA}别把事情搞复杂，不然我就走人。",
 "[smalltime crook] {sternA}No. We-We'll be there soon.":
    "[smalltime crook] {sternA}不。我们——我们马上就到。",
 "You really trust this guy?": "你真信这家伙？",
 "[hushed, cool guy voice] [shrugs] {smugA}I tried already.{smugB} Ten million is the most they could bring in cash. I'm not one for a paper trail.":
    "[hushed, cool guy voice] [shrugs] {smugA}我已经试过了。{smugB}一千万是他们能带的现金上限。我不喜欢留纸质记录。",
 "[hushed, cool guy voice] [shrugs]{neutralA}Vault hunting's a dangerous business. There aren't too many people interested in keys that are willing to pay. {sternA}Better to get the quick money.":
    "[hushed, cool guy voice] [shrugs]{neutralA}猎秘藏是危险的生意。对钥匙感兴趣又肯付钱的人不多。{sternA}还是拿快钱好。",
 "[hushed, cool guy voice] [shrugs]{smugA}We've met a few times. He's a bit of a prick, but most Hyperion guys are.":
    "[hushed, cool guy voice] [shrugs]{smugA}我们见过几面。他有点讨人厌，但大多数 亥博龙的人都这样。",
 "[hushed] {sternB}How well do you know this Vasquez guy?":
    "[hushed] {sternB}你对这个 Vasquez 有多熟？",
 "[hushed] {sternB}So, why don't we just steal the money from these Hyperion guys and keep the key?":
    "[hushed] {sternB}那我们干嘛不直接把这些 亥博龙人的钱抢了，钥匙也留下？",
 "[hushed] {neutralB}Can we get more money out of them? {sternB}It is a vault key.":
    "[hushed] {neutralB}我们能从他们那儿多要点钱吗？{sternB}毕竟是秘藏钥匙。",
 "[hushed] {inquireA}Can't blame a girl for trying.": "[hushed] {inquireA}女孩子试试也不行吗。",
 "[hushed] {inquireA}That makes sense. In and out.":
    "[hushed] {inquireA}有道理。速战速决。",
 "[hushed] {sternB}I've noticed that.": "[hushed] {sternB}我也注意到了。",
 "[smalltime crook] {sternB}Look. Let me make it crystal clear. I want ten million dollars.":
    "[smalltime crook] {sternB}听着。我把话说清楚。我要一千万。",
 "[smalltime crook] [beat] {sternA}That's right. We'll be waiting for you.":
    "[smalltime crook] [beat] {sternA}没错。我们等你。",
 "Which is the only reason I'm interested in this deal.":
    "这也是我唯一对这笔交易感兴趣的理由。",
 "{happyA}{body-A}Sasha's told me a lot about you.":
    "{happyA}{body-A}萨莎 跟我说了很多你的事。",
 "{neutralA}{body-X}Strauss?": "{neutralA}{body-X}Strauss？",
 "[dubious/confused]{smugA}Livia... huh. [beat] {sternA}{body-A}I could've swore-":
    "[dubious/confused]{smugA}Livia……嗯。[beat] {sternA}{body-A}我发誓我——",
 "{smugC}{body-A} I hope I didn't keep you waiting.":
    "{smugC}{body-A} 希望我没让你久等。",
 "{smugA}Sorry about the delay.": "{smugA}抱歉耽搁了。",
 "{thinkA}That's interesting.": "{thinkA}有意思。",
 "{sternA}{body-sitA}So, how long have you been an {thinkB}archaeologist?":
    "{sternA}{body-sitA}那你做{thinkB}考古学家多久了？",
 "Getting out there in the dirt...": "去野外钻在土里……",
 "{slyC}Fascinating work.": "{slyC}迷人的工作。",
 "{smugC}uncovering priceless artifacts.": "{smugC}发掘无价文物。",
 "{smugA}Okay... all business. {smugC}I can respect that.":
    "{smugA}好……只谈正事。{smugC}我尊重这点。",
 "I just started.": "我刚入行。",
 "I've been at it awhile.": "我干这行有一阵子了。",
 "Long enough to find a vault key.": "久到能找出一把秘藏钥匙。",
 "{smugC}Long enough... to find a vault key.":
    "{smugC}久到……能找出一把秘藏钥匙。",
 "{happyA}Well, that seems like the perfect amount of time.":
    "{happyA}那看来时间刚刚好。",
 "{HappyA}If all this goes as planned, you'll see  just how rewarding it can be.":
    "{HappyA}要是这一切按计划走，你就会明白这回报有多大。",
 "{smugC}I've been doing it a couple of years.": "{smugC}我干了几年了。",
 "{HappyA}It can be tough, but it's rewarding work.":
    "{HappyA}这活儿可能很苦，但回报不错。",
 "{happyB}Must be tough... {HappyA}being away from friends... friends like Sasha.":
    "{happyB}一定很难吧……{HappyA}离开朋友……像 萨莎 这样的朋友。",
 "{SmugC}I just started actually.": "{SmugC}其实我刚入行。",
 "{slyC}Wow. {smugB}What are the odds? Finding something as rare as a vault key so early into your career.":
    "{slyC}哇。{smugB}这运气也太好了吧？职业生涯刚开始就能找到秘藏钥匙这么稀罕的东西。",
 "{smugB}Beginners luck I guess.": "{smugB}大概是新手运气吧。",
 "[beat, studying] {sternA}Hmmm... There's probably more to it than that.":
    "[beat, studying] {sternA}嗯……恐怕不止是这样。",
 "[back to phone, smalltime crook voice] {sternA}No, man. This thing is hot. I got offers so if you want it, you gotta get down here.":
    "[back to phone, smalltime crook voice] {sternA}不，老兄。这东西很抢手。有人出价了，你想要就得下来。",
 "{smugA}They expect a nervous, small time Pandoran thug... so I give them what they want.":
    "{smugA}他们期待一个紧张兮兮的 潘多拉 小混混……那我就给他们想要的。",
 "[dubious/confused]{smugA}Libia... huh. [beat] {sternA}{body-A}I could've swore-":
    "[dubious/confused]{smugA}Libia……嗯。[beat] {sternA}{body-A}我发誓我——",
 "I guess we're a go.": "看来我们可以开始了。",
 "[smalltime crook] You gonna finish that?": "[smalltime crook] 那个你还要喝吗？",
 "[smalltime crook] What is this? Water? What're you doing?":
    "[smalltime crook] 这是什么？水？你干嘛呢？",
 "[postpax] Oh, she's a... lightweight.": "[postpax] 哦，她……酒量差。",
 "[Play it cool]": "[装作若无其事]",
 "[Nod confidently]": "[自信地点头]",
 "[Signal for help]": "[发信号求救]",
 "[Wave him off]": "[挥手打发他走]",
 "You must be August.": "你一定是 August。",
 "*Yuck*": "*呕*",
 "*Ahem*": "*咳*",
 "{angryB}Ahem...": "{angryB}咳……",
 "{angryB}August?": "{angryB}August？",
})
