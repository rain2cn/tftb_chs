# 批次3-9：第1章 env_12_prosperityjunction_shadeshouse_fiona（Fiona 被扣在 Shade 的店里 → 挑拨 Finch/Kroger → 从 Shade 房间逃出去）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g')):
    T.update(_load(_f, _n))

# —— 说话人标记（保留原文）——
T.update({
 "FINCH": "FINCH",
 "KROGER": "KROGER",
 "FIONA": "FIONA",
 "BANDIT": "BANDIT",
 "SHADE": "SHADE",
 "AUGUST": "AUGUST",
 "VAUGHN": "VAUGHN",
 "SASHA": "SASHA",
 "RHYS": "RHYS",
 "STRANGER": "STRANGER",
 "FELIX": "FELIX",
})

# —— 内部/技术条目：刻意保留英文 ——
T.update({
 "[GIVE BOOZE]": "[GIVE BOOZE]",
 "SARAH ROTH\tSO LONG, FAREWELL, I HOPE TO SEE YOU SOON....!\t10": "SARAH ROTH\tSO LONG, FAREWELL, I HOPE TO SEE YOU SOON....!\t10",
 "10 AM\t20 KB": "10 AM\t20 KB",
})

# —— 开场：Fiona 被扣在角落 ——
T.update({
 "Shade. He runs the museum.": "Shade。这家博物馆是他开的。",
 "Yeah? He's a real friggin' creepball.": "是吗？他可真是个瘆人玩意儿。",
 "Whose place is this anyway?": "这到底是谁的地方？",
 "Fiona, see that corner over there? That corner is your foster home until the deal's over.":
    "Fiona，看到那边那个角落了吗？交易结束之前，那个角落就是你的寄养家庭。",
 "Or... or until... I mean, until *our* thing's over. Right?": "或者……或者直到……我是说，直到*我们*的事办完。对吧？",
 "Beep.": "嘀。",
 "Whichever's... whichever comes first.": "哪个先……哪个先到算哪个。",
 "Okay, got it.": "好，明白。",
 "She doesn't need to know about *our* thing.": "她不需要知道*我们*的事。",
 "\"Your\" thing?": "\"你们\"的事？",
 "You don't need to concern yourself with the theoretical plans of scary people.":
    "你不用去操心可怕的人那些假设性的计划。",
 "Kroger. What's going on? You cookin' somethin' up on the side here?":
    "克罗格。怎么回事？你们在私下搞什么名堂？",
 "Just stand there quietly and don't make us nervous.": "安静站着别动，别让我们紧张。",
 "So that's it? Just \"get in the corner.\" Can't I at least take a walk outside or something?":
    "就这样？就\"站到角落去\"？我连出去散个步都不行吗？",
 "No, you cannot take a walk outside or something.": "不行，你不能出去散个步什么的。",
 "Fair? We're being *more* than fair, we're being charitable.[beat] But that can change.":
    "公平？我们*已经*够公平了，我们是在做慈善。[beat] 但那随时可以变。",
 "Guys. C'mon. This friggin' sucks.": "哥们。拜托。这他妈的太糟了。",
 "You know *I'm* the one that got the key... how is this fair at all?":
    "你们知道钥匙*是*我弄来的……这哪里公平了？",
 "[annoyed sigh]": "[annoyed sigh]",
 "Oh, don't be all, [exaggerated sigh]. It's annoying, okay? You can't be annoying, that's another rule.":
    "哦，别摆出那副[exaggerated sigh]的样子。这很烦人，行吗？不准烦人，这是另一条规矩。",
 "Kroger, it's okay. Fiona will be the perfect guest.": "克罗格，没事的。Fiona 会是最完美的客人。",
 "She will *precisely* follow the house rules, *precisely* because she is a smart woman who understands her situation.":
    "她会*一丝不苟*地遵守这里的规矩，*正因为*她是个明白自己处境的聪明女人。",
 "Will ya.": "是吗。",
 "And make no certain waves.": "而且绝不惹事生非。",
 "She will offer us no trouble.": "她不会给我们添任何麻烦。",
 "Everythin's all about her and her crap, ooohhhh, no time to play softball with me anymore! You can't be like Tracy, that's another rule.":
    "什么都围着她和她那点破事转，哦哦哦，再也没空陪我玩球了！不准像 Tracy 那样，这也是另一条规矩。",
 "Look, I just want the deal to go through and... what's mine be mine... as they say.":
    "听着，我只想把这交易做完，然后……我的归我……就像他们说的。",
 "Well that sounds like we're gonna get along just fine, then.":
    "那听起来我们会相处得很愉快。",
 "I'm a *very* smart woman, Finch. And maybe later today... you'll get a demonstration.":
    "我*非常*聪明，芬奇。也许今天晚些时候……你会看到一次演示。",
 "But I'll give you the benefit of the doubt.": "但我先不急着下结论。",
 "I'm not a master in deciphering cryptic wordplay, but... I *might* interpret that as a veiled threat.":
    "我不太擅长解读隐晦的文字游戏，但是……我*也许*会把它理解成一个暗藏的威胁。",
 "Alright, Kroger, slow it down.": "好了，克罗格，慢点。",
 "This is not the road you wanna take with me. You might not like where it ends up.":
    "跟我走这条路可不是你想要的。你可能会不喜欢它的终点。",
 "Ohhhh you-- you are givin' me flashbacks over here! All the times I wanted to punt my mom in the stomach for makin' me give the dog a bath!":
    "哦哦哦你——你让我想起过去那些破事了！每次我妈逼我给狗洗澡，我都想一脚踹在她肚子上！",
 "[exaggerated sighs again]": "[exaggerated sighs again]",
 "[sighs, then sarcastic:] It's Pandora, so... a clambake?":
    "[sighs, then sarcastic:] 这里是 潘多拉，所以……是烤蛤蜊宴？",
 "For the last time.[beat] Stow it.": "最后一次。[beat] 闭嘴。",
 "What is-- what the Hell could be going on out there?":
    "外面到底——外面到底他妈的在闹什么？",
 "[quietly] Alright, geez.": "[quietly] 好了好了，天哪。",
 "I mean, this-- whatever that is-- it's not-- it can't mess up *our* thing, right?":
    "我是说，这——不管那是什么——不会——不会搅了*我们*的事吧？",
 "[processed: far away, outside] Arrhghghhg!": "[processed: far away, outside] 啊啊啊啊！",
 "You know... Kroger?": "你知道……克罗格？",
 "Can I leave?": "我能走吗？",
 "If you have to take a dump, I don't care.": "你要是得上厕所，我不管。",
 "[serious, but quiet] I *know* what you're planning.[beat] Okay?":
    "[serious, but quiet] 我*知道*你们在谋划什么。[beat] 行吗？",
})

# —— Fiona 逼供 Kroger："我知道你们要干嘛" ——
T.update({
 "*If* there's somethin' we's been plannin'... which... I'm not sayin' there is... but *if* there is... How'd you find out?":
    "*要是*我们真在谋划什么……这个……我没说有……但*要是*有的话……你怎么知道的？",
 "Because I've seen enough stories to know that's nothin' without the proof of it.":
    "因为我故事看得够多，知道没有证据就什么都算不上。",
 "So tell me how.": "那就告诉我你是怎么知道的。",
 "[intense whisper] I'm clairvoyant.": "[intense whisper] 我有千里眼。",
 "Claire who?": "什么眼？",
 "[dreamily] Your mind is an open book to one such as I. It's not really even an open book, it's like... a book on tape that some annoying person just left playing somewhere.":
    "[dreamily] 对像我这样的人来说，你的心思是本摊开的书。其实算不上摊开的书，更像是……一本被哪个烦人精丢在哪儿一直放着的有声书。",
 "[annoyed] I'm psychic.": "[annoyed] 我是通灵的。",
 "[laughs] You? A psychic? What am I thinkin' right now, then?":
    "[laughs] 你？通灵？那我现在在想什么？",
 "Mmmmm?": "嗯…………？",
 "What is it?": "想的是什么？",
 "Can't wait to rob August!": "等不及要抢 August 了！",
 "You want seafood.": "你想吃海鲜。",
 "Concern over your height.": "担心自己的身高。",
 "[Give up]": "[放弃]",
 "[quietly intense] You're thinking... man, I can't *wait* to rob August of all that freakin' money.":
    "[quietly intense] 你在想……天哪，我真是*等不及*要把 August 那堆破钱抢过来。",
 "[quietly] Oh. My. God.": "[quietly] 我的。天。哪。",
 "Nope, not-- not even *remotely* close.": "不对，一点——一点都不*沾边*。",
 "So... t'was all in good fun and all that, but... you can screw off now.":
    "所以……刚才是开玩笑闹着玩的，不过……你现在可以滚了。",
 "[quietly intense] You're thinking... man, ever since Finch said, \"clambake\" all I want to eat are seafood. Why did I skip lunch?":
    "[quietly intense] 你在想……天哪，自从 芬奇 说了\"烤蛤蜊宴\"，我就只想吃海鲜。我干嘛要跳过午饭？",
 "Sure you do.[tiredly] And *how* do you know, this time? Tea leaves?":
    "你当然知道。[tiredly] 那这次你是*怎么*知道的？看茶叶渣？",
 "You know, I *do* know what you're planning.": "你知道吧，我*确实*知道你们在谋划什么。",
 "[quietly intense] You're thinking... am I tall enough for the world to really respect me?":
    "[quietly intense] 你在想……我够高吗，这个世界真的会尊重我吗？",
 "You better watch it, girlie. I'm not in any mood for jokes about my general appearance, okay, I get that enough from my church.":
    "你最好注意点，丫头。我可没心情听人拿我的长相开玩笑，行吗，我在教会里听得够多了。",
 "That's what I thought.": "我就知道。",
 "No way. He wouldn't. Finch is a rock.": "不可能。他不会的。芬奇 是块石头。",
 "[sighs] Fine. I'll play along.[beat] What'd he tell you.":
    "[sighs] 行。我陪你玩。[beat] 他跟你说了什么。",
 "What'd he tell you.": "他跟你说了什么。",
 "Well that rock is more like a sponge. Pliable. Drains easily.":
    "那块石头其实更像海绵。柔顺。一挤就出水。",
 "You know, two people can't really keep a secret unless... one of them is dead.":
    "你知道，两个人要真守住一个秘密，除非……其中一个死了。",
 "Especially some two bit grifter who's stuck in a basement.":
    "尤其是某个被困在地下室的三流骗子。",
 "Because my buddy Finch ain't talked to nobody.": "因为我哥们 芬奇 谁都没说过话。",
 "He said you're plannin' to steal the Vault Key.": "他说你们打算偷秘藏钥匙。",
 "We're not some backwater podunks playin' adventure.[beat] Now go back to your friggin' corner. Leave me alone.":
    "我们可不是什么玩冒险游戏的乡下土包子。[beat] 现在滚回你那该死的角落去。别烦我。",
 "Why the Heck would we steal the Vault Key? You think we're stupid?":
    "我们干嘛要去偷秘藏钥匙？你觉得我们蠢吗？",
 "He told me... that you're plannin' on takin' that money from August the very first chance you get.":
    "他告诉我……你们打算一有机会就从 August 手里把那笔钱拿走。",
 "He told me... that you're plannin' on runnin' away together. Get married, go to some exotic island, shack up, start a boat repair shop.":
    "他告诉我……你们打算一起私奔。结婚，去个异国小岛，同居，开一家修船铺。",
 "Nahhh, he's not really....[beat; thinks] You know... I mean, if he like, really... if he confessed to likin' me or somethin', it'd be... it'd be awkard, I mean really awkward, but I might-- I might just go along with it for a month or somethin' to let him down easy.":
    "不不，他不是真的……[beat; thinks] 你知道……我是说，要是他真的……要是他跟我表白喜欢我之类的，那会很……那会很尴尬，真的超尴尬，但我可能——我可能会配合他一个月什么的，好温柔地拒绝他。",
 "But nahhhhh.": "但才不呢。",
 "Go back to your corner.": "滚回你的角落去。",
 "Okay, fun's over, go back to your corner.": "好了，玩够了，滚回你的角落去。",
 "Nothin'?": "什么都没说？",
 "[tiredly running through it] I got a sister off-planet, lost my pop to the bog, and I'll add another notch to my Death Belt if you don't turn the heck around and look the heck the other way.":
    "[tiredly running through it] 我有个妹妹在别的星球，我老爹在沼泽里没了，你要是再不他妈的转过身去朝他妈的别处看，我就要在死亡腰带上再刻一道痕了。",
 "Nothin'! I'm just curious what makes a man like you tick.":
    "什么都没说！我只是好奇像你这样的男人是靠什么运转的。",
 "Let's rap, Kroger. Tell me about yourself. Your dreams, your unfortunate realities...":
    "聊聊吧，克罗格。说说你自己。你的梦想，你那不幸的现实……",
 "Oh geez, what is this, what're ya doin'.": "哦天哪，这算什么，你在干嘛。",
 "Kroger, c'mon. Your *face* is the only source of information I need.[laughing at the ease of it all] Your expressions are giving me everything!":
    "克罗格，别这样。我需要的信息来源就是你的*脸*。[laughing at the ease of it all] 你的表情把什么都告诉我了！",
 "Oh really? What's my *face* saying the plan is, huh?":
    "哦是吗？那我的*脸*说计划是什么，啊？",
 "We're not stealing the Vault Key, alright? That would be capital D-U-M-M dumb, so...":
    "我们没在偷秘藏钥匙，行吗？那简直是蠢到家的蠢，所以……",
 "Just... c'mon, give a guy a break, go back to your corner.":
    "就……拜托，放过我吧，回你的角落去。",
})

# —— 继续套话 + 递酒 ——
T.update({
 "It seems to be saying that you are going to try and steal that Vault Key.":
    "它好像在说，你们打算想法子偷走那把秘藏钥匙。",
 "The way your eyebrows are twitchin', it's like a freakin' puppet show.":
    "你那眉毛抖的，简直像在他妈演木偶戏。",
 "You're robbing August, Kroger, c'mon, let's not pretend otherwise.":
    "你们要抢 August，克罗格，别装了。",
 "Kid-- kidnapping-- you think we're gonna *kidnap* that weirdo? He has a bed made out of *hair*.":
    "绑——绑架——你以为我们会去*绑*那个怪胎？他的床是拿*头发*做的。",
 "Who'd pay us for somebody who'd do somethin' like that? I don't know and I don't wanna know![beat] Just go away.":
    "谁会为干这种事的人付赎金？我不知道，也不想知道！[beat] 走开。",
 "Kroger, c'mon, you're kidnapping Shade, it's no big mystery.":
    "克罗格，别装了，你们在绑架 Shade，这又不是什么大秘密。",
 "Alright, show and tell's over, go away now.": "好了，表演结束了，现在走开。",
 "Shoo fly. Don't bother me.": "走开，苍蝇。别烦我。",
 "[adopting some voice] Wanna sip of the ol' bubbly?":
    "[adopting some voice] 想来一口老香槟吗？",
 "Suuuurrre.": "当……然。",
 "[curious] Thanks.[beat] I guess.": "[curious] 谢了。[beat] 我想。",
 "No probs.": "没事。",
 "No, to be honest, not really. At all.": "不，说实话，一点都不想。完全不想。",
 "Hey. C'mon. It's been like three whole minutes. Do you *really* wanna watch me until this thing's blown over?":
    "嘿。拜托。才过去三分钟。你真*愿意*一直看着我直到这事过去？",
 "But I'm gonna... because this is my job, just like your job is to keep your lid zipped.":
    "但我还是会看着……因为这是我的工作，就像你的工作是把嘴闭紧一样。",
 "C'mon, let me go.": "拜托，放我走吧。",
 "Hey.": "嘿。",
 "Safety first.[beat; puts it in his jacket] I hate fishing broken glass out of my hair.":
    "安全第一。[beat; puts it in his jacket] 我最讨厌从头发里挑碎玻璃了。",
 "Actually...": "其实……",
 "No.": "不。",
 "[sighs] Can I just get out of here? The deal will go fine, and... if it doesn't, you can hunt me down, I'll make it easy, I promise.":
    "[sighs] 我能不能就离开这儿？交易会顺利的，而且……要是不顺利，你可以来追我，我不会躲，我保证。",
 "Sure.": "好啊。",
 "Really?": "真的？",
 "If we're gonna be here awhile, why don't you... you know, tell me about yourself...":
    "既然我们要在这儿待一阵子，你干嘛不……你知道，跟我说说你自己……",
 "How'd you get into this racket? Bad bets or job fair?":
    "你是怎么入这行的？赌输了还是招聘会？",
 "'Cause this isn't a first date. And your candor is less stimulating than you think.":
    "因为这不是第一次约会。而且你的坦白没你以为的那么有意思。",
 "Take two steps back.": "往后退两步。",
 "Finch, bubby... let's not go round and round. I already *know* what you're planning.":
    "芬奇，老哥……我们别绕圈子了。我*已经知道*你们在谋划什么。",
 "[disinterested] Oh yeah?[beat] What am I plannin'.":
    "[disinterested] 哦是吗？[beat] 我在谋划什么。",
 "Look, when I said I knew what you were plannin'... I wasn't lying.":
    "听着，我说我知道你们在谋划什么的时候……我没撒谎。",
 "Tell me again what I'm *planning*?": "再说一遍我在*谋划*什么？",
 "You don't exactly need a telescope to see what's goin' on here... You're gonna try and heist the Vault Key.":
    "看清楚这里在发生什么，你压根用不着望远镜……你们打算动手抢那把秘藏钥匙。",
 "Mmmmm. The Vault Key.": "嗯。秘藏钥匙。",
 "I don't need a Vault Key. And I don't particularly *want* one, either.":
    "我不需要秘藏钥匙。我也不是特别*想要*一把。",
 "And if I *did* want one, I'd certainly not be connived into discussing it with someone like you.":
    "就算我*真的*想要，我也绝不会被人套着跟像你这样的人讨论它。",
 "No offense.": "无意冒犯。",
 "You want to kill these Hyperion guys, right? You got some kind of grudge?":
    "你们想杀了这些 亥博龙的人，对吧？你们有什么仇？",
 "A Hyperion miner pushed your nanna into a pit or somethin'?":
    "哪个 亥博龙矿工把你奶奶推进坑里了还是怎么着？",
 "I ain't got no tussle with Hyperion.[beat] And I ain't got no tussle with you, *yet*.":
    "我跟 亥博龙没梁子。[beat] 我跟你也没梁子，*暂时*。",
 "[coldly indifferent] Good chat.": "[coldly indifferent] 聊得不错。",
 "[bluntly] You're gonna rob August.": "[bluntly] 你们要抢 August。",
 "Mm. That's an intriguing premise.": "嗯。这前提挺有意思。",
 "But I wonder... what in the world could have filled your head with such a novel idea.":
    "不过我很好奇……到底是什么让你脑子里冒出这么新奇的想法。",
 "Or are you just making up stories for fun.": "还是你只是编故事解闷。",
 "You shouldn't leave your diary laying around like that.":
    "你不该把日记就那么摊在外头。",
 "It's called a journal, Fiona.[beat] A diary is for someone who uses words like, \"staycation.\"":
    "那叫日志，Fiona。[beat] 写\"日记\"的是那种会说\"宅家度假\"的人。",
 "Now, please, be a dear, keep to your mischief in silence.":
    "现在，乖一点，安静地搞你的小把戏。",
 "I mean, August can't figure out that we're--[gets cut off]":
    "我是说，August 不可能看出来我们——[gets cut off]",
 "I just guessed, is all. I'm a walking fortune cookie, what can I say?":
    "我瞎猜的，就这样。我就是个会走路的幸运饼干，我能说什么？",
 "What can I say. Go away.": "我能说什么。走开。",
 "Okay.": "好。",
 "[casual] Now get out of here.": "[casual] 现在滚出去。",
 "I know Kroger like I know the warts on my son's back.[beat] He didn't say a thing.":
    "我了解 克罗格，就像了解我儿子背上的疣子。[beat] 他什么都没说。",
 "And if you try to lie to me again, I'll be able to say that I know him like I know your insides. Which is to say... intimately.":
    "你要是再敢对我撒谎，我就能说，我了解他就像了解你的内脏一样。也就是说……了如指掌。",
 "How did you--...?": "你怎么——……？",
 "No, he didn't.": "不，他没有。",
 "Your buddy, Kroger... he sang like a stuck bird. Didn't even take much prodding, to tell you the truth.":
    "你那位哥们 克罗格……他像只被卡住的鸟一样啥都唱了。说实话，都不用怎么撬。",
 "[serous] Kroger told me everything, Finch.[beat] No foolin'.":
    "[serous] 克罗格 全告诉我了，芬奇。[beat] 不骗你。",
 "Kroger, what's that, uh... what's that *spot* on your neck, here?":
    "克罗格，你脖子上那个，呃……那个*印*是什么？",
 "Get away, alright? Just... go-- just-- stand over there.":
    "离远点，行吗？就……去——就——站那边去。",
 "Oh, it was just a bug, nevermind.": "哦，只是个虫子，算了。",
 "Huh? What are you talkin' about?": "啊？你在说什么？",
 "[muttering to herself] I hate being on the wagon...": "[muttering to herself] 我真讨厌戒酒……",
 "[muttering] Eggh. It's like cheese.": "[muttering] 呃。像奶酪一样。",
})

# —— 挑拨 Kroger（"Finch 有新欢 Doris"）——
T.update({
 "[panicky whisper] Oh, I *knew*-- I *knew* this was a *bad* idea, I don't know *why* I let Finch talk me into this, it just had, like, *stank* on it from the *very* beginning.":
    "[panicky whisper] 哦，我*就知道*——我*就知道*这主意*烂*，我不知*道*自己干嘛要让 芬奇 说服我，这事从一开始就带着一股*臭*味。",
 "[panicky whisper] I have not been able to sleep, my back is all outta whack...":
    "[panicky whisper] 我一直睡不着，我的背全乱了套……",
 "[panicky whisper] I've been daydreamin' at work and that is *not* me.":
    "[panicky whisper] 我上班的时候一直在走神，那*不是*我。",
 "[panicky whisper] I yelled at my cats for *no* reason.":
    "[panicky whisper] 我无缘无故地朝我的猫吼叫。",
 "[panicky whisper] It's been all just the stress of this.":
    "[panicky whisper] 全是这事给的压力。",
 "Finch's new steady, *Doris*. I don't know what he sees in her, to be honest. When she smiles, it's all teeth, she's like a shark.":
    "芬奇 的新相好，*Doris*。说实话我不知道他看上她什么。她一笑就是一嘴牙，像条鲨鱼。",
 "What? We already-- we got already a dame in the group, he wants doubles now?":
    "什么？我们已经——我们组里已经有个娘们了，他还想再来一个？",
 "There's another...": "还有另一个……",
 "Kroger, listen to me. All bullcrap aside... Finch wants me in on it with him.":
    "克罗格，听我说。别的废话先放一边……芬奇 想让我跟他一起干。",
 "What her?": "什么她？",
 "[getting angry] That mother-suckin'... I *knew* she was gonna... He wants the bigger share for *her*, I know he does.":
    "[getting angry] 那个混账……我*就知道*她会……他想给*她*多分一份，我知道。",
 "What? Why would he do that?": "什么？他为什么要那样？",
 "Think about it. One hundred percent of something is more than fifty percent. It's a scientific law.":
    "你想想。某样东西的百分之百比百分之五十多。这是条科学定律。",
 "Kroger, listen to me. Finch is gonna betray you.": "克罗格，听我说。芬奇 要背叛你。",
 "[quieter] I've had to take a... poop... for like... thirteen hours.":
    "[quieter] 我已经憋着……拉屎……大概……十三个小时了。",
 "This has *not* been a fun time, let me tell you.": "我跟你说，这*可不是*什么愉快的时光。",
 "Kroger, you've *got* to get out while you can, pal.[beat] This *isn't* going to work out, trust me.":
    "克罗格，趁还来得及你*必须*退出，老兄。[beat] 这事*成不了*，相信我。",
 "[panicky whisper] Look, just... don't tell him I know you know, alright? I need someone... just... *neutral*, with this, ya know?":
    "[panicky whisper] 听着，就……别告诉他我知道你知道了，行吗？这事我需要有人……就……*中立*，你懂吗？",
 "[sighs] Thanks.": "[sighs] 谢了。",
 "[cold] I prefer the term confidence artist.": "[cold] 我更愿意叫自己\"信任艺术家\"。",
 "Sure.[beat] I ain't no mark, you understand? If Kroger said anythin' about anythin', I'll deal with him later.":
    "当然。[beat] 我可不是什么好骗的肥羊，你明白吗？要是 克罗格 真说了什么，我回头再收拾他。",
 "[cold] You're a grifter, right? That's what you do.": "[cold] 你是个骗子，对吧？你就干这个的。",
 "But that doesn't mean you and I have somethin' to discuss ourselves.":
    "但那不代表你和我之间有什么好谈的。",
 "You're a grifter. Right?": "你是个骗子。对吧？",
 "And leave me with my thoughts.": "让我自己待着想想。",
 "So run along.": "所以走开吧。",
 "[Show Knife]": "[亮出小刀]",
 "Kroger wanted me to betray you.": "克罗格 想让我背叛你。",
 "He told me about Doris.": "他跟我提了 Doris。",
 "He wanted to cut you out.": "他想把你踢出局。",
 "[coldly correcting] Confidence artist.": "[coldly correcting] 信任艺术家。",
 "Yeah.[beat] I ain't no *mark*. You understand? If Kroger really said anythin' about anythin'... I'll square with him later.":
    "是啊。[beat] 我可不是什么*肥羊*。你明白吗？要是 克罗格 真说了什么……我回头再跟他算账。",
 "Imagine that.": "想不到吧。",
 "[cold] That's funny... Kroger has one that looks just alike.":
    "[cold] 真有意思……克罗格 也有一把一模一样的。",
 "Where'd you get it.": "你从哪儿弄来的。",
 "It didn't just fall outta the sky, now.": "总不能是从天上掉下来的吧。",
 "The knife...": "那把刀……",
 "I found it stuck in a dead bandit who was also stabbing another bandit.":
    "我发现它插在一个死土匪身上，那家伙当时还在捅另一个土匪。",
 "Circle of life.": "生命之环。",
 "It's mine. Kroger and I must have the same knife-guy.":
    "是我的。克罗格 和我肯定找的是同一个做刀的。",
 "His \"knife-guy's\" himself, so I doubt that very much.":
    "他的\"做刀的\"就是他自己，所以我很怀疑。",
 "But I'll be takin' this just the same.": "不过我还是要把这个拿走。",
 "Keep your mystery, then.": "那你就留着你的神秘吧。",
 "Well I had to clean it up a little.": "这个……我得把它擦干净一点啊。",
 "But later... you're gonna see a man's head twist off.":
    "但待会儿……你会看到一个人的脑袋被拧下来。",
 "He said that?": "他这么说的？",
 "Alright, well, for the time bein'... let's keep nice and composed as chamber music.":
    "好吧，那暂时……我们就保持得跟室内乐一样平和。",
 "You know when I got it? When Kroger handed it to me and said, \"Do me a favor, and gut that son of a bitch so we only have to split the money two ways.\"":
    "你知道我什么时候拿到它的吗？是 克罗格 递给我，说\"帮我个忙，把那狗娘养的开了膛，这样我们就能只分两份钱。\"",
 "Kroger wanted me to lull you into a false sense of security, and then bash in your head with any available heavy object.":
    "克罗格 想让我让你放松警惕，然后用随便什么能拿到的重物砸烂你的脑袋。",
 "If Kroger'd wanted me dead... he'd have had plenty of opportunities along the way.":
    "要是 克罗格 想让我死……这一路上他有的是机会。",
 "Mm-hm.": "嗯哼。",
 "Did he now.": "是吗。",
 "Kroger's pissed about Doris, Finch. That's why he told me.":
    "克罗格 因为 Doris 很不爽，芬奇。所以他跟我说了。",
 "What?": "什么？",
 "He's jealous of the whole arrangement.": "他对整桩安排都吃醋。",
 "Moanin' about, \"What about me, when am I gonna meet someone.... your career can only make you so happy,\" you know, on and on.":
    "一直在抱怨，\"那我呢，我什么时候才能遇到人……事业只能让你快乐到这个地步\"，你知道，没完没了。",
 "But I'm with you, Finchy. Till the end, alright? We can take him out, together.":
    "但我站你这边，芬奇y。一直到死，行吗？我们可以一起把他干掉。",
 "Kroger wanted to cut you out of the deal completely.":
    "克罗格 想把你彻底踢出这笔交易。",
 "If Kroger'd wanted me out of the deal... he'd have had plenty of opportunities to kill me along the way.":
    "要是 克罗格 想让我出局……这一路上他有的是机会杀我。",
 "*Not* that way, I mean--[gets cut off]": "*不是*那种方式，我是说——[gets cut off]",
 "I know what you mean. But that's just as likely as the other thing.[beat] It's not happenin'.":
    "我知道你什么意思。但那跟另一件事一样不可能。[beat] 不会发生的。",
 "Forget Kroger, okay, Finch? Just... hook up with me and let's do this thing, together.":
    "别管 克罗格 了，行吗，芬奇？就……跟我合作，我们一起干这事。",
 "Get. Now.": "滚。现。在。",
})

# —— Shade 来报信 + 交易开场（August / Rhys / Sasha）——
T.update({
 "Um, I just wanted to let you know that the gentlemen from Hyperion *have* arrived... only just fashionably late.":
    "呃，我只是想来通知一下，亥博龙的先生们*已经*到了……只是稍微晚了一点点，恰到好处地晚。",
 "Excuse me, excuse me, oh, I hope you haven't been too bored in here.":
    "打扰一下，打扰一下，哦，希望你们在这儿没太无聊。",
 "They seem nice!": "他们看起来挺和善的！",
 "Well except for the one that slapped me. Though... perhaps that was my fault.":
    "除了打我的那个。不过……也许那是我的错。",
 "[muttering to himself in the background] Oh, it is just so awfully *hot* in here.":
    "[muttering to himself in the background] 哦，这里面实在是*太*热了。",
 "Anyhoo... while the *negotiations* - how exciting- are going on, you can all listen in through the fan here.":
    "总之……趁着*谈判*——多么令人兴奋——进行的时候，你们可以通过这儿的通风扇听着。",
 "What is August doing?": "August 在干什么？",
 "This isn't my fault.": "这不是我的错。",
 "[Signal Sasha]": "[给 Sasha 发信号]",
 "I've been meanin' to get one of those, uh, picture-boxes, but the damned thing can never find reception...":
    "我一直想买一个那种，呃，图像盒子，但那鬼东西老是收不到信号……",
 "They're not exactly what I expected.": "他们跟我预想的不太一样。",
 "[Signal Kroger]": "[给 Kroger 发信号]",
 "[Signal Finch]": "[给 Finch 发信号]",
 "[Signal Both]": "[给两人发信号]",
 "[laughter]": "[laughter]",
 "Think you can cut me out of the loop!": "以为能把我甩在外头！",
 "Make a good cookie jar.": "当个不错的饼干罐正合适。",
 "Yes sir!": "是的先生！",
 "[being strangled] What are you talking about!": "[being strangled] 你在说什么！",
 "[struggling] Think you can get one over on me, ole boy?": "[struggling] 以为你能骗到我，老家伙？",
 "Kaw-kaww! Kaw-kaww!": "嘎——嘎！嘎——嘎！",
 "[death screams]": "[death screams]",
 "Your newest attraction.": "你最新的展品。",
 "The insolence! After I bring *you* in!": "真是放肆！明明是我把*你*带进来的！",
 "Give 'em a good home.": "给它们找个好归宿。",
 "[to herself] I wish it hadn't come to this...": "[to herself] 我真希望事情没走到这一步……",
 "No!": "不！",
 "[death gurgle]": "[death gurgle]",
 "[quickly under his breath] She's a liar.": "[quickly under his breath] 她在撒谎。",
 "Okay, stop the music, I would *know* if that happened, alright? I was right behind the wall!":
    "行了，别演了，要是真发生过我*不可能*不知道，行吗？我就在墙后面！",
 "You had your chance. You talked for God knows how long, so let me fill in some blanks here to--[gets cut off]":
    "你机会用过了。你说了不知道多久，现在让我来补几个空白——[gets cut off]",
 "Shut up!": "闭嘴！",
 "*How* would you know! You didn't even know I was *there* until a half hour ago!":
    "你*怎么*可能知道！半小时前你连我*在不在场*都不知道！",
 "I *still* don't even know if you were there, Fiona! There's no *proof* of any of this--[gets cut off]":
    "我*到现在*都还不知道你到底在不在场，Fiona！这些事一点*证据*都没有——[gets cut off]",
 "Enough!": "够了！",
 "[sigh] Yeah.[beat] There's more, though.": "[sigh] 是啊。[beat] 不过还有更多。",
 "You said something about a Bandit Lord.": "你提到过一个土匪头子。",
 "You said something about a Vault Hunter.": "你提到过一个秘藏猎人。",
 "You said that the Vault Key broke.": "你说秘藏钥匙摔碎了。",
 "You said... things got... complicated.": "你说……事情变得……复杂了。",
 "[sigh] Yeah.[beat] It did.": "[sigh] 是啊。[beat] 确实复杂了。",
 "Oh. Got it.": "哦。明白。",
 "[flat] People.": "[flat] 人嘛。",
 "Who says that?": "谁会说这种话？",
 "I hope it doesn't get in the way of our thing. I mean, if everyone's already dead, how are we goin' to kill everyone and take the money? It'll get in the way and--":
    "我希望这不会搅了我们的事。我是说，要是人都死光了，我们怎么去杀光所有人、然后把钱拿走？这会碍事，而且——",
 "Acruing. That's the one.": "是\"积累\"。就是这个。",
 "Acruing.": "是\"积累\"。",
 "A quality you seem to lack, and might consider... what's the word I'm looking  for Kroger?":
    "一种你似乎欠缺的素质，或许该考虑一下……那个词怎么说来着，克罗格？",
 "Besides, most of the truly smart people I have ever met all know when to keep their mouth shut.":
    "再说，我见过的真正聪明的人，大多都知道什么时候该把嘴闭上。",
 "*Hey*. You don't have to be so rough, alright?": "*嘿*。你不用这么粗暴，行吗？",
 "Because, we need to wait for the deal to actually transpire.":
    "因为，我们得等交易真正发生。",
 "Finch? Why don't we just kill her now?": "芬奇？我们干嘛不现在就把她杀了？",
 "You just never shut up, do you?": "你就是永远闭不上嘴，是吧？",
 "But if we're going to friggin' kill her anyways...": "可反正我们都他妈要杀她了……",
 "[Forceful]Kroger! ...If the deal doesn't happen, we  bring her back to Vallory. So *she* can kill her.":
    "[Forceful]克罗格！……要是交易没成，我们就把她带回给 瓦洛里。让*她*来杀。",
 "Can't we just say she tried somethin'?": "我们就不能说她动了手吗？",
 "Besides, you can't kill me. You even said so.": "再说，你们不能杀我。你自己说的。",
 "Hey, guys! There's nothin' to discuss here!": "嘿，各位！这儿没什么好讨论的！",
 "It's the great boon of free will. We can do anything we like. We simply, as if this moment, choose not to. We're being downright charitable.":
    "这就是自由意志的伟大恩赐。我们想干什么都行。我们只是，就在此刻，选择不那么做。我们简直是在做慈善。",
 "Sure we can.": "当然可以。",
 "Why don't you just try it, asshole. See what it gets you.":
    "你倒是试试看啊，混蛋。看看能落着什么好。",
 "We have a plan, we're sticking to it.": "我们有计划，我们按计划来。",
 "...I don't see how they could get much worse.": "……我看不出还能糟到哪儿去。",
 "What?! No!": "什么？！不！",
 "[to fiona]Now keep your voice down, if you don't wish for things to become unpleasant.":
    "[to fiona]现在把声音放低点，如果你不想让事情变得不愉快的话。",
 "Ha, you'll be getting out in a body bag.": "哈，你会是装在尸袋里出去的。",
 "Just let me out of here!": "让我出去！",
 "Oh, they can.": "哦，它们能。",
 "Please. She'll just go in the corpse hole like everyone else.":
    "拜托。她会跟其他人一样被扔进尸体坑。",
 "We should just put a hole in her head'n be done with it.":
    "我们干脆在她脑袋上开个洞，了事。",
 "I don't like this. She gonna screw up our plan to --[interrupted]":
    "我不喜欢这样。她会搅了我们的计划，去——[interrupted]",
 "Wait, screw up your plan to--steal the money.": "等等，搅了你们去——抢钱的计划。",
 "It'll get you a bullet, if you don't shut your mouth.": "你要是不闭嘴，就会换来一颗子弹。",
 "I don't know-- if it's a good plan.": "我不知道——这计划好不好。",
 "You don't know much. So, we're sticking with the plan.":
    "你知道的不多。所以，我们按计划来。",
 "I'm just some poor girl looking for her lucky big break!": "我只是个想撞大运的可怜女孩！",
 "Yeah!": "对！",
 "Ain't that just everyone's story...  huddled masses just yearning for that moment.":
    "这不就是每个人的故事嘛……挤在一起的人群，只渴望那一刻的到来。",
 "Save it for someone who cares.": "留着讲给在乎的人听吧。",
 "Let me be on the level with you.": "我跟你说实话吧。",
 "How little we care.": "我们有多不在乎。",
 "How little. we. care.": "我们。有多。不在乎。",
 "It's downright tragic.": "简直悲惨。",
 "That it is. What's the most tragic part Kroger?": "确实。最悲惨的部分是什么，克罗格？",
 "Quite right Kroger, Quite right.": "说得对，克罗格，说得对。",
 "They're like the small yippy dogs.": "他们就像那种叫个不停的小狗。",
 "You mean like Corgis? I love Corgis as long as someone else washes 'em.":
    "你是说柯基那种？我喜欢柯基，只要别人负责给它们洗澡。",
 "Always barking at everything. But do you need to be scared of them?":
    "对什么都叫。但你需要怕它们吗？",
 "This one, she talks a mean game. But she's a talker.":
    "这一个，她嘴上很凶。但她就是个嘴炮。",
 "That's right.": "没错。",
 "No! Not scared at all.": "不！一点都不怕。",
 "Naw, you can just wring a Corgi's neck, easy.": "不，你一把就能拧断柯基的脖子，轻松。",
 "[mocking][over exaggerated sigh]Uuunnngh.": "[mocking][over exaggerated sigh]呃嗯嗯。",
 "[Frustrated anger]Kroger! You can never shut your hole! So, shut your hole before I give you a bloody second one.":
    "[Frustrated anger]克罗格！你这张嘴就永远闭不上！所以在我在你身上开第二个血洞之前，把嘴闭上。",
 "[exasperated]Shouldn't have brought you in on this.": "[exasperated]真不该把你拉进这事。",
 "You're goin' ta Cut me loose. I *knew* you'd do that. Can't trust a double crosser!":
    "你要把我甩了。我*就知道*你会这么干。不能信一个背后捅刀的！",
 "[regaining composure] Kroger, there isn't going to be any third cross. My temper flared. We're doing one cross, and no more...":
    "[regaining composure] 克罗格，不会有什么第三次背叛。我刚脾气上来了。我们只背叛一次，不会更多……",
 "The triple cross. Have to watch for it.": "三重背叛。得防着点。",
 "You just need to stay calm.": "你只需要保持冷静。",
 "That's right! You're gunna triple cross me!": "没错！你要对我三重背叛！",
 "Iit doesn't matter.": "无所谓。",
 "Kroger, it doesn't matter.": "克罗格，无所谓。",
 "If you cross them once, it's a double cross.": "你背叛他们一次，叫背叛。",
 "Okay... just one... double... cross. Uh... two? One...": "好……就一次……背……叛。呃……两次？一次……",
 "And twice is a triple?": "两次就是三重？",
 "But...": "但是……",
 "Look how she's treating me. And I sure haven't done anything like double cross her... yet.":
    "看看她怎么对我的。而我肯定还没干过什么背叛她的事……暂时。",
 "You know that Vallory, is going to smoke you both.": "你知道的，瓦洛里 会把你们两个都干掉。",
 "there won't even be anything left for the skags to knaw on.": "到时连给异犬啃的东西都不会剩下。",
 "They have a gun on that big space station pointed at us right now. A gun designed to destroy cities.":
    "他们那座大太空站上有把枪现在就对着我们。一把用来摧毁城市的枪。",
 "If you think Vallory is dangerous, do you know what Hyperion is going to do?":
    "如果你觉得 瓦洛里 危险，那你知道 亥博龙会做什么吗？",
 "Which I am saying, because it's pretty sweet. It's the best offer you're going to hear all day. And that counts any other offers I might make.":
    "我这么说，是因为这条件挺优厚。这是你今天能听到的最好的提议。这还算上我可能提出的其他提议。",
 "I have an offer.": "我有个提议。",
 "It's a pretty sweet one if I do say so myself.": "恕我自夸，这条件挺优厚。",
 "You know what shade needs less of?": "你知道 Shade 需要少一点什么吗？",
 "His valuables.": "他的宝贝。",
})

# —— 小刀"Marissa" 与科基闲聊 ——
T.update({
 "[muttering to himself]don't need you goin' all... action hero on me. Cralwlin' in vents, gettin' machine guns, been enough trouble already.":
    "[muttering to himself]不需要你给我来那套……动作英雄。爬通风管、抢机枪，麻烦已经够多了。",
 "Get away from that.": "离那个远点。",
 "Ya sure? Could get a hook hand.": "你确定？说不定能换只钩子手。",
 "Ah Finch, ya always were one for the classics.": "啊 芬奇，你就喜欢走经典路线。",
 "I think they're sexy. Pirate wench an all.": "我觉得挺性感的。海盗婆娘那一款。",
 "...no.": "……不。",
 "I prefer the standard, two handed girl myself.": "我个人还是喜欢标准款，两只手的姑娘。",
 "You want to lose that hand?": "你想丢掉那只手吗？",
 "I was just stretching mine out!": "我只是在伸展我的手！",
 "I wasn't joking about your hand.": "我说你的手的时候可不是开玩笑。",
 "Yaaaaaawn.": "哈——欠。",
 "Two more steps and you're slag. Plan or no plan.": "再走两步你就成渣了。管他有没有计划。",
 "alright, if she goes any closer to the door, you can do it.": "好吧，她要是再往门口靠近一点，你就可以动手了。",
 "Let me do it! Let me doooo it.": "让我来！让我来嘛。",
 "Awwww...": "唉……",
 "It's locked.": "锁着的。",
 "I don't see a lock on it.": "我没看到有锁。",
 "Bolted shut. A dead end.": "栓死了。是条死路。",
 "I mean, as far as you're concerned. It's locked.": "我是说，对你来说。它是锁着的。",
 "...what was pretty good?": "……什么挺好的？",
 "Ha. That was actually pretty good, Kroger.": "哈。这招其实挺高明，克罗格。",
 "I uh... mean It was a speck. Not a bug. My mistake.": "我呃……我是说那是个小点。不是虫子。我搞错了。",
 "Oh uh...": "哦呃……",
 "A bug?! What kind?! Was it green?! I don't want to die! Get it off! Get it off!":
    "虫子？！哪种？！是绿色的吗？！我不想死！弄掉它！弄掉它！",
 "didn't say anything about a little bleedin'.": "我可没说不能流点血。",
 "What the hell do you want? Keep in mind, Finch said I can't kill you yet.":
    "你到底想干嘛？记住，芬奇 说了我还不能杀你。",
 "Bet you'd squeal.": "我打赌你会叫得很难听。",
 "And I've been wantin' ta bleed you like a stuck pig since I first saw ya.":
    "而且我从见你第一眼起就想把你像头被捅的猪一样放血。",
 "You do what needs done.": "该干的你就干。",
 "Get it?": "懂了吗？",
 "The wanting to bleed me, shoot me in the head, and do other horrible things. I get it.":
    "想给我放血、朝我脑袋开枪、还有干别的可怕的事。我懂。",
 "...just leave me alone, lady.": "……别烦我了，女士。",
 "I just wanted to let you know. I get it.": "我只是想让你知道。我懂。",
 "It's your job, I know. In fact? Good work.": "这是你的工作，我知道。其实？干得不错。",
 "Staaaay the course.": "坚——持——下去。",
 "You just stay the the course. Don't let me get too upity.": "你就坚持下去。别让我太飘。",
 "[confused]I uh... will?": "[confused]我呃……会的？",
 "Why you ask? Because I'm a great asset. I could help you out in dozens of ways. Hundreds! My skills are multiplicity, and my talents numerous!":
    "你问为什么？因为我是极有价值的人。我能在几十个方面帮到你。几百个！我的技能多种多样，我的才能数不胜数！",
 "you are not a pleasant person.": "你这人一点都不讨人喜欢。",
 "Won't you even consider-- it just for a little?": "你就不能考虑一下——就一下下？",
 "I would take pleasure in guttin' you, girl.": "开你的膛我会很享受的，姑娘。",
 "No?": "不行？",
 "Don't do that.": "别那样。",
 "I'm thinking...": "我在想……",
 "That you should let me go.": "你该放我走。",
 "you're supposed to ask why.": "你应该问为什么。",
 "It's all just a question of who sticks who first.": "问题就在于谁先捅谁。",
 "You know, and I know, that crossing Vallory is stupid. You don't want her as an enemy.":
    "你知道，我也知道，得罪 瓦洛里 是蠢事。你不会想让她当敌人。",
 "I already made that mistake, and look where it got me.":
    "我已经犯过那个错了，看看我落到什么下场。",
 "Everyone's the enemy. That's all there is on this podunk death pit of a crap hole.":
    "每个人都是敌人。这个乡下死坑破洞里就只有这个。",
 "Just know... when the time comes. I'm the one that does the sticken'.":
    "你只要知道……到时候。捅刀的人是我。",
 "I bet, you'd squeal real good.": "我打赌，你会叫得特别好听。",
 "Guess there's a first time for everything.": "看来什么事都有第一次。",
 "Got nothing to say?": "没什么要说的？",
 "That's a nice knife you have.": "你那把刀不错。",
 "Gutten'": "开膛",
 "[muttering]you try and take my knife and i'll gut you with my bare hands...":
    "[muttering]你敢动我的刀，我就空手把你开膛……",
 "nnnnuuuunnngh... [satisfied sigh]": "嗯嗯嗯嗯嗯……[satisfied sigh]",
 "That sounds like something to see.": "听起来挺值得一看。",
 "What are you doing?! Stop playing around. I'll take that knife away  if you keep treating it like some toy.":
    "你在干什么？！别玩了。你再把它当玩具，我就把刀收走。",
 "[completely serious]done it before... messy, but satisfyin'.":
    "[completely serious]以前干过……很脏，但挺爽。",
 "He treats you like a really stupid child. One that got dropped on his head and now walks with a limp and a slur.":
    "他把你当成个特别蠢的小孩。那种小时候脑袋摔过、现在走路一瘸一拐还大舌头的。",
 "You're right. Around here we trust our children to handle their own gutting knives.":
    "你说得对。我们这儿都放心让小孩自己拿开膛刀。",
 "he just thinks he knows everything. Thinks he does, but he doesn't... doesn't know everything.":
    "他就是自以为什么都懂。自以为懂，其实他不……不是什么都懂。",
 "He doesn't treat me like a child.": "他没把我当小孩。",
 "Your partner treats you like a child.": "你那位搭档把你当小孩。",
 "The way our plan goes, no one will be alive enough to need talkin' to.":
    "照我们的计划走，没人会活到需要跟人谈话。",
 "Taking things that belong to other people, important things, things they need. That's my specialty.":
    "拿走属于别人的东西，重要的东西，他们需要的东西。那是我的专长。",
 "Don't need ya. Got it covered.": "用不着你。我搞得定。",
 "That's a laugh. Why you?": "真可笑。凭什么你？",
 "Let that specialty be your specialty.": "那你就专心搞你的专长吧。",
 "You know, I could help you pull this triple cross off.":
    "你知道，我可以帮你把这场三重背叛做成。",
 "Or drained of blood until you die...": "或者被放血放到死……",
 "...just be quiet. This is going to work.": "……安静点。这会成的。",
 "Or killed by goons.": "或者被打手干掉。",
 "Kroger? Kroger... kroger... krooooger.": "克罗格？克罗格……克罗格……Krooooger。",
 "[to himself]This has to work.": "[to himself]这必须成功。",
 "Maybe you'll get blasted with lasers.": "也许你会被激光轰成灰。",
 "You know you're going to mess this up. Vallory, or Hyperion is going to kill you. Or both.":
    "你知道你会把这搞砸的。瓦洛里 或者 亥博龙会杀了你。或者两边都来。",
 "What?!": "什么？！",
 "Blink first, or I'll take one of your eyes.": "谁先眨眼，我就挖掉谁一只眼睛。",
 "Hey. Kroger. Let me see that bitchin' knife.": "嘿。克罗格。让我看看那把酷刀。",
 "...Yeah. One of those... things.": "……是啊。那种……东西。",
 "Also, I don't like people I'm going to use 'er on ta touch 'er. One of those... things, ya know?":
    "还有，我不喜欢我要用她去捅的人碰她。那种……讲究，你懂吗？",
 "But no, you can't have it. Skinny scruffs would have blood leaking out his ears if I gave you a weapon.":
    "但不行，你不能拿。要是我给你武器，你这小瘦猴子耳朵里都得往外冒血。",
 "Marissa is a pretty one. I can see why ya want ta handle 'er.":
    "Marissa 是把漂亮货。难怪你想摸摸她。",
})

# —— 继续拉扯 + 手比脸 （"你有癌症"）——
T.update({
 "Hey Kroger.": "嘿 克罗格。",
 "That's not true! Is it?": "那不是真的吧！是吗？",
 "Did you know if your hand is bigger than your face, you probably have cancer?":
    "你知道如果你的手比脸大，那你很可能得了癌症吗？",
 "Ha. Cancer free.": "哈。没癌症。",
 "Very funny.": "真好笑。",
 "Hey kroger.": "嘿 克罗格。",
 "Actually, it's if both your hands together are bigger than your face.":
    "其实是说，如果你两只手合起来比脸大。",
 "how's it look?": "看着怎么样？",
 "Yeah but she....": "是啊，但她……",
 "[confused]...I... yes. Precisely that.": "[confused]……我……是的。正是那样。",
 "Just ignore her. She's got nothin' but words. And you know what they say about those.":
    "别理她。她除了嘴上功夫什么都没有。你知道人们怎么说那种东西。",
 "So I'm pretty sure you have a *lot* of cancer.": "所以我很确定你得了*好多*癌症。",
 "Yeah... They can't hurt ya if you're deaf.": "是啊……你要是聋了就伤不到你。",
 "I remember what it is now. You have cancer if you're an idiot.":
    "我想起来了。你要是傻子的话才得癌症。",
 "Kroger! We talked about this.": "克罗格！我们谈过这个。",
 "You think you're funny?! we'll see how funny you are when...":
    "你以为你很好笑？！等……的时候我们再看看你有多好笑。",
 "You.": "你。",
 "What are ya looking at?": "你在看什么？",
 "...well, stop it.": "……好吧，别看了。",
 "You have dead eyes.": "你的眼神是死的。",
 "That's what my mother used to say.": "我妈以前也这么说。",
 "You ever seen a person's teeth fly out the back of their head?":
    "你见过一个人的牙齿从他后脑勺飞出来吗？",
 "You know what would be-- good to do?": "你知道什么会是——好主意吗？",
 "How about I go tell him you got the knife off me, so he doesn't get suspicious. But later, when I make the signal, we take him.":
    "不如我去跟他说，是你从我这儿把刀拿走的，这样他就不会起疑。但之后，等我发信号，我们就动手抓他。",
 "But if I had to choose, I'd back the one of you who isn't asking me to gut someone.":
    "但如果要选，我会站在你们当中那个没叫我开人膛的人那边。",
 "I could've done it, too.": "我本来也能做到。",
 "You could have tried.": "你本可以试试。",
 "So, I'm thinking, you need a new partner.": "所以我觉得，你需要个新搭档。",
 "Marissa!": "Marissa！",
 "Shhh. Don't let him know, you know.": "嘘。别让他知道，你懂的。",
 "He wanted me to distract you, and then he was going to use your own knife and slit your throat.":
    "他想让我分散你的注意，然后用你自己的刀割开你的喉咙。",
 "He took my...": "他拿走了我的……",
 "He took your knife.": "他拿走了你的刀。",
 "[super casual like]Finch is going to betray you.": "[super casual like]芬奇 要背叛你。",
 "Let's keep it under our hats for now, but when I give the signal, we'll jump him together.":
    "这事先别说出去，等我发信号，我们一起上。",
 "Kroger. Get him!": "克罗格。抓住他！",
 "Finch, now!": "芬奇，现在！",
 "I just... I got nerves.": "我只是……我有点紧张。",
 "We all got nerves. You need to get yours under control.":
    "我们都紧张。你得把你自己的控制住。",
 "So sit down, and close any holes ya might have sound coming out of.":
    "所以坐下，把身上所有能出声的洞都闭上。",
 "People should have dreams... no matter how lofty.": "人应该有梦想……不管多高远。",
 "Not interested.": "没兴趣。",
 "There's two of us, and we got guns. and an't even got ta shoot you, cause I got this.":
    "我们有两个，还有枪。而且都不用开枪打你，因为我有这个。",
 "We'll see...": "走着瞧……",
 "Okay, you're going to totally kill everyone and take the money.":
    "好，你们会把所有人都杀光，然后把钱拿走。",
 "You won't be able to keep me in here.": "你们没法把我关在这儿。",
 "I can really respect that. I can even get in on that, three guns are better than none.":
    "我真的很欣赏这个。我甚至可以加入，三把枪总比没有强。",
 "There's nothin' you can do.": "你什么都做不了。",
 "Are you sure? Cause I think I'm going to walk out of this room with your blessing. As your partner even.":
    "你确定？因为我觉得我会带着你的祝福走出这个房间。甚至是以你搭档的身份。",
 "Yeah, time to...": "是啊，该……",
 "Sounds like August is slag rollin' the deal. Guess it's time to..":
    "听着像是 August 把那交易给搞废了。看来该……",
 "Kill me?! You're already dead, you're just too dumb to know it yet!":
    "杀我？！你已经死了，只是你蠢到还没意识到！",
 "[sounds of fighting and exertion]": "[sounds of fighting and exertion]",
 "[roar of anger]": "[roar of anger]",
 "[grunt of pain]": "[grunt of pain]",
 "What do you think you want? Cause I think you want to bother me...":
    "你以为你想要什么？因为我觉得你就是想烦我……",
 "I can just disappear into the wind.": "我可以直接消失得无影无踪。",
 "Don't have ta, but I want ta. You have a quality about you. One I'd love to see removed from this planet. Permanent like.":
    "不是非得做，但我想做。你身上有种特质。我很想看着它从这个星球上消失。永久的。",
 "You don't have to kill me you know.": "你知道，你不必杀我。",
 "You're risking a lot crossing Vallory.": "得罪 瓦洛里，你冒的风险可不小。",
 "Without risk, there's no reward.": "没有风险，就没有回报。",
 "Now, why don't you buzz off before I swat ya.": "现在，在我拍死你之前，滚远点吧。",
 "[flat]My heart is breaking.": "[flat]我的心都碎了。",
 "I've changed my mind. I don't want to talk to you.": "我改主意了。我不想跟你说话。",
 "I rarely speak of him with such a soft touch.": "我很少用这么柔和的语气提起他。",
 "Your partner there seems a bit... thick.": "你那位搭档看起来有点……迟钝。",
 "You think you can do this with him? Think he can pull it off without screwing it up?":
    "你觉得跟他能干成这事？觉得他能不搞砸地办成？",
 "I could help. You know. Probably a lot.": "我可以帮忙。你知道的。大概能帮很多。",
 "...lots. I have a lot of experence with--Look I can help.":
    "……很多。我在——这方面经验很多。听着，我能帮忙。",
 "I've got buttloads of experience.": "我经验多得能堆成山。",
 "You got a load, that I won't deny.": "你确实有一堆，这我不否认。",
 "With you? Ha.": "跟你？哈。",
 "You two are going to blow this.": "你们两个会把这搞砸的。",
 "But with me, it'll work.": "但有我，就能成。",
 "This is true. It's also why it's not meant to be.": "这是真的。这也是为什么这事注定不成。",
 "I can guarantee I'm less of a block. *I'm* a downright circle. Not a sharp corner on me.":
    "我保证我不那么硌人。*我*就是个正圆。身上没有一个尖角。",
 "I already have one partner too many. One I got now is a downright block. Has its ups, but mostly downs.":
    "我搭档已经多一个了。我现在这个就是个十足的方块。有好处，但大多是坏处。",
 "come on, look. Let me in on the deal, and we'll get that money. Together.":
    "拜托，你看。让我加入这笔交易，我们就能拿到钱。一起。",
 "So run along, and leave me with my thoughts.": "所以走开吧，让我自己待着想。",
 "Careful you don't sway us from our current path.": "小心点，别把我们带偏了。",
 "[laughs]She's not classy enough for a body bag!": "[laughs]她还不够格装进尸袋！",
 "Quite right Kroger. Quite right.": "说得对，克罗格。说得对。",
 "Right into cinder.": "直接推进炉灰里。",
 "What do you think it does to people?": "你觉得它会把人变成什么样？",
 "If we blow this because 'you got nerves'...": "要是我们因为你'紧张'而搞砸了……",
 "If we still need jobs after this , I'd rather the boss was happy.":
    "要是这事之后我们还需要活儿干，我还是希望老板满意。",
 "She don't say it anymore.": "她不再说那句话了。",
 "You're funny looking.": "你长得挺逗。",
 "Why?": "为什么？",
 "'Sides, she ain't the type to promote internally. Can make an employee disgruntled.":
    "再说，她不是那种会内部提拔的人。会让员工心生不满。",
 "If you got something to say, say it. Or stow it.": "你有话就说。不然就咽回去。",
 "Regardless, if you don't want to experience it, real personal like, just walk away.":
    "不管怎样，你要是不想亲身、切身体会一下，就走开。",
 "Over there.": "去那边。",
 "Her name's Marissa.": "她叫 Marissa。",
 "You're knife's a girl?": "你的刀是个姑娘？",
 "All knives are.": "所有的刀都是。",
 "I assume you use... her... for-- lots of things.": "我猜你用它……用她……干很多事。",
 "I even get them to just, give them to me sometimes. No fuss or muss.":
    "有时候我甚至能让人直接把它们送给我。不吵不闹。",
 "Get you Marissa back, and you can just do what comes natural.":
    "把 Marissa 还给你，你就能顺其自然了。",
 "[panicing] Hey, that, uh... that-- that sounds serious, alright?":
    "[panicing] 嘿，那个，呃……那——那听起来挺严重的，行吗？",
 "[pickup2] That this is *it*!": "[pickup2] 就是这个*了*！",
})

# —— 交易现场：August / Rhys / Sasha 交锋 ——
T.update({
 "{SlyC}It's not our fault {HappyA}you wanted to {SlyB}come early.":
    "{SlyC}你想{HappyA}早到，那{SlyB}可不是我们的错。",
 "{SlyC}Eh, I'll {SmugC}be a good host.": "{SlyC}呃，我会{SmugC}当个好东道主。",
 "{sternA}Where's the key?": "{sternA}钥匙呢？",
 "[cold] {AngryA}I would {AngryB}think.": "[cold] {AngryA}我想{AngryB}也是。",
 "[trying to make a joke] {SlyB}{body-sitB}That'll buy a {SlyC}couple lunches.":
    "[trying to make a joke] {SlyB}{body-sitB}够买{SlyC}几顿午饭了。",
 "{SlyB}Yeah.": "{SlyB}是啊。",
 "[sighs] {sternA}{body-sitB}Alright, alright, {SternB}the baby wants its bottle? {ThinkB}Fine.":
    "[sighs] {sternA}{body-sitB}行行行，{SternB}宝宝要喝奶了？{ThinkB}好。",
 "{SlyA}{body-sitA}Uh uh, {SlyB}no, I know how {SmugA}this works. We see the merchandise first, {SmugC}then you see the money.":
    "{SlyA}{body-sitA}不不，{SlyB}不行，我懂{SmugA}这是什么套路。先看货，{SmugC}再看钱。",
 "{SmugA}{body-sitA}Oh we got the money, {SlyB}don't worry.":
    "{SmugA}{body-sitA}哦，钱我们有，{SlyB}别担心。",
 "{sternA}Now where's the {SternC}key?": "{sternA}现在钥匙{SternC}在哪儿？",
 "[sighs] {sternA}{body-sitA}Alright, {SternB}the baby wants its bottle? {ThinkB}Fine.":
    "[sighs] {sternA}{body-sitA}好吧，{SternB}宝宝要喝奶了？{ThinkB}好。",
 "{SlyB}We got it, alright, {SmugC}it's right here. {sternA}So show us {SternB}the key.":
    "{SlyB}我们有，行吗，{SmugC}就在这儿。{sternA}那就把{SternB}钥匙拿出来给我们看。",
 "{SlyC}Vasquez. [Laughs] He was just the {SmugA}go-between, {slyA}the middle man.":
    "{SlyC}Vasquez。[Laughs] 他只是个{SmugA}中间人，{slyA}跑腿的。",
 "{sternA}I'm the one who's {SternB}buying the key.": "{sternA}买钥匙的人是{ SternB}我。",
 "{smugB}The puppet, {SmugC}the pigeon.": "{smugB}那个傀儡，{SmugC}那个冤大头。",
 "[quietly to Vaughn]{worryC}Stop.": "[quietly to Vaughn]{worryC}停。",
 "{SlyC}What?": "{SlyC}什么？",
 "{SternA}You're {SternB}not Vasquez. I {ThinkB}know Hugo, I just talked to him a {SmugB}few hours ago.":
    "{SternA}你{SternB}不是 Vasquez。我{ThinkB}认识 Hugo，我几小时前{SmugB}才跟他通过话。",
 "[coldly freaked out] {NeutralB}{body-sitB}What the hell {SternA}are you doing?":
    "[coldly freaked out] {NeutralB}{body-sitB}你到底{SternA}在干什么？",
 "{SlyC}I'm Vasquez. And there's {SlyA}nobody else coming.":
    "{SlyC}我就是 Vasquez。而且{SlyA}不会再有别人来了。",
 "He's got {SlyC}trains leaving both ends of the station, if you {SmugC}know what I mean.[gets cut off]":
    "他这站台{SlyC}两头都发了车，如果你{SmugC}懂我意思。[gets cut off]",
 "{happyA}Yeah, he ate some bad stuff... {SlyB}or something.  I dunno. He's been camped out {SmugC}in the executive washroom since lunchtime.":
    "{happyA}是啊，他吃了什么不干净的东西……{SlyB}还是怎么着。我也不知道。他从午饭时间起就{SmugC}蹲在行政洗手间里没出来。",
 "{SlyA}Hugo couldn't make it.  He's {SlyB}sick.": "{SlyA}Hugo 来不了。他{SlyB}病了。",
 "[grossed out] {SadA}Eck, okay, I got the picture, {SadC}well done.":
    "[grossed out] {SadA}呃，行，我明白了，{SadC}说得好。",
 "{SlyA}You know, with his new {SlyB}job and all. Had to make {HappyB}an impression.":
    "{SlyA}你知道，他刚{HappyB}上了新{ SlyB}岗位。得留个{HappyB}好印象。",
 "{SlyC}{Body-sitB}Vasquez?[beat] {SmugB}Is he coming?":
    "{SlyC}{Body-sitB}Vasquez？[beat] {SmugB}他会来吗？",
 "{SmugC}Yeah, he can't, {WorryB}or couldn't , {SlyB}make it. He {FearB}had to process... {SlyB}process a new marketing... {HappyB}plan.":
    "{SmugC}嗯，他不能，{WorryB}或者说来不了。他{FearB}得处理……{SlyB}处理一个新的营销……{HappyB}方案。",
 "{HappyA}So, what's {ThinkB}your name?": "{HappyA}那，你{ThinkB}叫什么名字？",
 "{SternA}It's {SternB}Rhys.": "{SternA}叫{SternB}瑞斯。",
 "{SmugB}{body-sitB}Reece?": "{SmugB}{body-sitB}Reece？",
 "{SternC}Rhys.": "{SternC}瑞斯。",
 "{thinkB}Isn't that what I said?": "{thinkB}我不是这么说的吗？",
 "{SternB}Sure.": "{SternB}行。",
 "{SlyA}You want my name? {SternA}My name's {SternB}One Million Dollars for all you should care. {SmugC}You're a Vault Key to me, {SlyC}that's it.":
    "{SlyA}你想要我的名字？{SternA}在你眼里我叫{SternB}一百万美金就行。{SmugC}对我来说你就是一把秘藏钥匙，{SlyC}就这样。",
 "{SternA}Okay, {ShockD}okay, look, I don't know what {ThinkA}the Hell you think you're doing, {ThinkB}but... this is {RageA}not how I operate, {SmugB}alright? I expected {SternB}Vasquez, and I got {AngryA}you.":
    "{SternA}好，{ShockD}好，听着，我不知道{ThinkA}你以为你在干什么，{ThinkB}但……我{ RageA}不是这么办事的，{SmugB}行吗？我期待的是{SternB}Vasquez，结果来了个{AngryA}你。",
 "{SlyA}I have {SlyB}yours, August.[beat] {SlyC}You don't need mine.":
    "{SlyA}我有{SlyB}你的名字，August。[beat] {SlyC}你不需要知道我的。",
 "[getting frazzled] {ShockB}{body-sitB}Okay, {sternA}look, I don't know what the {RageA}Hell you think you're doing, but {SternB}we're-- we're all here for a {ThinkB}lot of money and {AngryA}a freakin' Vault Key, {ShockD}alright?":
    "[getting frazzled] {ShockB}{body-sitB}好，{sternA}听着，我不知道你{RageA}他妈以为自己在干什么，但{SternB}我们——我们都是为了{ThinkB}一大笔钱和{AngryA}一把该死的秘藏钥匙才来的，{ShockD}行吗？",
 "{sternC}Yeah!": "{sternC}对！",
 "{SternC}It doesn't {AngryA}matter what our names are. {AngryB}We're Hyperion, {SlyB}sent here on authority of {SlyC}Vasquez.":
    "{SternC}我们叫什么{AngryA}不重要。{AngryB}我们是 亥博龙的人，{SlyB}受{SlyC}Vasquez 之命来这儿。",
 "{SmugA}And we're here for one thing... {SmugB}to buy a Vault Key.":
    "{SmugA}我们来只为一件事……{SmugB}买一把秘藏钥匙。",
 "So {AngryA}why don't we skip all the yakkety-yak {AngryB}and get to it.":
    "所以{AngryA}我们就别废话了，{AngryB}直接谈正事。",
 "{ThinkB}{body-sitB}Okay, {ShockA}so... {SmugC}the way I, ah, {ShockD}usually {ThinkA}do these things is...":
    "{ThinkB}{body-sitB}好，{ShockA}那么……{SmugC}我，呃，{ShockD}平时{ThinkA}办这种事的方式是……",
 "[pickup2][louder again] Or are you going to rise to the occasion, stand tall, look me in the eyes and say \"I am a winner, Rhys\"?  [beat] Say it! Say you are the winner who is going to sell this Vault Key right now, enjoy the spoils of success, and go to his grave knowing the glory of triumph!\"":
    "[pickup2][louder again] 还是说你要挺身而出，站直了，看着我的眼睛说\"我是个赢家，瑞斯\"？[beat] 说啊！说你就是那个赢家，马上要把这把秘藏钥匙卖掉，享受成功的战利品，带着胜利的荣光进坟墓！\"",
 "\"What if I had seized that chance by the throat, what if I had beaten my fears, taken what was so rightfully mine?\"":
    "\"要是我当初一把掐住那个机会，要是我战胜了恐惧，拿回本该属于我的东西，会怎么样？\"",
 "{sternA}August.": "{sternA}August。",
 "[picukup2][softly, through his tears] I am a winner, Rhys!  [beat, then shouted] I... Am... A... Winner!":
    "[picukup2][softly, through his tears] 我是个赢家，瑞斯！[beat, then shouted] 我……是……个……赢家！",
 "*Listen*. Just shut up and listen for two friggin' seconds.":
    "*听着*。你就他妈闭嘴听我说两秒。",
 "What does it *look* like I'm doin'?": "我看*上去*像是在干什么？",
 "We can't kill her yet, you dumb truck.": "我们还不能杀她，你这笨卡车。",
 "What the Hell are you talkin' about? Vallory--[gets cut off]": "你他妈在说什么？瓦洛里——[gets cut off]",
 "What are you doin'?": "你在干什么？",
 "What if the Hyperion boys never show up?": "要是 亥博龙的人一直不出现呢？",
 "Only *we* can wreck this thing, okay?": "只有*我们*能把这事搞砸，行吗？",
 "But what's the *point* in waitin'?": "但等下去有什么*意义*？",
 "[plain] Well, it's been fun.": "[plain] 好吧，玩得挺开心。",
 "Hey!": "嘿！",
 "Now Vallory said to bring her back if the deal goes bad. Right? So has the deal happened yet?":
    "瓦洛里 说要是交易出问题就把她带回去。对吧？那交易发生了吗？",
 "We'd have to bring her back, precisely.": "我们确实得把她带回去。",
 "I guess... I guess we'd have to bring her back.": "我想……我想我们得把她带回去。",
 "Unless you want to get personally disemboweled by Vallory, you can't lay a finger on me unless the deal screws up.":
    "除非你想被 瓦洛里 亲手掏空肚子，否则只要交易没搞砸，你们就不能碰我一根手指。",
 "And don't-- don't take that as a-- look, you *can't* make the deal screw up, okay, that's another rule.":
    "还有别——别把这当成——听着，你们*不能*把交易搞砸，行吗，这也是另一条规矩。",
 "Ahh, the ill-fitting dreams of the aggressively ambitious.[beat] I think we both know that was never gonna happen, Fiona.":
    "啊，野心勃勃的人那些不合身的梦想。[beat] 我想我们都知道那根本不可能发生，Fiona。",
 "Wait, *you're* robbing the deal? *I* wanted to rob the deal!":
    "等等，*你们*要抢这笔交易？*我*才想抢这笔交易！",
 "[correcting herself] I mean, *you're*-- you're *robbing* the *deal*?":
    "[correcting herself] 我是说，*你们*——你们要*抢*这笔*交易*？",
 "And you...": "还有你……",
 "What! No! That's-- that's not right, guys, I mean, c'mon.":
    "什么！不！那——那不对，各位，拜托。",
 "Shut up.": "闭嘴。",
 "Don't worry, lil' chicken, not a safe will get dropped on your unconcerned head 'til it needs to.":
    "别担心，小鸡仔，不到时候保险柜不会砸在你那个毫不在意的脑袋上的。",
 "Yeah, not until we wanna.": "是啊，等我们想的时候再说。",
 "Wait until the money comes then kill anyone and everyone who stands between us and it, the end.":
    "等钱到了，然后杀掉任何挡在我们和钱之间的人，就这样。",
 "Don't make waves.": "别惹事。",
 "We're *stickin'* to the plan.": "我们*按*计划来。",
 "[repeating the plan] Wait until the money comes...": "[repeating the plan] 等钱到了……",
 "[slightly sarcastic] It's Pandora, so... a clambake?": "[slightly sarcastic] 这里是 潘多拉，所以……是烤蛤蜊宴？",
 "What the-- what the Hell is that?": "什——那到底是什么？",
 "It's a double cross!": "这是内部背叛！",
 "Everything is fine.": "一切都好。",
 "Every man for himself!": "各顾各的！",
})

# —— 交易失控前的猜疑链 ——
T.update({
 "But what if Vasquez talked?": "但要是 Vasquez 说漏了嘴呢？",
 "Nobody knows about it but us and Vasquez.": "除了我们和 Vasquez，没人知道。",
 "What if it's other-- other folks comin' for the Key?": "要是有别的——别的人也是冲着钥匙来的呢？",
 "A, uh, \"double cross?\"": "一个，呃，\"内部背叛\"？",
 "[tsk tsk] You boys are, what, the tenth guys on the deal, last to know?":
    "[tsk tsk] 你们几个，算什么，这买卖的第十拨人，最后才知道的？",
 "Isn't there a word for... when somebody goes behind the back of their partner... to get more than their fair share?":
    "有没有一个词来形容……有人背着搭档搞鬼……想拿超过自己那份的？",
 "Double cross, that's it!": "内部背叛，就是这个！",
 "Shut. Up.": "闭。嘴。",
 "Listen to the lady. Everything's *fine*.": "听这位女士的。一切都*好*。",
 "Oh please, everything's *fine*, boys. I'm sure it's just a little afternoon delight. Let's not get carried away.":
    "哦拜托，一切都*好*，小伙子们。我敢说只是点午后的小插曲。别激动过头。",
 "What! Why?": "什么！为什么？",
 "Abandon ship! Every man for himself!": "弃船！各顾各的！",
 "What the Hell are you-- Why are you listenin' to *her* for?":
    "你他妈——你干嘛要听*她*的？",
 "She seems to know--[gets cut off]": "她好像知道——[gets cut off]",
 "She seems to know what![beat] She doesn't know anything, she's just interested in savin' her own crust.":
    "她好像知道什么！[beat] 她什么都不知道，她只想保住自己那条命。",
 "Kroger's playing dumb!": "克罗格 在装傻！",
 "Finch wants to kill you!": "芬奇 想杀了你！",
 "August is playing you!": "August 在耍你！",
 "I don't know.": "我不知道。",
 "Who'd he woulda talked to? He wouldn't wanna screw this up.":
    "他能跟谁说？他不会想把这事搞砸的。",
 "It's just... Hyperion, I mean, why would they just agree to pay all that money when they could just *take* the stupid thing by force?":
    "只是……亥博龙，我是说，他们既然能直接*抢*走那玩意儿，干嘛还要同意付这么多钱？",
 "Because it's easier this way, now just relax.": "因为这样更省事，现在放松点。",
 "I don't know. Maybe... maybe we should quit it while we can--[gets cut off]":
    "我不知道。也许……也许我们该趁早收手——[gets cut off]",
 "Because maybe they know!": "因为也许他们知道！",
 "And why would we *quit* what we haven't even *started*.": "我们干嘛要*收手*，这事我们连*开始*都还没开始。",
 "Or maybe those *explosions* are Hyperion drones come to massacre the whole thing!":
    "或者那些*爆炸*是 亥博龙的无人机，来把这整件事血洗了！",
 "Or maybe it won't work!": "或者也许这根本行不通！",
 "Can you even trust each other?": "你们连彼此都信不过吧？",
 "Vallory will kill us all!": "瓦洛里 会把我们都杀了！",
 "What if Hyperion never show up?": "要是 亥博龙的人一直不出现呢？",
 "Because the deal *hasn't* *happened* *yet*.": "因为这交易*还* *没* *发生*。",
 "Bad idea, fellas.": "烂主意，伙计们。",
 "I wanted to rob the deal!": "我才是想抢这笔交易的人！",
 "[mindlessly repeating] Wait until the money comes then kill anyone and everyone who stands between us and it.":
    "[mindlessly repeating] 等钱到了，然后杀掉任何挡在我们和钱之间的人。",
 "What! She's gonna die anyway, so who freakin' cares if she knows what we're gonna do!":
    "什么！她反正都要死了，那她知不知道我们要干什么有什么关系！",
 "You're not allowed to kill me!": "你们不许杀我！",
 "Just try it, asshole.": "你倒是试试啊，混蛋。",
 "The deal will go fine!": "交易会顺利的！",
 "If you wanna kill me, I'll gladly invite you to try, but... I don't think it'll end well for you.":
    "你要是想杀我，我很乐意请你试试，但……我觉得对你来说结局不会太好。",
 "Hey. Kroger.": "嘿。克罗格。",
 "Oh yeah, what are you gonna do? *Nag* me to death?": "哦是吗，你打算怎么办？*唠叨*死我？",
 "You. Stop talking.": "你。闭嘴。",
 "That's *not* what I'm talkin' about.": "我说的*不是*这个。",
 "Nothin' to worry about, we're all gonna get paid here.": "没什么好担心的，我们都能拿到钱。",
 "Guys, hey, look, the deal's gonna go down just fine, alright?":
    "各位，嘿，听着，这交易会顺顺利利的，行吗？",
 "Who cares? *I* care!": "谁在乎？*我*在乎！",
 "Until the money actually *shows up*, this whole thing is up in the air, okay?":
    "在钱真的*到手*之前，这整件事都悬着呢，行吗？",
 "What if there's nothin' for us to *steal*!": "要是根本没什么可给*我们偷*的呢！",
 "Until we get the money, we're not *out*, do you get it?":
    "在拿到钱之前，我们还没*抽身*，你懂吗？",
 "Wow, uh, fellas, this is a *bad* idea.": "哇，呃，伙计们，这是个*烂*主意。",
 "Slag off!": "滚！",
 "Oh, go to Hell, buddy, like you and \"touched in the head\" guy over here have a better shot!":
    "哦，见鬼去吧，老兄，好像你和这边这位\"脑子有毛病\"的家伙就更行似的！",
 "Vallory doesn't really cotton to double crossers, and... you *really* don't wanna get on her Naughty list.":
    "瓦洛里 可不太待见背后捅刀的人，而且……你*真的*不想上她的黑名单。",
 "Don't concern yourself with the plans of scary people, Fiona.":
    "别去操心可怕的人的计划，Fiona。",
 "This whole thing will work... but not if you can't keep from melting down.":
    "这整件事能成……但前提是你别崩溃。",
 "Nobody else.": "没有别人。",
 "Okay, alright, I get it, I'm sorry.": "好，好吧，我明白，对不起。",
 "Not Hyperion, not August...": "不是 亥博龙，不是 August……",
 "If one of em's dead.[beat] I mean, how long have you even *known* each other?":
    "除非其中一个死了。[beat] 我是说，你们认识对方到底有多*久*？",
 "I don't know... my mama always said... the only way two people can keep a secret?":
    "我不知道……我妈总说……两个人要守住一个秘密，唯一的办法？",
 "Look, *girlie*...": "听着，*丫头*……",
 "Lets partner up": "我们合作吧",
 "You have it backwards, girlie. You're on *our* time, here.":
    "你搞反了，丫头。现在是我们*在*计时。",
 "You *idiots* are gonna get us all frickin' *killed*! Can't you rob Vallory on your *own* time and leave me out of it?":
    "你们这些*白痴*会把我们全都他妈*害死*！你们就不能在你们*自己的*时间抢 瓦洛里，别把我扯进去？",
 "Look, if you're gonna do this, I can help, okay?": "听着，你们要是真要做，我能帮忙，行吗？",
 "Whaddya say?": "怎么样？",
 "What do I say? I say splitting the pot three frickin' ways when you can just split it two is a stupid thing to do when you hold all the cards.":
    "我怎么说？我说，牌都在你手里的时候，明明能分成两份，非他妈分成三份，那是蠢事。",
 "And we *do* hold all the cards, girlie.": "而牌*确实*都在我们手里，丫头。",
 "I'm good at the whole \"Sneaky thieving\" thing, so... let's partner up. It'll make *all* of our lives that much easier.":
    "我很擅长\"偷偷摸摸地偷东西\"这种事，所以……我们合作吧。这会让*我们所有人*的日子轻松得多。",
 "And *especially* not her.": "尤其*不*告诉她。",
 "They're here, so everybody just shut up.": "他们到了，大家都闭嘴。",
 "[muttering] Vasquez and his wet nurse for all I care.": "[muttering] Vasquez 跟他奶妈一起来随便。",
 "Look, everything's *fine*.": "听着，一切都*好*。",
 "Wait wait wait, who are they?": "等等等等，他们是谁？",
 "They're here, it's all going as planned.": "他们到了，一切按计划进行。",
 "So take a load off.": "所以放松点。",
 "There's no way August or Hyperion didn't have somethin' extra worked out on the side...":
    "August 或者 亥博龙不可能没有另外的打算……",
 "[sing songy] I wouldn't be so sure about that...": "[sing songy] 我可没那么确定……",
 "For the *last* time...[gets cut off]": "*最后*一次……[gets cut off]",
 "Hey, last chance to make a deal with me. Going once, going twice...":
    "嘿，跟我做交易的最后机会。一次，两次……",
 "Oh c'mon, Kroger! Of *course* Finch would say that! Will you wake up!":
    "哦拜托，克罗格！芬奇 当然会那么说！你清醒点行不行！",
 "Wait, did August... did August just ask where Vasquez was?":
    "等等，August……August 刚才是问 Vasquez 在哪儿吗？",
 "Kroger...": "克罗格……",
 "[paranoid] Sh.": "[paranoid] 嘘。",
 "And she has *exactly* four seconds to tell what the Hell is goin' on!":
    "而她只有*整整*四秒钟说清楚到底他妈的在发生什么！",
 "That is not-- that is *not*-- That's *not* Vasquez, alright, man, that's what they just said!":
    "那不是——那不是——那不是 Vasquez，行吗，老兄，他们刚自己说的！",
 "So what?! So this little-- this little I don't even what is tryin' to pull somethin', okay, *that's* so what.":
    "那又怎样？！这个小——这个我都不知道怎么形容的家伙在搞鬼，行吧，*那又怎样*。",
 "Kroger!": "克罗格！",
 "[sighs]Fiona. Help calm my junkie loser friend, here.[beat] Did you know anythin' about this?":
    "[sighs]Fiona。帮我安抚一下我这位瘾君子废柴朋友。[beat] 这事你事先知道吗？",
 "So.*What*.": "那。又。怎样。",
 "Listen, you guys, Kroger, I mean, c'mon... you gotta believe me, I had *no* idea!":
    "听着，你们，克罗格，我是说，拜托……你们得相信我，我*完全*不知道！",
 "You *both* were in the bar, I never even *suggested* Hyperion, that was all August's thing! If his contact fell through, hey, that's not on me.":
    "是*你们俩*在酒吧里，我连 亥博龙都*没提过*，那全是 August 的主意！他的联系人出了问题，嘿，那可不赖我。",
 "Wait, you're on those *animal* meds again!? I told you *today* of *all days* keep your head clear!":
    "等等，你又吃那些*兽用*药了？！我跟你说过*今天*——偏偏今天——得保持头脑清醒！",
 "That is *not*-- that is *not* the point!": "那*不是*——那*不是*重点！",
 "Look, let's just see where this whole thing is--[gets cut off]":
    "听着，我们先看看这整件事——[gets cut off]",
})

# —— 彻底翻脸 + 逃进 Shade 的房间 ——
T.update({
 "[paranoidly yelling] No no no no, there is *somethin'* goin' on... and I am not lettin' *anyone* outta my sight until we figure out just what that somethin' is, okay?":
    "[paranoidly yelling] 不不不不，肯定*有*什么事在发生……在弄清那是什么之前，我*谁*都不放走，行吗？",
 "Yeah, what's goin' on!": "对，到底怎么回事！",
 "Okay, you see what she's doin'? She's tryin' to exploit the fact the you have the shakes right now, so...[gets cut off]":
    "好，你看出来她在干什么了吗？她在利用你现在手抖这件事，所以……[gets cut off]",
 "[paranoidly yelling] The \"shakes\"? I don't have... I don't have the *shakes* right now, Finch! I am perfectly clear!":
    "[paranoidly yelling] \"手抖\"？我没……我现在没*手抖*，芬奇！我清醒得很！",
 "Why don't you ask *Finch* what's goin' on. He's the one cool as ice right now.":
    "你干嘛不问问*芬奇*怎么回事。现在冷静得像冰的人是他。",
 "[paranoidly yelling] Yeah, no *shit* that's not true, so why would she *ever* say that, huh! Why would you two be tryin' to pin this thing on me?!":
    "[paranoidly yelling] 是啊，这话*当然*是假的，那她*干嘛*要说这种话，啊！你们俩干嘛要把这事往我头上扣？！",
 "Drop the act, Kroger! You *know* what's goin' on, you tried to bring me into it when Finch's back was turned!":
    "别装了，克罗格！你*知道*怎么回事，你趁 芬奇 背对着的时候还想拉我入伙！",
 "Okay, I know that's not true, so let's not play this like you're--[gets cut off]":
    "好了，我知道那不是真的，所以别演得好像你——[gets cut off]",
 "Okay, she doesn't know, so let's just--[gets cut off]":
    "好了，她不知道，所以我们干脆——[gets cut off]",
 "[ice cold] Okay. I've had enough of this Movie of the Week, drug freakout *bullshit*.":
    "[ice cold] 好。我受够这出每周电影、嗑药发作的*狗屁*了。",
 "Tell me... what the Hell is going on...": "告诉我……到底他妈的在发生什么……",
 "[ice cold] You have exactly three seconds to point that thing somewhere else... before it's goin' down your throat and out your friggin' ass.":
    "[ice cold] 你有整整三秒钟把那玩意儿指向别处……不然我就让它从你喉咙进去、从你那该死的屁股出来。",
 "Three.": "三。",
 "So do I...": "我也受够了……",
 "I mean it.": "我说真的。",
 "One.": "一。",
 "Four.": "四。",
 "Finch, *don't* you friggin' move.": "芬奇，你他妈*别*动。",
 "Two.": "二。",
 "Kroger's been playin' you like a harpsichord, Finch!": "克罗格 一直像弹大键琴一样在耍你，芬奇！",
 "I should *never* have brought you in!": "我*真不该*把你拉进来！",
 "I *knew* it!": "我*就知道*！",
 "Ow! You *hit* me with the gun!?": "哎哟！你用枪*打*我？！",
 "Finch has been in on it  the whole time! Those are *his* friends out there!":
    "芬奇 一直都知道！外面那些是*他*的朋友！",
 "August must be playing you *both*, don't you see that!": "August 肯定是在耍你们*两个*，你们看不出来吗！",
 "Huh?": "啊？",
 "Finch!": "芬奇！",
 "[more sounds of fighting and exertion]": "[more sounds of fighting and exertion]",
 "[fighting] Erghh... stop.... trying... to... live....!": "[fighting] 呃……别……再……想……活了……！",
 "[fighting] You.... get... off!": "[fighting] 你……给……我……滚开！",
 "[exerting] I... hate you!": "[exerting] 我……恨你！",
 "[exerting] You... drugged up... asshole!": "[exerting] 你……嗑药嗑傻的……混蛋！",
 "[sounds of fighting]": "[sounds of fighting]",
 "[exerting] This coulda been... so... easy!": "[exerting] 这本可以……很……简单的！",
 "[to herself] Reece?": "[to herself] Reece？",
 "{ThinkA}Moi?": "{ThinkA}我吗？",
 "{body-A} {sarcasticA}You just stay put, little miss. Don'tcha try nothing.":
    "{body-A} {sarcasticA}你就老实待着，小姐。别耍花招。",
 "[frustrated and without an outlet, shouted at the empty door] {Body-A} {AngryA}Don't you try nothing! {smugB}":
    "[frustrated and without an outlet, shouted at the empty door] {Body-A} {AngryA}你别耍花招！{smugB}",
 "{Body-Hips} {HappyB}Hi.": "{Body-Hips} {HappyB}嗨。",
 "{body-A} {FearA}Ah!": "{body-A} {FearA}啊！",
 "{thinkA}What are you doing in my room?": "{thinkA}你在我房间里干什么？",
 "{fearA}Not that I mind, I don't get many visitors back here.":
    "{fearA}不是说我介意，我这儿很少有客人来。",
 "Did you want something? Can I take your coat perhaps?":
    "你有事吗？要不要我帮你拿外套？",
 "{worryA}How did you get in here?!": "{worryA}你是怎么进来的？！",
 "{HappyA}Through the door.": "{HappyA}从门进来的。",
 "[still loud] {HappyB}I let those nice Hyperion men in. And then I came back here... where I belong.":
    "[still loud] {HappyB}是我放那些和善的 亥博龙先生们进来的。然后我就回到这儿……回到我该在的地方。",
 "{fearB}Is something wrong?": "{fearB}出什么事了吗？",
 "{body-handslow} {AngryA}You scared me, you asshole!": "{body-handslow} {AngryA}你吓到我了，你这混蛋！",
 "{body-armsup} {thinkA}You're the second person to call me that today. {HappyB}That's got to be good luck, right?":
    "{body-armsup} {thinkA}你是今天第二个这么叫我的人。{HappyB}这一定意味着好运，对吧？",
 "{Body-A} {SternB}What's wrong with you?": "{Body-A} {SternB}你有什么毛病？",
 "{body-A} {ThinkC}Oh, my god. So many things.[Awkward laugh]":
    "{body-A} {ThinkC}哦，天哪。毛病多着呢。[Awkward laugh]",
 "{ThinkA}But sometimes I practice.": "{ThinkA}不过有时候我会练习。",
 "{body-X} {WorryB}I uh... I {InquireA}didn't hear you come in.":
    "{body-X} {WorryB}我呃……我{InquireA}没听见你进来。",
 "{ThinkC}I get that a lot.{HappyA}": "{ThinkC}很多人这么说。{HappyA}",
 "{Body-ArmsUp} {FearA}Not-- not that I'm dead.": "{Body-ArmsUp} {FearA}不是——不是说我死了。",
 "{FearA}Where are my manners? {happyB}Come in, come in. There's plenty of room.":
    "{FearA}我的礼数呢？{happyB}进来，进来。地方够大。",
 "Do you want any tea?": "你想喝点茶吗？",
 "{ThinkC} But sometimes I like to switch things up.": "{ThinkC} 不过有时候我喜欢换换花样。",
 "{Body-X} {NeutralA} It's how I get into most places. Really.":
    "{Body-X} {NeutralA} 我进大多数地方都是这么进的。真的。",
 "{body-leanR} {SadA}Why are you back here?": "{body-leanR} {SadA}你怎么回这儿来了？",
 "{WorryB}...yeah.": "{WorryB}……是啊。",
 "[less chipper than normal] {ThinkC}You know... Pandora... does things to a person.":
    "[less chipper than normal] {ThinkC}你知道……潘多拉……会把人变得不一样。",
 "{HappyB}We could make a pillow fort!": "{HappyB}我们可以搭个枕头堡垒！",
 "You seem worried.": "你看起来有心事。",
 "The other woman and the man seemed a bit upset at them.":
    "另外那个女人和那个男人看起来对他们有点不满。",
 "But they seemed nice.": "但他们看起来挺和善。",
 "Did not want to hang out.": "不想一起玩。",
 "{body-LeanFX} {SchemeA}A couple of very dangerous creeps hijacked our deal and locked me in here.":
    "{body-LeanFX} {SchemeA}两个非常危险的怪胎劫了我们的交易，把我锁在这儿。",
 "{fearB}We were having such a nice chat.": "{fearB}我们刚才聊得正开心呢。",
 "{happyA} I don't get a lot of people like you back here.":
    "{happyA} 我这儿很少来像你这样的人。",
 "{SchemeA}And I know those guys. They have itchy trigger fingers...":
    "{SchemeA}而我了解那些人。他们手指头痒得很，就爱扣扳机……",
 "Is there anything more pure?": "还有比这更纯粹的吗？",
 "{FearA}Well, there's nothing thicker than blood. [drifitng]{thinkB}Especially when it dries, and you're scraping it off the wall, ugh...":
    "{FearA}这个嘛，没有什么比血更浓了。[drifitng]{thinkB}尤其是等它干了，你还得从墙上刮下来，呃……",
 "{AngryA}I have to get to her!": "{AngryA}我得去救她！",
 "{schemeB}And my sister is out there with them.": "{schemeB}而我妹妹就在外面跟他们在一起。",
 "[confused]{thinkB}Oookaaay.": "[confused]{thinkB}好……吧。",
 "...uh... you need *my* help?": "……呃……你需要*我*帮忙？",
 "Could you help me get out?": "你能帮我出去吗？",
 "{schemeB}Yes!": "{schemeB}能！",
 "{thinkC}Um... I do? [beat]{HappyA}Oh, meaning you need my help!":
    "{thinkC}呃……我需要吗？[beat]{HappyA}哦，你是说你需要我帮忙！",
 "{SmugB}So you need to help me get out of here.": "{SmugB}所以你得帮我从这儿出去。",
 "I mean, what would I have to gain from not being trustworthy?":
    "我是说，我不值得信任对我有什么好处？",
 "{HappyB}But I'm a people person.": "{HappyB}但我很擅长跟人打交道。",
 "{thinkA}I know it's hard to trust.": "{thinkA}我知道信任很难。",
 "{sadA}My friends are stuck out there with them.": "{sadA}我的朋友们跟他们一起困在外面。",
 "{HappyA} {Body-A}Well, if you need out, there's the way I came in.":
    "{HappyA} {Body-A}嗯，你要是想出去，我就是从那条路进来的。",
 "{SchemeA}I need to find a way to get the jump on them.":
    "{SchemeA}我得想办法先发制人。",
 "It's just nice to be really hanging out with someone... new! I hang out with people all the time.":
    "能真正跟一个……新朋友一起待着真好！我总跟人待在一起。",
 "{thinkB}They're not as vibrant as you, though.": "{thinkB}不过他们没你这么有生气。",
 "{SchemeB}No. They'll see us - at least me - leave. Then they'll kill me.":
    "{SchemeB}不行。他们会看到我们——至少看到我——离开。然后他们就会杀了我。",
 "{thinkA}Just let me know if there's anything I can help with.":
    "{thinkA}要是有我能帮上忙的，告诉我一声。",
 "I don't get to be useful often.": "我很少有机会派上用场。",
 "{thinkC}...ever.": "{thinkC}……从来没有。",
 "{HappyA}So, just let me know!": "{HappyA}所以，尽管跟我说！",
})

# —— Shade 的房间：床、通风口、工具 ——
T.update({
 "{Body-LeanL} {WorryA}So, this is where you sleep?": "{Body-LeanL} {WorryA}那，你就是睡在这儿的？",
 "{thinkB} It's where I can just close my eyes and be anything at all. Anywhere!":
    "{thinkB} 在这儿我可以闭上眼，成为任何东西。去任何地方！",
 "{happyA}Oh. Yeah. Those. [beat]I have a lot of parties.":
    "{happyA}哦。是啊。那些啊。[beat]我参加过很多派对。",
 "[confused]{sternA}...you mean dreams?": "[confused]{sternA}……你是说做梦？",
 "{body-Armsup} {HappyB}That's it! It's where the true magic happens!":
    "{body-Armsup} {HappyB}就是这个！真正魔法发生的地方！",
 "{body-A} {FearA}Sorry about that. It's chained to the wall.":
    "{body-A} {FearA}抱歉。它被链在墙上了。",
 "{ShockA}Why?": "{ShockA}为什么？",
 "{thinkC}Bed thieves. [beat]{body-hips}What do you need it for?":
    "{thinkC}偷床贼。[beat]{body-hips}你要它干什么？",
 "{body-HipL} {SchemeA}So I can get up there.": "{body-HipL} {SchemeA}这样我就能爬到那上面。",
 "{happyB}Here, I can get that for you.": "{happyB}来，我帮你弄。",
 "I'll even help!": "我还能帮你一把！",
 "{worryA}Did you see Sasha, my sister, when you were coming in? Was she okay?":
    "{worryA}你进来的时候看到我妹妹 萨莎 了吗？她还好吗？",
 "{thinkB}The pretty one with the hair?": "{thinkB}那个有头发的漂亮姑娘？",
 "{worryB}[very confused]She... has hair... yes.":
    "{worryB}[very confused]她……是有头发……对。",
 "{happyA}Oh yes, she seemed very nervous about something.":
    "{happyA}哦有，她好像对什么事很紧张。",
 "{thinkB}But I think she was... fine...": "{thinkB}但我觉得她还……好……",
 "{doubtfulA}...thanks.": "{doubtfulA}……谢了。",
 "{ThinkA}I have some tools over there. I use them...":
    "{ThinkA}我那边有些工具。我用它们……",
 "{thinkB}For... uh... things.": "{thinkB}做……呃……一些事。",
 "{happyA} {body-x}Sounds like my best bet...": "{happyA} {body-x}听着像是我最好的办法……",
 "{body-A} {SchemeB}Shade. Does this vent lead back out to the meeting room?":
    "{body-A} {SchemeB}Shade。这个通风口能通回会客厅吗？",
 "{HappyB}Oh, yes. Proper ventilation when you have, er... friends like mine, is a must.":
    "{HappyB}哦，能。有像我这样的，呃……朋友时，通风是必须的。",
 "There's nothing more important than friends.": "没有什么比朋友更重要了。",
 "{sadB}They're going to steal the money.": "{sadB}他们要把那笔钱偷走。",
 "{ThinkA}And your friends. There's nothing more important than friends.":
    "{ThinkA}还有你的朋友。没有什么比朋友更重要了。",
 "{ANgryA}That's my money. I need to save it.": "{ANgryA}那是我的钱。我得把它救回来。",
 "Not everyone is as... {fearA}lucky as me...": "不是每个人都像……{fearA}我这么走运……",
 "{Body-ArmsUp} {HappyB}Look at what we accomplished!": "{Body-ArmsUp} {HappyB}看看我们做成了什么！",
 "[only half paying attention]{SternA}We opened a vent.":
    "[only half paying attention]{SternA}我们打开了一个通风口。",
 "What a team!": "真是好队伍！",
 "{HappyB}But, we did it together! As best friends. Forever!":
    "{HappyB}但，是我们一起做到的！作为最好的朋友。永远！",
 "As best friends. Forever!": "作为最好的朋友。永远！",
 "[kind of sad]I had a lot of friends.": "[kind of sad]我以前有很多朋友。",
 "Back in Oasis, I--": "以前在 Oasis 的时候，我——",
 "It's been a long time since I had any friends.": "我已经很久没有朋友了。",
 "I bring the pluck.": "我来出胆量。",
 "I know! I'm a great adition to any sort of plan, or scheme.":
    "我知道！我对任何计划或阴谋都是极好的补充。",
 "Yeah. Okay. You can be useful.": "是啊。好吧。你能派上用场。",
 "{worryA}Anyway, I have to get moving now.": "{worryA}总之，我现在得走了。",
 "{FearB}I know it'd be safer to stay put in my bed... with some hot cocoa... what with ruffians about and all...":
    "{FearB}我知道待在我床上……喝点热可可……会更安全……毕竟外面到处都是流氓……",
 "{HappyA}Can I come with you?": "{HappyA}我能跟你一起去吗？",
 "Wait.": "等等。",
 "[loud whisper]I know the best spot to peek without getting caught. Let me come with you.":
    "[loud whisper]我知道最适合偷看又不会被抓的位置。让我跟你一起去。",
 "We can uh... I...": "我们可以呃……我……",
 "...don't want to be stuck in here alone.": "……我不想一个人困在这儿。",
 "I'll try and stay out of your way.": "我会尽量不碍你的事。",
 "You can hit me when I say something inappropriate.": "我说了不合适的话，你尽管打我。",
 "{SternA}You can come.": "{SternA}你可以来。",
 "[loud whisper] You... you won't regret this!": "[loud whisper] 你……你不会后悔的！",
 "Just stay quiet, and make yourself useful.": "安静点，然后让自己派上用场。",
 "Fine.": "行。",
 "{Body-A}{HappyB}Oh... yes. Fear is quite prudent.":
    "{Body-A}{HappyB}哦……对。恐惧是相当明智的。",
 "I uh... I can... get some work done on one of my other friends.":
    "我呃……我可以……在我另一个朋友身上做点活儿。",
 "{DoubtfulA}Stay here. It's dangerous, just... hide under {SmugA}your bed with that cocoa or something.":
    "{DoubtfulA}待在这儿。很危险，就……拿着你那杯可可{SmugA}躲到床底下什么的。",
 "Good luck saving yours.": "祝你能救回你的朋友。",
 "Don't worry. I'll just slow you down.": "别担心。我只会拖你后腿。",
 "{ThinkA}Anyway, I have lots to do around here!": "{ThinkA}总之，我这儿有好多事要做！",
 "[disappointed] I get it.": "[disappointed] 我明白。",
 "But gimme a holler if you need a hand. [wistful]Or a foot.":
    "但要帮忙就喊我一声。[wistful]或者要只脚也行。",
 "{thinkB}Other friends... waiting outside for me to... introduce them to the gang...":
    "{thinkB}别的朋友……在外面等着我……把它们介绍给大伙儿……",
 "{Body-A} {SchemeA}Good weight.": "{Body-A} {SchemeA}分量不错。",
 "{DoubtfulA}Worth a try.": "{DoubtfulA}值得一试。",
 "{body-Hips} {ThinkC}I've never opened a vent before! Always wanted to.":
    "{body-Hips} {ThinkC}我从没打开过通风口！一直想试试。",
 "{body-hips} {SchemeB}Think this will work?": "{body-hips} {SchemeB}你觉得这能行吗？",
 "{body-X} {ThinkA}Oh, what do you have there?": "{body-X} {ThinkA}哦，你那儿有什么？",
 "{thinkA}Seems like the type that can't help it.": "{thinkA}看起来是那种控制不住的类型。",
 "{thinkB}Not that I saw. They were perfect gentlemen!":
    "{thinkB}我没看到。他们是非常完美的绅士！",
 "{sternB}The Hyperion boys that showed up. What are they like? Have any weapons?":
    "{sternB}来的那些 亥博龙的人。他们什么样？带武器了吗？",
 "{schemeB} {body-hands}Something for maybe cracking a skull.":
    "{schemeB} {body-hands}大概是能砸开脑袋的东西。",
 "{thinkC}The tall one only a touch feisty.": "{thinkC}那个高的只是有点好斗。",
 "2014<<DATE": "2014<<DATE",
 "1406253728>>) Fiona might be able to reach it, if she could climb up there.":
    "1406253728>>) 如果 Fiona 能爬上去，她也许够得着。",
 "{thinkA}I didn't lock it!": "{thinkA}我没锁它！",
 "{sternC}Finch or Kroger did, I'm sure.": "{sternC}肯定是 芬奇 或 克罗格 锁的。",
 "{body-Leanr} {SternA}No going out that way. Damn.": "{body-Leanr} {SternA}那边出不去。该死。",
 "{body-A} {WorryA}Damnit. Locked.": "{body-A} {WorryA}该死。锁着。",
 "{Smuga}[soft]...yeah. That could work.": "{Smuga}[soft]……嗯。这也许行得通。",
 "{thinkB}I use the normal ways. Generally.": "{thinkB}我一般走正常途径。通常。",
 "{inquireA}Any idea how we can get out?": "{inquireA}知道我们怎么出去吗？",
 "{ThinkA} Oh! Ummm... um, um, um... There's the vent!":
    "{ThinkA} 哦！呃嗯……嗯，嗯，嗯……有通风口啊！",
 "{happyC}[overly excited]Really?! I am really glad to be helping. Like, a lot!":
    "{happyC}[overly excited]真的吗？！我特别高兴能帮上忙。真的，特别高兴！",
 "{happyB}Hiii.": "{happyB}嗨——。",
 "{smugA}...hiii.": "{smugA}……嗨——。",
 "{SchemeA}This seems to be bolted down.": "{SchemeA}这个好像被螺栓固定住了。",
 "{InquireB}Do you have any guns, explosives, something useful maybe?":
    "{InquireB}你有枪、炸药，或者什么有用的东西吗？",
 "{happyB}Useful stuff? Sure! Things like that... not in here, sadly.":
    "{happyB}有用的东西？当然有！那种东西……可惜不在这儿。",
 "{body-hips} {thinkB}Looking for something in particular?":
    "{body-hips} {thinkB}在找什么特别的东西吗？",
 "{thinkA}You can have it. I hadn't gotten around to opening it myself anyways.":
    "{thinkA}你拿去吧。反正我自己也一直没来得及打开它。",
 "{angryA}Hey! What are you... oh... so that's what was in there.":
    "{angryA}嘿！你在干——哦……原来里面是这个。",
 "{body-LeanR} {InquireA}It's no million bucks.": "{body-LeanR} {InquireA}这可不值一百万。",
 "{body-hipsx} {SternA}Finch or Kroger is probably right out there with a gun... I need to find another way out.":
    "{body-hipsx} {SternA}芬奇 或 克罗格 大概就端着枪在外面……我得另找条出路。",
 "{ANgryA}The deal's already started... I'm running out of time.":
    "{ANgryA}交易已经开始了……我时间不多了。",
 "{body-armsup} {FearB}Oooh, uh-- You probably shouldn't go out that way. Doesn't seem safe.":
    "{body-armsup} {FearB}哦，呃——你大概不该从那边出去。看起来不安全。",
 "{body-B} {SternB} Did you see Finch or Kroger out there?":
    "{body-B} {SternB} 你看到 芬奇 或 克罗格 在外面吗？",
 "{inquirea}...he's not.": "{inquirea}……他不在。",
 "{thinkC}I saw a big fellow crouched in the dark, with a gun. He... didn't seem all that nice.":
    "{thinkC}我看到一个大块头蹲在暗处，手里端着枪。他……看起来不太友善。",
 "{body-hips} {SchemeB}Might be a way out.": "{body-hips} {SchemeB}也许能出去。",
 "{body-B} {thinkA}Like that one?": "{body-B} {thinkA}像那个一样？",
 "{body-X} {doubtfulA}I'm just trying to find a way out. See if there was a vent behind it or something.":
    "{body-X} {doubtfulA}我只是想找条出路。看看它后面有没有通风口什么的。",
 "{body-A} {HappyA}Just like that one... Here, help me get the bed over there.":
    "{body-A} {HappyA}就跟那个一样……来，帮我把床搬到那边去。",
 "{happyB}That seems like a great plan.": "{happyB}这听起来是个好计划。",
 "{angryA}Those aren't going to work.": "{angryA}那些不管用。",
 "{happyA}I'm Shade! Pleasure to meet you.": "{happyA}我是 Shade！很高兴认识你。",
 "{doubtfulA}Uh... I'm Fiona.": "{doubtfulA}呃……我叫 Fiona。",
 "[deadpan] Is there?": "[deadpan] 有吗？",
 "Oh, goody.  I'll remember your birthday and everything.":
    "哦，好耶。我还会记住你生日什么的。",
 "Sure. We're best buds. Whatever you say.": "行。我们是好哥们。你说什么就是什么。",
 "I bring the pluck!": "我来出胆量！",
 "Look, Shade, thanks for your help but I don't have time to chat right now.":
    "听着，Shade，谢谢你的帮忙，但我现在没时间闲聊。",
 "[sad] Okay, I understand. [chipper again] But you can just  come over again tomorrow and we'll have a barbecue!":
    "[sad] 好吧，我明白。[chipper again] 不过你明天可以再来，我们搞个烧烤！",
 "{SternA}I gotta go.": "{SternA}我得走了。",
 "{body-B}{AngryA}I need to get that money.": "{body-B}{AngryA}我得把那笔钱拿回来。",
})

# —— 尾声：Fiona 从通风口爬出去 + 交互标签 ——
T.update({
 "[pickup3] Sure.": "[pickup3] 好。",
 "[pickup3] [distracted] {SternB}Sure.": "[pickup3] [distracted] {SternB}好。",
 "Bed": "床",
 "Vent": "通风口",
 "Front Door": "前门",
 "Back Door": "后门",
 "Crowbar": "撬棍",
 "Locker": "储物柜",
 "Desk": "书桌",
 "Pull": "拉",
 "Let me through!": "让我过去！",
 "What's wrong with you?": "你有毛病吗？",
 "I'm Fiona.": "我是 Fiona。",
 "[Cover his mouth]": "[捂住他的嘴]",
 "You scared the crap out of me!": "你把我吓死了！",
 "Asshole!": "混蛋！",
 "Yes, come with me.": "好，跟我来。",
 "No, stay here.": "不，待在这儿。",
 "[Hushed, tense energy] {SchemeA} I can hear 'em, so they can't be far.":
    "[Hushed, tense energy] {SchemeA} 我能听到他们，所以他们不会太远。",
 "There should be an air duct that leads to the room they're in. Find it. That's where you'll take your position.":
    "应该有一条通风管通往他们所在的房间。找到它。那就是你的位置。",
 "{SternA}Right. On it.": "{SternA}好。这就去。",
 "{SternA}Got it.": "{SternA}明白。",
 "[tense enegrgy]Are you in position?": "[tense enegrgy]你就位了吗？",
 "{SchemeA}I'm almost in the vent.": "{SchemeA}我快进通风口了。",
 "Good. When you get to the end of the air duct, let me know.":
    "好。到了通风管尽头告诉我一声。",
 "[alt -to herself]Hm. Sturdy enough.": "[alt -to herself]嗯。够结实。",
 "Excellent. If you run into trouble, I'll be here.":
    "很好。要是遇到麻烦，我在这儿。",
 "[hushed, tense] {inquireA}'Kay, I found the vent.": "[hushed, tense] {inquireA}好了，我找到通风口了。",
 "{body-handslow} {AngryA}You scared me you *asshole*!": "{body-handslow} {AngryA}你吓到我了，你这*混蛋*！",
 "{sternB}Get out of the way, asshole!": "{sternB}让开，混蛋！",
 "I don't have time for this.  MOVE!": "我没时间跟你耗。让开！",
 "{doubtfulA}Listen, my sister's in trouble. Let me through.":
    "{doubtfulA}听着，我妹妹出事了。让我过去。",
 "{AngryA}You scared the crap outta me!{AngryB}": "{AngryA}你把我吓死了！{AngryB}",
 "[anxious, time is running out] {SternC}Just get out of there. I need to get through.":
    "[anxious, time is running out] {SternC}快让开。我得过去。",
 "[to herself] Can't back out now.": "[to herself] 现在不能退缩。",
 "No. Stay here.": "不。待在这儿。",
 "[to herself, stealing]{SmugB}Don't mind if I do.": "[to herself, stealing]{SmugB}那我就不客气了。",
 "[to herself] What is this place?": "[to herself] 这是什么地方？",
 "[to herself, empty drawer]Nothing.": "[to herself, empty drawer]什么都没有。",
 "{worryB}Shhh. How did you get in here?!": "{worryB}嘘。你是怎么进来的？！",
 "[cheerful] {ThinkB}Hmmph, hmmph, hmmph, hmmph. After those Hyperions were kind enough to express interest in my collection.":
    "[cheerful] {ThinkB}哼哼，哼哼，哼哼，哼哼。毕竟那些 亥博龙的人好心对我的收藏表示了兴趣。",
 "[OS] Woah, what was that?": "[OS] 哇，那是什么声音？",
 "[OS] I didn't hear anything.": "[OS] 我什么都没听见。",
 "[whispering to Shade] {SternC}Keep it down!": "[whispering to Shade] {SternC}小声点！",
 "[whispering loudly] {thinkA}I came back to my special place.":
    "[whispering loudly] {thinkA}我回到我的特别之处了。",
 "[creeped out] {FearA}Sure.": "[creeped out] {FearA}行吧。",
 "[cackling] It's a little late for that.": "[cackling] 现在说这个有点晚了。",
 "{ThinkA}Oh, delighted. Sometimes you wanna talk to someone not {HappyA}decomposing, know what I mean?":
    "{ThinkA}哦，我很乐意。有时候你就是想跟一个还没{HappyA}腐烂的人说说话，懂我意思吗？",
 "{angryA}I always take care of my friends. {happyB}Even after they're gone.":
    "{angryA}我总是照顾好我的朋友。{happyB}就算他们走了之后也一样。",
 "[alt][to herself] Ugh... creepy.": "[alt][to herself] 呃……瘆得慌。",
 "[to Felix over the comm] I think I found something. How's Sasha doing?":
    "[to Felix over the comm] 我好像找到了什么。萨莎 怎么样？",
 "[over com] She cannot stall them forever.": "[over com] 她没法永远拖住他们。",
 "[alt]Ugh... gross.": "[alt]呃……恶心。",
 "[alt]Uhhh... no.": "[alt]呃……不行。",
 "[alt]I'm not touching that.": "[alt]我才不碰那个。",
 "[cont]The EMP range is weak, so you and Sasha will have to work together to pull this off.":
    "[cont]电磁脉冲装置的作用范围很小，所以你和 萨莎 得配合才能办成。",
 "[alt- for Puzzle redesign]I can see 'em. We don't have long. How do I get inside?":
    "[alt- for Puzzle redesign]我能看到他们。我们时间不多。我怎么进去？",
 "{happycx}My deepest apologies, but we're actually closed.{ThinkB} Also, this really isn't a door, but, uh...":
    "{happycx}万分抱歉，不过我们其实已经打烊了。{ThinkB} 另外，这其实不是一扇门，但是，呃……",
 "[to herself]Hm. Nothing back there.": "[to herself]嗯。后面什么都没有。",
 "Tool Chest": "工具箱",
 "Grab": "抓取",
 "Billboard": "广告牌",
 "Poster": "海报",
 "Portrait": "肖像",
 "[Smack him]": "[扇他一巴掌]",
 "Money": "钱",
 "ANIM (<<AUTHOR>>JEFF SARRE, FRI AUG 01 13": "ANIM (<<AUTHOR>>JEFF SARRE, FRI AUG 01 13",
 "25:45 2014<<date:1406924745>>) sk55_action_fionaClimbsOntoToolChest.chore":
    "25:45 2014<<date:1406924745>>) sk55_action_fionaClimbsOntoToolChest.chore",
})
