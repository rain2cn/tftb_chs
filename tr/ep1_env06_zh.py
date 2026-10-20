# 批次3-11：第1章 env_06_prosperityjunction_rhys_shadesbackroom（Rhys 线：去 Shade 的"奇珍世界"买秘藏钥匙）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g'), ('ep1_env12_zh.py', '_h'), ('ep1_env01_zh.py', '_i'),
               ('ep1_env09_zh.py', '_j')):
    T.update(_load(_f, _n))

# —— 说话人标记（保留原文）——
T.update({
 "RHYS": "RHYS",
 "RYHS": "RYHS",
 "VAUGHN": "VAUGHN",
 "SHADE": "SHADE",
 "AUGUST": "AUGUST",
 "SASHA": "SASHA",
 "FIONA": "FIONA",
 "STRANGER": "STRANGER",
 "ECHOCOMM": "ECHOCOMM",
 "LOADER": "LOADER",
})

# —— 内部 / 技术条目（刻意保留英文）——
T.update({
 "<<ID": "<<ID",
 "{B9964747-9B21-4DEE-A9DE-B89D5FBDB517}>>": "{B9964747-9B21-4DEE-A9DE-B89D5FBDB517}>>",
})

# —— 开场：Rhys 与 "August" 谈交易 ——
T.update({
 "Hugo couldn't make it.  He's sick.": "Hugo 来不了。他病了。",
 "Yeah, he ate some bad... stuff... or something.  Camped out in the executive washroom since lunchtime.":
    "是啊，他吃了什么不干净的……东西……还是怎么着。从午饭时间起就蹲在行政洗手间里没出来。",
 "He's got trains leaving both ends of the station, if you know what I --[gets cut off]":
    "他这站台两头都发车，如果你懂我——[gets cut off]",
 "Still is, actually, cause he's definitely not dead! But the place itself...[gets cut off]":
    "其实还开着，因为他绝对没死！但这地方本身……[gets cut off]",
 "He was a real thinker, you know, a real lover of animals...":
    "他是个真正的思想者，你知道，一个真正热爱动物的人……",
 "My grandpappy, he's the one who came up with this place.":
    "我爷爷，这地方就是他搞出来的。",
 "What happened? You get stuck in traffic?": "怎么了？你被堵路上了？",
 "Alright, well... I'll just leave you to your business things, then.":
    "好吧，那……我就不打扰你们谈生意了。",
 "Is, uh, is... Vasquez comin'?": "那个，呃……Vasquez 会来吗？",
 "[stern] Honey. Shut up.": "[stern] 亲爱的。闭嘴。",
 "Yeah, where's Vasquez?": "是啊，Vasquez 呢？",
 "[getting angry] You relax.": "[getting angry] 你才冷静。",
 "I'm Vasquez. And there's nobody else coming.": "我就是 Vasquez。而且不会再有别人来了。",
 "Don't tell me to shut up.": "别叫我闭嘴。",
 "Relax.": "冷静点。",
 "[laughing to himself] Because.... he's so... he's so obviously not him.[beat] Right?":
    "[laughing to himself] 因为……他……他显然根本不是他。[beat] 对吧？",
 "[coldly freaked out] What the Hell are you doing.": "[coldly freaked out] 你到底在干什么。",
 "What?": "什么？",
 "You're not Vasquez. I know Hugo, I just talked to him a few hours ago.":
    "你不是 Vasquez。我认识 Hugo，我几小时前才跟他通过话。",
 "Yeah, no, no, no, Hugo told us to tell you that we-- that he was Vasquez. As a joke, you know?":
    "是啊，不不不，Hugo 让我们告诉你，我们——他才是 Vasquez。开玩笑的，你知道？",
 "I'm the one who's buying the key.": "买钥匙的人是我。",
 "Vasquez was just the go-between, the middle man.": "Vasquez 只是个中间人，跑腿的。",
 "[quietly to Vaughn]Okay.": "[quietly to Vaughn]好。",
 "Yeah?": "是吗？",
 "Well... I guess... as long as you got the money... one Hyperion bootlicker's as good as another.":
    "这个……我想……只要你有钱……一个 亥博龙舔靴子的跟另一个也没什么两样。",
 "The puppet, the pigeon.": "那个傀儡，那个冤大头。",
 "[grossed out] Okay, I got the picture, well done.":
    "[grossed out] 好，我明白了，说得好。",
 "Yeah, he can't--he couldn't make it. He had to process... had to process a new marketing... plan.":
    "是啊，他不能——他来不了。他得处理……得处理一个新的营销……方案。",
 "But we're here to close this out for him.": "但我们是来替他敲定这事的。",
 "You know, with his new job and all. Had to make an impression.":
    "你知道，他刚上了新岗位。得留个好印象。",
 "Vasquez?[beat] Is he coming?": "Vasquez？[beat] 他会来吗？",
 "What's your name.": "你叫什么名字。",
 "You have one, right?": "你有名字吧？",
 "It's Rhys.": "叫 瑞斯。",
 "So let's all get friendly real fast. I mean, I'm trying. Aren't I? Aren't I trying?":
    "那我们就快点熟络起来吧。我是说，我在努力。不是吗？我没在努力吗？",
 "Yeah!": "对！",
 "[getting frazzled] Okay, look, I don't know what the Hell you think you're doing, but we're-- we're all here for a lot of money and a mother friggin' Vault Key, alright?":
    "[getting frazzled] 好，听着，我不知道你他妈以为自己在干什么，但我们——我们都是为了钱和一把他妈该死的秘藏钥匙才来的，行吗？",
 "I have yours. August.[beat] You don't need mine.": "我有你的名字，August。[beat] 你不需要知道我的。",
 "Rhys.": "瑞斯。",
 "Isn't that what I said?": "我不是这么说的吗？",
 "Reece?": "Reece？",
 "Just so we're on, uh, equal footing.": "只是为了让，呃，我们地位平等。",
 "You want my name? My name's One Million Dollars for all you should care. You're a Vault Key to me, that's it.":
    "你想要我的名字？在你眼里我叫一百万美金就行。对我来说你就是一把秘藏钥匙，就这样。",
 "No, we don't have to be buddies, dickhead, but... it'd just make me a heck of a lot more comfortable to know just who I'm gifting this Vault Key, too.":
    "不，我们不必当兄弟，混蛋，但……知道我把这把秘藏钥匙送给谁，会让我舒服很多。",
 "So let's skip all the yakkety-yak and get to it.": "所以别废话了，直接谈正事。",
 "And we're here for one thing... to buy a Vault Key.": "我们来只为一件事……买一把秘藏钥匙。",
 "It doesn't matter what our names our. We're Hyperion, sent here on authority of Vasquez.":
    "我们叫什么不重要。我们是 亥博龙的人，受 Vasquez 之命来这儿。",
 "Sure.": "行。",
 "Just... sit down and let's do this so we can move on with our lives.":
    "就……坐下，把这事办了，好继续过日子。",
 "This is a business transaction, we don't have to be buddies.":
    "这是一笔商业交易，我们不必当兄弟。",
 "We don't have to be friends.": "我们不必当朋友。",
 "You're not getting my name.": "你别想知道我的名字。",
 "My name's Rhys.": "我叫 瑞斯。",
 "Okay, look, I don't know what the Hell you think you're doing, but... this is not how I operate, alright? I expected Vasquez, and I got you.":
    "好，听着，我不知道你他妈以为自己在干什么，但……我不是这么办事的，行吗？我期待的是 Vasquez，结果来了个你。",
 "You can pout all you want. You're not getting my name.":
    "你爱闹脾气就闹。你别想知道我的名字。",
 "You're trying.": "你在努力。",
 "So... let's try again. My name's August. What's yours.":
    "那……我们再试一次。我叫 August。你呢。",
 "Do you want me to guess?": "你想让我猜吗？",
 "Let's see the money.": "让我们看看钱。",
 "We got it, don't worry.": "我们有，别担心。",
 "I know we said originally it was gonna be five hundred thousand...":
    "我知道我们一开始说的是五十万……",
 "You understand.": "你懂的。",
 "But I talked it over with my people.": "但我跟我的人商量过了。",
 "[sighs] Alright, the baby wants its bottle? Fine.":
    "[sighs] 好吧，宝宝要喝奶了？行。",
 "Uh uh, no, I know how this works. We see the merchandise first, then you see the money.":
    "不不不，我懂这是什么套路。先看货，再看钱。",
 "Where's the key.": "钥匙呢。",
 "[trying to make a joke] That'll buy a couple lunches.":
    "[trying to make a joke] 够买几顿午饭了。",
 "[cold] I would think.": "[cold] 我想也是。",
 "We got it, alright, it's right here. So show us the key.":
    "我们有，行吗，就在这儿。那就把钥匙拿出来给我们看。",
 "Eh, I'll be a good host.": "呃，我会当个好东道主。",
 "Now where's the key.": "现在钥匙呢。",
 "I'm August, but I figure you know that already.": "我是 August，但我想你已经知道了。",
 "You ever see anything so pretty in your miserable lives?":
    "你们这辈子见过这么漂亮的东西吗？",
 "I'd use it myself, but... you know... the monsters and all.":
    "我本想自己用，但……你知道……怪物什么的。",
 "It's state of the art alien crap.": "这是最先进的外星破烂。",
 "This thing'll practically dance at your wedding.":
    "这东西几乎能在你婚礼上跳舞。",
 "It's gorgeous.": "太美了。",
 "Eh, I've seen better.": "呃，我见过更好的。",
 "I prefer your girlfriend.": "我更喜欢你女朋友。",
 "[quietly] It's Goddamned gorgeous.": "[quietly] 这他妈太美了。",
 "Friggin' A right, it is.": "他妈的没错，就是这样。",
 "I mean, don't get me wrong, for a Vault Key it's fine... but you gotta remember, we're from Hyperion.[beat] Soooo.....":
    "我是说，别误会，作为秘藏钥匙它还行……但你得记住，我们可是 亥博龙的人。[beat] 所以……",
 "[unbelieving] Sure, okay.": "[unbelieving] 行吧，好吧。",
 "It's, ehhh...": "这个，呃……",
 "Like you could ever get with this.": "好像你能配得上这个似的。",
 "I think I prefer your girlfriend. Or maybe she just prefers me.":
    "我想我更喜欢你女朋友。或者也许她更喜欢我。",
 "Shut up.": "闭嘴。",
 "Rhys, for the love of--[gets cut off]": "瑞斯，天哪——[gets cut off]",
 "And you are flicking my last synapse.": "而你正在弹我最后一根神经。",
 "Quit it with the jokes and the ladi-friggin-da, 'I'm a charming asshole' routine, or you're gonna figure out real quick what it's like to screw up planetside, okay?":
    "别再开玩笑、摆那副他妈的'我是个迷人混蛋'的架子，不然你很快就会知道在地面上搞砸是什么滋味，行吗？",
 "And you're lucky I'm going to take that as a very mistimed, very stupid joke.":
    "你很走运，我就当你那是句时机极差、极其愚蠢的玩笑。",
 "No, that's what it is, just a joke, that's it, he means no disrespect.":
    "不，就是这样，就是个玩笑，仅此而已，他没有不敬的意思。",
 "[quietly] It's better than I imagined.": "[quietly] 比我预想的还好。",
 "Okay, so... the way I usually do these things is...":
    "好，那么……我平时办这种事的方式是……",
 "We're good guys, relax.": "我们是好人，放松点。",
 "Calm her down.": "让她冷静下来。",
 "Let's just finish this.": "我们把这事做完吧。",
 "I think your girlfriend needs to calm down.": "我觉得你女朋友需要冷静一下。",
 "Let's just, uh, let's just wrap this up, alright? We saw it, we like it, what more is there to talk about?":
    "我们就，呃，就把这事收个尾，行吗？我们看过了，我们喜欢，还有什么好谈的？",
 "[tentative] Can we, uh, can we just take the key and you take... our money?":
    "[tentative] 我们能，呃，我们能直接拿走钥匙，你拿走……我们的钱吗？",
 "And I know a prick like Vasquez can get an extra five hundred g's without sweatin' it, so...":
    "而且我知道像 Vasquez 这种混蛋不用眨眼就能多拿出五十万，所以……",
 "I've been waitin' here since this morning.": "我从今天早上就在这儿等了。",
 "What was the hold up?": "磨蹭什么呢？",
 "Sorry we're late.": "抱歉我们迟到了。",
 "You're early.": "你们早到了。",
 "You didn't hear the fight outside?": "你们没听到外面的打斗？",
 "Yeah, well... that's Pandora, for you. If it ain't a friggin' bug stampede some jerkoff is usin' you for rocket practice.":
    "是啊，这个……潘多拉 就是这样。不是他妈的虫子大迁徙，就是哪个混蛋拿你当火箭靶子练手。",
 "Yeah, sorry we're late. Getting here was a little more complicated than we thought it'd be.":
    "是啊，抱歉我们迟到了。到这儿的路上比我们想的复杂了点。",
 "Early? Are you kidding me? You think I like being here, you think this is fun? Have you seen the bathroom yet?":
    "早到？你在逗我吗？你以为我喜欢待在这儿？你觉得这很好玩？你见过那厕所了吗？",
 "It's not our fault you wanted to come early.": "你想早到，那可不是我们的错。",
 "[light sarcasm] Oh, excuse me! I don't know if you heard the explosions outside, but we had to mow down about a couple hundred bandits just so we could ring the Goddamned doorbell.":
    "[light sarcasm] 哦，抱歉！我不知道你有没有听到外面的爆炸声，但我们得干掉大概两百来个土匪才能按响这该死的门铃。",
 "[sarcastic] Oh. Forgive me your majesty. Didn't know you chipped a toe nail.":
    "[sarcastic] 哦。恕罪陛下。不知道您指甲缺了个角。",
 "Yeah, well, we almost died, so...": "是啊，这个，我们差点死了，所以……",
 "Every minute in this horror factory's like an hour.": "在这恐怖工厂里的每一分钟都像一小时。",
 "Wait.": "等等。",
 "[really agitated] Look, you said when I started to get a feeling about something that I should tell you and that we should walk away, right?":
    "[really agitated] 听着，你说过当我开始对某件事有预感时就该告诉你，我们就该走人，对吧？",
 "What feeling?": "什么预感？",
 "[getting agitated] IIIIII... I just don't like it. I got a-- I got a feeling.":
    "[getting agitated] 我我我我……我就是不喜欢。我有——我有种预感。",
 "What.": "什么。",
 "I get intuitions about this stuff!": "我对这种事有直觉！",
 "We're almost done!": "我们就快成了！",
 "What are you possibly feeling right now?": "你现在能有什么预感？",
 "Yeah, he just wants to buy a key from me.": "是啊，他只是想从我这儿买把钥匙。",
 "Listen, honey, we're good guys, okay? Relax. We just wanna buy a key from your boyfriend.":
    "听着，亲爱的，我们是好人，行吗？放松。我们只是想从你男朋友那儿买把钥匙。",
 "I think you need to watch your mouth.": "我觉得你该管好你的嘴。",
 "Don't worry about it. She-- she gets this way, it's no problem.":
    "别担心。她——她就这样，没问题的。",
 "Intuitions? You're not a Goddamned fortune teller!": "直觉？你他妈又不是算命的！",
 "[really frazzled] I just-- I just don't like it, they've had this dumb... attitude on their dumb faces since the moment they walked in!":
    "[really frazzled] 我只是——我就是不喜欢，他们从进门那一刻起就……一脸蠢样、摆着一副蠢态度！",
 "What are you talking about!": "你在说什么！",
 "[really frazzled] They... he pretended to be Vasquez, August!":
    "[really frazzled] 他们……他假装自己是 Vasquez，August！",
 "As a joke!": "说是开玩笑！",
 "[really frazzled] He's been a giant dick this entire time!":
    "[really frazzled] 他从头到尾都是个大混蛋！",
 "[very frazzled] And why... why wouldn't they show you the money! Huh? What's up with that!":
    "[very frazzled] 还有为什么……他们为什么不给你看钱！啊？这是怎么回事！",
 "Sasha!": "萨莎！",
 "[very frazzled] And this guy, he will not stop checking me out!":
    "[very frazzled] 还有这家伙，他一直盯着我看不停！",
 "Me! What did I do?!": "我！我干了什么？！",
 "[very frazzled] I can, like, feel his brain undressing me!":
    "[very frazzled] 我简直能感觉到他的脑子在扒我衣服！",
 "Sasha, nobody's looking at you!": "萨莎，没人在看你！",
 "Sasha, what the Hell are you--[gets cut off]": "萨莎，你到底在——[gets cut off]",
 "What the Hell is your problem? We're trying to make a deal, there's nothing going on!":
    "你到底有什么毛病？我们在谈交易，什么都没发生！",
 "Alright, please, let's just everyone calm down. Everything's cool. We all just want to get paid, right?":
    "好了，拜托，大家都冷静一下。一切都好。我们都只是想拿到钱，对吧？",
 "I haven't been looking at you! I haven't!": "我没在看你！我没有！",
 "Get your girlfriend in line, August, before she starts making my partner nervous.":
    "把你女朋友管好，August，别让她把我搭档搞得紧张。",
 "Actually, that's okay, you don't know it yet.": "其实，没关系，你还不知道呢。",
 "August.": "August。",
 "Know what?": "知道什么？",
 "[crying] Take it, take it, it's-- I can't even-- just take it, please!":
    "[crying] 拿去，拿去，它——我都——就拿去，求你！",
 "[quietly] What if... what if I had won.": "[quietly] 要是……要是我赢了会怎么样。",
 "[V.O.] What a bunch of bullcrap!": "[V.O.] 一派胡言！",
 "You can't see that one day... maybe ten years from now, maybe ten months, maybe tomorrow... you're gonna think back on right now and scream to the stars for mercy of death just so you'll not have to live in the wondering of what could have been.":
    "你看不到吗，总有一天……也许是十年后，也许是十个月后，也许是明天……你会回想起此刻，对着群星嘶吼求死，只为不用活在那份“本该如何”的煎熬里。",
 "It. You don't know how to differentiate the typical, everyday moments in your life from the opportunities sent by the Universe herself, prostrated, begging to be conquered.":
    "就是它。你分不清你人生中那些平常的日常时刻，和宇宙亲自俯身送来的、恳求你抓住的机会。",
 "What if I had seized that chance by the throat, beaten my fears and taken what was so rightfully mine.":
    "要是我当初一把掐住那个机会，战胜恐惧，拿回本该属于我的东西，会怎么样。",
 "Oh no? And what are you gonna do about it?": "哦，是吗？那你打算怎么办？",
 "[super cool] Can't let you leave with that, pal.": "[super cool] 不能让你带着那东西走，老兄。",
 "[in intense pain] Ahhhhhhhh!": "[in intense pain] 啊啊啊啊！",
 "Looks like he had a... change of heart.": "看来他……改变主意了。",
 "Whatever, I don't care, do whatever you want.": "随便，我不管，你爱干嘛干嘛。",
 "I mean... I don't know, if you really think...": "我是说……我不知道，如果你真的觉得……",
 "Well... just... wait, just wait.": "那……就……等等，先等等。",
 "I dunno, maybe today's not right for this.": "不知道，也许今天不适合做这个。",
 "If you have a feeling about things...": "如果你对事情有预感……",
 "No, really, I don't care.": "不，真的，我不管。",
 "If things are weird.": "要是事情不对劲。",
 "Because of what SHE said?": "因为*她*说的那些？",
 "I NEED that key!": "我*需要*那把钥匙！",
 "A deal's a deal!": "说好的就是说好的！",
 "[getting angry] Oh, c'mon, because of what she said?! There's no problem, let's just--[gets cut off]":
    "[getting angry] 哦，拜托，因为她说的那些？！没问题，我们就——[gets cut off]",
 "No, I'm-- I'm sorry guys, I was-- I thought I was gonna deal with Vasquez, and... now this, I just... I just  think we should call it off until I think things are square.":
    "不，我——我很抱歉各位，我本来——我以为要跟 Vasquez 打交道，然后……现在又出了这事，我只是……我只是觉得我们该先取消，直到我觉得事情摆平了。",
 "[getting upset] August, c'mon, I need that key! Promises were made and-- and my bosses are expecting--[gets cut off]":
    "[getting upset] August，别这样，我需要那把钥匙！说好了的，而且——我老板们还等着——[gets cut off]",
 "[getting annoyed] August, c'mon now, a deal's a deal. We didn't come all the way down here just to-[get cuts off]":
    "[getting annoyed] August，别这样，说好的就是说好的。我们大老远下来可不是为了——[get cuts off]",
 "[getting annoyed] August, what-- what are you doing? Let's just finish the deal so we can--[gets cut off]":
    "[getting annoyed] August，你——你在干什么？我们把这交易做完，好让我们——[gets cut off]",
 "[angry] Just give us a second!": "[angry] 给我们一秒钟！",
 "[anxious whisper] Rhys! This is your department, do something!":
    "[anxious whisper] 瑞斯！这是你负责的，快想办法！",
 "[laughing disdainfully] That is not what happened, are you kidding me with this?":
    "[laughing disdainfully] 事情不是那样的，你在跟我开玩笑吗？",
 "[laughing] What! Give me a break, that's what-- look, I'm the one talking here, I have talking rights.":
    "[laughing] 什么！饶了我吧，那是——听着，现在说话的是我，我有说话权。",
 "Whatever.": "随便。",
 "How would you know what happened.": "你怎么知道发生了什么。",
 "[getting a little sheepish] Cause... cause, you know.[beat] I was there.":
    "[getting a little sheepish] 因为……因为，你知道。[beat] 我当时在场。",
 "No you weren't!": "你才没有！",
 "C'mon, Rhys, it's been a full year and you haven't figured this stuff out yet?":
    "得了吧，瑞斯，都整整一年了，你还没搞明白这些事？",
 "Okay. You were there. What happened.": "好。你在场。发生了什么。",
 "He's...[to Rhys] You're just very conveniently leaving out the most important part of this whole thing, alright?":
    "他……[to Rhys] 你只是很方便地略过了整件事里最重要的部分，行吗？",
 "Which is?": "是什么？",
 "[sarcastic] Oh, this outta be good.": "[sarcastic] 哦，这肯定精彩。",
 "A Vault Hunter showed up.": "一个秘藏猎人出现了。",
 "The Vault Hunter showed up.": "那个秘藏猎人出现了。",
 "The Bandit lord came in.": "那个土匪头子闯了进来。",
 "The Bandit... ganglord guy made his big stupid entrance.":
    "那个土匪……帮派头子搞了他那套蠢兮兮的大登场。",
 "The Vault Key broke.": "秘藏钥匙坏了。",
 "The Vault Key shattered.": "秘藏钥匙碎了。",
 "It's, um, complicated...": "这事，呃，很复杂……",
 "It's, um, well... it's complicated...": "这事，呃，这个……很复杂……",
})

# —— Rhys/Vaughn 抵达 Shade 的"奇珍世界" ——
T.update({
 "[whining] C'mon, August, I, like, really need that key, man, just-- can't you cut me a break, here? Don't-- we have the money, c'mon, just give it!":
    "[whining] 拜托，August，我，那个，真的很需要那把钥匙，老兄，就——你就不能通融一下吗？别——钱我们有，拜托，就给我吧！",
 "[while \"fighting\" someone] It's mine, give it! Just-- what's your frickin' problem, man!":
    "[while \"fighting\" someone] 是我的，给我！就——你他妈有什么毛病，老兄！",
 "[while \"fighting\" someone] Let go! C'mon! I need... that... key!":
    "[while \"fighting\" someone] 放手！拜托！我需要……那把……钥匙！",
 "Oh... uh...": "哦……呃……",
 "Just in time for the Spring collection.": "正好赶上春季新品。",
 "Yeah.": "是啊。",
 "[very frazzled] They've been all, \"Oh, yes sir, and no, sir, and, oh, I have the money we agreed upon right here!\"":
    "[very frazzled] 他们一直在那套，“哦，是的先生，还有不，先生，还有，哦，我们说好的那笔钱就在这儿！”",
 "Nothing you're saying is bad!": "你说的没有什么不好的！",
 "[very frazzled] Nobody does that! And especially Hyperion ore monkeys who'd rather bomb a small village than talk things through.":
    "[very frazzled] 没人会那样！尤其是 亥博龙那群挖矿猴子，他们宁愿炸掉一个小村庄也不愿意坐下来谈。",
 "[crying] Just take-- take it, please, take the key, take Sasha, take it all, it's yours, please.":
    "[crying] 就拿——拿去吧，求你，把钥匙拿去，把 萨莎 拿去，全都拿去，都是你的，求你。",
 "Really?[beat] That's it?": "真的？[beat] 就这样？",
 "We're good?": "我们没事了？",
 "He hasn't. Okay?": "他没有。行吗？",
 "Maybe another time, fellas.": "也许改天吧，伙计们。",
 "August, wait!": "August，等等！",
 "Welcome, wonder seekers, to Shade's World of Curosities!":
    "欢迎，寻找奇观的人们，来到 Shade 的奇珍世界！",
 "[starting his patter] We're closed for renovations right now, but-":
    "[starting his patter] 我们现在装修歇业，但——",
 "Hyperion, gah!": "亥博龙，啊！",
 "[v-o] You're not stealing my meal ticket, goosesteppers!":
    "[v-o] 你们别想抢我的饭碗，踢正步的！",
 "Wait, I-": "等等，我——",
 "{ShockA} Hey!": "{ShockA} 嘿！",
 "{AngryB} There's more where that came from!": "{AngryB} 还多着呢！",
 "Hey!  You shot my vest!": "嘿！你打中了我的背心！",
 "Next time I'll aim for the pants!": "下次我瞄准裤子！",
 "{SmugA} Well, he's nuts.  So, what's the play?  {SmugC} Show him the money?  {SlyA}That usually lubricates friendships.":
    "{SmugA} 好吧，他是个疯子。那怎么演？{SmugC} 给他看钱？{SlyA}那通常能润滑一下交情。",
 "{SmugA} Of course, I guess we could also {SlyA}intimidate the poor bastard witha show of force.":
    "{SmugA} 当然，我想我们也可以{SlyA}用武力震慑一下这可怜虫。",
 "{SmugA} .... if we were total whackjobs, maybe...":
    "{SmugA} ……如果我们本来就是彻头彻尾的疯子的话，也许……",
 "{SlyB}... Of course, an argument could be made that we're {SmugA}already veering heavily into whackjob territory...":
    "{SlyB}……当然，也可以说我们{SmugA}早就严重偏进疯子领地了……",
 "{NeutralB} ... Well, maybe you are, I like to think {SlyB} I'm still pretty un-whackjob...":
    "{NeutralB} ……这个嘛，也许你是，我倒觉得{SlyB}我还挺不疯的……",
 "{SmugB}...or is it anti-whackjob?": "{SmugB}……或者说反疯子？",
 "{SlyB} A-whackjobbian?": "{SlyB} 无疯子主义者？",
 "{SternA}I wonder if Hyperion builds a whackjob meter...":
    "{SternA}不知道 亥博龙有没有造过疯子测量仪……",
 "{SlyA}...probably not... that sounds {SmugB}like more of a Torgue idea...":
    "{SlyA}……大概没有……那听着{SmugB}更像是 Torgue 的主意……",
 "{SlyB}You know what?  {SlyC}The hell with lubrication.  {SlyB} We've got a robot.  Let's show this loser {SmugB}how Hyperion negotiates.":
    "{SlyB}你知道吗？{SlyC}润滑个屁。{SlyB} 我们有台机器人。让这废物见识一下{SmugB} 亥博龙怎么谈判。",
 "{SmugB} Total whackjobs it is, then.": "{SmugB} 那就当彻头彻尾的疯子吧。",
 "{SmugA}Y'know, you're right.  {SlyC}Cash makes everything easier.  {SlyB}Go on and show him the money.":
    "{SmugA}你知道，你说得对。{SlyC}现金能让一切都好办。{SlyB}去吧，给他看钱。",
 "{ShockA} Me?  {WorryA}Are you nuts?": "{ShockA} 我？{WorryA}你疯了吗？",
 "I'm just an accountant.  I don't DO \"talking to gun-wielding lunatics.\"":
    "我只是个会计。我不做“跟持枪疯子谈话”这种事。",
 "Of course, I'm not sure a data miner is supposed to talk to them either.":
    "当然，我也不确定数据挖掘员就该跟他们谈。",
 "I guess that's why we have the robot.": "我想这就是我们带机器人的原因。",
 "{SmugA}Just flip on your Echo device, {SlyA}I'll talk you in.":
    "{SmugA}你打开 ECHO 装置就行，{SlyA}我来指引你。",
 "[wary] {SternB} Okay, but {AngryA}no screwing around! ...{SternC}like that time I let you be my wingman when I was asking out that {WorryA}temp in Marketing.":
    "[wary] {SternB} 好，但{AngryA}别乱来！……{SternC}就像那次我让你当我的僚机去约市场部那个{WorryA}临时工。",
 "{SmugA}No screwing around.  {SlyB}Got it.": "{SmugA}不乱来。{SlyB}明白。",
 "{SmugC} Well, I can't go back there.  {SlyA}That guy obviously has something against me.":
    "{SmugC} 那个，我不能回那儿去。{SlyA}那家伙显然对我有意见。",
 "{WorryA}He's got something against {SternA}HYPERION.  {WorryA}Besides, you're supposed to be the smooth one in this operation. {WorryB}I wouldn't know what to say.":
    "{WorryA}他是对{SternA}亥博龙有意见。{WorryA}再说，这次行动里你才是那个能说会道的。{WorryB}我根本不知道该说什么。",
 "Well, if you're gonna whine about it, maybe I SHOULD send the death robot to handle the negotiations.  That'd REALLY settle him down.":
    "好吧，你要抱怨的话，也许我*真*该派死亡机器人去谈。那肯定能让他*冷静*下来。",
 "Yeah, let's do that!": "好啊，就这么办！",
 "Scary robot it is, then.  But don't blame me if this gets messy.":
    "那就派吓人的机器人。但要是搞砸了别怪我。",
 "I'm already blaming you.": "我已经在怪你了。",
 "Well, I can't go.  YOU'RE the one who's chained to the money.":
    "那个，我去不了。*你*才是被钱拴住的那个。",
 "[starting to protest]  But- [resigned]  Crap.  Fine.  But what should I say?":
    "[starting to protest] 但是——[resigned] 糟。行。但我该说什么？",
 "Crap.  Fine.  But what should I say?": "糟。行。但我该说什么？",
 "Maybe you should've skulked.": "也许你该偷偷摸摸地来。",
 "Very funny.": "真好笑。",
 "Never an orbital death ray around when you need one.":
    "需要轨道死光的时候总是没有。",
 "Ha-ha.": "哈哈。",
 "Hm, guess they were angry after all.": "嗯，看来他们最后还是生气了。",
 "{SternA} He shot at me.": "{SternA} 他朝我开枪了。",
 "{SmugB} I saw.": "{SmugB} 我看见了。",
 "{SternC} He shot my vest.": "{SternC} 他打了我的背心。",
 "{SternA} I liked this vest.": "{SternA} 我喜欢这件背心。",
 "{FearC} Aaaaagh!  {AngryCX}Barbarians!  {AngryC}Visigoths!":
    "{FearC} 啊啊啊！{AngryCX}野蛮人！{AngryC}西哥特人！",
 "{AngryC}What are you-?": "{AngryC}你们在干——？",
 "[in the douchey corporate tone of, \"It's cute you thought you could hide\"]\t{SmugB}Hi there.":
    "[in the douchey corporate tone of, \"It's cute you thought you could hide\"]\t{SmugB}你好啊。",
 "{ThinkingB}You can't just go around destroying innocent {AngryB}people's property like this!":
    "{ThinkingB}你不能就这么到处毁坏无辜{AngryB}人家的财产！",
 "{AngryB}Who do you think you people are, anyway!?": "{AngryB}你们这些人以为自己是谁啊！？",
 "{ThinkingB}And yeah, I'm not so innocent!  {AngryC}But still!":
    "{ThinkingB}是啊，我也没那么无辜！{AngryC}但那又怎样！",
 "{AngryCX}Honestly, what {AngryC}IS it with you Hyperion guys?":
    "{AngryCX}说真的，你们这些 亥博龙的人到底{AngryC}怎么回事？",
 "{SlyC}For a LOT of money!": "{SlyC}为了一大笔钱！",
 "{SmugC}Mr. Shade, it has come to Hyperion's attention that you have a {SlyB}VERY unique item in your possession - {SmugA}an item that my associate and I would {SmugB}very much like to purchase from you.":
    "{SmugC}Shade 先生，亥博龙注意到你手上有一件{SlyB}非常独特的物品——{SmugA}一件我同伴和我{SmugB}非常想从你这儿买下的物品。",
 "{ThinkingC}Well, are we doing business?  {AngryB}Or do you want to bust up some more of my house with {AngryCX}your big ol' automoton?":
    "{ThinkingC}那么，我们是谈生意？{AngryB}还是你想用{AngryCX}你那台大自动机再砸我家几处？",
 "[trying to retain outrage] {HappyA}Wellll,  why didn't you say so in the first place, instead of {AngryC}breaking down my door {AngryB}like some sort of testosterone-addled {AngryCX}corporate stereotype?":
    "[trying to retain outrage] {HappyA}那个，你们干嘛不一开始就说，非要{AngryC}砸开我的门，{AngryB}像个睾酮过剩的{AngryCX}企业刻板印象？",
 "Don't make Hyperion call MORE robots.": "别逼亥博龙叫更多机器人来。",
 "[firm and intimidating] {SternA}Are you through being rude, or am {SternC}I going to have to call down more robots?":
    "[firm and intimidating] {SternA}你粗鲁够了吗？还是要我{SternC}再叫更多机器人下来？",
 "[scared] {FearC}All right, all right!  {FearA}What do you want from me?":
    "[scared] {FearC}好吧，好吧！{FearA}你们想从我这儿要什么？",
 "Sorry you made me do that.": "抱歉逼我这么做。",
 "[friendly]  {SmugA}Oh hey, you okay?": "[friendly]  {SmugA}哦嘿，你没事吧？",
 "[angry]  {AngryC}You broke my door!": "[angry]  {AngryC}你砸了我的门！",
 "{SmugC}Yeah, sorry 'bout that.  {SlyA}Sometimes these Loader Bots get a little clumsy.  {SlyC}But I had to get your attention, {SmugB}and you really didn't leave me much choice.":
    "{SmugC}是啊，抱歉。{SlyA}这些装载机器人有时候有点笨手笨脚。{SlyC}但我得引起你的注意，{SmugB}而你实在没给我多少选择。",
 "[suspicious]{ThinkingA}Attention?": "[suspicious]{ThinkingA}注意？",
 "Let's get down to business.": "我们说正事吧。",
 "[all-business] {SmugC}Good morning, sir!  {SlyC}On behalf of the Hyperion Corporation, I'm here to offer you a {SmugB}fantastic {SlyC}business opportunity!":
    "[all-business] {SmugC}早上好，先生！{SlyC}我代表 亥博龙公司，来为您提供一个{SmugB}绝佳的{SlyC}商业机会！",
 "[suspicious] {ThinkingA}Business {ThinkingB}opportunity?": "[suspicious] {ThinkingA}商业{ThinkingB}机会？",
 "{WorryA}Rhys!  {SlyB}Stop scaring the customer, and {NeutralB}tell him about the money!":
    "{WorryA}瑞斯！{SlyB}别吓唬客户了，{NeutralB}跟他说钱的事！",
 "[suspicious]  {ThinkingC}Money?": "[suspicious]  {ThinkingC}钱？",
 "{WorryA}Okay, I'm walking to the door.  {NeutralB}What now?":
    "{WorryA}好，我正走向门口。{NeutralB}现在呢？",
 "[to himself] {SternB}Jeez, this place is a mess...":
    "[to himself] {SternB}天哪，这地方真乱……",
 "{SternA} Okay, the briefcase is open and I'm at the door.":
    "{SternA} 好，手提箱打开了，我到门口了。",
 "{SmugA}Nice door, too.  {SmugB}Wonder where he got it.":
    "{SmugA}门也不错。{SmugB}不知道他从哪儿弄的。",
 "[angry] {AngryC}What!?": "[angry] {AngryC}什么！？",
 "[panicked] {FearA}What do I say, what do I say!?":
    "[panicked] {FearA}我说什么，我说什么！？",
 "{AngryC}You've got 'til the end of this sentence to get off my porch, {AngryCX}you oily corporate cog!":
    "{AngryC}你有直到这句话结束的时间滚下我的门廊，{AngryCX}你这油滑的公司齿轮！",
 "{SmugA}Good, now say this...": "{SmugA}好，现在说这个……",
 "{SmugC}With your permission, {SmugB}my handsome associate and I {SmugC}would like to purchase said artifact  from you for {SlyB}more money than you've seen in your lifetime.":
    "{SmugC}如蒙允许，{SmugB}我英俊的同伴和我{SmugC}想从您手上购买上述物品，出价{SlyB}超过您这辈子见过的钱。",
 "{SmugC}Mr. Shade.  It has come to the attention of  the {SmugB}Hyperion Corporation that you are in possession of a {SmugC}rare alien artifact.":
    "{SmugC}Shade 先生。{SmugB}亥博龙公司注意到您持有一件{SmugC}稀有的外星物品。",
 "{SmugB}With your permission, {SternA}my jackass associate and I {SlyA}would like to purchase said artifact  from you for {SmugB}more money than you've seen in your lifetime.":
    "{SmugB}如蒙允许，{SternA}我那位蠢货同伴和我{SlyA}想从您手上购买上述物品，出价{SmugB}超过您这辈子见过的钱。",
 "{FearA}Mr. Shade.  {NeutralB}It has come to the attention of the Hyperion Corporation that{SmugA}you are in possession of a rare alien artifact.":
    "{FearA}Shade 先生。{NeutralB}亥博龙公司注意到{SmugA}您持有一件稀有的外星物品。",
 "{HappyC}Oh my GOD!  You are my new best friends ever!":
    "{HappyC}我的天啊！你们是我这辈子最好的新朋友！",
 "\"Check THIS out!\"": "“看这个！”",
 "{ThinkingB} Hey, it's money!  {HappyA}I love money!":
    "{ThinkingB} 嘿，是钱！{HappyA}我爱钱！",
 "{FearB}Check this out please!": "{FearB}请看这个！",
 "{SlyB}Check THIS out!": "{SlyB}看*这个*！",
 "{AngryB}Check what out?": "{AngryB}看什么？",
 "{WorryA}Oh.": "{WorryA}哦。",
 "\"We want to make you rich!\"": "“我们想让你发财！”",
 "{WorryA}See?": "{WorryA}看吧？",
 "{SmugB}We want to make you rich!": "{SmugB}我们想让你发财！",
 "{FearB}We want to make you rich!": "{FearB}我们想让你发财！",
 "{ThinkingC}How?": "{ThinkingC}怎么发财？",
 "{AngryA}What?": "{AngryA}什么？",
 "\"I'm selling these fine leather jackets!\"": "“我在卖这些上好的皮夹克！”",
 "{SmugA}I'm selling these fine leather jackets!": "{SmugA}我在卖这些上好的皮夹克！",
 "{FearA}Oh, right.": "{FearA}哦，对。",
 "{FearB}I'm selling these fine leather jackets!": "{FearB}我在卖这些上好的皮夹克！",
 "[confused] {ThinkingB}What?": "[confused] {ThinkingB}什么？",
 "[confused] {FearA}What?": "[confused] {FearA}什么？",
 "{SlyA}Now, while he's confused, {SlyC}show him the money!":
    "{SlyA}现在，趁他糊涂，{SlyC}给他看钱！",
 "{HappyA}Hey!  {ThinkingB}Is that a frankly obscene amount of money {HappyB}I see before me?":
    "{HappyA}嘿！{ThinkingB}我眼前看到的{HappyB}是不是一笔简直下流的巨款？",
 "{AngryA}Time's up!": "{AngryA}时间到了！",
 "{FearC} Wait!": "{FearC} 等等！",
 "Knock.": "敲门。",
 "Now take a deep breath and gently knock on the door.":
    "现在深呼吸，轻轻敲门。",
 "Ring the doorbell.": "按门铃。",
 "[static burst covers this] Fuck you.": "[static burst covers this] 去你的。",
 "Now gently ring the doorbell...": "现在轻轻按门铃……",
 "There's not a doorbell.": "没有门铃。",
 "[faux panic] Oh my god, abort!  Abort!": "[faux panic] 我的天，中止！中止！",
 "[\"sorry, i missed that\"] What's that?": "[\"sorry, i missed that\"] 什么？",
 "Call him out with an insult.": "用一句侮辱把他叫出来。",
 "Wait, what?": "等等，什么？",
 "Now take a deep breath and shout \"Hey loser!\"": "现在深呼吸，大喊“嘿，废物！”",
 "[takes a deep breath] Hey jerkwad!": "[takes a deep breath] 嘿，蠢货！",
 "Rhys?  Fine, I'll knock on the door.": "瑞斯？行，我去敲门。",
 "Put one foot in front of the other": "一只脚放在另一只脚前面",
 "{SternA}I meant to do that.": "{SternA}我是故意的。",
 "{SlyB}Right.  {SmugA}Now open the briefcase, so he can see the money.":
    "{SlyB}对。{SmugA}现在打开手提箱，让他看到钱。",
 "{AngryA}I know how to walk, ass-[Vaugh trips] {FearA}Wah!":
    "{AngryA}我知道怎么走路，混——[Vaugh trips] {FearA}哇！",
 "{SlyA}Left foot, right foot, left foot.": "{SlyA}左脚，右脚，左脚。",
 "Just relax...": "放松……",
 "{SmugB}Just relax and open the briefcase so he'll be able to {SlyA}see the money.":
    "{SmugB}放松，打开手提箱，这样他就能{SlyA}看到钱。",
 "Don't think about the gun.": "别想那把枪。",
 "{SmugB}Just open the briefcase and try not to think about the gun.":
    "{SmugB}打开手提箱，尽量别想那把枪。",
 "{AngryA}Jerk.": "{AngryA}混蛋。",
 "{WorryA}Hey, are you there? Is this on?  {FearA}I'm opening the briefcase...":
    "{WorryA}嘿，你在吗？这开着吗？{FearA}我在打开手提箱……",
})

# —— Shade 的导览：神秘楔石（假秘藏钥匙）——
T.update({
 "[enthused] {HappyB}Welcome, friends, to {HappyC}Shade's World of Curiosities!":
    "[enthused] {HappyB}欢迎，朋友们，来到{HappyC} Shade 的奇珍世界！",
 "[enthused] The Enchanted Training Bra of {HappyB}Mad Moxxi!":
    "[enthused] {HappyB}疯婆莫西的附魔训练胸罩！",
 "[enthused] {HappyC}Handsome Jack's Death Pants!": "[enthused] {HappyC}帅杰克的死亡之裤！",
 "[enthused] The inexplicable oddities of the World of Curiosities has delighted and amazed the good citizens of Prosperity Junction in good times and bad!":
    "[enthused] 奇珍世界这些不可思议的怪东西，无论顺境逆境都给繁荣枢纽的善良市民带来欢乐与惊叹！",
 "[enthused] {HappyCX}The Biggest Ball on Pandora!": "[enthused] {HappyCX}潘多拉上最大的球！",
 "{SternA}Yup, that's a wedge all right.": "{SternA}没错，那确实是个楔子。",
 "{ThinkingB}Not just any wedge, young man....": "{ThinkingB}可不是普通的楔子，年轻人……",
 "[enthused] {HappyB}And, of course, the coup de grace, the piece de resistance, {HappyC}what you've all been waiting for, the one, the only, {HappyCX}the Wedge of Mystery!":
    "[enthused] {HappyB}当然，还有压轴大戏、镇馆之宝，{HappyC}你们一直在等的，独一无二的{HappyCX}神秘楔石！",
 "{THinkingC}\tIs it the control panel of an alien spaceship?":
    "{THinkingC}\t它是外星飞船的控制面板吗？",
 "{HappyC}Ever since my grandpappy stumbled upon this engimatic artifact, curious onlookers have speculated as to its origins and purposes!":
    "{HappyC}自从我爷爷偶然发现这件神秘物品以来，好奇的围观者一直在猜测它的来历和用途！",
 "An ancient computer?": "一台古老的电脑？",
 "{HappyB}Or maybe a fragment from an elusive Eridian Vault!?":
    "{HappyB}或者也许是来自某个难觅踪影的伊瑞德秘藏的碎片！？",
 "{HappyA}Go on, big guy.  {HappyC}Throw it.": "{HappyA}来吧，大块头。{HappyC}扔过去。",
 "{angryA}Powers?": "{angryA}能力？",
 "{HappyA}Ah, the arched eyebrow of a skeptic! But here, {thinkingB}prepare to gawk in amazement as your athletically-inclined {happyA}associate throws this ordinary souvenir pen at the {happyCX}fantastic Wedge of Mystery!":
    "{HappyA}啊，怀疑者挑起的那道眉毛！但来，{thinkingB}准备惊掉下巴吧，你那运动能力出众的{happyA}同伴要拿这支普通的纪念笔扔向{HappyCX}神奇的神秘楔石！",
 "{ThinkingC}No one can know for sure, but there can be NO doubting the wondrous and inexplicable {HappyCX}POWERS OF THE WEDGE!":
    "{ThinkingC}没人能确定，但{HappyCX}楔石那奇妙而不可解释的力量绝对不容置疑！",
 "Pretty cool, huh?": "挺酷吧？",
 "[whispering] {SMugA}This is so cool!": "[whispering] {SMugA}这太酷了！",
 "[whispering] {SlyA}Just listen, {slyc}he's getting to the good part!":
    "[whispering] {SlyA}听着，{slyc}他要讲到精彩部分了！",
 "[whispering] {AngryA}Cool?  It's a modern art project!":
    "[whispering] {AngryA}酷？这就是个现代艺术项目！",
 "[whispering] {AngryA}I THINK I'm risking life, limb, and future employment prospects {AngryB}for a badly-painted hunk of rock.":
    "[whispering] {AngryA}我*觉得*我正在拿命、四肢和未来的职业前途{AngryB}去换一块画得很难看的石头。",
 "[whsipering] {SlyA}Wait for it...": "[whsipering] {SlyA}等着看……",
 "[whispering] {SlyC}What do you think?": "[whispering] {SlyC}你觉得呢？",
 "I can sense your skepticism.": "我能感觉到你的怀疑。",
 "[whispering]  {SlyC}Just hold on, it's about to get good...":
    "[whispering]  {SlyC}再等等，马上要精彩了……",
 "[whispering] {SmugB}My Vaughn-sense is picking up skepticism.":
    "[whispering] {SmugB}我的 沃恩 直觉探测到怀疑了。",
 "[whsipering]  {SternC}Ya think?  'Cause right now I'm {WorryA}thinking about running back to Hyperion and begging for forgiveness.":
    "[whsipering]  {SternC}你说呢？因为我现在{WorryA}正想着跑回 亥博龙求饶。",
 "[whispering] {SmugA}Relax... {SlyC}this is about to get good...":
    "[whispering] {SmugA}放松……{SlyC}马上要精彩了……",
 "[whispering]  {AngryA}I can't believe I let you talk me into this!":
    "[whispering]  {AngryA}我不敢相信我居然被你说服了！",
 "This is gonna rock!": "这肯定会很棒！",
 "[whispering] {slyC}Can you believe it?  {Slyb}This nutjob has a genuine Eridian artifact!":
    "[whispering] {slyC}你信吗？{Slyb}这疯子手上有一件真正的伊瑞德物品！",
 "[whispering] {SternA}I'll believe it when I see it.":
    "[whispering] {SternA}眼见为实。",
 "Nice job.": "干得好。",
 "{SmugA}Nice job back there.": "{SmugA}刚才干得不错。",
 "{AngryA}No thanks to you, Mr. \"Left Foot Right Foot.\"":
    "{AngryA}可不是靠你，“左脚右脚先生”。",
 "{SmugB}Ha!": "{SmugB}哈！",
 "{AngryA}No thanks to you, Captain Doorbell.": "{AngryA}可不是靠你，门铃队长。",
 "{SmugB}It worked, didn't it?": "{SmugB}管用了，不是吗？",
 "{AngryA}No thanks to you.  {Sternb}I mean leather jackets? Seriously?":
    "{AngryA}可不是靠你。{Sternb}我是说，皮夹克？认真的？",
 "{SmugA}We're in, aren't we?": "{SmugA}我们进来了，不是吗？",
 "{FearA}I thought you were gonna guide me in.": "{FearA}我以为你会指引我。",
 "{smugA}You're welcome.": "{smugA}不客气。",
 "{SmugA}Thanks for not dicking with me.": "{SmugA}谢谢你没耍我。",
 "Ooh, I touched his grandfather's corpse?": "哦，我碰到他爷爷的尸体了？",
 "[whispering] {SlyC}The kind that's gonna make us rich!":
    "[whispering] {SlyC}那种能让我们发财的！",
 "[whispering] {WorryA}What kind of looney are we dealing with here?":
    "[whispering] {WorryA}我们这是在跟什么疯子打交道？",
 "[whispering] {ThinkB}Wait, that corpse was {WorryC}his grandfather?":
    "[whispering] {ThinkB}等等，那具尸体是{WorryC}他爷爷？",
 "Professor Penumbra?": "Penumbra 教授？",
 "[to vaughn] {SternC}What kind of name is Penumbra?":
    "[to vaughn] {SternC}Penumbra 是什么鬼名字？",
 "[to rhys] {smugc}Dude, we used to work for a guy called \"Handsome Jack.\"":
    "[to rhys] {smugc}老兄，我们以前给一个叫“帅杰克”的家伙干活。",
 "[to vaughn]  Good point.": "[to vaughn]  有道理。",
 "[with a little edge on it... he's still pissed about the door] {AngryA}Welcome, door-destroying barabarians, {HappyB}to Shade's World of Curiosities!":
    "[with a little edge on it... he's still pissed about the door] {AngryA}欢迎，破坏门的野蛮人，{HappyB}来到 Shade 的奇珍世界！",
 "[still angry] {AngryA}Founded over twenty-five years ago by my Grandfather, {AngryB}the non-violent and door-respecting Professor Penumbra...":
    "[still angry] {AngryA}由我爷爷创立于二十五年前，{AngryB}那位非暴力、尊重门扉的 Penumbra 教授……",
 "[annoyed] {AngryC}The World of Curiosities has been the home (a home with a functioning front DOOR, I might add) {AngryB}of Pandora's most inexplicable oddities for over two decades now!":
    "[annoyed] {AngryC}二十多年来，奇珍世界一直是（顺便说一句，一扇功能完好的*前门*俱全的）{AngryB}潘多拉 最不可思议怪物的家园！",
 "[annoyed]The Death Pants of Handsome Jack!": "[annoyed]帅杰克的死亡之裤！",
 "[annoyed] The Biggest Ball on Pandora.": "[annoyed] 潘多拉 上最大的球。",
 "[annoyed]{AngryA}Mad Moxxi's training bra!": "[annoyed]{AngryA}疯婆 莫西 的训练胸罩！",
 "[still somewhat angry] {AngryB}But, of course, you don't care about any of that, do you?  {AngryA}You came down here for the coup de grace, the piece de la resistance, the one, {ThinkingA}the only, the Wedge of Mystery!":
    "[still somewhat angry] {AngryB}但当然，你们对那一切都不在意，对吧？{AngryA}你们下来是为了压轴大戏、镇馆之宝，那个独一无二的{ThinkingA}、绝无仅有的神秘楔石！",
 "{FearA}That's it?  {WorryA}We're risking life, limb, and employment for that?":
    "{FearA}就这个？{WorryA}我们冒着生命、四肢和饭碗的风险就为了那个？",
 "[annoyed]{AngryB}Ever since my grandpappy stumbled upon this enigmatic artifact, thousands have speculated as to its origins and purpose.":
    "[annoyed]{AngryB}自从我爷爷偶然发现这件神秘物品以来，成千上万的人都在猜测它的来历和用途。",
 "[a little less annoyed] {ThinkingB}Is it the control panel of an alien spaceship?":
    "[a little less annoyed] {ThinkingB}它是外星飞船的控制面板吗？",
 "[into it] {HappyA}An ancient computer?": "[into it] {HappyA}一台古老的电脑？",
 "[really into it] {HappyC}Or maybe a fragment from an elusive Eridian Vault!?":
    "[really into it] {HappyC}或者也许是来自某个难觅踪影的伊瑞德秘藏的碎片！？",
 "Go on, big guy.  Throw it.": "来吧，大块头。扔过去。",
 "No one can know for sure, but there can be NO doubting the wondrous and inexplicable POWERS OF THE WEDGE!":
    "没人能确定，但楔石那奇妙而不可解释的力量绝对不容置疑！",
 "Powers?": "力量？",
 "You want this baby because of the POWERS, right?    Here, Mr. Roboto, take this pen and throw it at the Wedge!":
    "你想要这东西是因为它有*力量*，对吧？来，机器人先生，拿这支笔扔向楔石！",
 "This is so cool!": "这太酷了！",
 "[whispering] This is so cool!": "[whispering] 这太酷了！",
 "[whispering] Just listen, he's getting to the good part!":
    "[whispering] 听着，他要讲到精彩部分了！",
 "[whispering] Cool?  It's a modern art project!":
    "[whispering] 酷？这就是个现代艺术项目！",
 "What do you think?": "你觉得呢？",
 "[whispering] What do you think?": "[whispering] 你觉得呢？",
 "[whispering] I THINK I'm risking life, limb, and future employment prospects for a badly-painted hunk of rock.":
    "[whispering] 我*觉得*我正在拿命、四肢和未来的职业前途去换一块画得很难看的石头。",
 "[whsipering] Wait for it...": "[whsipering] 等着看……",
 "[whispering]  Just hold on, it's about to get good...":
    "[whispering]  再等等，马上要精彩了……",
 "[whsipering]  Ya think?  'Cause right now I'm thinking about running back to Hyperion and begging for forgiveness.":
    "[whsipering]  你说呢？因为我现在正想着跑回 亥博龙求饶。",
 "[whispering] My Vaughn-sense is picking up skepticism.":
    "[whispering] 我的 沃恩 直觉探测到怀疑了。",
 "[whispering] Relax... this is about to get good...":
    "[whispering] 放松……马上要精彩了……",
 "[whispering]  I can't believe I let you talk me into this!":
    "[whispering]  我不敢相信我居然被你说服了！",
 "This is gonna be great!": "这肯定会很棒！",
 "[whispering] I'll believe it when I see it.": "[whispering] 眼见为实。",
 "[whispering] Can you believe it?  This nutjob has a genuine Eridian artifact!":
    "[whispering] 你信吗？这疯子手上有一件真正的伊瑞德物品！",
 "[whispering] Shhh!": "[whispering] 嘘！",
 "[whispering] You threatend this loony with a Loader Bot?":
    "[whispering] 你用装载机器人威胁这疯子？",
 "[whispering] Wait, that corpse was his grandfather?":
    "[whispering] 等等，那具尸体是他爷爷？",
 "[to vaughn] What kind of name is Penumbra?": "[to vaughn] Penumbra 是什么鬼名字？",
 "[to rhys] Dude, we used to work for a guy called \"Handsome Jack.\"":
    "[to rhys] 老兄，我们以前给一个叫“帅杰克”的家伙干活。",
 "I'll pay you to shut up about the door. ($200)": "我付钱让你别再提那扇门。（$200）",
 "{WorryA}Look, I'm sorry about the door.  {Sternb}If I give you some money to fix it, {sternC}will you stop grinding my gears?":
    "{WorryA}听着，门的事我很抱歉。{Sternb}要是我给你点钱修它，{sternC}你能不能别磨我了？",
 "{AngryA}Two hundred.": "{AngryA}两百。",
 "{smugc}A hundred bucks.": "{smugc}一百块。",
 "{thinkingA}How much money?": "{thinkingA}多少钱？",
 "{ShockA}How?": "{ShockA}怎么付？",
 "{worryA}Oh.  Fine.": "{worryA}哦。行。",
 "{shockC}No way.  I know for a fact that you've got at least five hundred in your pocket.":
    "{shockC}不行。我很确定你口袋里至少装着五百。",
 "{smugB}Done.  {neutralB}Vaughn, give him two hundred.":
    "{smugB}成交。{neutralB}沃恩，给他两百。",
 "{HappyC}Thanks, friend!  your generous compensation {HappyB}warms the cockles of my forgiveness gland!":
    "{HappyC}谢谢，朋友！你慷慨的补偿{HappyB}温暖了我那颗宽恕腺！",
 "I'm sorry about the door.": "门的事我很抱歉。",
 "{sternB}Look, I'm sorry about the door.": "{sternB}听着，门的事我很抱歉。",
 "{AngryB}Sorry don't pay the contractor, buddy.": "{AngryB}道歉付不起工钱，哥们。",
 "[amazed] {ShockC}Son of a bitch... a real Eridian Artifact.":
    "[amazed] {ShockC}狗娘养的……一件真正的伊瑞德物品。",
 "[FearB]Careful there, sport.  The Wedge doesn't like to be touched by living things.  [to himself] {ThinkingA}Learned THAT the hard way.":
    "[FearB}小心点，小伙子。楔石不喜欢被活物碰。[to himself] {ThinkingA}这我可是*吃过大亏*才学到的。",
 "[wandering off] Now, where'd I put my negotiating shoes?":
    "[wandering off] 我把那双谈判专用鞋放哪儿了？",
 "[breaking out of reverie] {ShockA}Rhys, this is a real, honest-to-god alien artifact!  {HappyC}Hyperion spends gazillions of dollars looking for stuff like this!":
    "[breaking out of reverie] {ShockA}瑞斯，这是一件货真价实的、如假包换的外星物品！{HappyC}亥博龙花无数钱到处找这种东西！",
 "{SlyA}I know.": "{SlyA}我知道。",
 "Handsome Jack went crazy hunting down stuff like this!":
    "帅杰克为了找这种东西都疯了！",
 "{SmugA}I know.": "{SmugA}我知道。",
 "{HappyB}If we bring this back to our bosses for a piddly briefcase full of cash-":
    "{HappyB}要是我们把这东西带回去给老板，换回一小箱可怜的现金——",
 "{SmugC}We'll be gods among men, {SlyB}I know.":
    "{SmugC}我们就会成为人中之神，{SlyB}我知道。",
 "So, who's ready to make a deal, friends?": "那么，谁准备好做交易了，朋友们？",
 "I should warn you, I can be a pretty savvy negotiator... Grandpa said I had a perfect poker face...":
    "我得提醒你们，我可是个相当精明的谈判者……爷爷说我有张完美的扑克脸……",
 "... or maybe he said I had a face that got hit by a poker...":
    "……或者也许他说的是我这张脸被扑克牌打过……",
 "[through teeth] Don't get greedy, don't get greedy, don't get greedy...":
    "[through teeth] 别贪心，别贪心，别贪心……",
 "Mister Shade, Hyperion is prepared to offer you ONE MILLION DOLLARS  for this spectacular artifact.":
    "Shade 先生，亥博龙愿意为这件壮观的物品向您出价*一百万美金*。",
 "One... million...dollars?": "一……百……万……美金？",
 "Mister Shade?  Are you okay?": "Shade 先生？你没事吧？",
 "Okay!?  I'm better than okay, I'm a bona fide millionaire!  I'm rich!  I'm well-off, I'm financially secure!":
    "没事！？我比没事好几了，我是货真价实的百万富翁！我发财了！我富裕了，我财务自由了！",
 "[aside]{SternB}Maybe I should've low-balled him.": "[aside]{SternB}也许我该给他压个低价。",
 "[aside] {AngryA}Ya think?": "[aside] {AngryA}你说呢？",
 "{HappyB}Here boys, have a couple hundred on me!  And some souvineer floaty pens!  Heck, take anything you want, {HappyC}I'm retired, baby!":
    "{HappyB}来，小伙子们，这几百块拿去花！还有些浮空纪念笔！见鬼，想要什么随便拿，{HappyC}我退休啦，宝贝！",
 "[calming him down]  Mister Shade... Mister Shade.  The Hyperion Corporation is happy that you're so happy, but there's still some paperwork to go through.":
    "[calming him down]  Shade 先生……Shade 先生。亥博龙公司很高兴你这么高兴，但还有些文件要走。",
 "Paperwork?": "文件？",
 "Transfers of ownership, non-disclsoure agreements, that sort of thing.":
    "所有权转让、保密协议，那一类东西。",
 "Sure, no problem-o!  I'm gonna be rich!": "当然，没问题！我要发财了！",
 "Let's just walk over here while my friend figures out how to pick up the Wedge...":
    "我们走到这边来，让我朋友想想怎么把楔石搬走……",
})

# —— 砍价 + Shade 的独白 ——
T.update({
 "Mr. Shade, Hyperion will give you 750 thousand for the Slab.":
    "Shade 先生，亥博龙愿意为这块石板给你七十五万。",
 "{HappyB}Now THAT is a generous offer!  Hell, at that price I'll even throw in a few souinveers!":
    "{HappyB}这才叫慷慨的报价！见鬼，这个价我还能附送几件纪念品！",
 "{SmugA}That won't be necessary-": "{SmugA}那倒不必——",
 "{HappyA}Necessary, shmessary, {HappyB}I'm rich!":
    "{HappyA}必不必的，管他呢，{HappyB}我发财了！",
 "{SlyA}Yes, well, before we can complete the transaction, {SmugB}my associate has a few forms for you to sign.":
    "{SlyA}对，不过在完成交易之前，{SmugB}我同伴有几份表格要你签。",
 "{ThinkingC}Forms?": "{ThinkingC}表格？",
 "{SternA}Transfer of ownsership, non-disclosure agreements, {SmugA}that sort of thing.":
    "{SternA}所有权转让、保密协议，{SmugA}那一类东西。",
 "{ThinkingB}I'll need to read them.": "{ThinkingB}我得读一下。",
 "{smugB}Of course.  Let's just walk over here while my associate figures out how to pick up the Wedge.":
    "{smugB}当然。我们走到这边来，让我同伴想想怎么把楔石搬走。",
 "{SlyA}Mister Shade, the Hyperion corporation is prepared to offer you 500 thousand dollars for your so-called Slab of Mystery.":
    "{SlyA}Shade 先生，亥博龙公司愿意为你那块所谓的神秘石板出价五十万美元。",
 "{AngryA}Five hundred?  I don't know...": "{AngryA}五十万？我不知道……",
 "What would Grandpa say?": "爷爷会怎么说？",
 "\"Help, help, I've been poisoned,\" probably...": "大概会说“救命，救命，我中毒了”……",
 "[through teeth] Rhys, what are you doing?": "[through teeth] 瑞斯，你在干什么？",
 "On the one hand, 500 thousand is a lot of money...":
    "一方面，五十万是很多钱……",
 "On the other hand, it is kind of an insult, and not in a playful, we'll all laugh about later over pina coladas kind of way...":
    "另一方面，这有点侮辱人，而且不是那种我们以后会喝着椰林飘香哈哈一笑的玩笑式侮辱……",
 "But on the third hand, I'm getting kind of hungry...":
    "但第三方面，我有点饿了……",
 "But on the fourth hand, I'm wondering where that third hand came from...":
    "但第四方面，我在纳闷那只第三只手是从哪儿来的……",
 "But on the fith hand... what was i talking about again?":
    "但第五方面……我刚才在说什么来着？",
 "Okay, okay.  One million.  And that's my final offer.":
    "好，好。一百万。这是我的最终报价。",
 "{SternB}Okay, 750.  Final offer.": "{SternB}好，七十五万。最终报价。",
 "[contemplating] 750 thousand...": "[contemplating] 七十五万……",
 "{SlyA}I could always go down to 400 thousand.": "{SlyA}我也可以随时降到四十万。",
 "{FearC}Agh!  Okay 500 thousand!": "{FearC}啊！好，五十万！",
 "{WorryA}[relieved sigh]": "{WorryA}[relieved sigh]",
 "You're a tough negotiator, Mr. Stripey Pants!": "你真是个难缠的谈判对手，条纹裤先生！",
 "Thanks.  Now, if you'll just sign a few forms, my associate will give you your money.":
    "谢谢。现在，只要你签几份表格，我同伴就会把钱给你。",
 "Forms?": "表格？",
 "I'll need to read them.": "我得读一下。",
 "Of course.  Let's just walk over here while my associate figures out how to pick up the Wedge.":
    "当然。我们走到这边来，让我同伴想想怎么把楔石搬走。",
 "{HappyA}Oh, what the heck, five hundred thousand it is!":
    "{HappyA}哦，管他呢，就五十万吧！",
 "[relieved sigh]": "[relieved sigh]",
 "{HappyA}You're a tough negotiator, Mr. Stripey Pants!":
    "{HappyA}你真是个难缠的谈判对手，条纹裤先生！",
 "{THinkingC}Um, is this some sort of Hyperion negotiating strategy?":
    "{THinkingC}呃，这是某种 亥博龙谈判策略吗？",
 "{FearB}A million dollars!  {HappyA}We're offering a million dollars!":
    "{FearB}一百万！{HappyA}我们出一百万！",
 "{WorryC}Dude!": "{WorryC}老兄！",
 "{FearCX}One... million...dollars?": "{FearCX}一……百……万……美金？",
 "{WorryB}Mister Shade?  Are you okay?": "{WorryB}Shade 先生？你没事吧？",
 "{HappyB}Okay!?  I'm better than okay, I'm a bona fide millionaire!  I'm rich!  {HappyC}I'm well-off, I'm financially secure!":
    "{HappyB}没事！？我比没事好几了，我是货真价实的百万富翁！我发财了！{HappyC}我富裕了，我财务自由了！",
 "{SternC}Nice negotiating there.": "{SternC}谈得真好。",
 "{sternc}Hey, YOU weren't saying anything.": "{sternc}嘿，是*你*什么都不说。",
 "Here boys, have a couple hundred on me!  And some souvineer floaty pens!  Heck, take anything you want, I'm retired, baby!":
    "来，小伙子们，这几百块拿去花！还有些浮空纪念笔！见鬼，想要什么随便拿，我退休啦，宝贝！",
 "All right, let's get this over with so I can use my newfound wealth to fix my door.":
    "好，我们把这事了结，好让我用这笔新财富修我的门。",
 "{AngryB}And don't get any ideas about screwing me over...":
    "{AngryB}别打什么坑我的主意……",
 "{HappyB}\t...I've got a pretty good poker face...": "{HappyB}\t……我可有张不错的扑克脸……",
 "{FearA}... Seriously, it's been hit by a poker...": "{FearA}……说真的，它被扑克牌打过……",
 "[through teeth] {worryA}Don't get greedy, don't get greedy, don't get greedy...":
    "[through teeth] {worryA}别贪心，别贪心，别贪心……",
 "{SmugA}Mister Shade, Hyperion is prepared to offer you ONE MILLION DOLLARS  for this spectacular artifact.":
    "{SmugA}Shade 先生，亥博龙愿意为这件壮观的物品出价*一百万美金*。",
 "[aside]Maybe I should've low-balled him.": "[aside]也许我该给他压个低价。",
 "[aside] Ya think?": "[aside] 你说呢？",
 "{HappyC}Heck, this almost makes me forget about the door! [suddenly dark] {AngryC}ALMOST.":
    "{HappyC}见鬼，这几乎让我忘了门的事！[suddenly dark] {AngryC}几乎。",
 "{thinkingC}But other than that, {HappyC}yay me!  Here, have a couple of souvineers, guys!  I'm rich!":
    "{thinkingC}除此之外，{HappyC}为我欢呼吧！来，小伙子们，拿几件纪念品！我发财了！",
 "{SmugB}Mr. Shade, Hyperion will give you 750 thousand for the Slab.":
    "{SmugB}Shade 先生，亥博龙愿意为这块石板给你七十五万。",
 "{thinkingB}750, huh?  That's... acceptable.  I guess.":
    "{thinkingB}七十五万，是吗？那……可以接受。我想。",
 "{smugA}[relieved sigh]": "{smugA}[relieved sigh]",
 "Splendid.  Now, my partner has some forms to sign before we give you your money.":
    "太好了。现在，在我们付钱之前，我搭档有几份表格要签。",
 "Mister Shade, the Hyperion corporation is prepared to offer you 500 thousand dollars for your so-called Slab of Mystery.":
    "Shade 先生，亥博龙公司愿意为你那块所谓的神秘石板出价五十万美元。",
 "Five hundred?  I don't know...": "五十万？我不知道……",
 "{NeutralB}Okay, okay.  One million.  {sternB}And that's my final offer.":
    "{NeutralB}好，好。一百万。{sternB}这是我的最终报价。",
 "Okay, 750.  Final offer.": "好，七十五万。最终报价。",
 "I could always go down to 400 thousand.": "我也可以随时降到四十万。",
 "Agh!  Okay 500 thousand!": "啊！好，五十万！",
 "Oh, what the heck, five hundred thousand it is!": "哦，管他呢，就五十万吧！",
 "[annoyed]  {AngryA}Is this a negotiating tactic, {AngryB}like knocking down my door?":
    "[annoyed]  {AngryA}这是谈判手法吗，{AngryB}像砸我的门那样？",
 "A million dollars!  We're offering a million dollars!": "一百万！我们出一百万！",
 "Dude!": "老兄！",
 "Nice negotiating there.": "谈得真好。",
 "Hey, YOU weren't saying anything.": "嘿，是*你*什么都不说。",
 "{SlyB}Shh, do you here that? {SlyC}That's the Rhys Train baby!":
    "{SlyB}嘘，你听到了吗？{SlyC}那是 瑞斯 号列车，宝贝！",
 "[still stunned] {body-carrycase}{ShockA}Choo-freakin'-choo.":
    "[still stunned] {body-carrycase}{ShockA}呜——呜。",
 "{SmugC}I told you... Golden Boys.": "{SmugC}我跟你说过……黄金男孩。",
 "[still stunned] {ShockA}Golden, hell, {HappyB}we're gonna be platinum.":
    "[still stunned] {ShockA}黄金算什么，{HappyB}我们要当白金。",
 "{SmugA}Once in a lifetime, right?": "{SmugA}一生一次，对吧？",
 "[still stunned] {ShockA}Ten lifetimes.": "[still stunned] {ShockA}十辈子一次。",
 "{SmugA}I TOLD you I was the best data miner Hyperion had ever seen.":
    "{SmugA}我*跟*你说过我是 亥博龙见过的最好的数据挖掘员。",
 "[still stunned] {ShockA}We're gonna be gods.": "[still stunned] {ShockA}我们要成神了。",
 "Well, stop staring and throw it!": "好了，别看呆了，扔啊！",
 "[to himself] Take that, Vasquez": "[to himself] 接招吧，Vasquez",
 "Define \"bad.\"": "给“坏”下个定义。",
 "You know, it makes them crazy. Loco. Cuckoo bananas.":
    "你知道，那会让他们发疯。癫狂。疯得像香蕉一样。",
 "When living things pass through the Slab, it does something bad to their brains!":
    "活物穿过石板时，那东西会对他们的脑子做点不好的事！",
 "{AngryC}Hey!  {AngryB}What did I tell you about touching the Slab!":
    "{AngryC}嘿！{AngryB}我跟你说过别碰石板！",
 "Hey, I come by my eccentricities naturally.": "嘿，我的怪癖是天生的。",
 "[to himself] Like you?": "[to himself] 像你一样？",
 "{WorryA}Not to do it?": "{WorryA}是别碰它吗？",
 "Congratulations, you vaporized a-ow! [alt \"Where'd it-ow!\" or \"Ow!\"]":
    "恭喜，你把一个东西汽化了——哎哟！[alt：它去哪了——哎哟！/ 哎哟！]",
 "[still a little bit of an attitude]{THinkingB}So, you were saying {HappyA}something about making me rich?":
    "[still a little bit of an attitude]{THinkingB}所以，你刚才{HappyA}说要让我发财？",
 "[enthused] Ta-daaaa!": "[enthused] 哒——哒啊！",
 "{HappyB}So, let's talk money!": "{HappyB}那，我们谈钱吧！",
 "What the hell?": "搞什么？",
 "[still a little bit of an attitude]So, you were saying something about making me rich?":
    "[still a little bit of an attitude]所以，你刚说了要让我发财？",
 "So, let's talk money!": "那，我们谈钱吧！",
 "Uh, probably?": "呃，大概吧？",
 "You sure THOSE'LL work?": "你确定*那些*管用？",
 "Great.": "好极了。",
 "Hey, I just had a thought... how's that LoaderBot gonna pick up the artifact anyway?  Won't the pincers go right through it like the pen?":
    "嘿，我刚想到……那台装载机器人到底要怎么把物品拿起来？夹钳不会像那支笔一样直接穿过去吗？",
 "Electromagnetic grippers.": "电磁夹钳。",
 "I really should give Yvette a raise.": "我真该给 Yvette 加薪。",
 "Offer all the money.": "出全部的钱。",
 "Offer most of the money": "出大部分的钱",
 "Offer half the money": "出一半的钱",
 "Okay, take it all.": "好，全都给它。",
 "Up offer.": "提高报价。",
 "Lower offer": "降低报价",
 "{thinkingA}So let's see the money!": "{thinkingA}那就让我们看看钱！",
 "Now {HappyC}let's see that money!": "现在{HappyC}让我们看看钱！",
})

# —— Shade 的讲解 + 展品互动 ——
T.update({
 "[enthused] {HappyB}Founded over twenty-five years ago by my grandfather, the eccentric Professor Penumbra....":
    "[enthused] {HappyB}由我祖父、古怪的 Penumbra 教授创立于二十五年前……",
 "We're about to buy a Vault Key!": "我们马上要买到一把秘藏钥匙了！",
 "Shade's Door": "Shade 的门",
 "Intimidate Shade": "恐吓 Shade",
 "Show Him the Money": "给他看钱",
 "Loader Bot": "装载机器人",
 "Artifact": "物品",
 "Throw Pen At": "把笔扔向",
 "Touch": "触摸",
 "Hopefully that isn't this guy's LAST visitor...": "希望那不是这家伙的最后一位访客……",
 "Subtle.": "真含蓄。",
 "All I see is a bunch of junk. This better not be a wild goose chase.":
    "我看到的只有一堆破烂。这最好不是白跑一趟。",
 "[Disdainful] Yeah.": "[Disdainful] 是啊。",
 "[Coughs] Yeesh. All this dust is so... [Can't find the word]":
    "[Coughs] 呃。这灰尘真是……[Can't find the word]",
 "...Dusty?": "……灰？",
 "Well come on - We're almost done here.": "好了，快点——我们快办完了。",
 "[Back to Shade] Oh wait. Did you sign the back of that one?":
    "[Back to Shade] 哦等等。那一份的背面你签了吗？",
 "You figure out how we're going to get that wedge yet?":
    "你想出怎么把那楔石搬走了吗？",
 "Um. Not yet.": "呃。还没。",
 "...okay and this one's in double-triplicate, purely for tax reasons...":
    "……好，这一份要一式三份，纯粹出于税务原因……",
 "...birthdate there. Signature there. Copy those letters into the box below...":
    "……生日填那儿。签名那儿。把那些字母抄进下面的框里……",
 "[Grumbling quietly to himself] Great great great great planet. Really good times...":
    "[Grumbling quietly to himself] 好得不得了的好星球。真是美好时光……",
 "You okay there buddy?": "你还好吗，老兄？",
 "Let's just get this over with. The sooner this dusty hell is in our rearview, the better.":
    "我们把这了结吧。这个灰扑扑的地狱越早从后视镜里消失越好。",
 "[Gestures to Shade's] Be sure to tell him that. He'll love it.":
    "[Gestures to Shade's] 一定要告诉他这话。他会喜欢的。",
 "[projected]  Does he know who we are?": "[projected]  他知道我们是谁吗？",
 "[v-o][surly] We're closed!": "[v-o][surly] 我们打烊了！",
 "[projected a little]He says he's closed!": "[projected a little]他说他打烊了！",
 "[v-o][surlier] I SAID we're closed!": "[v-o][surlier] 我说了我们打烊了！",
 "Stop screwing around and flash the ID, man!": "别磨蹭了，把证件亮出来，老兄！",
 "Hmmm.": "嗯。",
 "Hey, you!  We're here for your Vault Key!": "嘿，你！我们是为你的秘藏钥匙来的！",
 "[surly] You're early-": "[surly] 你们早到了——",
 "{HappyC} Next time I aim for the pants!": "{HappyC} 下次我瞄准裤子！",
 "Did you tell him we were here on official business?":
    "你告诉他我们是来办公事的了吗？",
 "Are all your dates this good?": "你的约会都这么精彩吗？",
 "Oh yeah.": "是啊。",
 "The anticipation is making me urpy!": "这期待感让我想吐！",
 "Get on with it, already!": "快点开始吧！",
 "Classy.": "真有品味。",
 "You'd never guess this tourist trap had a genuine Vault Key.":
    "你绝对想不到这个坑游客的地方会有一把真秘藏钥匙。",
 "The Vault Key's on the other side of the fence, I can practically taste it.":
    "秘藏钥匙就在栅栏那边，我几乎能尝到它的味道了。",
 "Ew.": "呃。",
 "[as his grandfather, Prof. Penumbra] (As Professor Penumbra) Greetings, true believers!  This is your old pal Professor Penumbra, welcoming you to Shade's World of Curiosities, now under new and legally kosher management!":
    "[as his grandfather, Prof. Penumbra] （以 Penumbra 教授的口吻）向你们问好，忠实的信徒们！我是你们的老朋友 Penumbra 教授，欢迎来到 Shade 的奇珍世界，现已由全新且法律上完全合规的管理层接管！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) We're closed for the day, but please be sure to come back tomorrow to experience the intrigue and wonder of Shade's World of Curiosities!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）我们今天歇业，但请务必明天再来，体验 Shade 奇珍世界的诡秘与奇观！",
 "He's not the guy with the Vault Key, is he?": "他不是那个有秘藏钥匙的人吧？",
 "On Pandora?": "在 潘多拉 上？",
 "Is that a corpse or a corpse-like mannequin?": "那是具尸体，还是像尸体的假人？",
 "Nah.  Our guy's not a professor...or a corpse.": "不。我们那位既不是教授……也不是尸体。",
 "[worried] Tomorrow?  We can't wait until tomorrow... Vasquez'll be here in HOURS.":
    "[worried] 明天？我们等不到明天……Vasquez 几*小时*后就到了。",
 "Eh, I'm pretty sure that's just for the tourists.": "呃，我很确定那只是给游客看的。",
 "[as his grandfather, Prof. Penumbra]": "[as his grandfather, Prof. Penumbra]",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) Incidentally, it has come to my attention that SOME Prosperity Junction busybodies are spreading scurrilous rumors about my retirement from Shade's World of Curiosities!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）顺便说一句，我注意到繁荣枢纽有些爱管闲事的家伙在散布关于我从 Shade 奇珍世界退休的污蔑性谣言！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra)  Let me just say, shame!  Shame on you!  You're all bastard people, and I hate your ass faces!  Um...  Shade's World of Curiosities!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）我只想说，可耻！你们真可耻！你们全是一群混账东西，我讨厌你们那张蠢脸！呃……Shade 的奇珍世界！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) Gape at the Wedge of Mystery!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）来瞪大眼睛看神秘楔石！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) Witness the Stinging Singing Cactus!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）见证会蜇人的歌唱仙人掌！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) Drool at Mad Moxxi's Wedding Dress!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）为疯婆 莫西 的婚纱流口水吧！",
 "[as his grandfather, Prof. Penumbra](As Professor Penumbra) The greatest gathering of weirdness this side of Pandora, all found at Shade's World of Curiosities!":
    "[as his grandfather, Prof. Penumbra]（以 Penumbra 教授的口吻）潘多拉 这一侧最盛大的怪诞聚会，尽在 Shade 的奇珍世界！",
 "[contemplative]  Corpse as barker.  Clever.": "[contemplative]  用尸体招揽客人。挺聪明。",
 "{sternC}It's locked.  We'll have to go through the front door.":
    "{sternC}锁着。我们得从前门进去。",
 "Shout \"hey skag face\"": "喊一声“嘿，异犬脸”",
 "I will pay you to shut up about the door. ($200)": "我付钱让你别再提那扇门。（$200）",
 "Isn't he expecting us?": "他不是在等我们吗？",
 "[stunned] Son of a bitch...": "[stunned] 狗娘养的……",
 "When we bring this back to Hyperion-": "等我们把这带回去给 亥博龙——",
 "Rhys, this is.... I'm gonna be the Vice-President in Charge of Unbelievable Spending!":
    "瑞斯，这……我要当上“难以置信开销”副总裁了！",
 "I think he wasnt' expecting someone from Hyperion.": "我觉得他没料到会有 亥博龙的人来。",
 "Mr. Shade, as you are no doubt aware, you are in possession of a rare alien artifact colloquially known as a \"Vault Key.\"":
    "Shade 先生，您想必知道，您持有一件俗称“秘藏钥匙”的稀有外星物品。",
 "With your premission, my handsome associate and I would like you to put aside you obvious antipathy towards the Hyperion Corporation":
    "如蒙允许，我英俊的同伴和我希望您暂且放下对 亥博龙公司明显的反感",
 "Now, we understand your hesitance towards doing business with the Hyperion Coroporation...":
    "我们理解您对与 亥博龙公司做生意有所犹豫……",
 "Doubts, shmouts, let's sell you a Vault Key, friends!":
    "疑虑什么的，管它呢，我们就卖你一把秘藏钥匙，朋友们！",
 "But as you can see, my handsome associate and I are more than prepared to smother your doubts under this enormous pile of money.":
    "但如您所见，我英俊的同伴和我已经准备好用这一大堆钱把您的疑虑埋掉。",
 "Mr. Shade?": "Shade 先生？",
 "Mr. Shade, we understand your  reluctance to sell your Vault Key to the Hyperion Corporation.":
    "Shade 先生，我们理解您不愿把秘藏钥匙卖给 亥博龙公司。",
 "Mr. Shade, we understand your reluctance to sell your Vault Key to the Hyperion Corporation.":
    "Shade 先生，我们理解您不愿把秘藏钥匙卖给 亥博龙公司。",
 "But as you can see, my jackass associate and I are more than prepared to smother your doubts under this enormous pile of money.":
    "但如您所见，我那位蠢货同伴和我已经准备好用这一大堆钱把您的疑虑埋掉。",
 "[confidential][near giddy] Can you believe it?  We're about to buy a Vault Key!":
    "[confidential][near giddy] 你信吗？我们马上要买到一把秘藏钥匙了！",
 "[sighs] Story of my life...": "[sighs] 我这辈子的写照……",
 "[still somewhat angry... NOT bored] But of course, you don't care about any of that, do you?  You just want to do your dirty business, leave your money on the dresser and get out of here...":
    "[still somewhat angry... NOT bored] 但当然，你们对那一切都不在意，对吧？你们只想办完你们那点脏事，把钱扔在梳妆台上然后滚出去……",
 "Well, wait no more, door-killers....": "那就不用再等了，拆门凶手们……",
 "I give you... the Vault Key!": "我给你们……秘藏钥匙！",
 "[enthused] And of course, the coup de grace, the piece de resistance, the thing that's gonna make me rich, the one, the only, the Vault Key!":
    "[enthused] 当然，还有压轴大戏、镇馆之宝，那个将要让我发财的、独一无二的秘藏钥匙！",
 "{body-CarryCase}{ShockA}Handsome Jack's death pants?": "{body-CarryCase}{ShockA}帅杰克的死亡之裤？",
 "{HappyC}Spoiler - they needed to be laundered.  {THinkC}HEAVILY.":
    "{HappyC}剧透——它们需要洗。{THinkC}大洗特洗。",
 "What should I be looking for?": "我该找什么？",
 "We're on a timetable.": "我们时间有限。",
 "It's LITERALLY a key to untold alien riches!": "它就是一把通往无数外星财富的*钥匙*！",
 "I'd better scan it with my E-Eye first.  Just to make sure it isn't leaking radiation of something.":
    "我还是先用 ECHO 眼扫一下。确保它没在漏辐射什么的。",
 "But you will note that it is fully charged with freaky Eridian energies":
    "但你会注意到它充满了诡异的伊瑞德能量",
 "Discovered by my grandfather just before his sudden and tragic death ...":
    "是我祖父在他突然而悲惨地死去之前发现的……",
 "This amazing Vault Key is not only in prisitine condition...":
    "这把惊人的秘藏钥匙不仅保存得完好如新……",
 "That's 'cause it's throbbing with exotic alien energies!":
    "那是因为它正脉动着异域外星能量！",
 "See how it floats?": "看到它怎么飘着了吗？",
 "Wait, this thing is charged up?": "等等，这东西是充了电的？",
 "If you could find one, of course.": "当然，前提是你能找到一把。",
 "Why, you could open a Vault with that sucker right now!":
    "你瞧，你现在就能用这玩意儿打开一个秘藏！",
 "[stunned] I'm too happy to be embarassed by that.":
    "[stunned] 我太高兴了，都不觉得那尴尬。",
 "[confidential][cool as heck]See? Lady Baltimore.": "[confidential][cool as heck]看吧？巴尔的摩女士。",
 "I know!": "我知道！",
 "Stall him.": "拖住他。",
 "[under breath] {body-carrycase}{SmugB}I'll keep this mouthbreather busy.  {slyB}You inspect the Key.":
    "[under breath] {body-carrycase}{SmugB}我来拖住这个用嘴呼吸的。{slyB}你检查钥匙。",
 "So, when do I get my money?": "那，我什么时候能拿到钱？",
 "That's a good question.": "问得好。",
 "I know, right?": "我也觉得。",
 "Yeah, maybe you should get scanning.": "是啊，也许你该去扫描了。",
 "Uh, Rhys?  Maybe I should handle the haggling-": "呃，瑞斯？也许该由我来砍价——",
 "Why?": "为什么？",
 "Mr. Shade, Hyperion is prepared to offer you-": "Shade 先生，亥博龙愿意向你出价——",
 "I would?": "我会吗？",
 "Um, before we make an offer, could we take the Vault Key out of the case for a closer look?":
    "呃，在我们出价之前，能先把秘藏钥匙从展示柜里拿出来仔细看看吗？",
 "Welcome aboard the Rhys Train": "欢迎乘坐 瑞斯 号列车",
 "I told you we'd be Golden Boys": "我跟你说过我们会成为黄金男孩",
 "This is WAY better than my blind dates.": "这比我那些相亲强*太多了*。",
 "I told you so.": "我早说过。",
 "It's real.  Wow.": "是真的。哇。",
 "[stunned] Nice to know I'm not the only one stunned into incoherence.":
    "[stunned] 还好不只我一个人惊得说不出话。",
 "[stunned] It's really real.  It's actually really real.":
    "[stunned] 它真的是真的。它真真切切的是真的。",
 "[confidential]I TOLD you this would work.": "[confidential]我*跟*你说过这能成。",
 "Thought it'd be bigger.": "我以为它更大。",
 "[stunned]  Dude, don't even TRY to pretend like you're not awestruck here.":
    "[stunned]  老兄，别装了，你明明也被震住了。",
 "[stunned]  Weird.  I always thought a Vault Key'd be bigger.":
    "[stunned]  怪了。我一直以为秘藏钥匙会更大。",
 "[stunned] He's too stunned to say something cool.":
    "[stunned] 他惊得说不出帅话了。",
 "What's wrong with your buddy?": "你搭档怎么了？",
 "Maybe Vasquez never mentioned Hyperion.": "也许 Vasquez 从没提过 亥博龙。",
 "[scary voice]  {SmugA}There are two ways we can go with this, Mr. Shade.":
    "[scary voice]  {SmugA}这事有两条路可走，Shade 先生。",
 "[scary voice]  {SternB}You can sell your Vault Key and let us \"goosestep\" out of here.":
    "[scary voice]  {SternB}你可以把秘藏钥匙卖了，让我们“踢着正步”离开这儿。",
 "[scared] Or?": "[scared] 或者？",
 "[scary voice]  {SlyA}Less cash.  More robots.": "[scary voice]  {SlyA}钱少点。机器人多点。",
 "[scary voice] {SternA}OR you can wait for the next offer from Hyperion.":
    "[scary voice] {SternA}或者你可以等 亥博龙的下一次报价。",
 "[scared] NEXT offer?": "[scared] 下一次报价？",
 "[sympathetic] Yeah, sorry about that.  These Loader Bots can be so clumsy.":
    "[sympathetic] 是啊，抱歉。这些装载机器人有时候笨手笨脚的。",
 "[casual]So before anything get any clumsier, is there any chance that we can trade you an {SmugC}absurd amount of money for your Vault Key?":
    "[casual]所以趁事情还没变得更笨手笨脚，我们能不能用{SmugC}一笔荒唐的巨款换你的秘藏钥匙？",
 "[confused]  What?": "[confused]  什么？",
 "[all-business and cheery] {SlyC}Mr. Shade, thank you for arranging to meet with us today.":
    "[all-business and cheery] {SlyC}Shade 先生，感谢您安排今天与我们见面。",
 "A Vault Key, yeah, I know.  I was the one who contacted you guys, remember?":
    "秘藏钥匙，是啊，我知道。是我联系你们的，记得吗？",
 "[intrigued]  {fearC}Let's talk about that cash.": "[intrigued]  {fearC}我们谈谈那笔钱吧。",
 "[confidential to Shade] Robotics gets all the crap programmers.":
    "[confidential to Shade] 机器人部门只能招到最烂的程序员。",
 "[intrugued] {ThinkA}How... absurd?": "[intrugued] {ThinkA}多……荒唐？",
 "[intrigued] {ThinkB}How \"obscene\" {ThinkC}are we talking about here?":
    "[intrigued] {ThinkB}你说的“下流”{ThinkC}是到什么程度？",
 "[all-business] {SmugC}We at the Hyperion Corporation have taken a keen interest in your Vault Key, and would love to purchase said Vault Key for an {SlyC}obscene amount of money.":
    "[all-business] {SmugC}我们 亥博龙公司对您的秘藏钥匙产生了浓厚兴趣，很想用{ SlyC}一笔下流的巨款买下它。",
 "{AngryB}Rhys!  Stop scaring the poor guy and let's {SternC}tell him about all the money we're gonna pay him for the Vault Key!":
    "{AngryB}瑞斯！别吓唬这可怜人了，我们{SternC}跟他说说买秘藏钥匙要给他多少钱！",
 "[intrigued] {THinkC}Money?  How much money?": "[intrigued] {THinkC}钱？多少钱？",
 "'Cause I've got pretty": "因为我可是有张相当",
 "I just never imagined Hyperi": "我只是从没想过 HYPERI",
 "Believe me,": "相信我，",
 "Enough to retire.": "足够退休。",
 "[contemplative]  I've always wanted to vegetate peacefully...":
    "[contemplative]  我一直想安安静静地躺着长草……",
 "Mr. Shade, with the money in this briefcase you could quit your, um, job, retire, and do absolutely NOTHING for the rest of your life.":
    "Shade 先生，用这个手提箱里的钱，你可以辞掉你的，呃，工作，退休，余生什么都不*用做*。",
 "Enough to do anything.": "足够做任何事。",
 "[contemplative] I've always wanted to carve my face in a mountain...":
    "[contemplative] 我一直想把我的脸刻在山壁上……",
 "Mr. Shade, with the money in this briefcase you could do just about whatever you wanted.":
    "Shade 先生，用这个手提箱里的钱，你想干什么几乎都行。",
 "Enough to buy anything.": "足够买下任何东西。",
 "Mr. Shade, with the money in this briefcase you could buy just about anything on this entire planet.":
    "Shade 先生，用这个手提箱里的钱，整个星球上你几乎什么都能买。",
 "[contemplative] I've always wanted to own a politician...":
    "[contemplative] 我一直想拥有一个政客……",
 "Let's just say it's more money than any of us has ever seen in our lifetime, okay?":
    "我们就说这笔钱比我们任何人这辈子见过的都多，行吗？",
 "[conemplative] Well...": "[conemplative] 这个……",
 "Especially if I'm gonna have to deal with [suprresses queasiness] Hyperion.":
    "尤其是我还得跟[suprresses queasiness] 亥博龙打交道。",
 "'Cause I've got a pretty active imagination when it comes to money.":
    "因为一说到钱，我的想象力可是很活跃的。",
 "[to himself] Are we taking a shower with this guy?": "[to himself] 我们要跟这家伙一起洗澡吗？",
 "I think he's still pissed about the door.  I'll get a better price.":
    "我觉得他还在为门的事生气。我能谈个更好的价。",
 "I'm the one who showed him the money.  He likes me.": "给他看钱的是我。他喜欢我。",
 "So I heard.": "我听说了。",
 "Well, I didn't knock down his door.": "这个嘛，砸他家门的不是我。",
 "I think he likes you better.": "我觉得他更喜欢你。",
 "Maybe he's intimidated by you machismo.": "也许他被你的男子气概吓到了。",
 "Must be.  I'll scan": "一定是。我扫描",
 "You might have a point.": "你说得有道理。",
 "You think ol' Shade just fell off the kumquat truck?  If I unlock my display case, you two'll swipe the Key with your nasty robot!":
    "你以为老 Shade 刚从金橘车上掉下来？要是我打开展示柜，你们俩就会用那台讨厌的机器人把钥匙顺走！",
 "[concerned] Cybernetic eyeball?": "[concerned] 电子眼？",
 "[smoothing things over] Why don't you give the Key the once-over with that weird cybernetic eyeball of yours while Mr. Shade and I talk price.":
    "[smoothing things over] 你干嘛不用你那只古怪的电子眼把钥匙检查一遍，我和 Shade 先生谈谈价格。",
 "Radiation, pshaw!  I've been handling it, and I feel perfectly fine.":
    "辐射，呸！我一直拿着它，感觉好得很。",
 "Why don't you scan the Key for": "你干嘛不扫描一下钥匙，看看",
 "[projected] Maybe he forgot?": "[projected] 也许他忘了？",
 "[projected a little, confused]]Maybe he forgot?": "[projected a little, confused]]也许他忘了？",
 "[projected] And don't forget to flash the Hyperion ID this time!":
    "[projected] 这次别忘了把 亥博龙的证件亮出来！",
 "We'll do the first thing.": "我们做第一件事。",
 "Or is your big ol' automoton still hungry for the blood of innocent doors!?":
    "还是说你那台大自动机还渴望着无辜门扉的鲜血！？",
 "Well?  Do you want to buy a Vault Key?": "怎么？你想买一把秘藏钥匙吗？",
 "We'll be gods among men, I know!": "我们会成为人中之神，我知道！",
 "That doesn't mean anything - his ECHO chatter with Vasquez made it sound like a recent acquisition.":
    "那说明不了什么——他跟 Vasquez 的 ECHO 通话听起来像是最近才到手的。",
 "I notice he didn't say anything about a Vault Key.": "我注意到他完全没提秘藏钥匙。",
 "Look": "看着",
 "Open Case": "打开展示柜",
 "Scan": "扫描",
 "{SmugA}Hmmm.  No obvious flaws.": "{SmugA}嗯。没有明显瑕疵。",
 "Hey, any chance I can take this out of the case?": "嘿，我能不能把它从展示柜里拿出来？",
 "You think ol' Shade just fell off the turnip truck?":
    "你以为老 Shade 刚从萝卜车上掉下来？",
 "Waitaminute.  You just want to get your hands on the Key so that you can steal it with your scary Hyperion robot.":
    "等等。你只是想上手摸到钥匙，好让你用那台吓人的 亥博龙机器人把它偷走。",
 "Not": "不是",
 "We'd never-": "我们绝不会——",
 "It's okay, Vaughn.  If it'll make Mr. Sahde more comfortable, I can examine the Key from the outside.":
    "没关系，沃恩。要是能让 Shade 先生更放心，我可以在外面检查钥匙。",
 "[with bravado] The Wedge of Mystery.": "[with bravado] 神秘楔石。",
 "What's this?": "这是什么？",
 "What makes it so mysterious?": "它为什么这么神秘？",
 "[mysterious] Its uncanny ability to stand perfectly still and exude WEDGENESS!":
    "[mysterious] 它那不可思议的能力：纹丝不动地站着，并散发出*楔性*！",
 "[to himself]  Doesn't LOOK like a wedge...": "[to himself]  看起来可不像楔子……",
 "Is it fragile?": "它易碎吗？",
 "Don't touch the Wedge!": "别碰楔石！",
 "No, its just doesn't like people touching it.  Learned that the hard way...":
    "不，它只是不喜欢被人碰。这我可是吃过大亏才学到的……",
 "Hikeba.": "嗨克吧。",
 "Ya think?": "你说呢？",
 "Me?": "我？",
 "Vaughn, make the man an offer.": "沃恩，给这人出个价。",
 "[confidential] I think we'll get a better price if it's coming from someone who DIDN'T break his door.":
    "[confidential] 我觉得由一个*没*砸他家门的人来出价，我们能拿到更好的价格。",
 "[confidential]  Good point.": "[confidential]  有道理。",
 "You're the money guy, aren't you?": "你是管钱的那个，对吧？",
 "[somewhat proud] Hey, I guess I am.": "[somewhat proud] 嘿，我想是吧。",
 "Will do.": "好。",
 "Why don't you examine the merchandise while I work out a deal with Captain Sunglasses.":
    "你检查一下货，我去跟墨镜队长谈生意。",
 "How good?": "多好？",
 "This good.": "这么好。",
 "Duh.": "废话。",
 "Totally duh.": "绝对废话。",
 "Dude.": "老兄。",
 "Double dude.": "双重老兄。",
 "Hi there.": "你好啊。",
 "[loud, in battle] Don't stare at it, hack it!": "[loud, in battle] 别盯着看，黑进去！",
 "I should really give Yvette a raise.": "我真该给 Yvette 加薪。",
 "There'll be plenty of time to play with the Loader Bot after I finish examining the Vault key.":
    "等我检查完秘藏钥匙，有的是时间玩装载机器人。",
 "[a little quieter] I bet Vasquez is already on his way...":
    "[a little quieter] 我打赌 Vasquez 已经在路上了……",
 "Oh yeah.  Between the burnings-in-effigy and the straight-up vandalism, it's":
    "是啊。又是焚像又是直接搞破坏，这",
})

# —— 展品与算命机 ——
T.update({
 "{HappyB}Do you like it?  It's super valuable.": "{HappyB}你喜欢吗？它超级值钱。",
 "{ShockA}Where'd you get that?": "{ShockA}你从哪儿弄来的？",
 "[to himself] I still believe in you, boss.": "[to himself] 我依然信你，老板。",
 "Whoah.": "哇。",
 "{NeutralA}Why?": "{NeutralA}为什么？",
 "{SternC}Savages.": "{SternC}野蛮人。",
 "{HappyC}It's one of the few pictures of Handsome Jack {HappyB}that hasn't been sprayed with paint, bullets, or {FearB}feces.":
    "{HappyC}这是帅杰克少数几张{HappyB}没被喷上油漆、子弹或者{FearB}粪便的照片之一。",
 "Why is that giant Marcus head painted like a clown?":
    "为什么那颗巨大的 马库斯 头像被画成小丑的样子？",
 "It was frighetning the kiddies, so I decided to improve it.":
    "它把小孩都吓着了，所以我决定改良一下。",
 "By turning it into a giant scary clown?": "把它变成一个巨大的吓人小丑？",
 "[to himself]  I've never met Marcus, but from I hear, I doubt he'd approve.":
    "[to himself]  我从没见过 马库斯，但据我所知，我怀疑他不会同意。",
 "[to himself] Its eyes keep following me... [shudder]":
    "[to himself] 它的眼睛一直跟着我……[shudder]",
 "Poke Nose": "戳鼻子",
 "[as marcus](As Marcus) Welcome to Marcus Munitions, where every warm gun is a promise of fun!":
    "[as marcus]（以 马库斯 的口吻）欢迎来到 马库斯 军火，这里每一把温热的枪都是一份快乐的承诺！",
 "[sarcastic] Great Marcus you've got there.": "[sarcastic] 你这 马库斯 做得真好。",
 "use": "使用",
 "[to himself]": "[to himself]",
 "Sorry, friend.  One fortune per customer!": "抱歉，朋友。每位顾客只算一次命！",
 "[to himself]  I don't need a machine to tell me my fortune.":
    "[to himself]  我不需要机器来告诉我我的命运。",
 "[intrigued] I haven't seen one of these since I was a kid.":
    "[intrigued] 我从小时候起就没见过这种东西了。",
 "[to Shade] Does it work?": "[to Shade] 它管用吗？",
 "Well, it told me I was gonna get rich today, so it's got THAT going for it.":
    "这个嘛，它说今天我会发财，所以这点上它还算靠谱。",
 "\"A journey of a thousand miles begins with a single explosion.\"":
    "“千里之行，始于一次爆炸。”",
 "Pandoran humor, meh.": "潘多拉 式幽默，啧。",
 "\"You are destined for badassness.\"": "“你注定要牛气冲天。”",
 "I would've settled for \"greatness,\" but that'll do, too.":
    "我本来能接受“伟大”，但这个也行。",
 "Hey Vaughn, you're my greatest asset.": "嘿 沃恩，你是我最大的资产。",
 "Is that you talking, or the machine - you know what, I'm just going to take it.":
    "是你在说还是机器在说——算了，我就当是吧。",
 "\"Your friends are your greatest asset.\"": "“你的朋友是你最大的资产。”",
 "[wistful] Aren't we all.": "[wistful] 我们不都是嘛。",
 "\"Please help, I'm trapped in this box.\"": "“救命，我被困在这个盒子里了。”",
 "\"Outlook hazy.  Check again later.\"": "“前景不明。请稍后再试。”",
 "What a rip-off.": "真是坑钱。",
 "{SmugA}You inspect the Vault Key yet?": "{SmugA}你检查过秘藏钥匙了吗？",
 "{WorryA}No.": "{WorryA}没有。",
 "{SlyC}Then get on it.  {SmugA}We're close to a deal here.":
    "{SlyC}那就去检查。{SmugA}我们快谈成了。",
 "Let's talk turkey, Mr. Shade.": "我们说正事吧，Shade 先生。",
 "Okay, but don't try any funny business.": "好，但别动什么歪心思。",
 "Hyperion is prepared to off you THIS much for your Vault Key...":
    "亥博龙愿意为你的秘藏钥匙出*这么*多……",
 "Is that an eight or a five?": "那是八还是五？",
 "It's a three...": "是三……",
 "Here's my counter-offer.": "这是我的还价。",
 "How many briefcases do you think we have, anyway?": "你以为我们有多少个手提箱？",
 "Okay, lop off a couple of zeroes.": "好，砍掉两个零。",
 "Let's try this again...": "我们再试一次……",
 "Is that a joke?": "那是玩笑吗？",
 "Hyperion accountants never joke about money.": "亥博龙的会计从不在钱上开玩笑。",
 "How about this?": "这个怎么样？",
 "[annoyed] That number's higher than the last one.": "[annoyed] 这个数字比上一个大。",
 "Is it?  Imagine that.": "是吗？真是想不到。",
 "You're trying Hyperion's patience, Mr. Shade...": "你在考验 亥博龙的耐心，Shade 先生……",
 "Really?  Here.": "真的？给你。",
 "I think you forgot a couple digits there, friend.": "我觉得你漏了几个数字，朋友。",
 "I think this would be fair...": "我觉得这样才公平……",
 "Hey Rhys, does the Vault Key check out okay?": "嘿 瑞斯，秘藏钥匙检查得怎么样？",
 "Yo, pal, how's that scanning coming?": "嘿，老兄，扫描进展如何？",
 "This'd be goinga LOT easier if you finish up that scanning and give me a hand, Rhys.":
    "你要是把扫描做完来帮我一把，这事会轻松*得多*，瑞斯。",
 "It's better than your last offer.": "比你上次的报价好。",
 "THIS is just a picture of a butt.": "*这*只是一张屁股的照片。",
 "[sigh]  Let's just start over.": "[sigh]  我们从头再来吧。",
 "Door": "门",
 "[surprised shriek]": "[surprised shriek]",
 "You sure this is the guy?": "你确定是这家伙？",
 "Thanks.": "谢谢。",
 "{body-carrycase}{ShockA}Nice reflexes.": "{body-carrycase}{ShockA}反应不错。",
 "Yeah.  This is weird.": "是啊。这挺怪的。",
 "{ShockA}{WorryB}It's all in the {WorryB}swagger.": "{ShockA}{WorryB}全靠{WorryB}气场。",
 "Nice reflexes.": "反应不错。",
 "{body-carrycase}{SmugC}Did you swagger as {SmugA}}much as you could have swaggered, {SmugB}or did you leave some swagger on the table?":
    "{body-carrycase}{SmugC}你是把气场摆{SmugA}到十足了，{SmugB}还是留了几分在桌上？",
 "{body-carrycase}{SmugA}Never an orbital death ray around {SmugC}when you need one.":
    "{body-carrycase}{SmugA}需要轨道死光的时候{SmugC}总是没有。",
 "[dry] {SternC}Ha.": "[dry] {SternC}哈。",
 "{body-carrycase}{SmugB}Want me to imagine you're wearing {SmugC}CLEAN underwear?":
    "{body-carrycase}{SmugB}要我设想你穿的是{SmugC}干净内裤吗？",
 "{body-carrycase}{SmugC}You should probably dodge next time.":
    "{body-carrycase}{SmugC}下次你大概该躲一下。",
 "{WorryB}Guess he's not afraid of the {SlyC}death rays.":
    "{WorryB}看来他不怕{SlyC}死光。",
 "{WorryB}Luckily, I didn't {SlyC}have enough time to {HappyB}imagine him in his underwear.":
    "{WorryB}幸好我没{SlyC}来得及{HappyB}想象他穿内裤的样子。",
 "[wary] Okay... but no screwing around.": "[wary] 好……但别乱来。",
 "I've already got ONE voice in my head giving me bad advice... I don't need another.":
    "我脑子里已经有一个声音在给我出馊主意了……我不需要再来一个。",
 "[faux sympathetic] {SlyA}Oh hey, sorry you made me do that.  You okay?":
    "[faux sympathetic] {SlyA}哦嘿，抱歉让你逼我这么做。你没事吧？",
 "[faux sympathetic] {SlyC}Yeah, these Loader Bots they're just... they're so clumsy.":
    "[faux sympathetic] {SlyC}是啊，这些装载机器人就是……它们太笨手笨脚了。",
 "So much money it's making my wrist hurt, okay? You wanna take it off here?":
    "钱太多了，我手腕都疼了，行吗？你想在这儿卸下来吗？",
 "You should lift from the back.": "你该从后面抬。",
 "[contmplative]  Hmmmm.": "[contmplative]  嗯……",
 "The inexplicable Wedge of Mystery!": "不可思议的神秘楔石！",
 "Now, how much money are you carting around in that briefcase?":
    "那么，你那个手提箱里装了多少现金？",
 "Now, I believe you said something about smothering me in money?":
    "我记得你说过要用钱把我埋起来？",
 "[confidential] He doesn't know that.": "[confidential] 他不知道那点。",
 "[confidential]  We ARE eager.": "[confidential]  我们*确实*很急切。",
 "[confidential] What should I be looking for?": "[confidential] 我该找什么？",
 "[confidential] Since when do you know what a patina is?":
    "[confidential] 你从什么时候开始知道什么叫“包浆”了？",
 "[confidential]  I know, but maybe it's got a scratched patina or something we can use to drive the price down.":
    "[confidential]  我知道，但也许它有个刮花的包浆什么的，能让我们压价。",
 "[confidential] We're kind of on a timetable here, Vaughn.  Maybe we should just buy the Vault Key and get out of here.":
    "[confidential] 我们时间有限，沃恩。也许我们就该把秘藏钥匙买了然后走人。",
 "[confidential][sarcastic]Stall him with some of your accounting stories.":
    "[confidential][sarcastic]拿你那些会计故事去拖住他。",
 "[confidential]  Will do.  You look for any defects in the Key that we can use to drive the price down.":
    "[confidential]  好。你找找钥匙上有什么瑕疵能让我们压价。",
 "Uhhh, what's wrong with your pal?": "呃，你搭档怎么了？",
 "{body-CarryCase}Weird, isn't it?   Sometimes he just freezes up.  [confidnetial] Personally, I think it's all that cybernetic crap in his head.  Best to just steer clear of him until it passes.":
    "{body-CarryCase}挺怪的吧？他有时就那么僵住。[confidnetial] 我个人觉得是他脑子里那堆电子破烂闹的。最好离他远点，等它过去。",
 "Ooh, I Love talking about numbers!  Especially 82, that saucy little minx...":
    "哦，我爱聊数字！尤其是 82，那个风骚的小妖精……",
 "Got it.": "明白。",
 "[gesturing to Shade] Why don't we go talk about numbers while my partner examines the merchandise.":
    "[gesturing to Shade] 我们不如去那边聊数字，让我搭档检查一下货。",
 "[confidential] Examine the merchandise!": "[confidential] 去检查货！",
 "I'd rather you didn't.": "我希望你别这样。",
 "Yes, you should.": "对，你该去。",
 "{SmugC}Wonder what it looks like in the non-visible spectrum.":
    "{SmugC}不知道它在不可见光谱下是什么样。",
 "[to himself] {SmugB}If there's any flaws in this, my pathetic human eye sure can't see 'em.":
    "[to himself] {SmugB}要是这上面有瑕疵，我这双可悲的人眼肯定看不出来。",
 "That's some family.": "真是一家人。",
 "In Vasquez's correpsondence, he said it was a family heirloom.":
    "在 Vasquez 的通信里，他说这是件传家宝。",
 "How'd a place like this get a Vault Key?": "这种地方怎么会有秘藏钥匙？",
 "[alt][pickup1] Does he know who we are?": "[alt][pickup1] 他知道我们是谁吗？",
 "[alt][pickup1] Yeah, but it'd be the perfect place to hide one.":
    "[alt][pickup1] 是啊，但这倒是藏一把的绝佳地点。",
 "[alt][pickup1]Hard to believe a dump like this has a Vault Key.":
    "[alt][pickup1]真难相信这种破地方会有一把秘藏钥匙。",
 "You could lose TEN Vault Keys in this crap.": "在这种破烂堆里你能弄丢*十把*秘藏钥匙。",
 "Jeez, this place is a mess...": "天哪，这地方真乱……",
 "Now knock on the door and shout \"Hey, skag face!\"":
    "现在敲门，然后喊“嘿，异犬脸！”",
 "Rhys?  Nothing? Fine.  I'm going rogue.": "瑞斯？没反应？行。我自己上了。",
 "I think I can hear him reloading...": "我好像能听到他在装弹……",
 "[angry and confused]  Who the hell are you!?": "[angry and confused]  你们他妈是谁！？",
 "[angry and confused]  What?  Another one!?": "[angry and confused]  什么？又来一个！？",
 "Check what out?  Are you about to dance or something?":
    "看什么？你是要跳舞还是怎么着？",
 "That would do it!": "那倒是能成！",
 "You've got 'til the end of this sentence to get off my porch, you whimpering corporate lackey!":
    "你有直到这句话结束的时间滚下我的门廊，你这呜呜叫的公司走狗！",
 "Oops.": "哎呀。",
 "No thanks to you,": "可不是靠你，",
 "{SHockA}No way.  {AngryB}I know you've got at least that much {sternC}in your pocket.":
    "{SHockA}不行。{AngryB}我知道你口袋里至少装着{sternC}那么多。",
 "[still stunned] MEN.  Today... we are Golden MEN.":
    "[still stunned] 兄弟们。今天……我们是黄金*兄弟*。",
 "[projecting] Did you lick the gate?  Come on man!  You don't know where that's been.":
    "[projecting] 你舔过那扇门？拜托，老兄！你不知道它之前待过哪儿。",
 "If I try to open this gate, he'll probably just shoot me.":
    "要是我去开这扇门，他大概会直接开枪打我。",
 "The word you were looking for is \"ghoulish.\"": "你想找的那个词是“食尸鬼般的”。",
 "Corpse.": "尸体。",
 "Not until the deal's done, friend.": "交易完成之前不行，朋友。",
 "[takes a deep breath]  Hey, skag face!": "[takes a deep breath]  嘿，异犬脸！",
 "Just for the record, which one of you is Vasquez?": "顺便问一下，你们哪个是 Vasquez？",
 "I'm Vasquez.": "我是 Vasquez。",
 "I'm Rhys.  Vasquez is sick.": "我是 瑞斯。Vasquez 病了。",
 "None of your business.": "不关你的事。",
 "'Cause\tI'd kind of like to match a face to all those secret ECHO communiques, y'know?":
    "因为\t我挺想给那些秘密的 ECHO 通信配上一张脸，你懂吗？",
 "{body-carrycase}{HappyA}And I'm Vaughn {fearB}[catches himself] -squez.":
    "{body-carrycase}{HappyA}我是 沃恩{fearB}[catches himself] -squez。",
 "{SmugC}I'm Vasquez,  Hyperion Vault Acquisitions, at your service.":
    "{SmugC}我是 Vasquez，亥博龙秘藏收购部，听候差遣。",
 "{SmugC}Vasquez couldn't make it today.  [confidential]  {SternC}Oozing  armpit buboes... [back to normal voice] {SlyC}So he authorized us to act on his behalf.":
    "{SmugC}Vasquez 今天来不了。[confidential]  {SternC}腋下正流着脓疮……[back to normal voice] {SlyC}所以他授权我们代表他行事。",
 "I'm Rhys.  This is Vaughn.  Vasquez authorized us to act on his behalf.":
    "我是 瑞斯。这位是 沃恩。Vasquez 授权我们代表他行事。",
 "{SternA}Let's keep names out of this.": "{SternA}这事就别提名字了。",
 "{HappyA}I'm Rhys, he's Vaughn.": "{HappyA}我是 瑞斯，他是 沃恩。",
 "[still annoyed about door] Just for the record, are YOU Vasquez [addressing Vaughn], or is it Slickpants McDoorDestroyer here?":
    "[still annoyed about door] 顺便问一下，*你*是 Vasquez 吗[a 指向 Vaughn]，还是这边这位油嘴拆门大王？",
 "[sarcastic] {ThinkB}Oooh, mysterious!": "[sarcastic] {ThinkB}哦，好神秘！",
 "{AngryB}Me Shade, big hat!  {HappyB}Names are fun.  Anyway...":
    "{AngryB}我是 Shade，大帽子！{HappyB}名字真好玩。总之……",
 "[amused]  {ThinkC}Vasquez and Vonsquez?  {HappyC}Whoah, the boys in the mail room must {HappyB}HATE you guys.":
    "[amused]  {ThinkC}Vasquez 和 Vonsquez？{HappyC}哇，收发室那帮人肯定{HappyB}恨死你们了。",
 "{THinkB}Oh, I get it.  You're the men with no names.":
    "{THinkB}哦，我懂了。你们是没名字的人。",
 "{worryA}Sure, let's go with that.": "{worryA}行，就这么说吧。",
 "Well, Misters Vasquez and Vonsqeuz...": "那么，Vasquez 先生和 Vonsqeuz 先生……",
 "{HappyA}Mr. Rhys, Mr. Vaughn...": "{HappyA}瑞斯 先生，沃恩 先生……",
 "{THinkA}Okay, Mr. Stripey Pants, Mr. Bowtie..": "{THinkA}好，条纹裤先生，领结先生……",
 "[enthused] Welcome to Shade's World of Curiosities!":
    "[enthused] 欢迎来到 Shade 的奇珍世界！",
 "So, Vonsquez!": "那么，Vonsquez！",
 "Are we ready to start showering yours truly with wealth, or what?":
    "我们准备好开始往*本人*身上撒钱了吗？",
 "Who?  Oh that is my name!": "谁？哦那是我！",
 "So, Vaughn ol' buddy!  When are we gonna crack open that Hyperion briefcase and start showering yours truly with all that filthy filthy lucre?":
    "那么，沃恩 老兄！我们什么时候打开那个 亥博龙手提箱，开始往*本人*身上撒那堆肮脏的钱？",
 "{HappyC}So, Nerdy O' Bowtie, {HappyB}when do we crack open that Hyperion briefcase and start showering yours truly with all that sweet {AngryB}screw you {HappyC}money?":
    "{HappyC}那么，领结书呆子，{HappyB}我们什么时候打开那个 亥博龙手提箱，开始往*本人*身上撒那堆甜甜的{AngryB}去你的{HappyC}钱？",
 "[confidential][actually enthused, under breath] I DO believe in Vault Keys, I DO believe in Vault Keys...":
    "[confidential][actually enthused, under breath] 我*确实*相信秘藏钥匙，我*确实*相信秘藏钥匙……",
 "{WorryA}Oh.  Right.": "{WorryA}哦。对。",
 "Unlock Lock #1": "打开 1 号锁",
 "Unlock Lock #2": "打开 2 号锁",
 "Unlock Lock #3": "打开 3 号锁",
 "Unlock Lock #4": "打开 4 号锁",
 "No problem-o, friend-o!  I keep the key behind the Handsome Jack billboard.  Just reach through the hole  near the bottom.":
    "没问题，朋友！钥匙我放在帅杰克广告牌后面。从底部附近的洞伸手进去就行。",
 "{SlyC}Whoah.  Vaughn, you should check this out.  There's a miasma of swirling alien energies up in this thing!":
    "{SlyC}哇。沃恩，你该看看这个。这东西里面有一团翻涌的外星能量瘴气！",
 "{ThinkA}I can't really tell.": "{ThinkA}我看不太出来。",
 "{SternA}Yes, that sounds awesome.   [pointed]  Any cracks or flaws?":
    "{SternA}嗯，听着很棒。[pointed]  有裂纹或瑕疵吗？",
 "One down...[sad] umpteen to go.": "开了一个……[sad] 还剩无数个。",
 "Why's this case have so many keys, anyway?": "这柜子干嘛要这么多把钥匙？",
 "Showmanship!": "表演效果！",
 "My wrist's getting sore.": "我的手腕都酸了。",
 "Try hauling all this money around.": "你试试扛着这么多钱到处跑。",
 "[under breath... he thinks no one can hear him] Thanks, boss.":
    "[under breath... he thinks no one can hear him] 谢谢，老板。",
 "[playful][confidential to Shade] My friend sometimes talks to dead people.":
    "[playful][confidential to Shade] 我朋友有时候跟死人说话。",
 "Accountant 8th Class.": "八级会计。",
 "[confidential] On it.": "[confidential] 好。",
 "[confidential]  I dunno.   Cracks, leaks... you know, a bargaining tool.":
    "[confidential]  不知道。裂纹、漏液……你知道，谈判筹码。",
 "[towards Shade]  Mr. Shade...": "[towards Shade]  Shade 先生……",
 "Hey Shade, do you mind if I take this out of the case?  The glass is messing with the scanner.":
    "嘿 Shade，我把它从柜子里拿出来行吗？玻璃干扰扫描仪。",
 "[a little projected] I dunno, flash him your badge!": "[a little projected] 不知道，把你的证件亮给他看！",
 "[projected a little] I guess he forgot... [less projected]that he's set up a million dollar deal... with Hyperion.":
    "[projected a little] 我猜他忘了……[less projected]他安排了一笔百万美元的交易……跟 亥博龙。",
 "Hoyah.": "吼呀。",
 "[annoyed]  You're early!": "[annoyed]  你们早到了！",
 "Hey, friend, you need help finding the display case key?  It's behind the Handsome Jack billboard.":
    "嘿，朋友，需要帮忙找展示柜的钥匙吗？就在帅杰克广告牌后面。",
 "Hey Rhys.  I've almost got this wrapped up.  Let's pop open the display case so we can get a closer look at the Vault Key.":
    "嘿 瑞斯。我这儿快搞定了。我们打开展示柜，仔细看看那把秘藏钥匙。",
 "[to himself] Whoah.": "[to himself] 哇。",
 "Um...": "呃……",
 "Hey!  Did you just loot a valuable item from my property like a common Vault Hunter?":
    "嘿！你刚才是像个普通秘藏猎人一样从我这儿顺走了一件值钱东西吗？",
 "Stay on target, Rhys.": "专注目标，瑞斯。",
 "Nice.": "不错。",
 "Eh, I'll just tack it on to the price of the Vault Key.": "呃，我就把它加进秘藏钥匙的价钱里。",
 "Everything okay over there?": "那边一切还好吗？",
 "Is that the seller?": "那就是卖家？",
 "[a little sarcastic] Could you knock on the door already?  I'm getting a little... anxious.":
    "[a little sarcastic] 你能不能赶紧敲门？我有点……着急了。",
 "Time's a'wasting, man.": "时间不等人，老兄。",
 "Need a little help with the ol' door-knocking thing?":
    "需要帮忙搞定敲门这档子事吗？",
 "He's expecting someone from Hyperion, right?": "他在等 亥博龙的人，对吧？",
 "Hyperion engagement protocol 37 - Produce Hyperion ID to initiate contact.":
    "亥博龙交战条例第 37 条——出示 亥博龙证件以启动接触。",
 "You DID bring your ID, didn't you?": "你*带*证件了吧？",
 "The anticipation is killing me.  Just not quickly enough.":
    "这期待感快把我折磨死了。只是死得不够快。",
 "All this waiting is making me queasy again, man.": "这么等下去我又想吐了，老兄。",
 "Hey, mister-": "嘿，先生——",
 "Oh.": "哦。",
 "My first Pandoran corpse.": "我在 潘多拉 的第一具尸体。",
 "Knock": "敲门",
 "Flash ID": "亮证件",
 "[cofnidential]  Just go.": "[cofnidential]  去吧。",
 "[confidential] Just go!": "[confidential] 去吧！",
 "[confidential][sarcastic] {body-CarryCase}Actually, I was thinking of engaging him in a spirited debate about the formatting of programmer comments.":
    "[confidential][sarcastic] {body-CarryCase}其实，我正想跟他热烈辩论一下程序员注释的格式问题。",
 "[confidential] [defensive] Hey! Proper indentation is important!":
    "[confidential] [defensive] 嘿！正确的缩进很重要！",
 "[to himself] {SmugC}Vasquez is gonna be so pissed.": "[to himself] {SmugC}Vasquez 会气疯的。",
 "[under breath] {WorryB}Sorry about this, boss.": "[under breath] {WorryB}抱歉了，老板。",
 "Hey mister -": "嘿，先生——",
 "[mild reaction] Agh!": "[mild reaction] 啊！",
 "{SmugB}You have no idea.": "{SmugB}你根本想不到。",
 "Billboard": "广告牌",
 "Reach Under": "伸手到下面",
 "That was a warning shot!  Next time I aim for the pants!":
    "那是警告射击！下次我瞄准裤子！",
 "{ShockB}Nah.  I'm good.": "{ShockB}不用。我没事。",
 "{body-carrycase}{ShockA}Are we gonna talk about{WorryC} how you almost just died?{WorryB}":
    "{body-carrycase}{ShockA}我们要不要聊聊你{WorryC}差点死掉那件事？{WorryB}",
 "...weird, we used to be so UN-whackjob...": "……怪了，我们以前可一点都不疯……",
 "You are really bad at this.": "你这方面真差。",
 "By \"rogue,\" I mean I'm knocking on the door now.": "我说的“自己上”，是指我现在去敲门。",
 "How rich?": "多富？",
 "This rich!": "这么富！",
 "[pickup1]I am equipped with extra-long vibrating pistons  for versatile thrusting movements. [ominous pause] Use of lubrication...DENIED.":
    "[pickup1]我配备了超长振动活塞，可进行多种方式的推顶动作。[ominous pause] 使用润滑……拒绝。",
 "It may have looks like a rotten slab of wood, but it was a DOOR to me!":
    "它看起来也许只是块腐烂的木板，但对我来说它曾是*一扇门*！",
 "[confidentuial] {SlyC}There'll be plenty of time for dicking around {SlyB}AFTER we're running Hyperion.":
    "[confidentuial] {SlyC}等我们掌管了 亥博龙，{SlyB}再有的是时间瞎搞。",
 "[whispering]  {WorryB}What kind of sicko are we dealing with here?":
    "[whispering]  {WorryB}我们这是在跟什么变态打交道？",
 "[whispering] {SternB} Good point.": "[whispering] {SternB} 有道理。",
 "[whispering][jocular]{WorryB} I don't know... but we're not exactly occupying the moral high ground here.":
    "[whispering][jocular]{WorryB} 我不知道……但我们也算不上占据道德高地。",
 "A hundred bucks?": "一百块？",
 "{SternD}Honestly, how much will it cost to make you shut up about the door?":
    "{SternD}说真的，要花多少钱才能让你别再不提那扇门？",
 "Yes, it's getting old.": "是啊，听腻了。",
 "Tell me about it... I can practically FEEL it undressing me with its eyes.":
    "还用你说……我几乎能*感觉*到它用眼睛在扒我衣服。",
 "[not getting it] Do you like it?  We had to go through like 20 takes to get it right!":
    "[not getting it] 你喜欢吗？我们拍了差不多二十遍才拍好！",
 "[under breath] Loose cannon, baby.": "[under breath] 失控大炮，宝贝。",
 "[confidential] {WorryB}I thought you were gonna guide me in!  {AngryC}What, did a wandering mage hit you with a Spell of Silence? You probably can't answer that...":
    "[confidential] {WorryB}我以为你会指引我！{AngryC}怎么，有个流浪法师给你下了沉默术？你大概也答不了这个……",
 "[confidential]  {SmugC}I was encouraging you to strike out on your own.":
    "[confidential]  {SmugC}我是在鼓励你独闯一番。",
 "[confidential] {SmugC}Yep.": "[confidential] {SmugC}对。",
 "[confidential]  {SternC}Well, next time, y'know, give a guy some {AngryB}warning before ya push him out of the nest.":
    "[confidential]  {SternC}好吧，下次，你知道，把人推出巢之前给点{AngryB}预告。",
 "{SmugB}Two hundred bucks?": "{SmugB}两百块？",
 "{SternB}Vaughn, give the man two hundred bucks.": "{SternB}沃恩，给这位两百块。",
 "[surly] {THinkB}Sure.": "[surly] {THinkB}好。",
 "[reading]\"I wish I were big.\"": "[reading]“我希望我很大。”",
 "[to himself] I'm already big...": "[to himself] 我已经很大了……",
 "[badly impersonating Handsome Jack] Hey there, Handsome Jack here!  I'm dead now, but my insatiable lust for power lives on at Shade's World of Curiosities!":
    "[badly impersonating Handsome Jack] 你好啊，我是帅杰克！我现在死了，但我那永不满足的权力欲仍在 Shade 的奇珍世界里活着！",
 "[badly impersonating Handsome Jack](As Handsome Jack) Hey, kids, it's your old pal Handsome Jack here!  I'm Pandora's greatest monster, but everyone loves me because I'm so darned snarky!":
    "[badly impersonating Handsome Jack]（以帅杰克的口吻）嘿，孩子们，是你老朋友帅杰克！我是 潘多拉 最伟大的怪物，但大家都爱我，因为我嘴皮子实在太溜了！",
 "[badly impersonating Jack](As Handsome Jack) Hey, friends, Handsome Jack here!  Worship me as a god, or I'll unleash my butt stallions!":
    "[badly impersonating Jack]（以帅杰克的口吻）嘿，朋友们，我是帅杰克！把我当神拜，不然我就放出我的屁股战马！",
 "[badly impersonating Handsome Jack](As Handsome Jack) Hey there, Handsome Jack here!  I'm dead now, but my insatiable lust for power lives on at Shade's World of Curiosities!":
    "[badly impersonating Handsome Jack]（以帅杰克的口吻）你好啊，我是帅杰克！我现在死了，但我那永不满足的权力欲仍在 Shade 的奇珍世界里活着！",
 "[to himself] {WorryC}Monster?": "[to himself] {WorryC}怪物？",
 "[to himself] [defensive] {WorryA}I LIKED the butt stallion.":
    "[to himself] [defensive] {WorryA}我*喜欢*那匹屁股战马。",
 "Vault Key": "秘藏钥匙",
 "I choose doors.": "我选门。",
 "[inside v-o hissed] They're early!": "[inside v-o hissed] 他们早到了！",
 "Well, he's nuts.": "好吧，他是个疯子。",
 "Of course, I guess we could just skip the lube and jam the Loader Bot though his door.":
    "当然，我想我们也可以省掉润滑，直接把装载机器人硬塞进他门里。",
 "Yeah, looks like.": "是啊，看来是这样。",
 "So, what's the play?  {SmugC} Show him the money?  {SlyA}That usually lubricates friendships.":
    "那怎么演？{SmugC} 给他看钱？{SlyA}那通常能润滑一下交情。",
 "You hear that?  WE'RE COMIN' IN DRY!": "听到了吗？我们干着进来了！",
 "[slightly projected]  {SmugA}Oh hey, why don't you examine it with that freaky cyber-eye you're always yakking about?":
    "[slightly projected]  {SmugA}哦嘿，你干嘛不用你老吹的那只诡异电子眼检查一下？",
 "[to himself] A box like that just begs to be opened.": "[to himself] 那样的箱子就是求人打开。",
 "[to himself]  [contemplative] Money.  I LIKE money.":
    "[to himself]  [contemplative] 钱。我*喜欢*钱。",
 "[confidential][stunned]  I'll never call you a cake again.":
    "[confidential][stunned]  我再也不会叫你软柿子了。",
 "Careful!  The Stinging Singing Cactii have a beaufitul voice, but a shocking contempt for their audience!":
    "小心！会蜇人的歌唱仙人掌有副美妙的嗓子，但对听众抱着惊人的鄙夷！",
 "[to himself] Weird.": "[to himself] 怪。",
 "[short shock sound]": "[short shock sound]",
 "[starts background of a song... Mike has an idea]":
    "[starts background of a song... Mike has an idea]",
 "I know what you're thinking... how'd Moxxi get away with a white wedding?":
    "我知道你在想什么……莫西 怎么穿得进白色婚纱？",
 "[appreciative]  Hmmm.": "[appreciative]  嗯。",
 "[badly impersonating Moxxi](As Moxxi) Hey sugar, I'm Moxxi, and I'm the sexiest sexpot in Pandora!":
    "[badly impersonating Moxxi]（以 莫西 的口吻）嘿，甜心，我是 莫西，潘多拉 上最性感的尤物！",
 "[badly impersonating Moxxi]  Right now you're staring longingly at my very first wedding dress, worn when I walked down the aisle with Jimbo Hodunk!  Well, I walked... he just kind of rolled.":
    "[badly impersonating Moxxi]  现在你正痴痴地盯着我人生第一件婚纱，那是我跟 Jimbo Hodunk 走进婚礼殿堂时穿的！嗯，是我走……他只是滚过来。",
 "[badly impersonating Moxxi](As Moxxi) If you keep poking me like that, I'm gonna have to charge extra.":
    "[badly impersonating Moxxi]（以 莫西 的口吻）你要是一直那样戳我，我可要加钱了。",
 "Mad Moxxi's Wedding Dress!": "疯婆 莫西 的婚纱！",
 "The Stinging Singing Cactus!": "会蜇人的歌唱仙人掌！",
 "Nice gun, though.": "不过枪不错。",
 "Nice gun.": "枪不错。",
 "Isn't it?  It's totes valuable.  [wistful] Grandpa Penumbra gave it to me just before he died.":
    "是吧？它超值钱。[wistful] Penumbra 爷爷在他死前给我的。",
 "How'd he die?": "他怎么死的？",
 "Somebody shot him.  It was horrible!": "有人开枪打死了他。太可怕了！",
 "Look At": "查看",
 "Poke": "戳",
 "Talk": "交谈",
 "Look Through": "透过看",
 "Dead Body": "尸体",
 "Gate": "大门",
 "Sign": "招牌",
 "Dead Guy": "死人",
 "Weird Guy": "怪人",
 "Loot": "搜刮",
 "[still somewhat angry] {AngryB}But, of course, you don't care about any of that, do you?  {AngryA}You came down here for the the coup de grace, the piece de resistance, the thing that's gonna make me rich, the one, the only, the Vault Key!":
    "[still somewhat angry] {AngryB}但当然，你们对那一切都不在意，对吧？{AngryA}你们下来是为了压轴大戏、镇馆之宝，那个将要让我发财的、独一无二的秘藏钥匙！",
 "I will pay you<ui_cash_dollar: -15><ui_cash_2: -15><ui_cash_0: -15><ui_cash_0: -15> to shut up about your door.":
    "我付你<ui_cash_dollar: -15><ui_cash_2: -15><ui_cash_0: -15><ui_cash_0: -15>让你别再提你那扇门。",
})

# —— 事后复盘（Rhys 与 Vaughn）+ 名人之厅 ——
T.update({
 "[bitter; big breath] Okay.[beat] That sucked.": "[bitter; big breath] 好。[beat] 那太糟了。",
 "I mean, I don't ever wanna see someone's brains come out of their nose, not ever again, not even if it's the weekend.":
    "我是说，我再也不想看到谁的脑浆从鼻子里流出来，再也不想，就算是周末也不行。",
 "Nothing's worth getting killed over.": "没什么值得拿命去换。",
 "The key's not worth getting killed over.": "那把钥匙不值得拿命去换。",
 "It was a little fun...": "还挺好玩的……",
 "Wow, okay, no. It didn't. At all.": "哇，好吧，不。一点都不好玩。",
 "C'mon... it was a little fun. Right?": "拜托……还算是有点好玩吧。对吧？",
 "You cannot honestly stand there and tell me that it didn't feel kind of great to kick all those guys' asses.":
    "你不能站在那儿老实告诉我，把那些家伙全部揍趴下一点都不过瘾。",
 "Let's just do this.": "我们把这事办了吧。",
 "Let's just get this over with so we can go home.": "我们把这事了结，好回家。",
 "No kidding, it sucked.": "没开玩笑，是糟透了。",
 "[tired] Just... it happened, and it's done, and we're fine, okay? Cope faster.":
    "[tired] 就……它发生了，已经结束了，我们没事，行吗？快点适应。",
 "Oh, I'm sorry, is my trying to cope with watching you turn a bunch of bandits inside out disturbing you?":
    "哦，抱歉，我尝试消化看着你把一群土匪翻个里朝外这件事，是不是打扰到你了？",
 "[annoyed] Yeah, no kidding, it sucked. I'm so glad I have you here to narrate.":
    "[annoyed] 是啊，没开玩笑，糟透了。真高兴有你在旁边解说。",
 "Why are we doing this?": "我们干嘛要做这个？",
 "Yeah, but, why are we doing this for Vasquez?": "是啊，但，我们干嘛要替 Vasquez 干这个？",
 "You know why.": "你知道为什么。",
 "The guy is an overpaid comptroller, alright?": "那家伙是个拿钱太多的审计主管，行吗？",
 "Janie told me that his last three projects failed.": "Janie 跟我说他前三个项目都失败了。",
 "He needs us way more than we need him.": "他需要我们远多过我们需要他。",
 "He'd kill us if we didn't.": "我们不干他就会杀了我们。",
 "I know it happened, like, six hours ago, but do you remember the corpse floating outside his office?":
    "我知道那是大概六小时前的事，但你记得他办公室外面飘着的那具尸体吗？",
 "If we get the key, none of it will matter.": "只要拿到钥匙，那些都不重要了。",
 "What do you think's gonna happen if we don't come through?":
    "你觉得我们要是不办成会怎样？",
 "We're all gonna get rich.": "我们都会发财。",
 "After this, you're gonna be able to go to any star system, any world, just point and say, \"I wanna buy that guy and make him dance for me when I'm bored.\"":
    "这事之后，你能去任何星系、任何世界，随手一指说“我想买下那家伙，无聊时让他给我跳舞”。",
 "[uncaring] Oh am I?": "[uncaring] 哦，是吗？",
 "You're gonna be richer than God.": "你会比上帝还有钱。",
 "We'll be heroes to Hyperion.": "我们会成为 亥博龙的英雄。",
 "Why do you think we're doing this? We're gonna be heroes when we get back, we'll have saved the entire company.":
    "你以为我们干嘛做这个？回去之后我们就是英雄，我们救了整个公司。",
 "Just listen a second.": "你先听我说一句。",
 "He doesn't deserve it.[beat] We should keep the key for ourselves.":
    "他不配。[beat] 我们该把钥匙留下自己用。",
 "And even if he's not planning to screw us... he didn't tell us what we were getting into, so...":
    "就算他没打算坑我们……他也没告诉我们我们会遇到什么，所以……",
 "Vasquez is not gonna share the reward with us. I've seen this movie too many times. There's no way.":
    "Vasquez 不会跟我们分享回报的。这种戏我看过太多次了。绝不可能。",
 "Those weren't psychos.": "那些不是疯子。",
 "Think about what this plan is. We come down here to Pandora, we almost get turned into soup by psychos...":
    "你想想这计划是什么。我们下来到 潘多拉，差点被疯子们煮成汤……",
 "Like I give a crap what species of hobo that was.":
    "我才不在乎那是什么品种的流浪汉。",
 "And why would he share the credit?": "而且他为什么要分功劳？",
 "It just doesn't make sense.": "这根本说不通。",
 "You know?": "你知道吗？",
 "Well let's screw him.": "那我们就坑他。",
 "We're already risking our necks for this.": "我们已经在为这事冒着脖子上的风险了。",
 "Well... we can always screw him before he screws us.":
    "这个……我们总可以在他坑我们之前先坑他。",
 "He's gonna share the money!": "他会分钱的！",
 "Sell it! Start a bidding war! Partner up with a Goddamn Vault Hunter! I don't know, use your imagination.":
    "卖掉它！搞一场竞标战！跟一个他妈秘藏猎人合作！我不知道，动动你的脑子。",
 "He's gonna share the money, Vaughn.": "他会分钱的，沃恩。",
 "What are you getting at...": "你想说什么……",
 "Vaughn.": "沃恩。",
 "[annoyed] Okay, are you doing the thing where you're cataloguing old girlfriends or something?":
    "[annoyed] 好，你是不是又在列旧女友清单还是什么？",
 "Stick with me here.": "你听我说。",
 "I'm being serious. I'm using my serious face.": "我是认真的。我正摆着我这张严肃脸。",
 "Let's keep the key.": "我们把钥匙留下。",
 "[hopeful] Right?": "[hopeful] 对吧？",
 "Yeah, let's do it.": "对，我们干。",
 "Whatever, I feel good.": "随便，我感觉很好。",
 "This is like a moment, you know? Like... I'm getting clarity. Like this is something we're gonna remember.":
    "这就像是个时刻，你知道吗？就像……我突然想通了。就像这是我们会记住的事。",
 "Or we're getting nuked in ten minutes because Vasquez mic'ed the money.":
    "或者十分钟后我们就被核平了，因为 Vasquez 在钱上装了窃听器。",
 "If today wasn't interesting enough...[beat] Let's do it.":
    "要是今天还不够刺激……[beat] 我们干。",
 "Let's stick to the plan.": "我们按计划来。",
 "We should really stick with the plan.": "我们真的该按计划来。",
 "Look, Vasquez made the deal, and this way everybody comes out on top, no grudges, no enemies, no Hyperion death squadrons, no worries.":
    "听着，交易是 Vasquez 定下的，这样做大家都受益，没怨恨、没敌人、没有 亥博龙死亡中队、没烦恼。",
 "I'm getting tired of just always sight-seeing.": "我厌倦了总是观光。",
 "[softly] What do I always say?[beat] Metaphors are dumb.":
    "[softly] 我总说的一句话是什么？[beat] 比喻很蠢。",
 "I would, but...": "我愿意，但是……",
 "You know I would, but...[trails off]": "你知道我愿意，但是……[trails off]",
 "But what?": "但是什么？",
 "Too scared to get even richer?": "太害怕变得更富有？",
 "What's the problem?": "有什么问题？",
 "Vasquez is too dangerous.": "Vasquez 太危险了。",
 "When he realizes... I mean, you can forget about bandits, Vasquez would turn us into Christmas ornaments before he let us just walk away with a Vault Key.":
    "等他意识到……我是说，土匪就别提了，Vasquez 在让我们带着秘藏钥匙走人之前，会先把我们做成圣诞装饰。",
 "It's an unneccessary risk.": "这是没必要的风险。",
 "It's just an unnecessary risk. If we do this, now, like we planned, we're all gonna do well.":
    "这只是没必要冒的风险。要是我们照计划现在就动手，大家都有好日子过。",
 "Why mess with that?": "干嘛要搅乱它？",
 "I want to run Hyperion.": "我想掌管 亥博龙。",
 "I don't wanna Vault Hunt or whatever, I wanna run Hyperion.":
    "我不想当什么秘藏猎人，我想掌管 亥博龙。",
 "And we actually have a chance to if we bring this key back to them.":
    "只要我们把钥匙带回去，我们就真有机会。",
 "Nothin, you got nothin' for me?": "什么，你对我没什么要说的？",
 "Alright, fine, be a giant puss the rest of your life and always get pounded by everyone else.":
    "好吧，行，那你这辈子就当个怂包，永远被别人吊打。",
 "[sighs] Yeah, I know how it sounded.": "[sighs] 是啊，我知道那听着什么样。",
 "Alright, let's just find this guy, August, buy the key and get the Hell out of here.":
    "好，我们去找那个叫 August 的家伙，买下钥匙，然后赶紧滚出这儿。",
 "Should I be taking your stoned silence as a yes... maybe?":
    "我把你这呆滞的沉默当成同意……也许？",
 "Alright, fine, be a giant puss the rest of your life and get screwed by everyone else.":
    "好吧，行，那你这辈子就当个怂包，被别人坑到底。",
 "No...? Are you having a flashback?": "不是……？你是不是又在闪回？",
 "Yeah, I know how it sounded.": "是啊，我知道那听着什么样。",
 "\"Screw that guy,\" remember?": "“坑那家伙”，记得吗？",
 "\"We're gonna get paid,\" remember?": "“我们会拿到钱”，记得吗？",
 "Let's be \"pretty awesome\" right now.": "我们现在就“牛气一把”。",
 "Our time will come, relax.": "我们的机会会来的，放松。",
 "I mean, I thought bandits were like cowboys or whatever.":
    "我是说，我以为土匪就是牛仔什么的。",
 "[out of breath] If you had told me... if you had told me any of that... was even possible down here...":
    "[out of breath] 要是你告诉过我……要是你告诉过我这些……在这下面居然可能发生……",
 "Man.": "天哪。",
 "C'mon, what are you getting at, spit it out.": "拜托，你想说什么，直说。",
 "Of course he does! He's lied already! He didn't tell us about any of this crud before we got here!":
    "他当然会！他已经撒过谎了！我们到这儿之前他根本没提过这些破事！",
 "Here's what I'm thinking.[beat] We keep the key.":
    "我是这么想的。[beat] 我们把钥匙留下。",
 "We keep the key, we use or sell it or whatever, and we go and buy a moon and live on that moon's beach and sip drinks that have little umbrellas in them until we die very old men of living too well.":
    "我们留下钥匙，自己用或者卖掉随便，然后去买一颗月亮，住在它的海滩上，喝着小伞插着的饮料，直到我们变成活得太过舒服的老头才死去。",
 "[chuckling]": "[chuckling]",
 "C'mon.": "拜托。",
 "And Vasquez can go bang his fourteen year old hookers or whatever useless functionaries do.":
    "而 Vasquez 可以去嫖他那十四岁的妓女，或者随便那些没用的官僚干什么。",
 "[light laughter]": "[light laughter]",
 "For crying out loud, the guy killed somebody before we left, a guy who does something like that has no reason to lie.":
    "老天爷啊，我们出发前那家伙就杀过人，干过这种事的人没理由撒谎。",
 "\"He says with a shaking determination...\"": "“他颤抖着坚定地说……”",
 "But you just said--[gets cut off]": "但你刚说——[gets cut off]",
 "Yeah, I know what I said.": "是啊，我知道我说了什么。",
 "He's got something in his pocket.": "他口袋里有什么东西。",
 "[grossed out] So we're picking dead men's pockets now?":
    "[grossed out] 所以我们现在要掏死人的口袋了？",
 "Wait...what are you doing?": "等等……你在干什么？",
 "What? He doesn't need it.": "怎么？他用不着了。",
 "Maybe he's just happy to see us.": "也许他只是见到我们很高兴。",
 "Listen, we're here to make a deal, alright? We're buying a... thing. Something valuable.":
    "听着，我们是来做交易的，行吗？我们要买一件……东西。很值钱的东西。",
 "We're looking for a man named August.[beat] We're supposed to meet him here.":
    "我们在找一个叫 August 的人。[beat] 我们该在这儿跟他碰头。",
 "Uh, we're here to meet August.  You know him?": "呃，我们是来见 August 的。你认识他？",
 "Yeah, yeah vomit, shit, I get it.": "是啊是啊，呕吐、大便，我懂了。",
 "[to August] who are these two bozos?": "[to August] 这两个傻瓜是谁？",
 "Alright then, what's your name, Slick?": "那好，你叫什么名字，滑头？",
 "It's locked.": "锁着。",
 "[annoyed] C'mon, are you serious?": "[annoyed] 拜托，你认真的？",
 "This feels like we came in the back... maybe there's a front door somewhere?":
    "这感觉像是我们从后面进来的……也许哪儿有扇前门？",
 "Yeah, I don't know if we can get to it with the flying freak squadron taking a crap everywhere...":
    "是啊，我不知道能不能过去，那支飞行怪胎小队到处拉屎……",
 "Well maybe there's a key or something and we just missed it.":
    "也许有把钥匙什么的，我们只是没看到。",
 "[muttering to himself] Wow, if we just randomly found the key, wouldn't that be amazing?":
    "[muttering to himself] 哇，要是我们随便就找到了钥匙，那岂不是太棒了？",
 "I mean, I never wanna see somebody's brains come out of their nose, not ever again...":
    "我是说，我再也不想看到谁的脑浆从鼻子里流出来，再也不想……",
 "How are you?": "你好吗？",
 "Hi!": "嗨！",
 "[being startled] Yaaah!": "[being startled] 呀啊！",
 "[being startled] Ahghgh!": "[being startled] 啊呃呃！",
 "Wait, wasn't there--[gets cut off]": "等等，不是有——[gets cut off]",
 "Are you two not just the handsomest devils I've seen in ages.":
    "你们俩真是我这么久以来见过最俊的小伙子。",
 "[pissed] Not great!": "[pissed] 不太好！",
 "[flustered] Asshole!": "[flustered] 混蛋！",
 "[angry] Yeah! Man![beat] What do you think you're doing?":
    "[angry] 是啊！老兄！[beat] 你以为你在干什么？",
 "[sighs] Okay, what is going on, who are you?": "[sighs] 好，到底怎么回事，你是谁？",
 "I am Shade.": "我是 Shade。",
 "Thanks!": "谢谢！",
 "I'm Shade, and this... is my World of Curiosities!":
    "我是 Shade，这里……就是我的奇珍世界！",
 "[flustered] What--what is this, is this part of the-- is like some kind of ride or something?":
    "[flustered] 什——这是什么，这是那个——是某种游乐项目之类的吗？",
 "Time can take a toll, you know. And on more things than one![light, sad laughter]":
    "时间会留下痕迹，你知道。而且不止体现在一件事物上！[light, sad laughter]",
 "But, um, unfortunately we are closed for renovations.":
    "但是，呃，很遗憾我们在装修歇业。",
 "[laughs] Dead? No! No, no, no, no, asleep, maybe, dead, that's-- you're getting ahead of yourself.":
    "[laughs] 死了？不！不不不不，是睡着了，也许，死了，那——你想太多了。",
 "[exasperated] Why are you pretending to be dead! Why!":
    "[exasperated] 你干嘛要装死！为什么！",
 "And I mean thanks because this is supposed to be an experience, it's supposed to be-- you know, it's supposed to have an effect.":
    "我是说谢谢，因为这本来就该是种体验，本该——你知道，本该有效果的。",
 "And let me tell you right off the very bat that I am deeply sorry that you strapping young threshers of gentlemen here have to witness it in such sad disrepair.":
    "我一开始就得说，我非常抱歉让你们这两位健壮的年轻绅士看到它如此破败的样子。",
 "You're already here, we can just hang out!": "你们既然来了，我们就一起玩玩嘛！",
 "I mean, we can do other things.": "我是说，我们也可以干点别的。",
 "But that doesn't mean you have to leave, of course, oh no.":
    "但那当然不代表你们得走，哦不。",
 "Don't do that!": "别那样！",
 "[being hit]Ah! Okay, okay, okay, I'm sorry, I didn't mean to scare you guys![laughing a little]":
    "[being hit]啊！好，好，好，对不起，我不是故意吓你们的！[laughing a little]",
 "It just... it just happened, you know, things happen, they happen.":
    "它就……它就是发生了，你知道，事情会发生，它们就是会发生。",
 "Since the moment we've walked in, it's been just been one big freaky puppet show, so--[gets cut off]":
    "从我们进门那一刻起，就一直是场大怪诞木偶戏，所以——[gets cut off]",
 "I wasn't paying attention.": "我没注意听。",
 "I thought it was interesting.": "我觉得挺有意思的。",
 "I can't wait to get out of here.": "我迫不及待想离开这儿。",
 "Look, Shade, or whatever, stop wasting our time. We're not here to see your weird zoo of death.":
    "听着，Shade，或者随便你叫什么，别浪费我们时间了。我们不是来看你这怪异死亡动物园的。",
 "\"Wasting time.\"[beat] \"No time to waste,\" \"Act now,\" \"Buy fast,\" \"We're digi-structing your future.\"":
    "“浪费时间。”[beat] “别浪费时间”、“立即行动”、“快点买”、“我们正在数码构造你的未来”。",
 "You're [stressing each syllable]Hyperion.[beat] Right? Here for August?":
    "你们是[stressing each syllable]亥博龙。[beat] 对吧？来找 August 的？",
 "You've never heard that before?": "你没听过那句话？",
 "And so you are here for August. Right?": "所以你们是来找 August 的。对吧？",
 "Yeah, we're Hyperion.": "对，我们是 亥博龙。",
 "Yeah, if you wanna buy something strange and illegal, this is the certainly the place to do it!":
    "是啊，你要买奇怪又非法的东西，这儿绝对是对的地方！",
 "I know a lot of things about a lot of things, and this thing in particular.":
    "我对很多事情都懂很多，尤其是这件事。",
 "Well... right this way, gentlemen, right this way.":
    "那么……这边请，先生们，这边请。",
 "You know anything about that?": "你知道那是什么吗？",
 "Oh, sure! Why didn't you say so? You're late, actually.":
    "哦，当然！你怎么不早说？其实你们迟到了。",
 "Yeah, we know.": "是啊，我们知道。",
 "I think it's really a triumph, though, I do.": "不过我觉得那真是一大成功，真的。",
 "Or something like that.": "或者差不多那样。",
 "And I mean that poetically, I don't mean that it has a lot of characters in it.":
    "我是从诗意的角度说的，不是说它里面有很多角色。",
 "Though it works that way, too.": "不过那样说也行。",
 "[happy] Oh, sure thing!": "[happy] 哦，当然！",
 "I wasn't really paying attention to him, anyway.": "反正我也没怎么注意他。",
 "Yeah, sure.": "是啊，当然。",
 "You interrupted him.": "你打断他了。",
 "I'm sure our, uh, illustrious guests here are tired of hearing this crap, am I right?":
    "我敢说我们这两位，呃，尊贵的客人已经听腻这些废话了，对吧？",
 "It was interesting, once, okay, I admit it, but once is enough.":
    "它有一次是挺有意思的，行，我承认，但一次就够了。",
 "On and on and on and on.": "没完没了没完没了。",
 "Every time I come here.": "我每次来这儿都这样。",
 "Well that's okay, we're all kidders here, we kid like friends do.":
    "没关系，我们这儿都是开玩笑的人，我们像朋友一样开玩笑。",
 "Thank you, Shade.": "谢谢你，Shade。",
 "Actually, I thought it was kind of interesting.": "其实，我觉得还挺有意思的。",
 "Well, it is interesting, it's very interesting, the carnal history of a bygone--[gets cut off]":
    "这个，它确实有意思，非常有意思，一个逝去时代的肉欲史——[gets cut off]",
 "Oh, well, forgive me Mr. Friggin' Manners, but when you've heard the same Goddamned story twelve times, then you can scold me on being impolite.":
    "哦，那抱歉了，礼貌先生，等你把同一个该死的故听了十二遍，你再来训我没礼貌吧。",
 "It's rude to interrupt somebody.": "打断别人是不礼貌的。",
 "Okay, but it was interesting once?": "好，但它是不是有一次挺有意思的？",
 "Where is he?": "他在哪儿？",
 "I figured.": "我就知道。",
 "August.[beat] Like the month.": "August。[beat] 像那个月份。",
 "Kind of.": "算吧。",
 "It's close enough.": "差不多够了。",
 "So let's start again: my name's August, what's yours.":
    "那我们重新开始：我叫 August，你呢。",
 "It's not a gift. I'm buying it.": "这不是礼物。我是买。",
 "Aren't I?": "不是吗？",
 "Aren't I trying?": "我没在努力吗？",
 "It's right here.": "就在这儿。",
 "Equal footing.": "地位平等。",
 "[coughing fit]": "[coughing fit]",
 "Are you alright?": "你没事吧？",
 "Yeah. I'm fine.": "嗯。我没事。",
 "We've seen stuff that make this look like a pile of crap.":
    "我们见过的东西能让这个看起来像一坨屎。",
 "[weirded out] What? I'm not.[to Rhys] I'm not![back to her] I'm not looking at you.":
    "[weirded out] 什么？我没有。[to Rhys] 我没有！[back to her] 我没在看你。",
 "[cold] Why do you keep looking at me.": "[cold] 你为什么一直看我。",
 "This guy has been lookin' at me like I'm a damn pork chop from the minute he walked in.":
    "这家伙从进门那一刻起就一直盯着我，像我是块该死的猪排。",
 "I can feel his brain undressing me.": "我能感觉到他的脑子在扒我衣服。",
 "Are you gonna do something about this or do I have to?":
    "这事你要不要管，还是得我自己来？",
 "Vaughn, stop it!": "沃恩，别这样！",
 "He's not looking at you.": "他没在看你。",
 "Ease off, psycho.": "放松点，神经病。",
 "I'm sorry, he really doesn't mean... like half the things he says.":
    "抱歉，他真的不是那个意思……他说的有一半都不能当真。",
 "Cause there's lots of ways.": "因为有很多种方式。",
 "Everybody's got a preference.": "每个人都有偏好。",
 "I've done it all ways, sideways, frontways.": "各种方式我都试过，侧着、正着。",
 "Calm your girl.": "让你女朋友冷静。",
 "Ummm, we... buy the key now...": "呃，我们……现在买钥匙……",
 "[unsure] Uh huh.": "[unsure] 嗯哼。",
 "Yeah...": "是啊……",
 "Makes sense.": "有道理。",
 "Recently refurbished.": "最近翻新过。",
 "You're my problem, that's what my problem is!": "你就是我的问题，这就是我的问题！",
 "No, you're trying something, something's not right!":
    "不，你在搞鬼，有什么不对劲！",
 "Sasha. C'mon.": "萨莎。别这样。",
 "Oh, c'mon!": "哦，拜托！",
 "Your current balance is now -- negative -- seven hundred and fifty thousand dollars. Thank you for using Hyperion bank services.":
    "您当前的余额现为——负——七十五万美元。感谢您使用 亥博龙银行服务。",
 "Your account has been automatically deducted -- seven hundred and fifty -- thousand dollars -- for the damage to company property -- one -- loader bot.":
    "您的账户已被自动扣除——七十五万——美元——用于赔偿公司财产损失——一台——装载机器人。",
 "Looks like a, uh, looks kinda like a technical with legs. Right? The armored plates?":
    "看起来像个，呃，像个长了腿的武装车。对吧？那些装甲板？",
 "[uncaring] Sure.": "[uncaring] 行。",
 "[reading] \"A common rakk. An active, strident and social creature. Particularly territorial during breeding season.\"":
    "[reading] “常见的拉卡。一种活跃、聒噪且群居的生物。繁殖季尤其具有领地意识。”",
 "What's not to like.": "有什么理由不喜欢呢。",
 "[wary] Or is he just happy to see us.": "[wary] 还是他只是见到我们很高兴。",
 "I... think he has something in his pocket.": "我……觉得他口袋里有什么东西。",
 "Ugh, there's gotta be some kind of... rule about stealing from a dead guy.":
    "呃，偷死人的东西总该有……什么规矩吧。",
 "There is, but I don't think his estate will complain.":
    "有，但我认为他的遗产继承人不会抱怨。",
 "[nervous] Nice fellow, huh.": "[nervous] 真是个好人，哈。",
 "[processed: speaker] Bewm, not to be confused with his brother Boom, was the first mate of Captain Flynt.":
    "[processed: speaker] 比姆，别跟他的兄弟布姆搞混，曾是弗林特船长的副手。",
 "[processed: speaker] As his name subtly implies, Bewm enjoyed hurling caustic explosives and making things blow up by any means necessary.":
    "[processed: speaker] 正如他的名字隐晦地暗示的那样，比姆喜欢投掷腐蚀性炸药，并用一切手段把东西炸掉。",
 "I was wondering why he didn't come to the company picnic...":
    "我还在纳闷他怎么没来公司野餐……",
 "[processed: speaker] Killed by stairs.": "[processed: speaker] 死于楼梯。",
 "[processed: speaker] Formerly a scientific researcher who worked for Hyperion, Professor Nakayama was obsessed with cloning Handsome Jack, who he carried a certain fondness for.":
    "[processed: speaker] 曾任 亥博龙科学研究员的 Nakayama 教授痴迷于克隆帅杰克，对他怀有某种偏爱。",
 "Oh, I remember this guy...": "哦，我记得这家伙……",
 "[processed: speaker] Not in the least bit insane. He will be missed.":
    "[processed: speaker] 一点也不疯。我们会想念他。",
 "[processed: speaker] Pandoran resident and fine dining connoisseur, Shade was held in high esteem by his fellow neighbors in Oasis.":
    "[processed: speaker] 作为 潘多拉 居民和美食鉴赏家，Shade 在绿洲镇的邻里间备受敬重。",
 "[getting nervous] I am really not into this at all.":
    "[getting nervous] 我真的一点都不喜欢这个。",
 "Can we just get on with this.": "我们能快点办完吗。",
 "[processed: speaker] Snappy dresser. Not a good sense of humor.":
    "[processed: speaker] 衣着讲究。幽默感不行。",
 "[processed: speaker] The cruel and enigmatic \"Sheriff\" of Lynchwood, she dated Handsome Jack before getting somewhat deservedly shot to death by Vault Hunters.":
    "[processed: speaker] 林奇伍德那位残忍而莫测的“警长”，她曾与帅杰克交往，后来被秘藏猎人开枪打死，多少算是罪有应得。",
 "[not wanting to] There's no where else to go. Let's just get through it.":
    "[not wanting to] 没别的地方可去了。我们就走过去吧。",
 "Alright, you know, the stuffed animals was one thing, but this is taking a turn that I really don't want it to.":
    "好吧，你知道，那些填充动物就算了，但这正朝着我很不想去的方向转。",
 "[big sigh]": "[big sigh]",
 "[processed: speaker] Right this way to the world famous Hall of Pandoran Luminaries.":
    "[processed: speaker] 这边请，前往世界闻名的 潘多拉 名人之厅。",
 "[processed: speaker] Come face to face with icons of the planet's turbulant history... and hear how each met their grisly fate.":
    "[processed: speaker] 与这颗星球动荡历史中的标志性人物面对面……听听他们各自如何迎来惨死的结局。",
 "[processed: speaker] Please, watch your step and[processed: dying tape deck] marvel at some of the unexpected ends of life's grand design.":
    "[processed: speaker] 请小心脚下，并[processed: dying tape deck] 惊叹于生命宏伟设计中那些出人意料的终点。",
 "[unnerved] Huh.": "[unnerved] 嗯。",
 "[quietly to himself] Some of this stuff is... interesting I guess.":
    "[quietly to himself] 这里面有些东西……我想还挺有意思的。",
 "Not a great place for a first date, right?": "首次约会来这儿可不太妙，对吧？",
 "Where is this guy, anyway?": "这家伙到底在哪儿？",
 "Why, of all places, did we have to meet up here?": "为什么非得在这种地方碰头？",
 "I'm startin' to get a little itchy.": "我开始有点坐不住了。",
})

# —— 尾声：复盘叙述收尾 ——
T.update({
 "[coughing] Alright, alright! Mission accomplished!": "[coughing] 好，好！任务完成！",
 "[reluctantly]Okay fine, but let me start at the beginning...":
    "[reluctantly]好，行，但让我从头说起……",
 "[postpax] I assume you'd have that kinda scratch as walkaround money.":
    "[postpax] 我想你应该会带那么多现钱当零花吧。",
 "[postpax] You Hyperion guys are usually so punctual.":
    "[postpax] 你们 亥博龙的人平时可守时了。",
 "[postpax] Gettin' 10 million together can't be too much trouble for you guys.":
    "[postpax] 凑一千万对你们来说应该不算太难吧。",
 "[postpax]I figured you'd want to take the tour, maybe get here a little early.":
    "[postpax]我以为你会想参观一下，所以早到一点。",
 "You want my name? My name's Ten Million Dollars for all you should care. You're a Vault Key to me,  'kay, that's it.":
    "你想要我的名字？在你眼里我叫一千万美金就行。对我来说你就是一把秘藏钥匙，行吧，就这样。",
 "[postpax] The kind that are hard to break.": "[postpax] 那种很难打断的。",
 "[postpax] Cash only for this deal.": "[postpax] 这单只收现金。",
 "[postpax] And I hope you brought big bills.": "[postpax] 希望你带的是大额钞票。",
 "Show him the money Vaughn.": "给他看钱，沃恩。",
 "[postpax] What's the problem?": "[postpax] 有什么问题？",
 "[postpax] No problem.": "[postpax] 没问题。",
 "[postpax] Show him the money, Vaughn.": "[postpax] 给他看钱，沃恩。",
 "[postpax] [frustrated] Maybe this'll give you some incentive to hurry it up.":
    "[postpax] [frustrated] 也许这能给你点动力快点。",
 "[postpax] Okay... Uh, sorry... all the passwords on this thing.":
    "[postpax] 好……呃，抱歉……这玩意儿上全是密码。",
 "[postpax] It's not a problem. It's a security thing, just give him a second.":
    "[postpax] 不是问题。这是安全设置，给他一秒钟。",
 "[postpax] [half joking] How about 9 million?": "[postpax] [half joking] 九百万怎么样？",
 "[postpax] [in stride] [laughs] Yeah right. How about, no. You Hyperion guys are always pushin' it.":
    "[postpax] [in stride] [laughs] 是哦。不行。你们 亥博龙的人老爱得寸进尺。",
 "[postpax] What's wrong with my face?": "[postpax] 我这张脸怎么了？",
 "[postpax] He's hiding something, August.": "[postpax] 他在隐瞒什么，August。",
 "[postpax] You can't trust a face like that.": "[postpax] 那种脸不能信。",
 "[postpax] I mean look at that guy. Look at his face.":
    "[postpax] 我是说看看那家伙。看看他那张脸。",
 "We're not Hyperion assholes.": "我们不是 亥博龙那帮混蛋。",
 "[postpax] [calm, soothing] {worryA}Hey, Sasha? Sasha, listen to me.":
    "[postpax] [calm, soothing] {worryA}嘿，萨莎？萨莎，听我说。",
 "[postpax] What's wrong with his face?": "[postpax] 他那张脸怎么了？",
 "[postpax] [calm, soothing]{sternA} Listen, whatever you think about my face aside, we are not the bad guys. {sada}I know Hyperion is awful people, but we need that key, to get back at one of those awful people...{angryA} So, pleeeeease... please trust us.":
    "[postpax] [calm, soothing]{sternA} 听着，先别管你对我的脸怎么看，我们不是坏人。{sada}我知道 亥博龙都是些烂人，但我们需要那把钥匙去坑他们中的一个……{angryA} 所以，求求你了……请相信我们。",
 "Please trust me.": "请相信我。",
 "You're making a big mistake.": "你在犯一个大错。",
 "[postpax]{smugA} I know you don't trust Hyperion.":
    "[postpax]{smugA} 我知道你不信 亥博龙。",
 "[postpax]{angryB} Yeah, ya think?": "[postpax]{angryB} 是啊，你说呢？",
 "[postpax] And I know you have zero reason to trust us... but I'm telling you... {sada}we are not like those assholes. In fact, we're trying get back at one of the worst assholes up there and we need that key to do it. {happyA}So please, take the money, and let us screw over one of the biggest jerks on Hyperion. Please.":
    "[postpax] 我也知道你没有理由信任我们……但我跟你说……{sada}我们跟那些混蛋不一样。其实我们正打算收拾上面最混蛋的一个，为此我们需要那把钥匙。{happyA}所以求你了，钱你拿走，让我们去坑 亥博龙上最欠揍的那个。求你。",
 "[postpax] I'm asking you to please trust me on this one.":
    "[postpax] 我请你在这件事上相信我一次。",
 "[postpax] {smugA}You're making a big mistake. This money we're offering... {slyA}is life changing... and it's right here.":
    "[postpax] {smugA}你在犯一个大错。我们出的这笔钱……{slyA}能改变人生……而且就在这儿。",
 "[postpax] Awesome. Let's do this.": "[postpax] 太好了。我们开始吧。",
 "[postpax] So you're sayin' this key will get used to screw over some wretched Hyperion stooge?":
    "[postpax] 所以你是说，这把钥匙会被用来坑某个可悲的 亥博龙走狗？",
 "[postpax] [calm, almost chipper] Alright, I'm sold.":
    "[postpax] [calm, almost chipper] 好吧，我被说服了。",
 "[postpax] That's exactly what we're saying.": "[postpax] 这正是我们要说的。",
 "[postpax] August, everything's fine now.": "[postpax] August，现在一切都好了。",
 "[postpax] No, no. It's okay. The feeling's gone, August. Let's do the deal.":
    "[postpax] 不，不。没事。那种感觉没了，August。我们做交易吧。",
 "[postpax] No, no no, I was wrong. We should definitely do it.":
    "[postpax] 不，不不，我错了。我们肯定该做。",
 "[postpax] The feeling's gone! The feeling's gone!":
    "[postpax] 那种感觉没了！那种感觉没了！",
 "[postpax] The bad feeling is gone, August. She said so herself. We still got a deal here. There's no problem, let's just-":
    "[postpax] 那种不好的感觉没了，August。她自己说的。我们这交易还在。没问题，我们就——",
 "[postpax] Hon, we're here, we should just do this. Really.":
    "[postpax] 亲爱的，我们都到这儿了，就把这事办了吧。真的。",
 "[postpax] Nah, I made up my mind.": "[postpax] 不，我决定了。",
 "[postpax] We're good here. Everyone relax. We just want to buy the key from August and go.":
    "[postpax] 我们没事。大家都放松。我们只是想从 August 那儿买下钥匙然后走。",
 "[postpax] Yeah, yeah... she's just freaking out... she does that sometimes.":
    "[postpax] 是啊，是啊……她只是吓着了……她有时这样。",
 "[postpax] Is she okay?": "[postpax] 她没事吧？",
 "Wait, wait, wait... how is that the most important thing? Did you forget the part about it all being your fault?!":
    "等等等等……那怎么就成了最重要的事？你忘了这一切都怪你那一部分了吗？！",
 "Oh come on, that was not my fault... not all of it.":
    "哦拜托，那不是我的错……不全是。",
 "[postpax]  [alt] Guess I figured...": "[postpax]  [alt] 我想着……",
 "[postpax]  [alt] with a deal this big...": "[postpax]  [alt] 这么大的交易……",
 "[postpax]  [alt] he'd show up in person.": "[postpax]  [alt] 他会亲自露面。",
 "[postpax] [whispered] Hey, be sure to use the Echo Eye on the key.":
    "[postpax] [whispered] 嘿，记得用 ECHO 眼扫一下钥匙。",
 "[postpax] [whispered] It might give us some info to go on. Help figure out which Vault it opens.":
    "[postpax] [whispered] 也许能给我们点线索，帮我们弄清它能打开哪个秘藏。",
 "[postpax] [whispered] It's times like these that make me glad I paid for these echo implants.":
    "[postpax] [whispered] 就是这种时候让我庆幸自己花钱装了这些 ECHO 植入体。",
 "[postpax] [whispered] I don't know if times like these come up enough to be worth 6 months of salary.":
    "[postpax] [whispered] 我不知道这种时候出现得够不够频繁，值不值半年薪水。",
 "[postpax] It was 4 months, okay?": "[postpax] 是四个月，行吗？",
 "[postpax] [whispered] And I knew one of the surgeons so, you know, I got a friend discount.":
    "[postpax] [whispered] 而且我认识其中一个外科医生，你知道，拿了个朋友价。",
 "[postpax] [whispered] [bullshit] What? No you did not. I filed all the paperwork for the-":
    "[postpax] [whispered] [bullshit] 什么？你才没有。那些文件全是我填的——",
 "[postpax] [whispered] It doesn't matter! All I'm saying is I'm glad I did it!":
    "[postpax] [whispered] 无所谓！我只是说我很庆幸我装了！",
 "[postpax] [whispered] Right, well, me too...": "[postpax] [whispered] 是啊，这个，我也是……",
 "[postpax] [whispered] Thank you! That's all I wanted.":
    "[postpax] [whispered] 谢谢！我就想听这句。",
 "[postpax] Are you making a face under there? I can't tell what you're thinking if-":
    "[postpax] 你在那底下做鬼脸吗？你要是——我就看不出你在想什么了——",
 "[pickup5] And what would that be?": "[pickup5] 那会是什么？",
 "[postpax] [coughing] And I'm not lying, okay. I'm... embellishing. And how the hell would you know anyway? You weren't at the deal.":
    "[postpax] [coughing] 而且我没撒谎，行吗。我只是……添油加醋。再说你他妈怎么会知道？你又不在交易现场。",
 "[postpax] Of course I was, ya dope. I can't believe you still haven't figured that out. I knew you were dense the moment I-":
    "[postpax] 我当然在，你这蠢货。我简直不敢相信你到现在还没想明白。我从——那一刻就知道你脑子慢。",
})

# —— 收尾补漏（带表情标签的变体等） ——
T.update({
 "We got the money, don't worry.": "钱我们有，别担心。",
 "That Bandit... ganglord guy made his big stupid entrance.":
    "那个土匪……帮派头子搞了他那套蠢兮兮的大登场。",
 "[angry] {AngryC}You broke my door!": "[angry] {AngryC}你砸了我的门！",
 "{HappyA}Ah, the arched eyebrow of a skeptic! But here, {thinkingB}prepare to gawk in amazement as your athletically-inclined {happyA}associate throws this ordinary souvenir pen at the {happyCX}fantastic Wedge of Mystery!":
    "{HappyA}啊，怀疑者挑起的那道眉毛！但来，{thinkingB}准备惊掉下巴吧，你那运动能力出众的{happyA}同伴要拿这支普通的纪念笔扔向{HappyCX}神奇的神秘楔石！",
 "I sense your skepticism.": "我能感觉到你的怀疑。",
 "{FearB}Careful there, sport.  The Wedge doesn't like to be touched by living things.  [to himself] {ThinkingA}Learned THAT the hard way.":
    "{FearB}小心点，小伙子。楔石不喜欢被活物碰。[to himself] {ThinkingA}这我可是*吃过大亏*才学到的。",
 "Transfer of ownsership, non-disclosure agreements, that sort of thing.":
    "所有权转让、保密协议，那一类东西。",
 "Corpse": "尸体",
 "{HappyB}Still {HappyC}is, actually, {FearA}cause he's definitely {FearB}not dead! {ThinkB}But the place itself...[gets cut off]":
    "{HappyB}其实还{HappyC}开着，{FearA}因为他绝对{FearB}没死！{ThinkB}但这地方本身……[gets cut off]",
 "{HappyA}My {HappyB}grandpappy, he's the {NeutralA}one who came up with this place.":
    "{HappyA}我{HappyB}爷爷，这地方就是{NeutralA}他搞出来的。",
 "{HappyA}He was a {ThinkA}real thinker, {HappyA}you know, a {ThinkA}real {ThinkB}lover of {HappyA}animals...":
    "{HappyA}他是个{ThinkA}真正的思想者，{HappyA}你知道，一个{ThinkA}真正{ThinkB}热爱{HappyA}动物的人……",
 "{SmugB}{body-sitB}I've been {SternA}waitin' here since {SternB}this morning.":
    "{SmugB}{body-sitB}我从{SternA}今天早上就在这儿{SternB}等了。",
 "{SternB}And I {AngryA}know a {AngryB}prick like Vasquez {SlyA}can get an extra {SmugB}five hundred g's {SmugA}without sweatin' it, {SternA}so...":
    "{SternB}而且我{AngryA}知道像 Vasquez 这种{AngryB}混蛋{SlyA}不用眨眼就能多拿出{SmugB}五十万，{SmugA}所以……",
 "{SternB}What was the hold up?": "{SternB}磨蹭什么呢？",
 "{AngryA}Yeah, where's {AngryB}Vasquez?": "{AngryA}是啊，{AngryB}Vasquez 呢？",
 "{SternC}Don't tell me to {SternB}shut up.": "{SternC}别叫我{SternB}闭嘴。",
 "{SlyC}Relax.": "{SlyC}冷静点。",
 "[getting angry] {angryB}You {AngryC}relax.": "[getting angry] {angryB}你{AngryC}才冷静。",
 "[stern] {sternA}{body-sitB}Honey, {SternC}shut up.": "[stern] {sternA}{body-sitB}亲爱的，{SternC}闭嘴。",
 "{HappyA}You have one, {SmugC}right?": "{HappyA}你有名字吧，{SmugC}对吧？",
 "{SmugA}{body-sitB}Just so we're on, {SmugB}uh, {HappyA}equal footing.":
    "{SmugA}{body-sitB}只是为了让，{SmugB}呃，{HappyA}我们地位平等。",
 "{sternC}You're {RageB}trying.": "{sternC}你{RageB}在努力。",
 "{AngryA}So let's all get friendly {SmugB}real fast. {SadB}I mean, {ShockB}I'm trying. {SadC}Aren't I trying? Huh? Aren't I trying?":
    "{AngryA}那我们就快点{SmugB}熟络起来吧。{SadB}我是说，{ShockB}我在努力。{SadC}我没在努力吗？啊？我没在努力吗？",
 "{NeutralB}So... {SternA}let's try {ShockC}again. {HappyA}My name's {HappyB}August. {SternA}What's {SternB}yours.":
    "{NeutralB}那……{SternA}我们{SternC}再试一次。{HappyA}我叫{HappyB}August。{SternA}你{SternB}呢。",
 "{NeutralB}So... {SternA}let's try {ShockC}again. {HappyA}My name's {HappyB}August. {SternA}What's {SternB}yours?":
    "{NeutralB}那……{SternA}我们{SternC}再试一次。{HappyA}我叫{HappyB}August。{SternA}你{SternB}呢？",
 "{SternC}Yeah!": "{SternC}对！",
 "{SlyA}So let's all get friendly {SmugB}real fast. {SadB}I mean, {ShockB}I'm trying. {SadC}Aren't I trying? Huh? Aren't I trying?":
    "{SlyA}那我们就快点{SmugB}熟络起来吧。{SadB}我是说，{ShockB}我在努力。{SadC}我没在努力吗？啊？我没在努力吗？",
 "{angryA}{body-sitB}Do {SlyC}you want me to {SmugA}guess?":
    "{angryA}{body-sitB}你{SlyC}想让我{SmugA}猜吗？",
 "This is just a business transaction.": "这只是一笔商业交易。",
 "{SmugA}{body-sitB}No, we don't have to be {AngryB}buddies, {SternB}dickhead. But it'd {ThinkB}just make me a heck of a lot more comfortable {NeutralB}to know {ShockD}just who {SmugB}I'm gifting this Vault Key to.":
    "{SmugA}{body-sitB}不，我们不必当{AngryB}兄弟，{SternB}混蛋。但{ThinkB}知道{ShockD}我把这把秘藏钥匙{SmugB}送给谁，会让我{NeutralB}舒服很多。",
 "{ThinkA}This is a business {thinkB}transaction, we don't have to be {SternB}buddies.":
    "{ThinkA}这是一笔商业{thinkB}交易，我们不必当{SternB}兄弟。",
 "{SlyC}You can pout all you {HappyA}want. You're not getting {HappyB}my name.":
    "{SlyC}你爱闹脾气就{HappyA}闹。你别想知道{HappyB}我的名字。",
 "{ThinkB}Isn't that what I said?": "{ThinkB}我不是这么说的吗？",
 "{SternC}It doesn't {AngryA}matter what our names our. {AngryB}We're Hyperion, {SlyB}sent here on authority of {SlyC}Vasquez.":
    "{SternC}我们叫什么{AngryA}不重要。{AngryB}我们是 亥博龙的人，{SlyB}受{SlyC}Vasquez 之命来这儿。",
 "So {AngryA}let's skip all the yakkety-yak {AngryB}and get to it.":
    "所以{AngryA}别废话了，{AngryB}直接谈正事。",
 "{HappyA}Yeah, no, no, no, Hugo {HappyB}told us to tell you that we, {FearB}that he was {SlyA}Vasquez. As a joke, you know?":
    "{HappyA}是啊，不不不，Hugo{HappyB}让我们告诉你，我们，{FearB}他才是{SlyA}Vasquez。开玩笑的，你知道？",
 "[laughing to himself] {HappyA}Because.... he's so... {SmugB}so obviously not him.[beat] {FearA}Right?":
    "[laughing to himself] {HappyA}因为……他……{SmugB}他显然根本不是他。[beat] {FearA}对吧？",
 "{SmugB}{body-sitB}Yeah?": "{SmugB}{body-sitB}是吗？",
 "{sternA}Well... I guess... as long as {ThinkB}you got the money... {SmugC}one Hyperion bootlicker's as good as another.":
    "{sternA}这个……我想……只要{ThinkB}你有钱……{SmugC}一个 亥博龙舔靴子的跟另一个也没什么两样。",
 "{SmugA}But we're here to {SlyC}close this out for him.":
    "{SmugA}但我们是来{SlyC}替他敲定这事的。",
 "You're just early.": "你们只是早到了。",
 "Bandits almost killed us!": "土匪差点杀了我们！",
 "{SlyB}{body-sitB}I know we said {SlyC}originally it was gonna be five hundred thousand...":
    "{SlyB}{body-sitB}我知道我们{SlyC}一开始说的是五十万……",
 "{HappyA}You understand.": "{HappyA}你懂的。",
 "{SmugA}But I talked it over with my {SmugC}people.":
    "{SmugA}但我跟我的{SmugC}人商量过了。",
 "{happya}{body-sitB}You ever see {HappyB}anything so pretty in {SmugA}your miserable {SmugC}lives?":
    "{happya}{body-sitB}你们{SmugA}这辈子{SmugC}见过{HappyB}这么漂亮的东西吗？",
 "{SmugC}{body-sitB}This thing'll {SlyB}practically {SlyC}dance at your wedding.":
    "{SmugC}{body-sitB}这东西{SlyB}几乎能在{SlyC}你婚礼上跳舞。",
 "I'd use it {ShockB}myself, {ShockD}but... {SternB}you know... the {ThinkB}monsters and all.":
    "我本想{ShockB}自己用，{ShockD}但……{SternB}你知道……{ThinkB}怪物什么的。",
 "It's {SlyC}state of the art {SmugA}alien crap.": "这是{SlyC}最先进的{SmugA}外星破烂。",
 "[really agitated] {AngryA}Look, {AngryB}you said when {FearA}I started to get a {FearB}feeling about {ShockB}something {InquireB}that I should tell you {SternB}and that we should walk away, {ShockB}right?":
    "[really agitated] {AngryA}听着，{AngryB}你说过当我{ FearA}开始对{ShockB}某件事有{FearB}预感时，{InquireB}就该告诉你，{SternB}我们就该走人，{ShockB}对吧？",
 "[getting agitated] {WorryA}IIIIII... {WorryB}I just don't like it. {WorryBX}I got a- I {WorryC}got a feeling.":
    "[getting agitated] {WorryA}我我我我……{WorryB}我就是不喜欢。{WorryBX}我有——我有{WorryC}种预感。",
 "{SternC}Wait.": "{SternC}等等。",
 "{SadC}What?": "{SadC}什么？",
 "{ShockD}What {ThinkB}feeling?": "{ShockD}什么{ThinkB}预感？",
 "We're {AngryA}almost done!": "我们{AngryA}就快成了！",
 "{angryA}{body-sitB}What are you possibly {shockD}feeling {ThinkB}right now?":
    "{angryA}{body-sitB}你现在{shockD}能有什么{ThinkB}预感？",
 "{shockA}I get {ShockB}intuitions about {angryB}this stuff!":
    "{shockA}我对{angryB}这种事有{ShockB}直觉！",
 "Everyone relax.": "大家都放松。",
 "{SternA}{body-sitB}Yeah, he just wants {SternB}to buy a key {NeutralB}from me.":
    "{SternA}{body-sitB}是啊，他只是想{SternB}从我这儿{NeutralB}买把钥匙。",
 "{happyA}{body-sitA}Listen, honey, {HappyB}we're good guys, okay? {SlyC}Relax. We just {SmugA}wanna buy a key from your boyfriend.":
    "{happyA}{body-sitA}听着，亲爱的，{HappyB}我们是好人，行吗？{SlyC}放松。我们只是想{SmugA}从你男朋友那儿买把钥匙。",
 "Is she okay?": "她没事吧？",
 "{ThinkB}{body-sitB}I think {SternB}you need to {AngryB}watch your {SternA}mouth.":
    "{ThinkB}{body-sitB}我觉得{SternB}你该{AngryB}管好你的{SternA}嘴。",
 "{SmugA}{body-sitA}I think your girlfriend {SmugB}needs to {SternB}calm the eff down.":
    "{SmugA}{body-sitA}我觉得你女朋友{SmugB}需要{SternB}冷静一下。",
 "Let's just wrap this up.": "我们把这事收个尾吧。",
 "[postpax]{AngryA}{body-sitA} Let's just, {FearA}uh, {SmugB}wrap this up, alright? {SternA}We saw it, {SternB}we like it, what {ThinkB}more is there to talk about?":
    "[postpax]{AngryA}{body-sitA} 我们就，{FearA}呃，{SmugB}把这事收个尾，行吗？{SternA}我们看过了，{SternB}我们喜欢，还有什么{ThinkB}好谈的？",
 "{FearA}{body-sitB}Don't {SternA}worry about it. {ThinkB}She-- {ThinkA}she gets this way, {WorryA}it's no problem.":
    "{FearA}{body-sitB}别{SternA}担心。{ThinkB}她——{ThinkA}她就这样，{WorryA}没问题的。",
 "[tentative] {SlyB}Can we, {WorryB}uh,{WorryA} take the key and {AngryA}you take... {HappyB}our money?":
    "[tentative] {SlyB}我们能，{WorryB}呃，{WorryA}拿走钥匙，{AngryA}你拿走……{HappyB}我们的钱吗？",
 "{AngryA}{body-sitB}Intuitions? {ShockB}What are you, a {AngryB}Goddamned {AngryC}fortune teller?":
    "{AngryA}{body-sitB}直觉？{ShockB}你是什么，{AngryB}他妈{AngryC}算命的？",
 "It's goddamned gorgeous.": "这他妈太美了。",
 "[quietly] {ThinkB}{body-sitA}It's goddamned gorgeous.":
    "[quietly] {ThinkB}{body-sitA}这他妈太美了。",
 "{happyA}{body-sitB}Friggin' A {SlyC}right, it is.": "{happyA}{body-sitB}他妈的{SlyC}没错，就是这样。",
 "Meh. It's no big deal.": "啧。没什么大不了的。",
 "{ThinkB}{body-sitA}It's, {SmugB}ehhh...": "{ThinkB}{body-sitA}这个，{SmugB}呃……",
 "[unbelieving] {SlyA}{body-sitB}Sure, {SlyC}okay.": "[unbelieving] {SlyA}{body-sitB}行吧，{SlyC}好吧。",
 "{SmugB}I mean, {WorryB}don't get me wrong, {SmugA}for a Vault Key it's {SlyC}fine... {ThinkB}but you {SternA}gotta remember, {SlyA}we're from Hyperion, mmkay?[beat] {HappyA}Soooo.....":
    "{SmugB}我是说，{WorryB}别误会，{SmugA}作为秘藏钥匙它{SlyC}还行……{ThinkB}但你{SternA}得记住，{SlyA}我们可是 亥博龙的人，懂吧？[beat] {HappyA}所以……",
 "It's not worth 10 million.": "它不值一千万。",
 "{sternA}{body-sitb}Shut {SternB}up.": "{sternA}{body-sitb}闭{SternB}嘴。",
 "{SchemeC}Like you {SmugB}could ever get {SmugA}with this.":
    "{SchemeC}好像你{SmugB}能配得上{SmugA}这个似的。",
 "{slyA}{body-sitA}I think I {SlyB}prefer your girlfriend. {SlyC}Or maybe she just prefers {SmugC}me.":
    "{slyA}{body-sitA}我想我{SlyB}更喜欢你女朋友。{SlyC}或者也许她更喜欢{SmugC}我。",
 "{WorryA}Rhys, {AngryA}for the love {AngryB}of--[gets cut off]":
    "{WorryA}瑞斯，{AngryA}天哪{AngryB}——[gets cut off]",
 "Quit {AngryB}it with the jokes and the {FearC}ladi-friggin-da, {RageA}'I'm a charming {SternB}asshole' routine, or you're {ThinkB}gonna figure out real quick what it's like to {AngryA}screw up planetside, {SternB}okay?":
    "别{AngryB}再开玩笑、摆那副{FearC}他妈的{RageA}'我是个迷人{SternB}混蛋'的架子，不然你{ThinkB}很快就会知道在地面上{AngryA}搞砸是什么滋味，{SternB}行吗？",
 "{AngryA}{body-sitB}And {SternB}you are {NeutralB}flicking my {SternC}last synapse.":
    "{AngryA}{body-sitB}而你{SternB}正在{NeutralB}弹我{SternC}最后一根神经。",
 "{ShockC}No, {WorryB}that's what it is, {SlyB}just a joke, {HappyC}that's it, he means {SlyA}no disrespect. (He's kind of a jerk).":
    "{ShockC}不，{WorryB}就是这样，{SlyB}就是个玩笑，{HappyC}仅此而已，他没有{SlyA}不敬的意思。（他是有点混蛋。）",
 "{SternA}{body-sitB}And you're {ThinkB}lucky I'm going to {AngryA}take that as a very {sternB}mistimed, very {SternC}stupid joke.":
    "{SternA}{body-sitB}你很{ThinkB}走运，我就当{AngryA}那是句时机极差、极其{SternB}愚蠢的{SternC}玩笑。",
 "[quietly]{ShockC} It's better than I {HappyC}imagined.": "[quietly]{ShockC} 比我{HappyC}预想的还好。",
 "Don't worry about the money.": "别担心钱的事。",
 "[very frazzled] {ShockB}And this guy, {angryA}he will {angryB}not stop checking me out!":
    "[very frazzled] {ShockB}还有这家伙，{angryA}他{angryB}一直盯着我看不停！",
 "{ShockA}Sasha, {ShockC}nobody's {ThinkB}looking at you!":
    "{ShockA}萨莎，{ShockC}没人{ThinkB}在看你！",
 "[very frazzled] {RageA}I can, like, {WorryDX}feel his {WorryD}brain {AngryA}undressing me!":
    "[very frazzled] {RageA}我简直能{WorryDX}感觉到他的{WorryD}脑子{AngryA}在扒我衣服！",
 "{ShockA}Really?[beat] That's {ShockC}it?": "{ShockA}真的？[beat] 就这样{ShockC}？",
 "{ThinkB}We're {WorryA}good?": "{ThinkB}我们{WorryA}没事了？",
 "{AngryA}Whatever, {AngryB}I don't care, do {AngryC}whatever you want.":
    "{AngryA}随便，{AngryB}我不管，{AngryC}你爱干嘛干嘛。",
 "{ShockD}I dunno, {ThinkB}maybe today's not right for this.":
    "{ShockD}不知道，{ThinkB}也许今天不适合做这个。",
 "{worryA}If {WorryB}things are weird.": "{worryA}要是{WorryB}事情不对劲。",
 "If {ThinkB}you have a {WorryC}feeling about things...":
    "要是{ThinkB}你对事情有{WorryC}预感……",
 "{sternA}No, {SadA}really, {SternC}I don't care.":
    "{sternA}不，{SadA}真的，{SternC}我不管。",
 "{SadA}Maybe another {SternA}time, fellas.": "{SadA}也许改天吧，{SternA}伙计们。",
 "[quietly] \"What if... what if I had won?\"": "[quietly] “要是……要是我赢了会怎么样？”",
 "[crying] {WorryC}Just take it. Take it, {sadC}please, take the key, take Sasha, take it all, it's yours, please.":
    "[crying] {WorryC}就拿去吧。拿去，{sadC}求你，把钥匙拿去，把 萨莎 拿去，全都拿去，都是你的，求你。",
 "[crying] {WorryC}Just take it, take it, {SadC}it's- {ShockD}I can't even- {WorryC}just take it, please!":
    "[crying] {WorryC}就拿去，拿去，{SadC}它——{ShockD}我都——{WorryC}就拿去，求你！",
 "{SlyA}Looks like he had{SlyB}... a change of heart.":
    "{SlyA}看来他{SlyB}……改变主意了。",
 "[in intense pain] Yeah, that's what I thou- GAHHHughhh...!":
    "[in intense pain] 是啊，我就是这么想的——啊啊啊啊……！",
 "[getting angry] {smugA}Oh, {WorryB}c'mon, {ThinkB} really? Because of what {SlyC}she said? There's no {SmugA}problem, let's just...[gets cut off]":
    "[getting angry] {smugA}哦，{WorryB}拜托，{ThinkB}真的？因为她说的那些？{SmugA}没问题，我们就……[gets cut off]",
 "{ThinkB}What {SmugB}the hell is your problem? {sternA}We're trying to {SternB}make a deal, there's {AngryB}nothing going on!":
    "{ThinkB}你{SmugB}到底有什么毛病？{sternA}我们在谈{SternB}交易，{AngryB}什么都没发生！",
 "{WorryA}Alright, {SternA}please, let's just everyone {SternC}calm down. Everything's {SlyB}cool. We {SlyC}just want to get paid, {HappyB}right?":
    "{WorryA}好了，{SternA}拜托，大家都{SternC}冷静一下。一切{SlyB}都好。我们{SlyC}只是想拿到钱，{HappyB}对吧？",
 "{angryA}He {ShockA}hasn't. {ThinkB}Okay?": "{angryA}他{ShockA}没有。{ThinkB}行吗？",
 "{WorryC}I haven't been {ShockC}looking at you! {FearC}I haven't!":
    "{WorryC}我没在{ShockC}看你！{FearC}我没有！",
 "{ThinkB}{body-sitA}Get your girlfriend in {AngryA}line, August, {sternA}before she starts {SternB}making my partner {SternC}nervous.":
    "{ThinkB}{body-sitA}把你女朋友{AngryA}管好，August，{sternA}别让她开始{SternB}把我搭档搞得{SternC}紧张。",
 "[angry] {angryA}Just {AngryC}give us a second!": "[angry] {angryA}就{AngryC}给我们一秒钟！",
 "{WorryA}I haven't been {ShockC}looking at you! {FearC}I haven't!":
    "{WorryA}我没在{ShockC}看你！{FearC}我没有！",
 "{AngryA}He {ShockA}hasn't. {ThinkB}Okay?": "{AngryA}他{ShockA}没有。{ThinkB}行吗？",
 "{WorryA}[getting a little sheepish] Cause... cause, you know.[beat]":
    "{WorryA}[getting a little sheepish] 因为……因为，你知道。[beat]",
 "{InquireA}C'mon, Rhys, it's been a full year and you haven't figured this stuff out yet?":
    "{InquireA}得了吧，瑞斯，都整整一年了，你还没搞明白这些事？",
 "{SmugA} Whatever.": "{SmugA} 随便。",
 "{AngryA}No you weren't!": "{AngryA}你才没有！",
 "{AngryA}He's...[to Rhys] You're just very conveniently leaving out the most important part of this whole thing, alright?":
    "{AngryA}他……[to Rhys] 你只是很方便地略过了整件事里最重要的部分，行吗？",
 "{AngryA}[laughing] What? Give me a break, that's what- look, I'm the one talking here, I have talking rights.":
    "{AngryA}[laughing] 什么？饶了我吧，那是——听着，现在说话的是我，我有说话权。",
 "How would you know what happened?": "你怎么知道发生了什么？",
 "{SchemeA}[laughing disdainfully] That is not what happened, are you kidding me with this?":
    "{SchemeA}[laughing disdainfully] 事情不是那样的，你在跟我开玩笑吗？",
 "[sarcastic] Oh, this oughta be good.": "[sarcastic] 哦，这肯定精彩。",
 "{angryC}[while \"fighting\" someone] Let go! C'mon! I need... that... key!":
    "{angryC}[while \"fighting\" someone] 放手！拜托！我需要……那把……钥匙！",
 "{AngryA}[while \"fighting\" someone] It's mine, give it! Just-- what's your frickin' problem, man!":
    "{AngryA}[while \"fighting\" someone] 是我的，给我！就——你他妈有什么毛病，老兄！",
 "{sadA}[whining] C'mon, August, I, like, really need that key, man, just-- can't you cut me a break, here? Don't-- we have the money, c'mon, just give it!":
    "{sadA}[whining] 拜托，August，我，那个，真的很需要那把钥匙，老兄，就——你就不能通融一下吗？别——钱我们有，拜托，就给我吧！",
 "{SternA}The Vault Hunter showed up.": "{SternA}那个秘藏猎人出现了。",
 "The Psycho Ganglord barged in.": "那个疯子帮派头子闯了进来。",
 "{SternA}That psycho... ganglord guy made his big stupid entrance.":
    "{SternA}那个疯子……帮派头子搞了他那套蠢兮兮的大登场。",
 "{SternA}The Vault Key shattered.": "{SternA}秘藏钥匙碎了。",
 "It's...complicated...": "这事……很复杂……",
 "{SternA}It's, um, well... It's complicated.": "{SternA}这事，呃，这个……很复杂。",
 "No, first we see the key.": "不，先看钥匙。",
 "I am Vasquez.": "我是 Vasquez。",
 "You're dealing with me, now.": "现在你在跟我打交道。",
 "Vasquez is sick.": "Vasquez 病了。",
 "My name is Rhys.": "我叫 瑞斯。",
 "You don't need my name.": "你不需要知道我的名字。",
 "My name is \"Ten Million Dollars.\"": "我叫“一千万美金”。",
 "What the hell is your problem?": "你到底有什么毛病？",
 "Everybody calm down.": "大家都冷静。",
 "Get her in line, August.": "把她管好，August。",
 "I was there.": "我当时在场。",
 "[pickup2]If you walk away now then one day -- maybe ten years from now, maybe ten months, maybe ten minutes -- you're gonna look back on this moment and *scream* to the stars for the mercy of death [beat] just so you won't have to endure another day of nagging despair over what could have, would have, *should have* been.":
    "[pickup2]要是你现在走开，那么总有一天——也许是十年后，也许是十个月后，也许是十分钟后——你会回望此刻，对着群星*嘶吼*求死[beat] 只为不用再忍受一天那种“本可以、本应该”的念兹在兹的绝望。",
 "[pickup2] Are you going to *die* wondering what if I had seized my *one chance* by the throat, beaten the fear and doubt, and taken what was so rightfully mine?  Are you going to die asking yourself [beat, then quietly] What if... what if I had won?":
    "[pickup2] 你要*死*在“要是我当初一把掐住那*唯一的机会*、战胜恐惧与怀疑、拿回本该属于我的东西”的疑问里吗？你要死的时候还在问自己[beat, then quietly] 要是……要是我赢了会怎么样？",
 "[pickup2] That this is it!": "[pickup2] 就是这个！",
 "[pickup1]This is the moment you've been waiting for your whole life.  The moment you're about to let slip by [beat] forever..":
    "[pickup1]这就是你等了一辈子的时刻。你即将让它溜走[beat] 永远……",
 "[beat] I guess I could've.": "[beat] 我想我本来可以的。",
 "You guess? I've been baking in the sun with rakk's dive bombing me for the last--":
    "你想？我在太阳底下烤着，被拉卡俯冲轰炸了整整——",
 "Your turn Fiona.": "轮到你了，Fiona。",
 "[VO] What a steaming load of skag crap.": "[VO] 好一坨热气腾腾的异犬屎。",
 "Which is...?": "是什么……？",
 "Yeah, okay... I get it... [to Rhys] This fraud conveniently left out the most important part to this whole thing.":
    "是啊，好吧……我懂了……[to Rhys] 这个骗子很方便地略过了整件事里最重要的部分。",
 "You couldn't have asked me first? You kidnapped me hours ago.":
    "你就不能先问我一句？你几小时前就把我绑来了。",
 "Oh, shut up!": "哦，闭嘴！",
 "Well, that sucks, cause I'm trying to get it in your lying mouth!":
    "那你可惨了，因为我正想把它塞进你那张撒谎的嘴里！",
 "Well, well, look who decided to show her face. I was just about to get to my favorite part. You know  where you come in and you ruin my life you [louder] no class, scheming, Pandoran scum!":
    "哟，哟，看看谁舍得露面了。我正要讲到我最喜欢的部分。就是你出场把我人生毁掉那一段，你这[louder]没教养、满肚子算计的 潘多拉 渣滓！",
 "Stop it, stop it! You're getting dirt in my eye!": "住手，住手！你把土弄进我眼睛里了！",
 "Tell me your side of the deal.": "说说你那边的交易版本。",
 "My turn for what?": "轮到我做什么？",
 "It is a nice haircut!": "这发型是挺好看的！",
 "Oh, nice haircut you lying Hyperion jackass.": "哦，发型真好看啊，你这撒谎的 亥博龙蠢驴。",
 "[sarcastic] Go on?": "[sarcastic] 继续说？",
 "[sarcastic] I can't wait.": "[sarcastic] 我等不及了。",
})

# —— 最后补漏 ——
T.update({
 "{HappyA}Ah, the arched eyebrow of a skeptic! But here, {thinkingB}prepare to gawk in amazement as your athletically-inclined {happyA}associate throws this ordinary souvenir pen at the {HappyCX}fantastic Wedge of Mystery!":
    "{HappyA}啊，怀疑者挑起的那道眉毛！但来，{thinkingB}准备惊掉下巴吧，你那运动能力出众的{happyA}同伴要拿这支普通的纪念笔扔向{HappyCX}神奇的神秘楔石！",
 "{SternC}You're {RageB}trying.": "{SternC}你{RageB}在努力。",
 "[Show Money]": "[亮出钱]",
 "[Blow his mind]": "[震住他]",
 "[Break his heart]": "[伤他的心]",
})
