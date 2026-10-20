# 批次3-17：第1章 env_16_arenaunderground_rhys（地下：Rhys 与 Sasha 被困，接通通讯、启动升降台）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g'), ('ep1_env12_zh.py', '_h'), ('ep1_env01_zh.py', '_i'),
               ('ep1_env09_zh.py', '_j'), ('ep1_env06_zh.py', '_k'), ('ep1_env05_zh.py', '_l'),
               ('ep1_env03_zh.py', '_m'), ('ep1_env07_zh.py', '_n'), ('ep1_env17_zh.py', '_o'),
               ('ep1_env14_zh.py', '_p')):
    T.update(_load(_f, _n))

T.update({
 "RHYS": "RHYS",
 "SASHA": "SASHA",
 "VAUGHN": "VAUGHN",
 "FIONA": "FIONA",
 "SKAG": "SKAG",
 "PSYCHO": "PSYCHO",
 "PSYCHO 1": "PSYCHO 1",
 "BANDIT": "BANDIT",
 "BANDIT 1": "BANDIT 1",
 "BANDIT 2": "BANDIT 2",
 "BANDIT 3": "BANDIT 3",
 "BANDIT 4": "BANDIT 4",
 "BANDITBRO": "BANDITBRO",
 "ZER0": "ZER0",
 "ATLASCOMM": "ATLASCOMM",
 "HJAI": "HJAI",
 "CHORE; NOTE": "CHORE; NOTE",
 "SFS": "SFS",
 "Yelp": "嗷",
 "..." : "...",
 "<<ID": "<<ID",
 "{890B4CF2-2CF2-4DD9-A5E9-441D25CBB364}>>": "{890B4CF2-2CF2-4DD9-A5E9-441D25CBB364}>>",
 "{DFCCED66-2373-49E0-BE4F-B2244A9257E6}>>": "{DFCCED66-2373-49E0-BE4F-B2244A9257E6}>>",
 "{76DEDD39-D711-4865-8BA2-36ECA4CF6994}>>": "{76DEDD39-D711-4865-8BA2-36ECA4CF6994}>>",
 "{60B80856-051A-49F0-B8FC-E6ED93CE7EFB}>>": "{60B80856-051A-49F0-B8FC-E6ED93CE7EFB}>>",
})

# —— 开场：被困地下，与 Sasha 互相试探 ——
T.update({
 "[echo]{FearA}Hey Vaughn?[beat] Vaughn? Can you hear me?":
    "[echo]{FearA}嘿 沃恩？[beat] 沃恩？你能听到我吗？",
 "[echo]I can't get a signal.": "[echo]我收不到信号。",
 "[echo]Ow! [beat]What the hell are you doing?":
    "[echo]哎哟！[beat]你他妈在干什么？",
 "[knowingly[echo]] Problems?": "[knowingly[echo]] 有问题？",
 "[split this line for the choices]Hey, Vaughn! Open up, buddy! Hello!?  [beat]Ha ha, you are hilarious, now open the damn hatch!":
    "[split this line for the choices]嘿，沃恩！开门，哥们！喂！？[beat]哈哈，你真逗，现在把那该死的舱门打开！",
 "[echo fumbling] [edit out \"Would you chill out?\"] I got this. Okay? Just give me a second.":
    "[echo fumbling] [edit out “Would you chill out?”] 我来弄。行吗？给我一秒钟。",
 "[echo desperate]Fiona! Fiona!? Open up, please. It's pitch black in here.":
    "[echo desperate]Fiona！Fiona！？开开门，求你。这里面漆黑一片。",
 "[frustrated] Who closed it?": "[frustrated] 谁关的？",
 "[annoyed] I don't know. I didn't really see.": "[annoyed] 我不知道。我没太看清。",
 "[desperate] Why would they close the dam hatch?":
    "[desperate] 他们干嘛要把舱门关上？",
 "Maybe it wasn't them.": "也许不是他们。",
 "Can't worry about it.": "担心也没用。",
 "Fiona's screwing me.": "Fiona 在坑我。",
 "I mean, unless...": "我是说，除非……",
 "Well I guess I don't know unless.": "那我想不“除非”我就不知道。",
 "You're lucky you didn't lose a hand.": "你运气好，没丢一只手。",
 "Maybe it wasn't them...": "也许不是他们……",
 "Yeah. Lucky.": "是啊。运气好。",
 "Shoo.": "走开。",
 "I've climbed down *ladders* before, alright?":
    "我以前是爬过*梯子*的，行吗？",
 "Don't get fresh.": "别动手动脚。",
 "Let me be very clear. The day I need your help is the day it's already too late.":
    "我把话说清楚。等我需要你帮忙那天，就已经太迟了。",
 "Just trying to help, so... take it easy.":
    "我只是想帮忙，所以……别激动。",
 "Hey, what is your problem? I'm *sorry* if I wanted to make sure you didn't fall on your ass.":
    "嘿，你有什么毛病？如果我是不想让你摔个屁股墩，那我*很抱歉*。",
 "I don't have a problem, okay, that's just it. Take care of yourself, don't worry about me.":
    "我没毛病，行吗，就是这样。管好你自己，别操心我。",
 "Hey, look, where I come from, chivalry isn't dead.[proudly] There's *twice* as many bathrooms for women than men, and *I* wouldn't have it any other way.":
    "嘿，听着，在我来的地方，骑士精神还没死。[proudly] 女厕所数量是男厕所的*两倍*，而*我*绝对不会让它变成别样。",
 "I mean... this is pretty far from the typical bandit den. Most of 'em don't even have running water.":
    "我是说……这离典型的土匪窝差得挺远。它们大多数连自来水都没有。",
 "What *is* this place?": "这地方到底*是*什么？",
 "The money's close, but...": "钱就在附近，但是……",
 "This must have been an Atlas facility.[beat] They made weapons, like Hyperion... before they went under.":
    "这里以前一定是阿特拉斯的设施。[beat] 他们造武器，跟 亥博龙一样……在他们倒闭之前。",
 "It's not a bandit den. See those columns?": "这不是土匪窝。看到那些柱子了吗？",
 "I mean, that's-- that's probably because there's so many girls in the factory, come to think of it...":
    "我是说，那——那大概是因为工厂里女工特别多，这么一想……",
 "Nevermind.": "算了。",
 "[singing] Ho-Hooo, why don't you blow?": "[singing] 嚯——嚯，你怎么不吹？",
 "[muttering] Slurp it, drink it, eat it...": "[muttering] 吸它，喝它，吃它……",
 "[whisper; anxious] \"Which one do I want?\" Are you kidding?":
    "[whisper; anxious] “我该选哪个？” 你开玩笑吧？",
 "[whisper] So... you've probably never thrown a punch before, but... which one do you want?":
    "[whisper] 那……你大概从没挥过拳，但……你想选哪个？",
 "[whisper] There's no other way out and the door's right there. Time to nut up.":
    "[whisper] 没别的出路了，门就在那儿。该硬气点了。",
 "[whisper] I have a gun, you have your...[sees his baton] stick. Let's just do this.":
    "[whisper] 我有枪，你有你的……[sees his baton]棍子。我们干吧。",
 "[whisper] Which one do you want?": "[whisper] 你想选哪个？",
 "[whisper] So... c'mon.": "[whisper] 那……来吧。",
 "Slurp it! Drink it! Eat it! Sniff!": "吸它！喝它！吃它！闻它！",
 "[singing] One man to strike the bell!": "[singing] 一个人去敲钟！",
 "[singing] Two men to man the wheel!": "[singing] 两个人去掌舵！",
 "I don't know why people complain about the psycho shift. It's fun!":
    "我不知道为什么大家都抱怨疯子班。挺好玩的！",
 "Roll me over! Roll me over!": "把我翻过来！把我翻过来！",
 "I used to think Ralph just complained to complain, but, no...":
    "我以前觉得 Ralph 只是为抱怨而抱怨，但不……",
 "[to the psycho] Right?": "[to the psycho] 对吧？",
 "It's fun!": "挺好玩的！",
 "[whisper] [sigh] I'll take the, uh, axe guy, I guess.":
    "[whisper] [sigh] 那我要那个，呃，拿斧头的吧。",
 "[whisper] [sigh] I'll take the Bandit, then.":
    "[whisper] [sigh] 那我要那个土匪。",
 "[whisper] I'll get the little guy.": "[whisper] 我搞定那个小的。",
 "[whisper] I'll get the big guy.": "[whisper] 我搞定那个大的。",
 "[whisper] [sarcastic] You know what, Sasha, I've never been able to pick between chocolate and vanilla and I can't really pick now, so...":
    "[whisper] [sarcastic] 你知道吗，萨莎，我连巧克力和香草都选不出来，现在也真选不出来，所以……",
 "[whisper] You are such a... I don't even know the word.":
    "[whisper] 你真是个……我连词都想不出来。",
 "[whisper] I'll take the little guy, you take the psycho.":
    "[whisper] 我搞那个小的，你搞那个疯子。",
 "[whisper] I'll take the big guy, you take the bandit by the controls.":
    "[whisper] 我搞那个大的，你搞定控制台边那个土匪。",
 "[whisper] [sighs] Okay, fine.": "[whisper] [sighs] 好，行。",
 "[exerting herself] It won't... budge!": "[exerting herself] 它……纹丝不动！",
 "Who knows... but we can't worry about it right now.":
    "谁知道……但我们现在操心不了这个。",
 "*Or* they're just fine and the wind blew it shut.":
    "*或者*他们没事，只是风把它吹关上了。",
 "Yeah. Or that.": "是啊。或者那样。",
 "If I had to guess? Fiona's enacting her *secret plan* to screw me out of a million dollars.":
    "非要我猜？Fiona 正在实施她的*秘密计划*，要把我那一百万坑走。",
 "[quietly] We need their little fingers... to polish the shells.":
    "[quietly] 我们需要他们的小手指……擦炮弹。",
 "[very excited] What *is* that thing tell me now Oh my God a lightning stick what is it how'd you get it tell me now what is it!":
    "[very excited] 那*是*什么东西现在告诉我 天哪一根闪电棍 那是什么你怎么弄到的现在告诉我那是什么！",
 "[grossed and saddened] Ughhh.": "[grossed and saddened] 呃呃。",
 "[being zapped] Aghghgh!": "[being zapped] 啊呃呃呃！",
 "[being knocked out] Ughgh!": "[being knocked out] 呃呃！",
 "Okay, calm down, it's a Stun Baton.": "好，冷静，那是根电击棒。",
 "[very excited] Lemme see it lemme see it lemme see it I wanna see it.":
    "[very excited] 让我看看让我看看让我看看我想看看。",
 "[very excited] Lemme see, lemme see.": "[very excited] 让我看看，让我看看。",
 "[very excited] Give it, lemme see it.": "[very excited] 给我，让我看看。",
 "[like a child whining] Why aren't you giving it to me!":
    "[like a child whining] 你干嘛不给我！",
 "Those guys *rarely* have anything good on--[them][gets cut off]":
    "那些家伙身上*很少*有什么好东西——[them][gets cut off]",
 "Ten dollars!": "十块钱！",
 "[sarcastic] Good job.": "[sarcastic] 干得漂亮。",
 "[sighs] It's locked.": "[sighs] 锁着。",
 "[a little disgruntled] Mm, well that didn't work. I was trying to open the door.":
    "[a little disgruntled] 嗯，那没管用。我本来想开门。",
 "There has to be a way out since those guys were in here. Let's just find what it is.":
    "既然那些家伙在这儿，肯定有出路。我们找找看是什么。",
 "My *sister* wouldn't do that.[beat] Well, I mean she *might* do that but she wouldn't have left me down here with you if that was what was happening.":
    "我*妹妹*不会那么做。[beat] 好吧，我是说她*也许*会那么做，但如果真是那样，她就不会把我跟你留在这下面了。",
 "[sighs] Good point.": "[sighs] 有道理。",
 "Don't say that.": "别说那种话。",
 "[muttering] Mr. Paranoid.": "[muttering] 多疑先生。",
 "Is this how it works?": "这东西是这么用的吗？",
 "Yeah, sure. Just don't, you know, touch me with it.":
    "是啊，当然。只是别，你知道，拿它碰我。",
 "[whisper] This thing is amazing.": "[whisper] 这东西真了不起。",
 "[muttering] Hope he didn't have anything we needed... like *keys*.":
    "[muttering] 希望他身上没什么我们需要的东西……比如*钥匙*。",
 "I know what I want for Arbor Day.": "我知道植树节我想要什么了。",
 "No, you'd end up somehow electrifying us both, forget it.":
    "不行，你最后肯定会把咱俩都电了，算了。",
 "Awww, you *suck* man.": "啊，你*真差劲*。",
 "It's... it's actually super annoying because these cage things are headed kind of right where the money is.":
    "这……其实特别烦人，因为这些笼子正朝钱所在的方向去。",
 "[sighs] Oh, c'mon.": "[sighs] 哦，得了吧。",
 "Look, if riding these things is the only out, then...":
    "听着，要是坐这东西是唯一的出路，那……",
 "They're big enough for us to sit on, so...": "它们够大，我们能坐在上面，所以……",
 "Let's just do it and get it over with.": "我们干脆干了，了结它。",
 "Then it's the only way.": "那这就是唯一的办法。",
 "Okay... I'm gonna go against my clear better judgment and let you play with this dangerous weapon, but you *have* to be care[ful]--[gets cut off].":
    "好……我要违背我明确的更好判断，让你玩这把危险的武器，但你*必须*小[心]——[gets cut off]。",
 "I guess... no time like the present. Right?": "我想……择日不如撞日。对吧？",
 "That's the spirit.": "这才对。",
 "Maybe, uh... maybe we should just try the hatch again? Wait until... the lock erodes?":
    "也许，呃……也许我们该再试试那个舱门？等到……锁锈掉？",
 "Well it's fine, just watch your head.": "没事，就是小心别撞到头。",
 "C'mon, what's the problem? Haven't you ever been in a minecart before?":
    "得了吧，有什么问题？你没坐过矿车吗？",
 "This is *insane*. We have *no* idea where these things are going, we could end up in the incinerator.":
    "这*太疯了*。我们*完全*不知道这些东西往哪儿去，我们可能最后进焚化炉。",
 "There is *no* other way out, dumbbell. We'll just have to take our chances.":
    "*没有*别的出路了，笨蛋。我们只能碰碰运气。",
 "Geez, let a girl catch her breath, alright?":
    "天哪，让姑娘喘口气，行吗？",
 "Okay... this *next* three, ready?": "好……这*一次*数三下，准备好了吗？",
 "Twoooo.": "二——。",
 "Okay, on three, ready?": "好，数三下，准备好了吗？",
 "Okay... I guess you just go when you're ready...":
    "好……那你想走的时候就走……",
 "I mean, what's it like being an emotionless cog spinning away, day after day, for the most blood thirsty, brutal, soul crushing, love-defying corporation in the whole wide universe.":
    "我是说，当一颗毫无感情的齿轮，日复一日地为全宇宙最好杀、最残暴、最磨灭灵魂、最违背爱的公司空转，是什么感觉。",
 "So.[beat] How is it over there, anyway?": "那么。[beat] 话说那边怎么样？",
 "I'm just wonderin'.[beat] What's it like?": "我只是好奇。[beat] 那儿是什么样？",
 "Where.": "哪儿。",
 "I'm just curious...": "我只是好奇……",
 "Is it fun?": "好玩吗？",
 "Is it something you like?": "是你喜欢的事吗？",
 "*What*.": "*什么*。",
 "[scared] I'm not, uh, I'm not really... kosher.... with... the heights.":
    "[scared] 我对……呃，我对……高度……不太……合得来。",
 "It's just the architecture of this place.[beat] We're actually 800 meters up.":
    "只是这地方的建筑结构。[beat] 我们其实在八百米高处。",
 "[discovering something a little interesting] Mm.":
    "[discovering something a little interesting] 嗯。",
 "Everyone's only so happy to climb the ladder even if it means using you for a rung.":
    "每个人都很乐意往上爬，哪怕那意味着拿你当一级梯档。",
 "Look, it's not that easy. Okay?": "听着，没那么容易。行吗？",
 "Sounds like a real hootenanny.": "听着真是场热闹派对。",
 "Look, when I was ten years old, I started a club with my friends just so I had an excuse to print business cards.":
    "听着，我十岁的时候跟朋友们弄了个俱乐部，就为了有借口印名片。",
 "Well... I guess you're well on your way, then.":
    "这个……那我想你走得很顺了。",
 "All I've ever wanted was to run a company, and Hyperion's the biggest company there is, so... there it is.":
    "我一直想做的就是经营一家公司，而 亥博龙是现存最大的公司，所以……就是这样。",
 "I gotta say, Rhys... that's pretty bleak.": "我得说，瑞斯……这挺灰暗的。",
 "Listen, it's one thing to be sick of being number two, but I've been number five hundred and fifty six for what feels like...[sighs] forever, so... I have to make it.":
    "听着，厌倦当老二是一回事，但我当第五百五十六号，感觉已经……[sighs] 一辈子了，所以……我必须成。",
 "I have to make *this* work, and... I have to get to the top of the Hyperion food chain or I'll have wasted basically my entire life.":
    "我必须把*这事*做成，而且……我必须爬到 亥博龙食物链的顶端，否则我这辈子基本上就白过了。",
 "Fine, forget it.": "行，算了。",
 "[muttering to herself] God... frickin' damn it.":
    "[muttering to herself] 天哪……他妈的。",
 "[whispering to herself] It's okay.": "[whispering to herself] 没事的。",
 "Your sister.": "你妹妹。",
 "All that money.": "那笔钱。",
 "Not falling, that's for sure.": "不掉下去，这是肯定的。",
 "I need your help so relax.": "我需要你帮忙，所以放松。",
 "This is scary for me, too!": "这对我也很吓人！",
 "Stop freaking out!": "别慌了！",
 "Okay, Sasha, look at me. It's gonna be fine, just don't think about it.":
    "好，萨莎，看着我。会没事的，别去想它就行。",
 "Like what.": "比如什么。",
 "I'm serious. Just focus on something else.":
    "我是认真的。专注在别的事情上。",
 "[sarcastic] Oh, okay. \"Just don't think about it,\" easy.":
    "[sarcastic] 哦，好。“别去想它就行”，说得轻松。",
 "I think my brain is shutting down.": "我觉得我的脑子在关机。",
 "I can't think of anything to think right now.": "我现在想不出任何能想的东西。",
 "Uhhhh, when we were kids she used to con bikers out of their guidance systems, and then when they'd try to drive they'd fly into cactuses.":
    "呃……小时候她常骗骑手们交出导航系统，然后他们一想开车就会飞进仙人掌里。",
 "Think about your sister.[beat] Tell me, uh, tell me a funny story about her or something.":
    "想想你妹妹。[beat] 跟我说，呃，跟我说个她的趣事什么的。",
 "Good enough.": "够好了。",
 "Okay.[beat] We're gonna get a case, and then get outta trouble, and then take a bath.":
    "好。[beat] 我们会拿到箱子，然后脱离麻烦，然后去洗个澡。",
 "Just think about all that money we're gonna get just as soon as we're off this lift thing.":
    "就想那笔钱——我们一离开这升降台玩意儿就能拿到。",
 "As soon we're off this fun cool ride.": "等我们离开这好玩又酷的玩意儿。",
 "Don't mention the lift thing.": "别提升降台那玩意儿。",
 "I'm just saying, it's a long way down.": "我只是说，摔下去很高。",
 "God, I hate you!": "天哪，我恨你！",
 "Well, not falling, that's for damn sure.": "好吧，不掉下去，这他妈是肯定的。",
 "And if *I* personally was scared of heights -- which I'm not, of course -- but if I *was*, I certainly wouldn't want to think about just how much and how hard I would die if I slipped off this thing.":
    "而如果*我*本人恐高——当然我不恐——但如果我*真的*恐，我肯定不想去想：要是我从这玩意儿上滑下去，会死得多惨、多难看。",
 "Yeah, well, you're *cured*, so you're welcome.":
    "是啊，那好吧，你*被治好了*，不客气。",
 "Well I hate it, it's annoying.": "我讨厌这样，很烦人。",
 "[tentatively] What are, uh... what are you afraid of?":
    "[tentatively] 你，呃……你怕什么？",
 "I guess we all have to be afraid of something.":
    "我想我们总得怕点什么。",
 "It doesn't look like it's heights, so...": "看起来不是高度，所以……",
 "And you took care of that guy back there alright...":
    "而且你刚才把那个家伙处理得还行……",
 "Look, If I flip out and just jump off tell my sister I died doing something cool, alright?":
    "听着，要是我崩了直接跳下去，跟我妹妹说我是做很酷的事死的，行吗？",
 "If I flip out and just jump off tell my sister I died doing something cool, alright?":
    "要是我崩了直接跳下去，跟我妹妹说我是做很酷的事死的，行吗？",
 "[a little panicked] Just give me something to think about. Something to focus on.":
    "[a little panicked] 给我点能想的东西。点能专注的东西。",
 "[a little panicked] I'm sorry, but can you just like... give me something to, uh, just say a topic.":
    "[a little panicked] 抱歉，但你能不能就……给我，呃，随便给个话题。",
 "Okay, thanks for sharing. Ass.": "好，谢谢分享。混蛋。",
 "[laughs a little]": "[laughs a little]",
 "[mocking him] \"Of not really *living*, ya know, bro?\"":
    "[mocking him] “怕没能真正*活过*，你懂的，兄弟？”",
 "I'm scared of... not doing anything memorable before I die. I guess.":
    "我怕……死之前没能做出什么值得记住的事。我想。",
 "I guess... I dunno, I guess I'm most scared of being a nobody. Of... being forgotten.":
    "我想……我不知道，我想我最怕的就是当个无名之辈。怕……被遗忘。",
 "[lightly laughing] Shut up.": "[lightly laughing] 闭嘴。",
 "Right now what I'm most afraid of?[beat] Hyperion.":
    "现在我*最*怕的是什么？[beat] 亥博龙。",
 "Vaughn and I are looking at life in the mailroom stockade if we don't get back in time to even things out... and that's if they're *nice*.":
    "要是我们不能及时回去把账摆平，沃恩 和我这辈子就得在收发室牢房里过了……而这还是在他们*客气*的情况下。",
 "Yeah, I know.": "是啊，我知道。",
 "[to herself as well to Rhys] We'll get back to time.[beat; then quieter] We'll get back.":
    "[to herself as well to Rhys] 我们会及时回去的。[beat; then quieter] 我们会回去的。",
 "[cold] We'll see.": "[cold] 走着瞧。",
 "No really. I'm not afraid of anything.": "不，说真的。我什么都不怕。",
 "Me? Nothin'.": "我？什么都不怕。",
 "Bullshit.": "放屁。",
 "Two minutes ago you were practically *daring* me to jump, and *now* this is suddenly a problem?":
    "两分钟前你还几乎是*激*我跳下去，*现在*这突然成问题了？",
 "Will you pull yourself together for crying out loud.":
    "你能不能振作一点，老天。",
 "But\tI'm *sorry* that my minor mental breakdown is harshing your mellow or whatever.":
    "但\t我*很抱歉*我这点小小的精神崩溃扫了你的兴还是怎么着。",
 "I didn't *know* it was gonna be like this, alright?":
    "我*不知道*会是这样，行吗？",
 "This is just... it's hard for me right now.": "这只是……现在对我来说很难。",
 "[muttering to herself] Ugh, I hate this.": "[muttering to herself] 呃，我讨厌这样。",
 "I mean God, can't you just be *nice*.": "我是说天哪，你就不能*友善*点吗。",
 "[calming breathing]": "[calming breathing]",
 "Ummmm...": "呃嗯……",
 "Let's... uh, let's... we can get off this way.": "我们……呃，我们……我们能从这边下去。",
 "[sigh] Oh great.": "[sigh] 哦，好极了。",
 "The money's moving towards us?": "钱在朝我们靠近？",
 "The money's... wait.": "钱在……等等。",
 "So I says to Mabel I says...": "所以我就跟 Mabel 说，我说……",
 "You already told me this story! You've told me this story like fifty times!":
    "这故事你已经跟我说过了！你跟我说了大概五十遍了！",
 "Oh, okay, well I'm *sorry*, geez, it's hard to remember, we all have the same masks.":
    "哦，好，那*对不起*，天哪，太难记了，我们面具都一样。",
 "That's it.": "就是这个。",
 "How's uh, how's Jenny doin'?": "那个，Jenny 怎么样？",
 "I'm *Mark*.": "我是*Mark*。",
 "Ohhhh, Mark! How the Hell are ya?": "哦——Mark！你他妈好吗？",
 "Well... uhhhh, guess that's where we gotta go.":
    "这个……呃……看来我们就得去那儿。",
 "This probably controls the platform.": "这大概控制着平台。",
 "Uh huh. Probs.": "嗯哼。大概吧。",
 "Why would they... why would they have skags, huh?":
    "他们干嘛……他们干嘛养异犬，啊？",
 "I don't know, but as long as they're in cages, I don't care.":
    "我不知道，但只要它们在笼子里，我不在乎。",
 "Yep.": "是啊。",
 "It's just a thought. You know....": "只是随便想想。你知道……",
 "[reading] Atlas.[beat] See?": "[reading] 阿特拉斯。[beat] 看到了吧？",
 "You know, I heard Atlas was at, uh, one point in time trying to find a Vault... just like Hyperion.":
    "你知道，我听说阿特拉斯在，呃，某个时期也试过找秘藏……跟 亥博龙一样。",
 "Well, I don't see any, so... let's just keep our head in the game, okay?":
    "这个，我没看到什么秘藏，所以……我们专心眼前的事，行吗？",
 "Are those the right words?": "这词用对了吗？",
 "Oh, and there's actually a landline here! I should be able to jack my comm in and intermix with Vaughn!":
    "哦，而且这儿居然有根有线线路！我应该能把我的通讯接进去，跟 沃恩 互通！",
 "[to Sasha; whispery] It, uh, it says I'm connected. He *should* be able to hear us.":
    "[to Sasha; whispery] 它，呃，它显示我连上了。他*应该*能听到我们。",
 "I've got a signal again so I'll try Vaughn real quick.":
    "我又收到信号了，我赶紧试试 沃恩。",
 "Okay, but make it snappy.": "好，但利索点。",
 "Okay, well... say something, then.": "好，那……说话啊。",
 "Soooo....": "那么……",
 "I'm sure he's just waiting for you to talk first.":
    "我确定他只是等你先开口。",
 "Vaughn? This is Rhys. Hello. Do you copy? Anyone there?":
    "沃恩？我是 瑞斯。喂。收到吗？有人在吗？",
 "This is Papa Bear sittin' front door with, uh...":
    "我是坐镇前门的熊爸爸，还有，呃……",
 "Hey, uh, breaker one niner, breaker one niner, do you copy, over?":
    "嘿，呃，十九号频道，十九号频道，收到吗，完毕？",
 "Carebear. What's your twenty, ol' buddy?":
    "爱心熊。你在什么位置，老伙计？",
 "Testing. Testing. One, two. Testing.": "测试。测试。一、二。测试。",
 "[vocal exercises; overly enunciated] Unique New York, Unique New York. Roberta ran rings around the Roman ruins.":
    "[vocal exercises; overly enunciated] 独特的纽约，独特的纽约。罗伯塔绕着罗马遗迹跑圈。",
 "You know this is hooked to my *brain*, right?":
    "你知道这是接到我*脑子*上的吧？",
 "*Fiona*!!! Can you hear me?! Hellooooooo? Anyone th[ere]--[gets cut off]":
    "*Fiona*！！！你能听到我吗？！喂——？有人在——[gets cut off]",
 "I think we're under... something... I don't know.[beat] That's Hanger Nineteen! Love you.":
    "我想我们在……什么东西下面……我不知道。[beat] 那是十九号机库！爱你。",
 "Look, Vaughn, if you can hear me, we're in Hanger Nineteen, so come meet us, okay?":
    "听着，沃恩，你要是能听到，我们在十九号机库，来找我们，行吗？",
 "He likes to feel needed.": "他喜欢觉得自己被需要。",
 "That wasn't so...[trails off]": "那也不算太……[trails off]",
 "[happily] Hey! Fiona!": "[happily] 嘿！Fiona！",
 "You can't think of *one*.": "你连*一个*都想不出来。",
 "I can't think of one.": "我一个都想不出来。",
 "Okay, let's see what we can do with this thing!":
    "好，看看我们能用这玩意儿干点什么！",
 "Oh. Right.": "哦。对。",
 "That was a mistake, that was a mistake, that was a mistake.":
    "那是个错误，那是个错误，那是个错误。",
 "*Why*!": "*为什么*！",
 "[nervously bracing himself for getting eaten] Ughhhh.":
    "[nervously bracing himself for getting eaten] 呃呃呃。",
 "No shit.": "废话。",
 "No way, this is factory-line muzac from this place's heyday.":
    "不可能，这是这地方全盛期的流水线背景音乐。",
 "Bossanova must not have figured out how to hack into their song library.[beat] Typical.":
    "Bossanova 肯定没搞明白怎么黑进他们的曲库。[beat] 典型。",
 "Bossanova?": "Bossanova？",
 "[being attacked] Aghhhhh!": "[being attacked] 啊啊啊啊！",
 "[being eaten] Mhghfhhfh!": "[being eaten] 唔呃呃呃！",
 "Oh shit!": "哦妈的！",
 "Hey! You!": "嘿！你！",
 "[being attacked] Ahhhhhh!": "[being attacked] 啊啊啊啊！",
 "Hit the button, raise the lift!": "按按钮，升起降台！",
 "[impressed] Oh, okay. Goin' for the gold there.":
    "[impressed] 哦，好。直接冲金牌去了。",
 "[whisper] Okay...[beat] One. Two...": "[whisper] 好……[beat] 一。二……",
 "[gruffly voiced] Kiss the floor, asshole!": "[gruffly voiced] 亲地板去吧，混蛋！",
 "[gruffly voiced] Freeze, asshole!": "[gruffly voiced] 别动，混蛋！",
 "[singing] Three men, to gallant braces!": "[singing] 三个人，去撑起那副背带！",
 "Hi": "嗨",
 "[singing] High-Oh! Come roll me over!": "[singing] 嗨——嚯！来把我翻过来！",
 "Why are you yelling?!": "你干嘛大喊？！",
 "[scared] Aghhh!": "[scared] 啊啊！",
 "Wow!": "哇！",
 "Five dollars!": "五块钱！",
 "Okay... you count down this time.": "好……这次你数。",
 "[in awe] Wooow.": "[in awe] 哇啊。",
 "{FearA}Oh I don't like this.": "{FearA}哦我不喜欢这样。",
 "[in awe] Woowww.": "[in awe] 哇啊啊。",
 "I mean, skags in cages?": "我是说，笼子里的异犬？",
 "In an Atlas factory?": "在阿特拉斯的工厂里？",
 "Am I missing something obvious?": "我是不是漏了什么明显的东西？",
 "It's a zoo, I guess?": "我想是个动物园？",
 "Are they experiments?": "它们是实验品吗？",
 "Whoah!": "哇！",
 "Crap! Uhh...": "糟！呃……",
 "Your guess is as good as mine.": "我跟你一样猜不出来。",
 "I don't know... a zoo... I guess? But wouldn't typically you see stuff more... exotic?":
    "我不知道……动物园……我想？但一般不是会看到更……奇特的东西吗？",
 "Yeah. And Pandora doesn't really *do* zoos anyway, so...":
    "是啊。而且 潘多拉 根本*不搞*动物园，所以……",
 "It's just kind of the sort of thing you'd see in Hyperion science departments. Like for makeup testing.":
    "这东西就是你会在 亥博龙科研部门看到的那种。比如用来测试化妆品。",
 "I don't know... are they being used for experiments, or...":
    "我不知道……它们是被用来做实验，还是……",
 "[no way] Here? For Bossanova?": "[no way] 在这儿？为 Bossanova？",
 "All this stuff looks retrofitted.": "这些设备看起来都是后期加装的。",
 "I thought skags grew like weeds here.": "我以为异犬在这儿的繁殖跟野草一样。",
 "It's just all really weird.": "就是一切都太怪了。",
 "[whisper] Sorry.": "[whisper] 抱歉。",
 "Mm.": "嗯。",
 "I can still access the system.": "我还是能接入系统。",
 "[muttering] I hope you know what you're doing...":
    "[muttering] 我希望你知道自己在干什么……",
 "The password is probably boobs but... it's honestly faster for to me to just bypass their infantile coding.":
    "密码大概是“咪咪”之类的，但……说实话，我直接绕过他们那幼稚的代码更快。",
 "[being killed] Arghhgh!": "[being killed] 啊呃呃！",
 "Hit the thing!": "按那个东西！",
 "Huzzah!": "哦耶！",
 "See what a little ingenuinity and schooling can get you in this day and age? And they say this galaxy is going to Hell in a...[trails off]":
    "看看这年头一点点聪明才智加学历能给你带来什么？他们还说这银河正一路滑向地狱……[trails off]",
 "*Why* did you open *all* the doors?!": "*为什么*你把*所有*门都打开了？！",
 "[a little panicked] Rhys!": "[a little panicked] 瑞斯！",
 "There was only-- I don't know, I only saw-- look, there only *one button*!":
    "只有——我不知道，我只看到——听着，那儿只*有一个按钮*！",
 "On second thought, you should have just tried boobs.":
    "再想想，你本来就该先试“咪咪”的。",
 "The doors are *already* open, genius! Hit the lift!":
    "门*已经*开了，天才！按升降台！",
 "Why?!": "为什么？！",
 "I just like the song!": "我就是喜欢这首歌！",
 "I wanted to know what it did!": "我想知道它是干什么的！",
 "See ya suckas!": "再见，傻逼们！",
 "Uhh.....": "呃……",
 "[big breath] Okay. Since you're such wimp that you need me. I'll try.":
    "[big breath] 好。既然你怂到需要我。我试试。",
 "I'm serious. I can't go through this without you, so... please. Be the rock.":
    "我是认真的。没你我撑不过去，所以……求你。当那块磐石。",
 "Not *my* rock, but... be *a* rock.": "不是*我的*磐石，但……当*一块*磐石。",
 "Look, Sasha... I need you..[long beat] To relax.":
    "听着，萨莎……我需要你……[long beat] 放松。",
 "You don't think this whole awful mess is scary for me, too?":
    "你觉得这一整摊糟事对我就不可怕吗？",
 "I'll try and work on that.": "我会试着克服的。",
 "We're in same boat, Sasha, okay? I've been in more therapy inducing experiences since stepping down on this planet than a month-long Hyperion corporate retreat!":
    "我们在同一条船上，萨莎，行吗？自从踏上这星球，我经历的该看心理医生的场面，比在 亥博龙开一个月公司团建还多！",
 "Yeah, I know. You haven't been good at hiding it.":
    "是啊，我知道。你藏得不太好。",
 "Okay! Alright! Geez, I'm fine.": "好！行！天哪，我没事。",
 "Stop freaking out! Stop freaking out! Your freaking out is freaking me out so stop it!":
    "别慌了！别慌了！你一慌把我也搞慌了，所以停下！",
 "Good?": "好了吗？",
 "[flat] I'm scared to say no, so... yeah, good.":
    "[flat] 我不敢说不好，所以……是啊，好了。",
 "[echo]Of course you can't. Ugh, you are *completely* useless.":
    "[echo]你当然听不到。呃，你*完全是*个废物。",
 "I thought... maybe... it was a pull door.": "我以为……也许……那是扇拉门。",
 "What *were* you gonna do with that Vault Key, anyway...?":
    "你拿到那把秘藏钥匙到底*打算*干什么……？",
 "Yeah, speaking of that... and not that I personally care... but...":
    "是啊，说到这个……倒不是我个人在乎……但是……",
 "Like, what was the plan?": "就是，计划是什么？",
 "Cause isn't Hyperion rich already?": "因为 亥博龙不是已经很有钱了吗？",
 "I wanted to screw Vasquez.": "我想坑 Vasquez。",
 "Be a hero to Hyperion.": "当 亥博龙的英雄。",
 "Get a giant pay-out.": "拿一笔巨额回报。",
 "The GPS works at least.": "至少 GPS 还能用。",
 "You know, if it'd been real?": "你知道，要是它是真的的话？",
 "[sigh] Soon we'll have the money and this whole national tragedy will be over...":
    "[sigh] 很快我们就能拿到钱，这场全国性悲剧也就结束了……",
 "You know him?": "你认识他？",
 "It was less about the Vault Key and more about just screwing over Vasquez.":
    "重点不在秘藏钥匙，而更在于坑掉 Vasquez。",
 "[getting pissed] As well as you can know any idiot flunkey who was promoted before his time.":
    "[getting pissed] 就跟你认识任何一个被提前提拔的白痴马屁精那样。",
 "A little.": "有点。",
 "Bad blood?": "有过节？",
 "I was gonna be the hero to Hyperion, I was gonna be... I was gonna be lifted on everyone's shoulders and crowd-surfed right to the President's quarters.":
    "我本来要当 亥博龙的英雄，我本来要……我本来要被人扛在肩上、人群托着我一路送到总裁办公室。",
 "Yeah, it would've been.": "是啊，本来会的。",
 "Oh.[beat] Cool.": "哦。[beat] 酷。",
 "I was gonna give it to them in exchange for a big fat promotion and a big fat pay-out.":
    "我本来要把它交给他们，换一次大大的晋升和一大笔钱。",
 "Using a Vault Key to get a bonus, huh. You really aim for the stars, there, don't ya?":
    "用一把秘藏钥匙去换年终奖，哈。你可真是志存高远，对吧？",
 "Right? Hyperion's right already?": "对吧？亥博龙已经很对了？",
 "Hyperion.": "亥博龙。",
 "This crap is scary for me, too.": "这破事对我也很吓人。",
 "It's too... I dunno, it's too *weird* for Atlas, so... this stuff must have been added by Bossanova's crew once the company went under.":
    "这太……我不知道，对阿特拉斯来说太*怪*了，所以……这些东西肯定是公司倒闭后 Bossanova 那帮人加上去的。",
 "[screaming in agony]": "[screaming in agony]",
 "[whisper] Uh-oh.": "[whisper] 哦哦。",
 "[death yells]": "[death yells]",
 "It's that freak!": "是那个怪胎！",
 "[whisper] Uhhhh... maybe we should....": "[whisper] 呃……也许我们该……",
 "Nice work, buddy!": "干得好，哥们！",
 "Can you hand over the case!": "能把箱子交出来吗！",
 "This is all your fault!": "这全是你的错！",
 "Yeah, but how?": "是啊，但怎么弄？",
 "Something around here must control the lift. Just find it.":
    "这附近肯定有东西控制着升降台。去找。",
 "Nice work, buddy, really, great show. Couldn't have done it better myself.":
    "干得好，哥们，真的，表演精彩。换我我也做不到更好。",
 "[yelling whisper] Rhys, shut up!": "[yelling whisper] 瑞斯，闭嘴！",
 "It's that one... right there... by your, uh, feet?":
    "就是那个……就在那儿……在你，呃，脚边？",
 "Hey, uh... pal? Can you hand over that case?":
    "嘿，呃……老兄？能把那只箱子交出来吗？",
 "No, it's okay.": "不，没事。",
 "You screwed up my whole deal, guy! Hey! I'm talkin' to you!":
    "你把我的整笔买卖搞砸了，老兄！嘿！我在跟你说话！",
 "Oh, so it's *you*! You're like a bad rash, man, I just can't get a cream big enough!":
    "哦，原来是*你*！你就像一片烂皮疹，老兄，我买不到够大的药膏！",
 "[whisper] Why would he be here?": "[whisper] 他怎么会在这儿？",
 "Yeah! I'm totally not!": "是啊！我完全不是！",
 "[gleeful] You're not totally incompetent!": "[gleeful] 你也不是完全无能！",
 "[annoyed] Uh-huh, slurp it, drink it, I'll get right on that.":
    "[annoyed] 嗯哼，吸它、喝它，我马上就办。",
 "[annoyed grunt] I *hate* getting the psycho shift.":
    "[annoyed grunt] 我*讨厌*排到疯子班。",
 "It's like genuinely hard to concentrate.": "我是说真的很难集中精神。",
 "Incestuous sheets! Rotten milk!": "乱伦的床单！腐坏的牛奶！",
 "Or maybe it was! Who knows, you don't.": "或者也许就是真的！谁知道呢，反正你不知道。",
 "Looks like a zoo.": "看起来像个动物园。",
 "[sigh] Let's just climb down.": "[sigh] 我们爬下去吧。",
 "What *is* that?": "那*是*什么？",
 "Why'd you stop?": "你怎么不走了？",
 "There's no bottom. It's...[trails off]": "看不到底。它……[trails off]",
 "This is like an emergency escape thing. We're climbing in the wrong way.":
    "这像是应急逃生用的。我们爬反了方向。",
 "It's the *only* way.": "这是*唯一*的出路。",
 "Okay, on three, alright?": "好，数三下，行吗？",
 "[jumping and landing]": "[jumping and landing]",
 "[yelling] Incestuous sheets! Rotten milk!": "[yelling] 乱伦的床单！腐坏的牛奶！",
 "[yelling] Hey!": "[yelling] 嘿！",
 "Crap!": "糟！",
 "Pick one!": "选一个！",
 "Pick one?!": "选一个？！",
 "God damnit!": "该死的！",
 "Shit. We should... uh... tell somebody....": "妈的。我们该……呃……跟谁说一声……",
 "Uhhhhh...": "呃……",
 "No keys, but... you know, good enough.": "没钥匙，但……你知道，够用了。",
 "Nothin', really.": "其实没什么。",
 "They went bust.[beat] Never found it.": "他们破产了。[beat] 从没找到过。",
 "What happened?": "发生了什么？",
 "[bored] Whoopie-dee-doo, let's find a way outta here now.":
    "[bored] 好棒棒哦，我们现在找条出路吧。",
 "[echo] Hey!!!!": "[echo] 嘿！！！！",
 "Hmmffp!": "唔呃！",
 "Lets get down. I'm going to lock pick that door, meanwhile maybe you can find a bypass to whatever is blocking communication.":
    "我们下去。我去撬开那扇门，同时你也许能找到绕过那个阻断通讯的东西的办法。",
 "Dammit, this rakking door. Made by Atlas. Cheap peace of shit.":
    "该死的，这破门。阿特拉斯造的。便宜货。",
 "So what's up with you and your buddy Vaughn.":
    "那你跟你那个哥们 沃恩 是怎么回事。",
 "If he pulls his weight.": "要是他尽了自己的本分的话。",
 "He's my partner.": "他是我的搭档。",
 "I'm busy here.": "我这儿正忙。",
 "...": "……",
 "It's not that simple.": "没那么简单。",
 "Hyperion brings order.": "亥博龙带来秩序。",
 "He was a hero.": "他是个英雄。",
 "He did that, not me.": "那是他做的，不是我。",
 "Jack ruined everything.": "Jack 毁掉了一切。",
 "You asshole! You rakking asshole!": "你这混蛋！你他妈的混蛋！",
 "He killed my father and his entire family.": "他杀了我父亲，还有他全家。",
 "What? I'm only telling the truth.": "什么？我只是在说实话。",
 "Sasha. Handome Jack was the most loved person on Pandora. You would have loved him if you were in my shoes.":
    "萨莎。帅杰克是 潘多拉 上最受爱戴的人。你要是处在我的位置，你也会喜欢他的。",
 "Did you ever meet him?": "你见过他吗？",
 "Hm. No. I didn't get the sublime opportunity.":
    "嗯。没有。我没得到那份崇高的机会。",
 "What is that suppose to mean?": "那是什么意思？",
 "I see why you hate him so much. He only killed your kind of people.":
    "我明白你为什么这么恨他了。他只是杀了你那种人。",
 "Hyperion has brought nothing but order to Pandora.":
    "亥博龙给 潘多拉 带来的只有秩序。",
 "To the Jack with you Rhys.": "去你的 Jack，瑞斯。",
 "I'll take that as a compliment.": "我就把这当夸奖了。",
 "You know what? Stop asking me questions.  I'm trying to focus.":
    "你知道吗？别再问我问题了。我要集中精神。",
 "What? Hyperion and Jack killed people. Lots of people!":
    "什么？亥博龙和 Jack 杀过人。杀了很多很多人！",
 "Nevermind. Just let it go.": "算了。别在意。",
 "Why because asking you about Handsome Jack ruins your day?":
    "为什么，因为问你帅杰克的事就毁了你的一天？",
 "Hey. Did you hear me?": "嘿。你听到我说话了吗？",
 "{SmugA}Hey -- Jack only killed bandits and lowlifes. {SternC}He was a hero.":
    "{SmugA}嘿——Jack 只杀土匪和渣滓。{SternC}他是个英雄。",
 "Your kind think yourselves soo lofty. You must be too good to answer to someone like me.":
    "你们这种人自以为高高在上。你一定是高贵到不屑回答我这样的人。",
 "Nevermind? Nevermind? You ignore me and now Nevermind.":
    "算了？算了？你无视我，现在又说算了。",
 "Just let it go.": "别在意了。",
 "Nevermind": "算了",
 "He killed people I knew, friends and fa-":
    "他杀了我认识的人，朋友和家——",
 "To the Jack with you asshole.": "去你的 Jack，混蛋。",
 "Tell me why I don't cut your ass down right now.":
    "告诉我为什么我现在不一枪把你放倒。",
 "We're in a room full of skags.": "我们在一间满是异犬的屋子里。",
 "Sasha has a gun! I repeat Sasha has a gun!":
    "萨莎 有枪！我重复一遍，萨莎 有枪！",
 "Breaker breaker, we are in a room full of, um. Skags.":
    "十九号频道，我们在一间满是，呃。异犬的屋子里。",
 "I've got a connection!": "我接通了！",
 "We're in hangar 19": "我们在十九号机库",
 "I love you.": "我爱你。",
 "Yeah hold them off.": "是啊，拖住他们。",
 "I don't take orders from you!": "我不听你的命令！",
 "Let's rock.": "开干吧。",
 "[Thumbs up]": "[竖大拇指]",
 "I don't take orders from you. Or your kind.":
    "我不听你的命令。也不听你那种人的。",
 "They're going to kill us if you don't get that lift down.":
    "你要是不把升降台弄下来，他们会杀了我们。",
 "I'll do that. Just hold them off.": "我来弄。你只管拖住他们。",
 "Sticky Icky": "黏糊糊",
 "Hands Off": "别碰",
 "Food Pulp": "食物糊",
 "It's in Bandit.": "这是土匪文写的。",
 "What Rhys?": "怎么了 瑞斯？",
 "Dammit": "该死",
 "You better rakking hurry up.": "你他妈最好快点。",
 "Figure it out!": "想出办法来！",
 "What did you just do?": "你刚才干了什么？",
 "Sticky icky?!": "黏糊糊？！",
 "Make it go faster!": "让它快点！",
 "I'm trying!": "我在试！",
 "Holy.  Hurry man.": "我的天。快点，老兄。",
 "Are you seriously releasing all the Skags?":
    "你真要把所有异犬都放出来？",
 "Their wiring is all criss crossed.": "它们的线路全交叉接错了。",
 "Just push everything!": "全都按一遍！",
 "Too close!": "太近了！",
 "Faaaaaaaaaaa": "啊啊啊啊啊啊啊",
 "Shoot him!": "开枪打他！",
 "Rak Rhys do it!": "操，瑞斯 快动手！",
 "[seething mad, catching her breath] God bless it Rhys. You and your friend are going to die on Pandora if you don't know how to rakking pull a trigger!":
    "[seething mad, catching her breath] 老天保佑，瑞斯。你们要是不会他妈扣扳机，你跟你的朋友会死在 潘多拉 上！",
 "[catching her breath] Good job. I, I didn't know you had it in you.":
    "[catching her breath] 干得好。我，我不知道你还有这一手。",
 "Now, hand me the gun Rhys.": "现在，把枪给我，瑞斯。",
 "Here's your gun.": "你的枪。",
 "I'm keeping it.": "我留着。",
 "[Throw into Cage]": "[扔进笼子]",
 "[Holster it]": "[收进枪套]",
 "I don't think so. I'm keeping it.": "我不这么认为。我留着。",
 "What ever.": "随便吧。",
 "Lets' go": "我们走",
 "Smartest thing you've said all day.": "这是你今天说过最聪明的话。",
 "Well thank goodness you asked, because he's actually super harmless.":
    "谢天谢地问了，因为他其实超级无害。",
 "You Hyperion guys are hated, reviled from here to there.":
    "你们 亥博龙的人到处都被人恨、被人骂。",
 "He's just a coworker at Hyperion.": "他只是 亥博龙的一个同事。",
 "Just mind your own business.": "管好你自己的事。",
 "Just another Hyperion idiot.": "又一个 亥博龙白痴。",
 "You and your dead leader Jack.": "你和你那位死掉的领袖 Jack。",
 "Rhys, Jack killed people. Lots of people.\nSince you work at Hyperion then you must be complicet with what he did.":
    "瑞斯，Jack 杀过人。很多人。\n既然你在 亥博龙工作，那你一定跟他做的事脱不了干系。",
 "Go ahead!": "动手啊！",
 "Give me that gun, okay?": "把那枪给我，行吗？",
 "You don't need to do that.": "你不必那么做。",
 "Woah. Sasha put. the. gun. away.": "哇。萨莎，把。枪。收。起。来。",
 "You don't man understa- You're not from here. You have no idea what shit Pandora has that can just. Kill you.":
    "你不明——你不是这儿的人。你完全不知道 潘多拉 有什么东西能。直接。弄死你。",
 "Give. Me. The. Gun.": "把。枪。给。我。",
 "{smugA}You really don't need to do that. There's nothing down here to worry about.":
    "{smugA}你真的不必那么做。这下面没什么好担心的。",
 "Ok let me try contacting them again.": "好，我试试再联系他们一次。",
 "Vaughn? You there buddy?  My compadre you there?  Dam. Something is blocking it.":
    "沃恩？你在吗哥们？我的伙伴你在吗？该死。有什么东西在阻断。",
 "Fff-Rakk, we need to get in touch with them. Something must be blocking the signal.":
    "操——妈的，我们得联系上他们。肯定有什么东西在阻断信号。",
 "That's what I just said.": "我刚就是这么说的。",
 "Or they're dead. Oh god.": "或者他们死了。哦天。",
 "See if you find a way to get a signal through.": "看看你能不能想办法把信号传出去。",
 "I see some wires, they're leading towards that hyrdolic over there.":
    "我看到一些电线，它们通向那边那个液压装置。",
 "Well get on it.  They could be dead up there.":
    "那就去弄。他们在上面可能已经死了。",
 "Calm down.": "冷静。",
 "You're crowding me.": "你挤到我了。",
 "I'm on it.": "我在弄。",
 "So hurry the eff up.": "那就赶紧他妈快点。",
 "Look you need to calm down.": "听着，你需要冷静。",
 "We are on Pandora fool. We can die in a split second.":
    "我们在 潘多拉 上，笨蛋。我们随时可能死。",
 "Just don't get in the way. Wait right there.  You're crowding me.":
    "别挡路就行。就在那儿等着。你挤到我了。",
 "Finally! EMP field down.": "终于！电磁脉冲场关掉了。",
 "Why join them, I mean.": "我是说，你干嘛加入他们。",
 "I'm so shitten glad he's dead.": "他死了我真他妈的庆幸。",
 "That makes you just as guilty and responsible for murder!":
    "那你就跟谋杀一样有罪、一样该负责！",
 "That's ridulous.": "这太荒唐了。",
 "I'm not a threat.": "我不是威胁。",
 "Back off.": "退后。",
 "ok.": "好。",
 "You fool!": "你这蠢货！",
 "No one is getting it.": "没人弄得成。",
 "{ShockD}Vaughn? Can you hear me Vaughn?": "{ShockD}沃恩？你能听到我吗 沃恩？",
 "We're trying to find you.": "我们在试着找你们。",
 "We're trapped down below.": "我们被困在下面。",
 "Get us out of here!": "把我们弄出去！",
})

# —— 通讯、电力继电器与互相盘问 ——
T.update({
 "{FearB}Fiona! Hey! It's me.  You gotta find us and get us out of here.":
    "{FearB}Fiona！嘿！是我。你得找到我们，把我们弄出去。",
 "Rhys has taken my gun. He won't give it back.":
    "瑞斯 抢了我的枪。他不肯还。",
 "We are going to die if we don't shed these fools.":
    "要是不甩掉这些傻子，我们会死。",
 "Open up the hatch!": "打开舱门！",
 "Vaughn, open up the hatch.": "沃恩，把舱门打开。",
 "Open up the hangar hatch!": "打开机库舱门！",
 "[Hissed] Vaughn! I need your help, man.":
    "[Hissed] 沃恩！我需要你帮忙，老兄。",
 "What the f-": "搞什么——",
 "Help!": "救命！",
 "Vaughn, you listen to me. No matter what I've said in the past, it doesn't matter.":
    "沃恩，你听我说。不管我过去说过什么，都不重要。",
 "{SlyC}Vaughn, hey buddy. I hope you can hear me.":
    "{SlyC}沃恩，嘿哥们。我希望你能听到我。",
 "[sing songy] Open up the hatch.": "[sing songy] 把舱门打开。",
 "Love you man.": "爱你老兄。",
 "We are in-": "我们在——",
 "[tired] Hangar 19.": "[tired] 十九号机库。",
 "You know. bromance. high adventure.": "你知道。兄弟情。惊险冒险。",
 "Beep Beep Beep Beep": "哔 哔 哔 哔",
 "Then we need get up there, right now. This our chance.":
    "那我们就得上去，现在马上。这是我们的机会。",
 "This looks like a lift, do your hackey thing and get the lift down!":
    "这看着像升降台，施展你那黑客本事把升降台弄下来！",
 "Wait what?": "等等什么？",
 "{SlyA}Looks like {SlyC}*my* money is... [beat] {SternC}right {ThinkB}above us!":
    "{SlyA}看来{SlyC}*我* 的钱……[beat] {SternC}就{ThinkB}在我们头顶上！",
 "Oh shit, the money it's moving!": "哦妈的，钱在移动！",
 "I'm redirecting the power as fast as I can, but it's being controlled from somewhere else!":
    "我在尽快改接电力，但它是从别的地方被控制的！",
 "{ShockB}Just get that lift running. {ShockA}*Now*.":
    "{ShockB}把升降台弄起来。{ShockA}*现在*。",
 "Shit what did you do?": "操，你干了什么？",
 "{ShockB}Can't you make it go faster?": "{ShockB}你就不能让它快点吗？",
 "{SadC}Um, apparently not.": "{SadC}呃，显然不行。",
 "Ah. Meat on the stick.": "啊。棍子上的肉。",
 "{RageB}Rhys?!": "{RageB}瑞斯？！",
 "{AngryB}I know.": "{AngryB}我知道。",
 "Dood get the lift down.": "老兄，把升降台弄下来。",
 "Let's go! Let's go. Before more bandits arrive or those dam skags eat us for lunch!":
    "快走！快走。趁更多土匪赶来或者那些该死的异犬把我们当午饭吃掉！",
 "You don't have to tell me twice.": "不用跟我说两遍。",
 "[whispering] Oh shit. Oh shit. It's Zero.": "[whispering] 哦妈的。哦妈的。是 Zer0。",
 "Make it go up?": "让它上去？",
 "Did you do that?": "那是你干的？",
 "I could've done that...": "我本来也能办到……",
 "can I have your autograph?": "能给我签个名吗？",
 "[Aim Gun at Zero]": "[把枪对准 Zer0]",
 "Sasha shoot him.": "萨莎，开枪打他。",
 "Nice work.": "干得好。",
 "I know I'm in awe too.": "我知道，我也很敬畏。",
 "[whispering] Sasha shoot him.": "[whispering] 萨莎，开枪打他。",
 "[whispering] Are you stupid?": "[whispering] 你傻吗？",
 "Hey, hey, dood in the tights. Get us our mo-":
    "嘿，嘿，穿紧身衣的老兄。把我们那一百万——",
 "Rhys you idiot.": "瑞斯 你这白痴。",
 "Excuse me, uh, Mr. Zero Sir. may I have your autograph?":
    "打扰一下，呃，Zer0 先生。能给我签个名吗？",
 "Are you goint to help us get our money?": "你会帮我们把钱拿回来吗？",
 "EMP interference over there.": "那边有电磁脉冲干扰。",
 "Hm.": "嗯。",
 "[breathing] Whew. Ok. Let's do this.": "[breathing] 呼。好。我们干吧。",
 "There. The field originates from that area. Let's go.":
    "那儿。场源来自那一片。我们走。",
 "Is it safe?": "安全吗？",
 "[to self] Let me know if you start hearing voices.":
    "[to self] 你要是开始听到声音了告诉我。",
 "It's all some kind of Psycho Gibberish...": "全是某种疯子胡话……",
 "What does it say?": "上面写了什么？",
 "[Gross] \"Smashed Meat Machine\"": "[Gross] “砸肉机”",
 "Okaaay.": "好——吧。",
 "Bandit Scribbles. It says Walkie Talkie.": "土匪涂鸦。写的是“对讲机”。",
 "This one looks like it says...": "这一个看着像是写着……",
 "[sigh] Hurry up.": "[sigh] 快点。",
 "Connect Blue Wire": "接蓝线",
 "Connect Red Wire": "接红线",
 "Connect Yellow Wire": "接黄线",
 "Pulled the blue wire.": "拔了蓝线。",
 "Dude! What the hell?": "老兄！搞什么？",
 "What was that? You're making me nervous.": "那是什么？你把我搞得紧张了。",
 "Fused. I'll leave that one alone.": "烧了。那个我就不动了。",
 "Take": "拿",
 "[to self] Rebooting. Okay, Guess I'll wait.":
    "[to self] 重启中。好，那我就等着。",
 "Does that mean you can call Fiona and Vaughn now?":
    "那是说你现在能给 Fiona 和 沃恩 打电话了吗？",
 "You must have missed something.\nCheck the pylons again.":
    "你肯定漏了什么。\n再检查一遍电力塔。",
 "[nervous]What's going on with Fiona and what's his face, Vaughn?":
    "[nervous]Fiona 和那个叫什么的，沃恩，他们怎么样了？",
 "You guys were going to buy a fake vault key, a con, I admire that. But Stealing really?":
    "你们本来要买一把假秘藏钥匙，是个骗局，我佩服。但偷？认真的？",
 "We were borrowing.": "我们是借。",
 "Impressed, huh?": "佩服了，哈？",
 "[Ignore her]": "[不理她]",
 "I'm not a thief like you.": "我不是你那种贼。",
 "We weren't technically *stealing.* We were borrowing the money til we sold the key.":
    "严格来说我们不是*偷*。我们是借那笔钱，等把钥匙卖掉再还。",
 "[sarcastic] Ah yes, \"Borrowing.\" Stealing's slightly prettier cousin.":
    "[sarcastic] 啊对，“借”。偷东西稍微好看点的表亲。",
 "Conning and Stealing, what the hell, like there's a difference?":
    "行骗和偷窃，搞什么，好像有区别似的？",
 "Oh please, conning requires skill and mark is voluntarily gives up the loot. Stealing is underhanded.":
    "哦拜托，行骗需要技巧，而且是目标自愿交出财物。偷窃是下三滥。",
 "No. You oh please.": "不。你才“哦拜托”。",
 "What? You and your's sister Fiona are the purest form of thiefs, stealing is stealing.":
    "什么？你和你妹妹 Fiona 就是最纯粹的贼，偷就是偷。",
 "Are you even listening?": "你到底在听吗？",
 "{HappyB}[irritated] Vaughn... I said get us out of here.":
    "{HappyB}[irritated] 沃恩……我说了把我们弄出去。",
 "You can't it's invisible.  It's an Electro Magne- nevermind.":
    "你不行，它是隐形的。是个电磁……算了。",
 "How can you see it if its invisible?": "如果它是隐形的，你怎么看得见？",
 "Echo Eye.": "ECHO 眼。",
 "Oh yeah. Should I shoot it?": "哦对。我该开枪打它吗？",
 "[nervous haha laugh] Wait.": "[nervous haha laugh] 等等。",
 "How's he involved in all this.": "他怎么掺和进这一切的。",
 "I don't like the way he looks. Like a mole or something.":
    "我不喜欢他那个样子。像只鼹鼠什么的。",
 "Get me out of here.": "把我弄出去。",
 "That's the tracking device right?": "那是追踪装置，对吧？",
 "Rhys! We need that lift down NOW!": "瑞斯！我们现在就需要那个升降台下来！",
 "[to self]It's coming from over there.": "[to self]信号从那边来。",
 "What is he to you?": "他对你来说是什么？",
 "Looks like it's controlled over here.": "看来是在这边控制的。",
 "[to self] Oh Gawd.": "[to self] 哦天。",
 "I don't understand you guys. I mean you have it easy up there. Riches, safety. Why come down here to Pandora and risk it all?":
    "我不理解你们这些人。我是说你们在上面过得轻松。富有、安全。干嘛下来到 潘多拉 冒这么大风险？",
 "I love money.": "我爱钱。",
 "My boss is a dick.": "我老板是个混蛋。",
 "It was a BIG mistake.": "这是个*大*错误。",
 "Down here there's actually *danger*.": "在下面才有真正的*危险*。",
 "Thanks, sorry about that and everything else. You're not bad after all.":
    "谢了，那事和其他事都抱歉。你终究不算坏。",
 "Thanks for the gun. I'd be a bitch too if someone was waving a gun around.":
    "谢了给枪。要是有人拿着枪乱挥，我也会变成个泼妇。",
 "[Awed] Awesome.": "[Awed] 太厉害了。",
 "I understand why you want to keep the gun. You've cool to me Rhys. Thanks.":
    "我理解你为什么想留着枪。你对我挺够意思，瑞斯。谢了。",
 "Keep the gun then. But you don't have to be a raging asshole.":
    "那就留着枪。但你不用当个狂暴混球。",
 "Don't worry. Vault Hunters don't talk to people like us.":
    "别担心。秘藏猎人不跟我们这种人说话。",
 "Ha. Vault Hunters don't talk to aholes. They usually just shoot them.":
    "哈。秘藏猎人不跟混球说话。他们一般直接开枪打他们。",
 "{FearC}Go ahead!": "{FearC}动手啊！",
 "{WorryA}There's *always* a need for violence here.":
    "{WorryA}在这儿*永远*有动武的理由。",
 "{NeutralB}Just give me the gun, okay?": "{NeutralB}把枪给我，行吗？",
 "{AngryC}Don't condescend to *me*, bootlicker.":
    "{AngryC}别对我居高临下，舔靴子的。",
 "{RageA}You think we just \"talk things out\" down here on Pandora?[beat] {FearB}I wouldn't be caught dead without this! [Sasha starts to fumble her thoughts a bit] {SadA}Or... I would be dead caught without this... Or... {AngryB}Whatever, just keep your distance jackass.":
    "{RageA}你以为我们在 潘多拉 这下面就是“把话谈开”？[beat] {FearB}我没这个就死路一条！[Sasha starts to fumble her thoughts a bit] {SadA}或者……没这个我就死得透了……或者……{AngryB}随便吧，你就保持距离，混蛋。",
 "Shows how much *you* know, Hyperion-Boy.":
    "可见*你*懂多少，亥博龙小子。",
 "[Nervous] So fix it, then.": "[Nervous] 那就修好它。",
 "Vaughn? Vaughn? Can you read me?": "沃恩？沃恩？能收到吗？",
 "Damn. Can't get a signal.": "该死。收不到信号。",
 "[Concentrating] Looks like... there's some sort of weird electromagnetic field down here. That must be what's jamming my comm.":
    "[Concentrating] 看来……这下面有某种奇怪的电磁场。肯定就是它干扰了我的通讯。",
 "Give me a second, give me a second...": "给我一秒钟，给我一秒钟……",
 "Can you, y'know, UNjam it?": "你能，呃，把它*解除*干扰吗？",
 "[Muttering to self] Some sort of localized electromagnetic field. Just gotta figure out its origin point.":
    "[Muttering to self] 某种局部电磁场。只要弄清它的源点就行。",
 "[To Sasha] Come on. It's coming from over there.":
    "[To Sasha] 来。信号从那边来。",
 "[To self] A-ha. There you are.": "[To self] 啊哈。找到你了。",
 "...and I'd rather not be stuck down here any longer than I have to be.":
    "……而且我不想在这下面多待一秒。",
 "[Exasperated] Just stop waving that gun around. You're making my nervous.":
    "[Exasperated] 别拿着那枪乱挥了。你把我搞得紧张了。",
 "A \"jiffy?\"": "“一眨眼？”",
 "Easy now. No need forWe'll be out of here in a jiffy.":
    "别急。不必——我们一眨眼就能出去。",
 "Well hurry up then.": "那就快点。",
 "Just give me some space. You and that gun are making me nervous.":
    "给我点空间。你和那把枪让我紧张。",
 "Don't worry. I'm on it.": "别担心。我在弄。",
 "Just hurry up and make yourself useful -- and find the others, okay?":
    "你快点、让自己有点用——然后找到其他人，行吗？",
 "I hope you know what you're doing.": "我希望你知道自己在干什么。",
 "This stuff looks *old*.": "这些东西看着很*老*。",
 "[Sharp gasp hearing something in the corner]": "[Sharp gasp hearing something in the corner]",
 "More gobbleydegook.": "又是些胡话。",
 "[Weird] \"Mommy's Little Earbox.\"": "[Weird] “妈妈的小耳箱。”",
 "[Wut.] \"Rise and Grind.\"": "[Wut.] “起来干活。”",
 "...annnnd in serious need of some repairs.": "……而且急需要修一修。",
 "Looks like those are the controls over there.": "看来那边就是控制台。",
 "[Satisfied] Boom! [beat] Sometimes I amaze me.":
    "[Satisfied] 砰！[beat] 有时候我自己都佩服自己。",
 "Man. I haven't seen tech like this since I was in school. This stuff's *old*...":
    "天哪。我上学之后就没见过这种技术了。这些东西*很老*……",
 "Until you're finished and I don't have to be trapped down here with you anymore.":
    "直到你弄完，我就不用再跟你困在这下面了。",
 "You do everything your sister tells you? How long are you gonna point that at me?":
    "你妹妹说什么你就做什么？你还要拿那玩意儿指着我多久？",
 "Do you even know what Hyperion means to us on Pandora?":
    "你到底知不知道 亥博龙对我们 潘多拉 人意味着什么？",
 "What the hell makes someone wanna join up with an outfit like that?":
    "到底是什么让人想去加入那种组织？",
 "The idea that anyone could follow *Handsome Jack* makes me sick.":
    "一想到有人会追随*帅杰克*，我就恶心。",
 "[Mocking] {HappyC}\"You know what I wanna be when I grow up? {FearB}A corporate stooge.\"":
    "[Mocking] {HappyC}“你知道我长大想当什么吗？{FearB}一个公司走狗。”",
 "{WorryA}It's crazy up there, too. Things actually aren't so {NeutralA}great at Hyperion right now...":
    "{WorryA}上面也乱得很。其实 亥博龙现在状况{NeutralA}不太好……",
 "{InquireA}His death was the {HappyA}best thing that ever happened to Pandora.":
    "{InquireA}他的死是{HappyA}潘多拉 发生过最好的事。",
 "{WorryB}Yeah? Feeling the weight of your corporate {WorryA}overlords, are ya? {SternC}[beat] Good.":
    "{WorryB}是吗？感受到你那些公司{WorryA}主子的分量了，是吧？{SternC}[beat] 很好。",
 "{SmugC}What section talks about killing {AngryB}anyone and anything that doesn't match with the Master Plan? {SternB}Huh, Rhys?":
    "{SmugC}哪一章讲杀掉{AngryB}任何不符合“大计划”的人和物？{SternB}啊，瑞斯？",
 "Order my ass. You're a bunch of murderers.": "秩序个屁。你们是一群杀人犯。",
 "[Sarcastic] {SmugA}Oh {ShockA}sorry. {SmugA}I guess talking about your evil corporate {SmugB}murder bosses can be a real {ShockA}concentration-killer.":
    "[Sarcastic] {SmugA}哦{ShockA}抱歉。{SmugA}我想谈论你们那些邪恶的公司{SmugB}杀人老板确实很{ShockA}打断专注。",
 "Can you lay off with the questions for a minute?":
    "你能停一会儿问题吗？",
 "Still. I'm surprised that a suit like you could even get up the stones to steal from \"Big Papa Hyperion.\"":
    "不过。我很惊讶像你这种西装货居然有胆量去偷“亥博龙大老爹”的东西。",
 "If you hadn't royally FUBAR'd me and Fiona's plans I'd be almost impressed.":
    "要不是你把我和 Fiona 的计划彻底搞砸了，我几乎就要佩服你了。",
 "We were *this close* to pulling it all off when you losers tromped through like a couple of drunk Bullymongs.":
    "你们这两个废物像两只喝醉的恶霸兽一样闯进来时，我们*就差这么一点*就全成了。",
 "We were going to pay it back.": "我们本来会还回去的。",
 "[Smirk] Impressed, huh?": "[Smirk] 佩服了，哈？",
 "That's high praise coming from a professional thief.":
    "这话从职业小偷嘴里说出来是高度赞美。",
 "[Correcting] \"Con artist.\" And please. I said *almost* impressed.":
    "[Correcting] “行骗艺术家。”还有拜托。我说的是*几乎*佩服。",
 "Don't lump me in with you and your sister - We're not *thieves*.":
    "别把我和你还有你妹妹归一类——我们不是*小偷*。",
 "[Scoff] Yeah, neither are we. We're \"con artists,\" asshole.":
    "[Scoff] 是啊，我们也不是。我们是“行骗艺术家”，混蛋。",
 "Why'd you guys try and pull something like that anyway?":
    "话说你们干嘛要搞那种事？",
 "Don't you all have, like, couches made of gold and diamond shoes up there on your moon base?":
    "你们在月球基地上不是有金子做的沙发和钻石鞋什么的吗？",
 "We have to *work* to survive.": "我们得*干活*才能活。",
 "What can I say? It was a brass ring and I went for it.":
    "我能说什么？那是个金环，我就去抓了。",
 "That much money on the line... who wouldn't try for that?":
    "那么一大笔钱摆在眼前……谁不会去试？",
 "It's not all sunshine and rainbows.": "不是一切都阳光彩虹。",
 "My boss is a total dick.": "我老板是个十足的混蛋。",
 "{ShockB}I mean you can't honestly stand there and pretend that Hyperion hasn't been responsible for *millions* of murders. {ShockB}[beat] Probably {FearC}billions.":
    "{ShockB}我是说，你不能站在那儿假装 亥博龙没有对*数百万*起谋杀负责。{ShockB}[beat] 也许是{FearC}数十亿。",
 "How do you even sleep at night knowing you work for grade-A assholes like that?":
    "知道自己给那种一等一的混蛋干活，你晚上怎么睡得着？",
 "{AngryB}Handsome Jack's done that and more.  {FearB}How could you follow a deranged lunatic like him?":
    "{AngryB}帅杰克干过那些，还有更多。{FearB}你怎么能追随他那种疯狂的精神病？",
 "[Disgusted] {sadA}Ugh. {AngryB}Screw you.": "[Disgusted] {sadA}呃。{AngryB}去你的。",
 "{WorryA}But I'm not him, okay? And I'm not responsible for what {WorryC}*he* did.":
    "{WorryA}但我不是他，行吗？我也不用为{WorryC}*他*做的事负责。",
 "{ThinkA}What Jack did was... {ThinkB}in a morally grey area. [beat] {SternA}At least.":
    "{ThinkA}Jack 做的事……{ThinkB}在道德上是灰色的。[beat] {SternA}至少。",
 "{NeutralA}You're right -- Jack was an asshole.  {SlyA}He didn't just ruin Pandora, he {SternC}also ruined Hyperion.":
    "{NeutralA}你说得对——Jack 是个混蛋。{SlyA}他不光毁了 潘多拉，他{SternC}也毁了 亥博龙。",
 "{SadB}Don't just keep ignoring me about this, Rhys. {SadA}Hyperion has a lot to answer for down here.":
    "{SadB}别一直在这件事上无视我，瑞斯。{SadA}亥博龙在这下面有很多账要交代。",
 "{SadA}God {SadB}people like you make me sick.":
    "{SadA}天哪{SadB}你这种人让我恶心。",
 "Why? It's all \"over my head?\"": "为什么？就都是“超出我理解范围”吗？",
 "[Quiet] It was a mistake. I just hope I can make everything okay now.":
    "[Quiet] 那是个错误。我只希望我现在能让一切好起来。",
 "He doesn't exactly seem like the \"embezzlement scheme\" type.":
    "他不太像搞“挪用公款计划”的那种人。",
 "How's that buddy of yours, Vaughn, fit into all this anyway?":
    "话说你那个哥们 沃恩 在这事里算什么？",
 "Follows you around.": "跟着你到处转。",
 "{SadB}The way he looks around with those little eyes of his behind those weird glasses. [beat] {ShockB}Follows you around.":
    "{SadB}他那双小眼睛躲在怪眼镜后面到处看的样子。[beat] {ShockB}就跟着你到处转。",
 "{WorryB}I sure wouldn't, guys like that creep me out.":
    "{WorryB}换我肯定不会，那种家伙让我发毛。",
 "Vaughn's none of your concern.": "沃恩 不关你的事。",
 "Then I'll just have to assume you're gonna stick a knife in my back the first chance you get, which is very much my concern.":
    "那我就只能认定你一有机会就会捅我背后一刀，而这非常关我的事。",
 "If he pulls his weight and does his part, then sure. A deal's a deal.":
    "要是他尽了自己的本分、做好他那份，那当然。说好的就是说好的。",
 "Of course I am.  He and I are in this together.":
    "当然是。他和我是一条船上的。",
 "Met him at the New Hire Ice Cream Social and we've been friends ever since.":
    "在新员工冰淇淋联谊会上认识他的，从那以后一直是朋友。",
 "I would've never expected that from someone like you.":
    "我从没想到你这种人会这样。",
 "[Beat] For Hyperion scum, that is.": "[Beat] 我是说，对 亥博龙渣滓来说。",
 "{ShockB}Um, what the hell was that?": "{ShockB}呃，那他妈是什么？",
 "{SadA}Allright, that's kind of impressive. {ShockB}But, how do I know you're not going to start up some sort of, I don't know, {ShockA}death machine and then leave me down here with it?":
    "{SadA}好吧，那还挺厉害的。{ShockB}但我怎么知道你不会启动什么，我不知道，{ShockA}死亡机器，然后把我跟它留在这儿？",
 "{SlyA}Relax. It's just one of the {SlyC}power systems starting up --":
    "{SlyA}放松。只是其中一个{SlyC}电力系统启动了——",
 "Typical Hyperion crap.": "典型的 亥博龙破烂。",
 "{FearA}Then you'll go back to Fiona with some sob story about{AngryC} \"oh boo hoo I tried to save her...\"":
    "{FearA}然后你会回去跟 Fiona 哭诉{AngryC}“哦呜呜我想救她来着……”",
 "{SmugA}Don't be ridiculous.": "{SmugA}别荒唐了。",
 "{AngryB}Hey. {ThinkB}I'm not the threat here. In case you've forgotten I'm the one trying to get us {ShockC}*out* of this [beat] and {SternC}you're the one with the gun.":
    "{AngryB}嘿。{ThinkB}我在这儿不是威胁。你要是忘了：我才是那个想把我们{ShockC}*弄出去*的人[beat]，而{SternC}拿着枪的是你。",
 "Stop freaking out and back off.": "别慌了，退后。",
 "[Thru heavy static] ...think it was Rhys...":
    "[Thru heavy static]……我想是 瑞斯……",
 "[Thru heavy static] ....Sasha?....": "[Thru heavy static]……萨莎？……",
 "{ShockA}Come on Rhys.": "{ShockA}来吧 瑞斯。",
 "Is that them?": "是他们吗？",
 "{AngryC}Put me on. I wanna talk to Fiona.":
    "{AngryC}把通讯给我。我要跟 Fiona 说话。",
 "Reeeally need you to open that hatch.": "真的、真的很需要你把那舱门打开。",
 "We're in a big metal room.": "我们在一间很大的金属屋里。",
 "{FearB}Vaughn. Are you still outside? If you are, {AngryC}open up the damn hatch.":
    "{FearB}沃恩。你还在外面吗？要是在，{AngryC}把那该死的舱门打开。",
 "{SadC}So... yeah... we're trapped in a dark, scary room down below here.{FearB}":
    "{SadC}所以……是啊……我们被困在下面一个又黑又吓人的房间里。{FearB}",
 "[Whispers] {ShockC}And this Sasha freak is {RageA}totally *crazy*.":
    "[Whispers] {ShockC}而且这个叫 萨莎 的怪胎 {RageA}完全*疯了*。",
 "Uh, yeah, so I don't know if any of that came through. But we're in...uh...it says...":
    "呃，是啊，我不知道那些有没有传过去。但我们在……呃……上面写着……",
 "Well I hope they heard any of --": "好吧，我希望他们听到了哪怕一点——",
 "{FearC}Gah!": "{FearC}嘎！",
 "{HappyA}Here.": "{HappyA}给。",
 "Oh. Thanks.": "哦。谢了。",
 "[Scoff] Jerk.": "[Scoff] 混蛋。",
 "{NeutralB}I'm gonna hang onto this for you.":
    "{NeutralB}我替你收着这个。",
 "Careful. Or I might just change my mind about you being total scum, Hyperion-Boy.":
    "小心点。不然我可能就改主意，不再觉得你是彻底的渣滓了，亥博龙小子。",
 "Pffft. Don't dork this up. You're still not off my crap list.":
    "嗤。别搞肉麻。你还在我的黑名单上。",
 "Think of it like an olive branch.": "就当这是一枝橄榄枝。",
 "Yeah. I get that. Sorry if I seemed a little... trigger-happy earlier.":
    "是啊。我明白。抱歉我刚才看起来有点……爱扣扳机。",
 "Fine. Guess you really ARE nothing but a raging asshole.":
    "行。看来你确实就是个狂暴混球。",
 "{SchemeB}Come on pal -- do your {ShockB}hacky thing.":
    "{SchemeB}来吧哥们——施展你那{ShockB}黑客本事。",
 "It's right above us.": "就在我们头顶上。",
 "Wait -- that means the case is on the move, right?":
    "等等——那就是说箱子在移动，对吧？",
 "Let's go then!": "那我们走！",
 "Bet it'd make a nice backscratcher.": "打赌它当挠背器不错。",
 "[Re: Rhys] That arm of yours detachable, boy?":
    "[Re: Rhys] 你那条手臂能拆下来吗，小子？",
 "Well well well, who let you ickle delights in here?":
    "哎呀呀，是谁把你们这些小可爱放进来的？",
 "[Quietly] What did I miss...?": "[Quietly] 我错过了什么……？",
 "I've got it - Don't worry!": "我搞定了——别担心！",
 "I thought you were supposed to be some master hacker! What did you miss?":
    "我以为你是什么大师级黑客！你漏了什么？",
 "{SlyB}A-ha! Got it!": "{SlyB}啊哈！搞定！",
 "Aw where you going pretties? Stay and play.":
    "哎呀你们要去哪儿，小美人？留下来玩玩嘛。",
 "{FearB} That's not making things better!": "{FearB} 那没让情况变好！",
 "Just, uh... stay out of their way.": "就，呃……别挡他们的路。",
 "{FearB} Oh, great.": "{FearB} 哦，好极了。",
 "Rhys... *come on*.": "瑞斯……*快点*。",
 "{HappyA}Oh good. At least {FearA}now when we die it'll have a nice {RAgeB}soundtrack.":
    "{HappyA}哦好。至少{FearA}现在我们死的时候会有个不错的{RAgeB}配乐。",
 "{ThinkA}Hang on, hang on, I've almost got it.":
    "{ThinkA}等等，等等，我快搞定了。",
 "{FearB}Rhys! Let's go! Getting caught in the middle of a skag/bandit fight is NOT on my bucket list.":
    "{FearB}瑞斯！我们走！被卷进异犬和土匪的混战可*不*在我的遗愿清单上。",
 "[Awed, whispered] Holy crap. Rhys. It's Zero.":
    "[Awed, whispered] 我的天。瑞斯。是 Zer0。",
 "{FearA}No! I thought that was you!": "{FearA}不！我以为那是你！",
 "{SternB}We're moving. Did you push a {ThinkB}button or something?":
    "{SternB}我们在动了。你按了个{ThinkB}按钮还是怎么着？",
 "[after an INTENSE moment,Trying to be cool but failing] I could've done that...":
    "[after an INTENSE moment,Trying to be cool but failing] 我本来也能办到……",
 "Thank you, Mr...? I'm sorry, I didn't catch your name.":
    "谢谢你，先生……？抱歉，我没听清你的名字。",
 "[Sarcastic, aside] Nice one, asswipe.": "[Sarcastic, aside] 干得漂亮，混球。",
 "[Endeared] Wowww you're a dork.": "[Endeared] 哇——你真是个书呆子。",
 "Ah shuddup.": "啊，闭嘴。",
 "Get away from that!": "离那个远点！",
 "{SternB}What the?": "{SternB}搞什么？",
 "[off screen] Hey!": "[off screen] 嘿！",
 "Dark tunnels. [beat] On Pandora, that never ends well.":
    "漆黑的隧道。[beat] 在 潘多拉，这从来没有好下场。",
 "Damn it Fiona, don't leave me all alone down here with this Hyperion asshole!":
    "该死 Fiona，别把我一个人跟这个 亥博龙混蛋留在这下面！",
 "{SadA} I wonder what this place was for.": "{SadA} 我在想这地方原来是干什么的。",
 "'Cause I certainly don't trust you.": "因为我当然不信你。",
 "{FearA}It's freakin' me out.": "{FearA}这让我发毛。",
 "{NeutralB}You wouldn't. 'Cause there's really {AngryB}no need for violence here.":
    "{NeutralB}你不会的。因为这儿真的{AngryB}没必要动武。",
 "{SlyA}I'll just -- hold on to it for you. [beat]{SternB}Until you calm down.":
    "{SlyA}我就——替你收着。[beat]{SternB}等你冷静下来。",
 "There's nothing down here to worry about.": "这下面没什么好担心的。",
 "I don't like being down here.": "我不喜欢待在这下面。",
 "And you're from Hyperion.": "而你是 亥博龙的人。",
 "I know you're from Hyperion. And were dumb enough to try and buy a *fake* vault key.":
    "我知道你是 亥博龙的。而且蠢到想买一把*假*秘藏钥匙。",
 "I'm gonna get you killed?  You don't even know me.":
    "我会害死你？你根本不了解我。",
 "*I* don't like being stuck down here with you, either. Okay?":
    "*我*也不喜欢跟你困在这下面。行吗？",
 "So let's get out of here as quickly as possible.":
    "所以我们尽快离开这儿吧。",
 "Feel however you like, just don't shoot me, alright?":
    "你爱怎么想怎么想，只是别开枪打我，行吗？",
 "Don't give me a reason to, and we'll be just fine.":
    "别给我理由，我们就相安无事。",
 "Sure. Just don't try anything funny.": "当然。只是别耍花样。",
 "Let's just focus on finding the others, getting out of here, and getting that money.":
    "我们专心地找到其他人、离开这儿、拿到那笔钱。",
 "Like you said, we need to find the others.": "就像你说的，我们得找到其他人。",
 "So fix it, then.": "那就修好它。",
 "Come on, fix the thing already, will ya?": "快点，把东西修好，行吗？",
 "Not yet.  But if I can get this computer working, maybe I can patch into the local network, and then we're in business.":
    "还没有。但如果我能让这台电脑运转起来，也许就能接进本地网络，那我们就有着落了。",
 "Then let's just get out of here as quickly as possible. [mocking Rhys's 'Okay'] Okay?":
    "那我们就尽快离开这儿。[mocking Rhys's 'Okay'] 行吗？",
 "And follow a deranged lunatic like *Handsome Jack*?":
    "还追随*帅杰克*那种疯狂的精神病？",
 "{WorryC}It's called the {WorryB}employee handbook.":
    "{WorryC}那叫{WorryB}员工手册。",
 "I guess some of you guys up there are also \"the little people\".":
    "我想你们上面有些人也是“小人物”。",
 "But still...": "但还是……",
 "{FearA}*We're* the bandits and lowlives he {WorryB}was killing !":
    "{FearA}*我们*才是他在杀的那些土匪和渣滓！",
 "{AngryB}Maybe not, but you still profited from it.":
    "{AngryB}也许不是，但你仍然从中获利。",
 "And I'm not responsible for what *he* did.": "而我不为*他*做的事负责。",
 "{SternB}So don't compare me to that jerk, alright?":
    "{SternB}所以别拿我跟他比，行吗？",
 "{ShockB}Wow, I-- I was {NeutralA}not expecting that...":
    "{ShockB}哇，我——我{NeutralA}没想到会这样……",
 "Maybe you're not so bad after all.": "也许你终究没那么坏。",
 "{SadA}Jack ruined everything, Rhys.{ShockB} *Everything.*":
    "{SadA}Jack 毁掉了一切，瑞斯。{ShockB} *一切。*",
 "No sense in holding it against you...": "也没道理因此怪你……",
 "{HappyB}Oh, {AngryB}I'm sorry -- is my upset over the deaths of {FearC}millions of Pandorans breaking your concentration?[beat] Oh, {RageA}boo frickin' hoo.":
    "{HappyB}哦，{AngryB}抱歉——我为{FearC}数百万 潘多拉 人的死而难过，是不是打断了你的专注？[beat] 哦，{RageA}可怜的小可怜。",
 "God people like you make me sick.": "天哪，你这种人让我恶心。",
 "{SmugB}I know what you're thinking: {SternB}\"he was just bringing order\",{WorryA} right?":
    "{SmugB}我知道你在想什么：{SternB}“他只是带来秩序”，{WorryA}对吧？",
 "That way you could stay nice and comfy up there on your moonbase.":
    "这样你们就能舒舒服服地待在月球基地上。",
 "Why not send a robot or something?": "干嘛不派个机器人还是什么的？",
 "{WorryA}Why risk your neck coming down to Pandora?":
    "{WorryA}干嘛冒着脖子上的风险下来 潘多拉？",
 "Why would anyone do something like that?": "怎么会有人干那种事？",
 "{InquireB}Why not stay home nice and comfy up there on your moonbase, {ShockB}climbing the corporate ladder?":
    "{InquireB}干嘛不留在家、舒舒服服待在月球基地上，{ShockB}爬你的公司阶梯？",
 "Which we all know just leads to more trouble.":
    "大家都知道那只会带来更多麻烦。",
 "{AngryB}Look... I know you're a Hyperion goon and all you care about is money, but even so...":
    "{AngryB}听着……我知道你是 亥博龙的打手，只在乎钱，但即便如此……",
 "{WorryB}Look... You're not the worst Hyperion scumbag I've ever run into, so...":
    "{WorryB}听着……你不是我遇到过最烂的 亥博龙渣滓，所以……",
 "Or were you just following orders?": "还是你只是奉命行事？",
 "{FearA}Do you have any idea how much a {FearB}*real* vault key is {FearA}worth? What it means to {FearB}open a vault?":
    "{FearA}你知道一把{*真的*}秘藏钥匙{FearA}值多少吗？打开一个秘藏{FearB}意味着什么？",
 "{InquireA}I've heard the stories. [beat] {ShockB}And I sure wouldn't mind finding out for myself.":
    "{InquireA}那些传说我听过。[beat] {ShockB}而且我也不介意亲自弄个明白。",
 "{SlyB}If I brought a vault key back up to Hyperion...":
    "{SlyB}要是我把一把秘藏钥匙带回 亥博龙……",
 "The next great leader -- and hero -- of Hyperion.":
    "亥博龙下一任伟大的领袖——兼英雄。",
 "{ShockB}No... I'd be {HappyB}*better* than Handsome Jack.  {HappyA}*I* wouldn't screw everything up.":
    "{ShockB}不……我会比帅杰克{HappyB}*更强*。{HappyA}*我*不会把一切都搞砸。",
 "{SlyA}They'd make me President {SlyB}*and* CEO.  {AngryA}Hyperion would be mine.":
    "{SlyA}他们会让我当总裁{SlyB}*兼* CEO。{AngryA}亥博龙就是我的了。",
 "{SlyB}I'd be the next Handsome Jack.": "{SlyB}我会是下一个帅杰克。",
 "{SmugB}You're already an asshole, {SmugA}so you're halfway there.":
    "{SmugB}你已经是混蛋了，{SmugA}所以你已经走到一半了。",
 "{SchemeB}That would be a nice change from Hyperion.":
    "{SchemeB}那会是相对 亥博龙的一个不错的变化。",
 "{SternA}You can have it.": "{SternA}随你。",
 "{WorryC}Vasquez screwed me over, I {ShockC}was just trying to return the favor.":
    "{WorryC}Vasquez 坑了我，我{ShockC}只是想还他个人情。",
 "{SadA}So you're an asshole to eveyone{InquireB} -- not just me?":
    "{SadA}所以你对所有人都混蛋{InquireB}——不只是对我？",
 "{InquireA}I gues we all have our reasons... but I {InquireB}still don't exactly trust yours.":
    "{InquireA}我想我们都有各自的理由……但我{InquireB}还是不太信你的。",
 "What about tha": "那……",
 "And then there's you and that guy Vaughn... I've seen this kinda thing before.":
    "然后还有你和你那个 沃恩……这种事我见过。",
 "{SchemeC}He's your loyal best friend now, {SchemeB}while you're a couple of nobodies.":
    "{SchemeC}他现在是你忠实的好朋友，{SchemeB}而你们俩都还什么都不是。",
 "{SchemeC}He's your obedient little lapdog now, {SchemeB}while you're a couple of nobodies.":
    "{SchemeC}他现在是你听话的小跟班，{SchemeB}而你们俩都还什么都不是。",
 "{SchemeC}He's your fully committed business associate now, {SchemeB}while you're a couple of nobodies.":
    "{SchemeC}他现在是你全心投入的生意伙伴，{SchemeB}而你们俩都还什么都不是。",
 "{SmugB}Are you really planning to share all that money with him?":
    "{SmugB}你真打算把那笔钱都跟他分？",
 "{ShockC}But what if you do pull off that big score one day?":
    "{ShockC}但要是你哪天真的干成了那一大票呢？",
 "{SmugB}Are you really going to share that power with him when you're running Hyperion?":
    "{SmugB}等你掌管 亥博龙了，你真打算跟他分享那份权力？",
 "{SmugB}Are you really going to share that glory with him?":
    "{SmugB}你真打算跟他分享那份荣耀？",
 "{SmugB}Are you really going to share the spoils with him?":
    "{SmugB}你真打算跟他分享那些战利品？",
 "{FearA}Well he *is* my best friend.": "{FearA}这个，他*确实*是我最好的朋友。",
 "We met in freshman math class and have been friends ever since.":
    "我们在大一数学课上认识，从那以后一直是朋友。",
 "Hey, that's actually kinda sweet": "嘿，那其实还挺暖的",
 "So Hyperion's a meritocracy. Yeah, right.": "所以 亥博龙是唯才是举。是啊，才怪。",
 "{ShockA}I don't think so.": "{ShockA}我不这么认为。",
 "{SlyC}That was the machine turning on.": "{SlyC}那是机器启动了。",
 "{WorryB] Give me a heads up next time if you don't want to get shot.":
    "{WorryB] 下次不想挨枪子就提前跟我说一声。",
 "{SternA}That was just a machine turning on.": "{SternA}那只是机器启动了。",
 "{InquireA}Just hurry up and get us {WorryA}out of here.":
    "{InquireA}你就快点把我们{WorryA}弄出去吧。",
 "{SlyC}Of course it'll work, I'm a genius with machines.":
    "{SlyC}当然会管用，我是机械天才。",
 "{InquireB}I thought the only way to do that was spree killing.":
    "{InquireB}我以为唯一的办法是连环杀人。",
 "{SmugC}That's how I rose up the ranks at Hyperion.":
    "{SmugC}我就是这么在 亥博龙升上去的。",
 "{ThinkA}Beats me.  I {ThinkB}turned it on, but we gotta give it a go and see what happens.":
    "{ThinkA}不知道。我{ThinkB}把它启动了，但只能试试看会怎样。",
 "{SadA}If this thing just fills the room with death rays -- {SadB}I'm gonna be very disappointed in you, Rhys.":
    "{SadA}要是这东西只是往屋里灌死光——{SadB}那我会对你非常失望，瑞斯。",
 "{SternD}It's never going to work if you keep bugging me while I try to get it working.":
    "{SternD}我在这儿想办法弄好它，你一直烦我，那它永远不会成。",
 "{AngryB}And to think I was starting to actually like you.":
    "{AngryB}想想我居然开始真的喜欢你了。",
 "{ShockA}Holy crap, you got that thing working?":
    "{ShockA}我的天，你把那玩意儿弄好了？",
 "I thought it was [pause to think] I dunno, something bad.":
    "我以为那是[pause to think] 我不知道，什么坏东西。",
 "{ShockB}So this is gonna {ShockC}work, then?":
    "{ShockB}那这真会{ShockC}管用了？",
 "{ShockC}We're finally going to be able to get in touch with our friends and get out of here now?":
    "{ShockC}我们终于能联系上我们的朋友、离开这儿了？",
 "[filtered]\tSystem online. Init Gortys lab control protocols.":
    "[filtered]\t系统上线。初始化 戈提斯 实验室控制协议。",
 "I hope they heard us.": "我希望他们听到了我们。",
 "It's as good as we've got right now.": "这是我们目前能想到最好的了。",
 "That's it?": "就这样？",
 "{NeutralA}I'm really not an ogre, you know.":
    "{NeutralA}我真不是个怪物，你知道。",
 "{FearA}Really?": "{FearA}真的？",
 "{WorryA}Thanks.": "{WorryA}谢了。",
 "{AngryB}Of course you are. I should've known.":
    "{AngryB}当然是。我早该知道。",
 "Yeah, I get it. [beat] I haven't exactly been responsible with it down here.":
    "是啊，我明白。[beat] 我在这下面确实不太负责任。",
 "{ShockB}Wow. That's the last thing I ever expected *you* to do.":
    "{ShockB}哇。这是我*最*没想到*你*会做的事。",
 "{SadA}Alright, Rhys. For a Hyperion toadie -- {InquireB}you're not such a bad guy.":
    "{SadA}好吧，瑞斯。作为一个 亥博龙走狗——{InquireB}你人还不算太坏。",
 "{FearA}We're gonna try to find a way out of this place and come find you. So just hang in there, wherever you are.":
    "{FearA}我们会想办法从这地方出去，然后来找你们。所以不管你们在哪儿，撑住。",
 "We're in a room that says Hanger 19 on the wall and... It smells... really bad. Like dead animals [beat] or really awful living ones.":
    "我们在一个墙上写着十九号机库的房间里，而且……闻起来……特别糟。像死掉的动物[beat] 或者特别恶心的活物。",
 "{SadB}That keeps making weird noises.": "{SadB}那东西一直发出怪声。",
 "{FearB}Or wherever you are -- *come get us out of here*.":
    "{FearB}或者不管你在哪儿——*来把我们弄出去*。",
 "{AngryC}Before this fascist gets me killed.":
    "{AngryC}趁这个法西斯还没把我害死。",
 "I think you think that means something different than it does on Pandora.":
    "我觉得你以为它的意思跟在 潘多拉 上的意思不一样。",
 "Totally.": "绝对的。",
 "[whispered to Rhys] Well... he's not killing us.":
    "[whispered to Rhys] 这个嘛……他还没杀我们。",
 "[not actually angry] Shaddup.": "[not actually angry] 闭嘴。",
 "[teasing] That was so dorky.": "[teasing] 刚刚那太书呆气了。",
 "Smooth move, jackass.": "真溜的一手，蠢驴。",
 "But if you'd like to, say, maim this guy don't let me stop you.":
    "但你要是想，比如说，把这家伙弄残，别让我拦着你。",
 "Pathetic.": "可悲。",
 "Idiot.": "白痴。",
 "Maybe just let me throw the gang signs while we're on Pandora, okay?":
    "也许在 潘多拉 的时候就让我来打帮派手势，行吗？",
 "You're going to get somebody killed.": "你会害死人。",
 "Room 9A...Gortys Prototype Calibration...yeah.":
    "9A 房间……戈提斯 原型校准……对。",
 "Hey, what the hell?": "嘿，搞什么？",
 "I don't like this one bit.": "我一点都不喜欢这样。",
 "I don't like this one bit...": "我一点都不喜欢这样……",
 "{NeutralA}Fiona may think {HappyB}teaming up with you and your little crony is a *profitable* idea, {SadA}but *I* think you're just gonna get us killed.":
    "{NeutralA}Fiona 也许觉得{HappyB}跟你和你那小跟班合作是个*划算*的主意，{SadA}但*我*觉得你只会把我们害死。",
 "So I've got my eye on you.": "所以我会盯着你。",
 "People like you [spits] ruined Pandora.": "你这种人 [spits] 毁了 潘多拉。",
 "I already told you to put that damn thing away -- or I'll take it away.":
    "我已经跟你说过把那鬼东西收起来——不然我就拿走。",
 "There's a door and a lift, both locked-out.": "有一扇门和一部升降台，都被锁死了。",
 "Nothing's powered up down here.  We need to find the power system.":
    "这下面什么都没通电。我们得找到电力系统。",
 "Then you better get it working.": "那你最好把它弄好。",
 "{NeutralA}Aha! Up there, looks like that might be the relays.":
    "{NeutralA}啊哈！上面，那看着可能是继电器。",
 "We find the others and get that *money*, and you'll never have to see me again.":
    "我们找到其他人、拿到那*笔钱*，你就再也不用见到我了。",
 "I will. [looking around]I just need to find the power relays.... Do me a favor. Keep an eye out.":
    "我会的。[looking around]我只是得找到电力继电器……帮我个忙。帮我盯着点。",
 "So, a big light switch.": "所以，一个大电灯开关。",
 "Go ahead.  Give me a reason to shoot you, big man.":
    "动手啊。给我个开枪打你的理由，大个子。",
 "Yep. Those are Atlas power relays alright -- but they're dead.":
    "对。那些确实是阿特拉斯电力继电器——但它们没电了。",
 "That exactly what I'm about to try. And I'm *telling you* so that when I walked over there to do it, you don't shoot me for doing something [air quotes] \"suspicious\".":
    "我正要试的就是那个。我*跟你说一声*，这样我走过去操作的时候，你不会因为我在做某种[air quotes]“可疑”的事就开枪打我。",
 "What are you telling me for?  Just go make them come alive again.":
    "你跟我说这个干嘛？去让它们活过来就行。",
 "{ShockD}Okay, okay - -I've got it...": "{ShockD}好，好——我搞定了……",
 "{HappyB}Yes!": "{HappyB}太好了！",
 "{FearB}No!": "{FearB}不！",
 "Ugh! You and your big, psychotic mouth.": "呃！你和你那张又大又疯的嘴。",
 "Woeful sorrow of unintended consequences.": "意外后果的悲惨悲伤。",
 "Calling all meat blossoms! It's we-murder-you time! [ run we-murder-you together as one word]":
    "呼叫所有肉花儿！到我们宰你们的时间了！[ run we-murder-you together as one word]",
 "Skagtastic death puppies! [beat] Eating the face off my face! Aiiiigh!":
    "异犬味的死亡小狗！[beat] 把我脸上的脸吃掉！啊啊啊！",
 "{WorryB}Zer0, buddy, nice to meet you.": "{WorryB}Zer0，哥们，很高兴认识你。",
 "I gotta say -- nice job.": "我得说——干得漂亮。",
 "{FearA}Or at least get that door open. Just {AngryC}get us out of here so we can {FearB}get to that case.":
    "{FearA}或者至少把门打开。就{AngryC}把我们弄出去，好让我们{FearB}去拿那只箱子。",
 "It is indeed the power relay.  Rather, one of them.  The system needs all three working before it'll come online.":
    "这确实是电力继电器。更确切说，是其中一个。系统需要三个都工作才能上线。",
 "{InquireA}And here I thought you might be different than all those other Hyperion bootlickers. {InquireB}Guess I was wrong.":
    "{InquireA}我还以为你可能跟其他那些 亥博龙舔靴子的不一样。{InquireB}看来我错了。",
 "You're kidding me. [beat] Hey!": "你开玩笑吧。[beat] 嘿！",
 "You think that gibberish will help them find us?":
    "你觉得那串胡话能帮他们找到我们？",
 "{RageA}So... come find us.  [beat] {AngryB}Nowish.":
    "{RageA}那……来找我们。[beat] {AngryB}就现在。",
 "{ShockC}Room 9A, Gortys Prototype Assembly.":
    "{ShockC}9A 房间，戈提斯 原型装配区。",
 "{WorryB}Yeah. So. Don't know if any of this is even coming through, but {SadB}we're in... uh...":
    "{WorryB}是啊。那么。不知道这些有没有传过去，但{SadB}我们在……呃……",
 "\"ROOM 9A": "“9A 房间",
 "GORTYS PROTOTYPE \"": "GORTYS 原型”",
 "Atlas, Hyperion -- all the same to me.": "阿特拉斯、亥博龙——对我来说都一样。",
 "Sure, whatever.": "当然，随便。",
 "[considering]Maybe, but...[geeking out] This is all old Atlas tech.":
    "[considering]也许吧，但……[geeking out] 这全是老阿特拉斯技术。",
 "Sure. Something like that.": "当然。差不多吧。",
 "{AngryB}Damn it, no signal.": "{AngryB}该死，没信号。",
 "{InquireB}So as usual, the only place left to go is down.":
    "{InquireB}所以跟往常一样，最后只能往下走。",
 "And I especially don't like being stuck down here with you.":
    "而且我特别不喜欢跟你困在这下面。",
 "{InquireB}There's you.": "{InquireB}还有你。",
 "Hey, jackass.  I'm talking to you.": "嘿，蠢驴。我在跟你说话。",
 "I don't care what Fiona told you, that money is ours.":
    "我不管 Fiona 跟你说了什么，那笔钱是我们的。",
 "Hyperion owes everyone on Pandora, and I intend to collect.":
    "亥博龙欠 潘多拉 上每个人，我打算去收。",
 "The hell it is! That money belongs to Hyperion, which means it belongs to me.":
    "放屁！那笔钱属于 亥博龙，也就是说它属于我。",
 "There's nothing more to deal with. Money. Ours.":
    "没什么好再谈的。钱。我们的。",
 "We'll deal with all that later. We need to get out of here first.":
    "那些我们以后再说。我们得先离开这儿。",
 "Actually, at the moment, it's technically neither of ours.":
    "其实，此刻严格来说它不属于我们任何一方。",
 "Keep tempting me, smart guy.": "继续激我，聪明人。",
 "Basically, you're ours now, too. Without us, you won't survive another ten minutes on Pandora.":
    "基本上，你现在也是我们的了。没有我们，你在 潘多拉 上撑不过十分钟。",
 "Sure, whatever.[beat] Look, I'm gonna scan this place and see if I can get us out of here.  So if you want out, don't shoot me.":
    "当然，随便。[beat] 听着，我要扫描一下这地方，看能不能把我们弄出去。所以你要是想出去，就别开枪打我。",
 "Look -- that lift, that locked door, and everything in this whole sector must be controlled by those computers, which are offline. You want out? Help me find the power relays.":
    "听着——那部升降台、那扇锁着的门，以及这整个区域的一切，肯定都由那些电脑控制，而它们离线了。你想出去？帮我找到电力继电器。",
 "Alright, let's get this relay cleared.": "好，我们把这个继电器清理出来。",
 "If it doesn't complain to Atlas, not me.": "只要它不向阿特拉斯投诉，就不怪我。",
 "This better work.": "这最好管用。",
 "Good.": "好。",
 "{NeutralA}Neither would I -- but thanks to {AngryA}you, I'll be lucky if I end up mopping {ThinkB}floors.":
    "{NeutralA}我也不会——但多亏{AngryA}你，我最后能去拖{ThinkB}地板就算走运了。",
 "{SternB}I'd be all the way there if it weren't for you.":
    "{SternB}要不是你，我早就爬到顶了。",
 "{SternD}Well, thanks to you, that's not gonna happen.":
    "{SternD}好吧，多亏你，那不会发生了。",
 "{AngryB}Well thanks to you, I never will.":
    "{AngryB}好吧，多亏你，我永远也到不了。",
 "{AngryA}Well thanks to you, Vasquez is gonna squash me like {FearB}a bug.":
    "{AngryA}好吧，多亏你，Vasquez 会像捏{FearB}虫子一样捏碎我。",
 "So you're partners, huh? I didn't think that was a Hyperion concept.":
    "所以你们是搭档，哈？我以为 亥博龙没这个概念。",
 "{NeutralB}A concept {FearB}*you people* clearly wouldn't understand.":
    "{NeutralB}一个{FearB}*你这种人*显然不会懂的概念。",
 "{FearA}Finally. Let's get this over with and get out of here.":
    "{FearA}终于。我们把这了结，然后离开这儿。",
 "{InquireA}I hate to admit it, but {InquireB}that was kind of impressive.":
    "{InquireA}我不想承认，但{InquireB}那还挺厉害的。",
 "So the machine did a thing... and?": "所以机器干了件事……然后呢？",
 "{SternB}Alright, time to see what this puppy can do for us.":
    "{SternB}好，看看这小家伙能为我们做什么。",
 "{FearA}But it's just my way of {SmugC}joking around. [Awkward laugh]":
    "{FearA}但这就是我{SmugC}开玩笑的方式。[Awkward laugh]",
 "{FearA}I, uh, might've been a bit harsh back there.":
    "{FearA}我，呃，刚才可能有点刻薄。",
 "{SadA}I should've shot you as soon as you turned that thing on.":
    "{SadA}你一启动那玩意儿我就该开枪打你。",
 "Now we just wait for Fiona and Vaughn to come find us, I guess.":
    "现在我们就等 Fiona 和 沃恩 来找我们吧，我想。",
 "Alright, Rhys, maybe you're not completely terrible. [She holsters her gun] I guess we can *try* to work together.":
    "好吧，瑞斯，也许你没那么糟。[She holsters her gun] 我想我们可以*试着*合作。",
 "{NeutralB}There's a lift right over there.  Let's go.":
    "{NeutralB}那边就有一部升降台。我们走。",
 "And why *did* you and Fiona screw us over with that forged vault key?":
    "还有你和 Fiona 到底*为什么*要用那把伪造的秘藏钥匙坑我们？",
 "{SadB}Anyway, {SternC}it's cute that you're taking it so {SmugA}personally.":
    "{SadB}总之，{SternC}你把它看得这么{SmugA}个人化，还挺可爱的。",
 "{FearB}Taking it personally?  {AngryB}You're the one pointing a gun {FearB}at *me*.":
    "{FearB}个人化？{AngryB}拿枪指着{FearB}*我*的人是你。",
 "{SadA}'Cause I know what {ShockC}you are. Take you and that guy Vaughn for instance --{WorryA} I've seen that sort of thing before.":
    "{SadA}因为我知道{ShockC}你是什么。就拿你和你那个 沃恩 来说——{WorryA}那种事我见过。",
 "{FearA}*We* wanted to screw over some local sucker. {AngryB}August and Vallory are the ones that brought *you people* into it.":
    "{FearA}*我们*本来想坑某个本地的冤大头。{AngryB}把*你们这种人*扯进来的是 August 和 瓦洛里。",
 "{WorryA}You're were just a couple Hyperion marks to us.":
    "{WorryA}对我们来说你们只是几个 亥博龙的肥羊。",
 "{SadA}It seemed like a brilliant idea at the time.":
    "{SadA}当时看起来是个绝妙的主意。",
 "{HappyA}And since we at least sort-of contacted Fiona and Vaughn, {InquireA}now all we have to do is -- {FearA}[gets cut off] find a way...":
    "{HappyA}既然我们至少算是联系上了 Fiona 和 沃恩，{InquireA}现在我们要做的只是——{FearA}[gets cut off] 想办法……",
 "Looks like we're stuck together for a while longer.":
    "看来我们还得凑在一起一阵子。",
 "So you're *not* just gonna shoot me in the -- [gets cut off] face.":
    "所以你*不*打算朝我——[gets cut off] 脸上开枪了。",
 "So...": "那么……",
 "{WorryB}Ugh. You're disgusting.": "{WorryB}呃。你真恶心。",
 "{SlyC}They all do, of course.": "{SlyC}当然，他们都这样。",
 "{SmugA}It's not like that.": "{SmugA}不是那样的。",
 "{WorryA}Have you taken a look around since you got down here?  {ShockA}It's exactly like that.":
    "{WorryA}你下来之后看过周围吗？{ShockA}就是这样。",
 "{WorryC}Pandora's made you insane.": "{WorryC}潘多拉 把你弄疯了。",
 "{SternC}And Hyperion's made you evil. {SternA}So I guess we're even.":
    "{SternC}而 亥博龙把你弄恶了。{SternA}那我想我们扯平了。",
 "Sure, whatever. [beat] Just help me find a way out of here.":
    "当然，随便。[beat] 帮我找条出去的路就行。",
 "{HappyA}Well... [using gun to point to items] There's one maglocked door and one lift --{SadB} both deactivated.":
    "{HappyA}这个……[using gun to point to items] 有一扇磁锁门和一部升降台——{SadB}都没激活。",
 "Scared of a few bandits?": "怕几个土匪？",
 "Smart move.": "明智之举。",
 "{ShockB}Come on, just {SmugA}put that away.": "{ShockB}得了吧，{SmugA}把它收起来。",
 "[Threatening]{InquireA}Maybe it'd be best to just {AngryC}shoot you right now?":
    "[Threatening]{InquireA}也许干脆现在{AngryC}开枪打你还更好？",
 "[Challenging Rhys] {SternB}You don't think I wouldn't!":
    "[Challenging Rhys] {SternB}你以为我不敢！",
 "{WorryC}*I'm* not the one with the gun.": "{WorryC}拿枪的*不是*我。",
 "That's all I need to know.": "我知道这些就够了。",
 "I just want to get my money back and get off this miserable rock.":
    "我只想把我的钱拿回来，然后离开这块悲惨的破石头。",
 "[Mocking] {SchemeB}\"All for the {FearB}little {SchemeB}scraps of power it gives me.\"":
    "[Mocking] {SchemeB}“全为了它给我的那{FearB}一点点{SchemeB}权力残渣。”",
 "[Mocking] {SchemeB}\"Working for a {FearB}fascist death machine\"":
    "[Mocking] {SchemeB}“为一个{FearB}法西斯死亡机器工作”",
 "{SchemeC}Karma's a bitch, isn't it?": "{SchemeC}因果报应很狠，对吧？",
 "{ShockB}This is a planet just {ShockA}*full* of people {SmugB}who'd love to shoot {SmugC}you in your face.":
    "{ShockB}这颗星球上{ShockA}*满是*想{SmugB}朝你脸上{SmugC}开枪的人。",
 "[To himelf]{NeutralA}I mean really, who has the brass to try and {SadC}sell a fake vault key to Hyperion?":
    "[To himelf]{NeutralA}我是说真的，谁有那个胆量想{SadC}卖一把假秘藏钥匙给 亥博龙？",
 "[to Sasha] {SternB}You two are either the craziest swindlers on Pandoria {SlyC}or the dumbest.":
    "[to Sasha] {SternB}你们俩要么是 潘多拉 上最疯的骗子{SlyC}，要么就是最蠢的。",
 "{HappyA}Now that's what I'm talking about!": "{HappyA}这才对嘛！",
 "{ShockA}See? {SlyA}No bogeymen here.": "{ShockA}看吧？{SlyA}这儿没什么妖怪。",
 "See": "看吧",
 "{ShockC}Hello? Vaughn?": "{ShockC}喂？沃恩？",
 "[To Sasha] {SternC}Damn. Lost em...": "[To Sasha] {SternC}该死。断了……",
 "Sorry, but, we might be stuck here for a while. And *I* wouldn't be caught dead without this.":
    "抱歉，但我们可能得困在这儿一阵子。而*我*没这个死都不干。",
 "Why don't you make yourself comfortable while I try to get the rest of this junk on-line?":
    "你为什么不去找个舒服的地方待着，我来把剩下的这些破烂弄上线？",
 "{AngryB}Where's my money?": "{AngryB}我的钱呢？",
 "{ShockD}Shh. [beat] {SternB}That's the tracker!":
    "{ShockD}嘘。[beat] {SternB}那是追踪器！",
 "{SternA}Asshole.": "{SternA}混蛋。",
 "Sasha... *come on*": "萨莎……*快点*",
 "Good work, now *come on*": "干得好，现在*快点*",
 "{WorryBX}Not one bit.": "{WorryBX}一点都不。",
 "Now who's scared?": "现在谁怕了？",
 "{SadB}So then you can do what?": "{SadB}那你能做什么？",
 "Stay where I can see you.": "待在我看得见的地方。",
 "{FearB}Maybe it'd {AngryA}be best to just calm down?":
    "{FearB}也许干脆{AngryA}冷静下来最好？",
 "And it can put big holes in little boys.": "而且它能给小男孩身上开大洞。",
 "{InquireA}Don't think I wouldn't.": "{InquireA}别以为我不敢。",
 "What made you even join-up in the first place?":
    "话说你当初到底为什么会加入？",
 "{SternC}Whatever, that's not gonna happen now. {WorryB}Thanks to you.":
    "{SternC}随便吧，现在不会发生了。{WorryB}多亏你。",
 "[consdering] {AngryA}Maybe so...": "[consdering] {AngryA}也许吧……",
 "{SadA}First Jack, now this guy Vasquez. {InquireB}Maybe you're better off without Hyperion, Rhys.":
    "{SadA}先是 Jack，现在是这个 Vasquez。{InquireB}也许没有 亥博龙你会更好，瑞斯。",
 "{SternD}Anyway, thanks to you and your sister I may find out soon enough.":
    "{SternD}总之，多亏你和你妹妹，我大概很快就能知道了。",
 "{ShockA}But hey, he's *your* friend.": "{ShockA}不过嘿，他是*你*的朋友。",
 "{ShockA}Well, I got it powered-on.": "{ShockA}好吧，我把它通上电了。",
 "{ShockC}Alright. [beat] We're almost home free.  {SchemeD}We know they're alive, and they know we're alive. Now all we need {ShockC}to do is get out!":
    "{ShockC}好。[beat] 我们快自由了。{SchemeD}我们知道他们活着，他们知道我们活着。现在我们只需要{ShockC}出去！",
 "{ShockB}Relieves nervous tension and all. {FearA}[beat] So...":
    "{ShockB}能缓解紧张情绪之类的。{FearA}[beat] 所以……",
})

# —— 收尾：谜题、Zer0 插曲与出口 ——
T.update({
 "{NeutralB}I guess we can *try* to work together on this.":
    "{NeutralB}我想我们可以*试着*在这事上合作。",
 "{ShockC}Nice work! [catching herself] For a Hyperion desk jockey.":
    "{ShockC}干得好！[catching herself] 作为一个 亥博龙坐办公室的。",
 "{HappyC}Score!": "{HappyC}得分！",
 "{FearB}There was only one \"open\" button. [beat] Just, uh... stay out of their way.":
    "{FearB}只有一个“打开”按钮。[beat] 就，呃……别挡他们的路。",
 "{WorryC}Huh. Looks like that {SmugB}kinda worked out in our favor.":
    "{WorryC}嗯。看来那{SmugB}还算对我们有利。",
 "{ShockA}Fiona! [beat, impressed] {ShockC}Damn. You really did it.":
    "{ShockA}Fiona！[beat, impressed] {ShockC}该死。你真做到了。",
 "{FearB}Fiona?": "{FearB}Fiona？",
 "{SadA}Acknowledge.": "{SadA}确认收到。",
 "Looks like it's... [beat] right above us.": "看来它……[beat] 就在我们头顶上。",
 "[ALT] Where's the money?": "[ALT] 钱呢？",
 "{ShockC}Where's the money?": "{ShockC}钱呢？",
 "{WorryC}Looks like it's... [beat] {ThinkB}right above us!":
    "{WorryC}看来它……[beat] {ThinkB}就在我们头顶上！",
 "{AngryA}Wait [beat] That means the {WorryA}money's on the move, right?":
    "{AngryA}等等[beat] 那就是说{WorryA}钱在移动，对吧？",
 "[ALT] Understanding who I'm getting into a *forced partnership* with is very much my concern.":
    "[ALT] 弄清我在跟谁建立*被迫的合伙关系*，非常关我的事。",
 "{SadC}If I'd pulled it off, I could've demote {ShockC}*him* to {NeutralB}janitorial. The prick.":
    "{SadC}要是我办成了，我就能把{ShockC}*他*降成{NeutralB}清洁工。那混蛋。",
 "[pickup3] {AngryA} Stop pointing that thing at me. What matters right now is {ShockD}finding a way out of here.":
    "[pickup3] {AngryA} 别拿那玩意儿指着我了。现在要紧的是{ShockD}找到出去的路。",
 "[pickup3] {ShockB}How could someone even join-up with a bunch of {ShockA}assholes like that?":
    "[pickup3] {ShockB}怎么会有人愿意加入{ShockA}那种混蛋组织？",
 "[pickup3] {ShockC}Understanding who I'm getting forced into a partnership with is {SternB}very much my concern.":
    "[pickup3] {ShockC}弄清我被迫跟谁合伙，{SternB}非常关我的事。",
 "TEMP - Skip Pylon Puzzle": "临时——跳过电力塔谜题",
 "TEMP - Skip to Bandits": "临时——跳到土匪段",
 "Rem((e In--rfA}e": "Rem((e In--rfA}e",
 "Lift: Raise": "升降台：上升",
 "--Sr(( Cr----$$$+": "--Sr(( Cr----$$$+",
 "LLLL((....": "LLLL((....",
 "St--ttttt B+or$": "St--ttttt B+or$",
 "{RageA}Sasha... *come {RageB}on*": "{RageA}萨莎……*快{RageB}点*",
 "{RageA}Good work, now {ShockA}*come on*": "{RageA}干得好，现在{ShockA}*快点*",
 "Just trust me on this one": "这件事就信我一次",
 "I really need your help.": "我真的很需要你帮忙。",
 "I know what Im doing.": "我知道我在干什么。",
 "Scared of bandits?": "怕土匪？",
 "Good thinking.": "想得好。",
 "Careful with that.": "小心那个。",
 "They all do.": "他们都这样。",
 "It's not like that.": "不是那样的。",
 "Pandora's made you nuts.": "潘多拉 把你弄疯了。",
 "To make a fortune.": "为了发大财。",
 "To bring back a Vault key.": "为了带回一把秘藏钥匙。",
 "To screw over Vasquez.": "为了坑掉 Vasquez。",
 "Of course, I'm a genius.": "当然，我是天才。",
 "Gotta try and find out.": "得试试才知道。",
 "Not if you keep bugging me.": "你一直烦我就不会。",
 "Thanks, Mr...?": "谢谢你，先生……？",
 "Pylon": "电力塔",
 "Power Relay": "电力继电器",
 "Computer": "电脑",
 "Broken Computer": "损坏的电脑",
 "Unpowered Computer": "断电的电脑",
 "Battery": "电池",
 "Battery Compartment": "电池仓",
 "Use Battery": "使用电池",
 "Lift": "升降台",
 "Gortys Core Wall": "戈提斯 核心墙",
 "[pickup4][in awe] Holy... this is... this is amazing!":
    "[pickup4][in awe] 我的……这……这太惊人了！",
 "[pickup4][quoting nostalgicly]\"The power of the gods...\"":
    "[pickup4][quoting nostalgicly]“诸神之力……”",
 "[pickup4][anoyed]": "[pickup4][anoyed]",
 "[pickup4][with effort] It's... still locked down for some reason.":
    "[pickup4][with effort] 它……不知为什么还是锁着。",
 "[pickup4] I'm figuring it out.  That's what I do.":
    "[pickup4] 我在弄清它。这就是我的本行。",
 "[pickup4] Do you even know what you're doing?": "[pickup4] 你到底知不知道自己在干什么？",
 "[pickup4][starting to get it] Oookay... I get it.":
    "[pickup4][starting to get it] 好——吧……我懂了。",
 "[pickup4]Problem?": "[pickup4]有问题？",
 "[pickup4]No, no problem. I just...": "[pickup4]不，没问题。我只是……",
 "[pickup4][a bit reluctant] I need your help.": "[pickup4][a bit reluctant] 我需要你帮忙。",
 "[pickup4][reluctant]Hey you're the techno guy.  I don't know anything about this stuff.":
    "[pickup4][reluctant]嘿，你才是技术哥。我对这些东西一窍不通。",
 "[pickup4]What if it shorts out or shocks me or something.":
    "[pickup4]要是它短路或者电到我或者别的什么怎么办。",
 "[pickup4]... you're the expert, you do it.": "[pickup4]……你是专家，你来。",
 "[pickup4]Just trust me. It's nothing that can hurt you.":
    "[pickup4]就信我。它伤不到你。",
 "[pickup4] Can we stop arguing? I need your help.":
    "[pickup4] 我们能别吵了吗？我需要你帮忙。",
 "[pickup4]Hey, I know what I'm doing.  I've been wiring tech forever.":
    "[pickup4]嘿，我知道我在干什么。我接线路接了半辈子。",
 "[pickup4][giving in] Fine. What do you need?": "[pickup4][giving in] 行。你需要什么？",
 "{NeutralA}[pickup4]I think these power relays have to be unlocked {ShockA}at the same time.":
    "{NeutralA}[pickup4]我觉得这些电力继电器必须{ShockA}同时解锁。",
 "[pickup4]\t{InquireB}You start.": "[pickup4]\t{InquireB}你先来。",
 "[pickup4]\t{WorryB}Ready?": "[pickup4]\t{WorryB}准备好了吗？",
 "{SadA}[pickup4] So you do one and I do the other, thats it?":
    "{SadA}[pickup4] 就是你做一个、我做另一个，就这样？",
 "[pickup4]I think so.": "[pickup4]我想是。",
 "[pickup4][thinking]Hmm...": "[pickup4][thinking]嗯……",
 "[pickup4][annoyed]Rhys![focus!]": "[pickup4][annoyed]瑞斯！[专注！]",
 "[pickup4] Will that help us get out of here?": "[pickup4] 那能帮我们离开这儿吗？",
 "[pickup4][to himself, as if mourning a friend]It's beautiful too, Damn shame.":
    "[pickup4][to himself, as if mourning a friend]它也很美，真可惜。",
 "[pickup4] Maybe if it we're still working, but this console's fried.":
    "[pickup4] 要是它还能用就好了，但这台控制台烧了。",
 "[pickup4][snide]Did you expect it to turn on?": "[pickup4][snide]你还指望它能开？",
 "[pickup4]Actually yeah. This looks like it SHOULD work... probably just a power issue.":
    "[pickup4]其实是啊。这看起来*应该*能用……大概只是供电问题。",
 "[pickup4][disapointed sigh]": "[pickup4][disapointed sigh]",
 "[pickup4][cont.] ...I could probably get manual access through the mainframe console-[cut off]":
    "[pickup4][cont.] ……我大概能通过主机控制台获得手动访问权——[cut off]",
 "[pickup4]Seriously?!  All this junk is broken!":
    "[pickup4]认真的？！这些破烂全坏了！",
 "[pickup4][aloud to himself] Haven't you been listening? This is ATLAS tech, it's built to last! I'm sure I can get it working.":
    "[pickup4][aloud to himself] 你一直没在听吗？这是阿特拉斯的技术，造出来就是耐用的！我肯定能把它弄好。",
 "[PICKUP4][sarcastic] Still broken?": "[PICKUP4][sarcastic] 还是坏的？",
 "[pickup4]Yep.": "[pickup4]是啊。",
 "[pickup4]Does it have power yet?": "[pickup4]它通电了吗？",
 "[pickup4]I'm working on it.": "[pickup4]我在弄。",
 "[pickup4]... What do you think that's all about?":
    "[pickup4]……你觉得那是怎么回事？",
 "[pickup4]I dunno.  Let's just get out of here.":
    "[pickup4]不知道。我们离开这儿吧。",
 "[pickup4][to himself] ...These must hold the power cores.":
    "[pickup4][to himself] ……这里肯定装着动力核心。",
 "[pickup4] Welp.  This battery's dead.": "[pickup4] 好吧。这块电池没电了。",
 "[pickup4] Dead is dead. We'll just have to find another one.":
    "[pickup4] 死了就是死了。我们只能另找一块。",
 "[pickup4] Can't you fix it?": "[pickup4] 你不能修好它吗？",
 "[pickup4][to himself] No  corrosion... that's a good sign.":
    "[pickup4][to himself] 没有锈蚀……这是个好迹象。",
 "[pickup4] Hey, I'm just getting started. Now stand back and watch the magic happen!":
    "[pickup4] 嘿，我才刚开始。现在退后，看奇迹发生！",
 "[pickup4][sarcastic]Amaaaaazing....": "[pickup4][sarcastic] 太——惊人——了……",
 "{SmugC}[pickup4][attaching the battery and restoring power] Aaaaand... tadaaa!":
    "{SmugC}[pickup4][attaching the battery and restoring power] 然后……哒哒！",
 "[pickup4] Is that the battery?": "[pickup4] 那是电池吗？",
 "[pickup4]Yeah, and it still looks good.": "[pickup4]是啊，而且看起来还挺好。",
 "[pickup4]{FearA}Stand {HappyB}back.": "[pickup4]{FearA}退{HappyB}后。",
 "[pickup4][fake electrocution] RrrrRRrrrRrRAAAhhhHHAARRRrr!!!":
    "[pickup4][fake electrocution] 呃呃呃啊啊啊啊啊！！！",
 "[pickup4][frightened scream!]": "[pickup4][frightened scream!]",
 "[pickup4][laughing at Sasha] I'm just messing with ya!":
    "[pickup4][laughing at Sasha] 我逗你玩的！",
 "[pickup4]Jerk.": "[pickup4]混蛋。",
 "[pickup4]Thats Fiona!  How'd you do that?!": "[pickup4]那是 Fiona！你怎么做到的？！",
 "[pickup4]The system reboot is trying to open some of the comm channels, but the signal is pretty weak...":
    "[pickup4]系统重启正在试着打开一些通讯频道，但信号挺弱的……",
 "[pickup4][urgent] Well, the computers are working now, bring the lift down so we can get up there!":
    "[pickup4][urgent] 好吧，电脑现在能用了，把升降台弄下来，好让我们上去！",
 "[pickup4] Can you fix it?": "[pickup4] 你能修好它吗？",
 "[pickup4]Well, no,  'cause it's \"missing\".  But if we find a replacment , we should be good.":
    "[pickup4]这个，不能，因为它“不见了”。但要是我们找到替换的，应该就行了。",
 "[pickup4][to himself]Missing core?! No wonder this isn't working.":
    "[pickup4][to himself]核心不见了？！难怪这不管用。",
 "[pickup4]Now... these things should be holding power cores... I wonder what the problem is?":
    "[pickup4]现在……这些东西里应该装着动力核心……我想知道问题在哪儿？",
 "{HappyB}[pickup4] See... easy.": "{HappyB}[pickup4] 看……简单吧。",
 "[pickup4][aloud to himself] Hm... I guessing this was raised remotely, but...":
    "[pickup4][aloud to himself] 嗯……我猜它是被远程升起的，但是……",
 "[pickup4] Very observational.": "[pickup4] 观察力不错。",
 "[pickup4] It's still raised.": "[pickup4] 它还是升着的。",
 "[pickup4]Hurry up.  I don't like it down here.":
    "[pickup4]快点。我不喜欢待在这下面。",
 "[pickup4]We'll be out soon. I just need a little more time.":
    "[pickup4]我们很快就出去了。我只是还需要一点时间。",
 "[pickup4][cold, annoyed]Is it working yet?": "[pickup4][cold, annoyed]管用了吗？",
 "[pickup4]Not until I get a working power core into that relay.":
    "[pickup4]除非我把一个能用的动力核心装进那个继电器。",
 "[pikcup4]Well get em back!": "[pikcup4]那就把它们弄回来！",
 "[pickup4]You did it!": "[pickup4]你做到了！",
 "[pickup4]": "[pickup4]",
 "[pickup4]Well, that did nothing.": "[pickup4]好吧，那什么都没干成。",
 "[pickup4][unimpressed] The lift still isnt moving.":
    "[pickup4][unimpressed] 升降台还是没动。",
 "[pickup4]I see that.": "[pickup4]我看得出来。",
 "[pickup4]Uh, Rhys?": "[pickup4]呃，瑞斯？",
 "[pickup4] [Nervous]Good 'cause...[she points at the Scag cages]":
    "[pickup4] [Nervous]那好，因为……[she points at the Scag cages]",
 "[pickup4] Yeah, I see it. I'll find a way to get it open.":
    "[pickup4] 是啊，我看到了。我会想办法打开它。",
 "Aw crap.": "啊，糟。",
 "[suprised scream!]": "[suprised scream!]",
 "[pickup4]Thanks.  I just need to get that hatch open and we're outta here!":
    "[pickup4]谢了。我只要把那舱门打开，我们就出去了！",
 "[pickup4] I am NOT going to be stuck down here for a while with you.  Do you \"hacky\" thing and get that hatch open!":
    "[pickup4] 我才不要跟你在这下面困一阵子。施展你那“黑客”本事把舱门打开！",
 "[pickup4]I'm glad someone does.": "[pickup4]我很高兴有人知道。",
 "[pickup4]Good. Let me know if you get stuck.": "[pickup4]好。卡住了告诉我。",
 "Lever": "拉杆",
 "Shiny Button": "闪亮的按钮",
 "Tempting Button": "诱人的按钮",
 "Terminal": "终端",
 "System that controls various cool things and stuff.": "控制各种酷东西和玩意儿系统。",
 "ACccCc-$$%": "ACccCc-$$%",
 "Skag Cage": "异犬笼子",
 "Reinforced cage. Contents: One Skag (pictured).":
    "加固笼子。内容物：一只异犬（如图）。",
 "Hey! Get away from that! Who's down there?!":
    "嘿！离那个远点！谁在下面？！",
 "[more to reassure herself] She can talk her way out of anything.":
    "[more to reassure herself] 她靠一张嘴什么都能脱身。",
 "Let's focus on the money.": "我们专注那笔钱。",
 "[Silence]": "[Silence]",
 "You've made it this far.": "你都走到这一步了。",
 "They'll tear him to pieces. He needs me.": "他们会把他撕成碎片。他需要我。",
 "Keep it down. The bandits will hear you.": "小声点。土匪会听到你。",
 "Vaughn. VAUGHN!": "沃恩。VAUGHN！",
 "Then concentrate on getting us out of here.": "那专心把我们弄出去。",
 "The money?! Do you have any idea what those bandits will do to them?!":
    "钱？！你知道那些土匪会对他们做什么吗？！",
 "We've got to focus on getting the money back.":
    "我们得专心把钱拿回来。",
 "Hey, if we wanted you dead, we would've done it by now.":
    "嘿，我们要是想你死，早就动手了。",
 "It's easier to pick us off if we're separated. Then you can take all the money.":
    "我们分开就更容易被你们一个个干掉。然后你就能把钱全拿走。",
 "You were hoping this would happen.": "你就盼着这事发生。",
 "\"Oh, I can murder you whenever I want.\" That's basically what you're saying, right?":
    "“哦，我想什么时候杀你就能什么时候杀。”你基本就是在这么说，对吧？",
 "Quiet. The bandits will hear you.": "安静。土匪会听到你。",
 "This is your fault.": "这是你的错。",
 "So you could pick us off one at a time. Then take all the money.":
    "这样你就能把我们一个个干掉。然后把钱全拿走。",
 "Admit it. You wanted this to happen.": "承认吧。你就想让这事发生。",
 "You've lost it.": "你疯了。",
 "Just stay where I can see you.": "就待在我看得见的地方。",
 "Keep moving.": "继续走。",
 "Fiona can talk her way out of anything. They'll be okay.":
    "Fiona 靠一张嘴什么都能脱身。他们会没事。",
 "I can't believe I trusted someone from Hyperion.":
    "我不敢相信我居然信了一个 亥博龙的人。",
 "We should never have let you come with us.": "我们根本不该让你跟我们一起来。",
 "[motioning down] Keep moving.": "[motioning down] 继续走。",
 "Fine. What would you like to do?": "行。你想怎么做？",
 "You're not running the show.": "这儿不是你说了算。",
 "If you've got a better idea th--": "你要是有更好的主意——",
 "Well, we have to find a way out. Let's go.": "好吧，我们得找到出路。走。",
 "They can handle themselves.": "他们能应付自己。",
 "No signal. We're completely cut off.": "没信号。我们完全断了联系。",
 "[to Sasha] No signal.": "[to Sasha] 没信号。",
 "I'm working on it.": "我在弄。",
 "We've gotta find a way out.": "我们得找到出路。",
 "Be careful with that.": "小心那个。",
 "In a few minutes, this place will be crawling with bandits.":
    "几分钟后，这地方就会爬满土匪。",
 "They know something's up.": "他们知道出事了。",
 "[motioning to the computers] We need to get down there.":
    "[motioning to the computers] 我们得下去那边。",
 "I'm on it. Just let me think.": "我在弄。让我想想。",
 "Take a breath. We'll figure this out.": "喘口气。我们会想出办法的。",
 "We have to hurry.": "我们得快点。",
 "I get it. Now let me think.": "我明白。现在让我想想。",
 "Save your breath.": "省点口水吧。",
 "Better safe than sorry.": "小心总比后悔好。",
 "What's your problem?": "你有什么毛病？",
 "I'm not letting you out of my sight.": "我不会让你离开我的视线。",
 "Don't test me.": "别试我。",
 "They already suspect something. It won't be long before this place is crawling with bandits.":
    "他们已经起疑了。用不了多久这地方就会爬满土匪。",
 "You were hoping this would happen! You wanted to separate us so you could pick us off! [disgusted] Ugh... Hyperions.":
    "你就盼着这事发生！你想把我们分开好一个个干掉！[disgusted] 呃……亥博龙的人。",
 "What?! You're the one that tried to ditch us. This was your plan all along!":
    "什么？！想甩掉我们的是你。这本来就是你的计划！",
 "My plan? You wanted to separate us so you could pick us off. [disgusted] Hyperions.":
    "我的计划？你想把我们分开好一个个干掉。[disgusted] 亥博龙的人。",
 "If we wanted to kill you we would've done it by now.":
    "我们要是想杀你，早就动手了。",
 "You're a bastard.": "你是个混蛋。",
 "You just tried to steal our van!": "你刚才还想偷我们的货车！",
 "It was money we brought to you... remember? Fake Vault Key?":
    "那是我们带给你们的钱……记得吗？假秘藏钥匙？",
 "Of course... the money... that's all that matters to you suits.":
    "当然……钱……对你们这些西装货来说就这个最重要。",
 "See? You're just lashing out now.": "看吧？你现在只是在乱发脾气。",
 "[echo] Vaughn, do you copy? Come in, Vaughn.":
    "[echo] 沃恩，收到吗？请回答，沃恩。",
 "[worried] They were spotted.": "[worried] 他们被发现了。",
 "How convenient.": "真方便。",
 "[hushed] Look -- that lift, that locked door, and everything in this whole sector must be controlled by those computers, which seem to be offline on this end.":
    "[hushed] 听着——那部升降台、那扇锁着的门，以及这整个区域的一切，肯定都由那些电脑控制，而这些在你这头好像离线了。",
 "Shit.": "妈的。",
 "[under his breath] Damnit.": "[under his breath] 该死。",
 "The money's close. It's practically right above us.":
    "钱就在附近。几乎就在我们头顶上。",
 "I hate those things.": "我讨厌那些东西。",
 "Will you lay off?": "你能不能别烦？",
 "It's one of the {SlyC}power systems starting up...":
    "这是其中一个{SlyC}电力系统启动了……",
 "How do I know you didn't start up a death machine to kill me?":
    "我怎么知道你不是启动了一台死亡机器来杀我？",
 "Give me a heads up next time if you don't want to get shot.":
    "下次不想挨枪子就提前跟我说一声。",
 "Why don't you back off?": "你干嘛不退后点？",
 "You make me sick.": "你让我恶心。",
 "Think what you want. I'd rather play for the winning team.":
    "你爱怎么想怎么想。我更愿意为赢的那队效力。",
 "I guess talking about your evil corporate bosses is a real concentration-killer.":
    "我想谈论你们那些邪恶的公司老板确实很打断专注。",
 "Order my ass. You're murderers.": "秩序个屁。你们是杀人犯。",
 "{SmugB}I guess talking about your evil corporate bosses is a real concentration-killer.":
    "{SmugB}我想谈论你们那些邪恶的公司老板确实很打断专注。",
 "{WorryA}Can you lay off with the questions for a minute?":
    "{WorryA}你能停一会儿问题吗？",
 "{InquireB}Oh, don't mind me. I'm just a worthless Pandoran.":
    "{InquireB}哦，别管我。我只是个没用的 潘多拉 人。",
 "Yeah, and I'll keep the other on you.": "是啊，另一只眼我继续盯着你。",
 "The money's on the move, but it's close. We have to hurry.":
    "钱在移动，但很近。我们得快点。",
 "{NeutralB}Think what you want. Me? I'd rather play for the winning team.":
    "{NeutralB}你爱怎么想怎么想。我？我更愿意为赢的那队效力。",
 "{AngryB}You make me sick.": "{AngryB}你让我恶心。",
 "{AngryB}Order my ass. You're {ShockB}a bunch of murderers.":
    "{AngryB}秩序个屁。你们{ShockB}是一群杀人犯。",
 "{NeutralB}Hyperion brings order.": "{NeutralB}亥博龙带来秩序。",
 "Time to go.": "该走了。",
 "Don't do anything stupid.": "别做蠢事。",
 "It's not who you really are.": "这不是你真正的样子。",
 "Working on it.": "正在弄。",
 "[shuddering in fear] Skags. Ugh.": "[shuddering in fear] 异犬。呃。",
 "YES.": "是。",
 "[meekly] Thank you.": "[meekly] 谢谢。",
 "We just saw that lift go up, can't you bring it back down?":
    "我们刚看到那升降台升上去了，你不能把它弄下来吗？",
 "[pickup4]Not yet... these relays should be holding power cores... I wonder what the problem is?":
    "[pickup4]还没有……这些继电器里应该装着动力核心……我想知道问题在哪儿？",
 "Is it fixed?": "修好了吗？",
 "[cont]What if one day you and your friend really do make a big score and rise up in the ranks?":
    "[cont]要是有一天你和你朋友真干成了大票，往上爬了呢？",
 "He is if I'm gonna be stuck with you two for awhile...":
    "如果我要跟你们俩困一阵子，那他就是……",
 "{SternB}Okay, you're not completely useless. {SchemeB}Can you bring the lift down?":
    "{SternB}好吧，你也不是完全没用。{SchemeB}你能把升降台弄下来吗？",
 "{SmugA}Absolutely.": "{SmugA}当然。",
 "{HappyC}YES!! Come on, lets get out of here!":
    "{HappyC}太好了！！来吧，我们离开这儿！",
 "Do your \"hacky-ting\" and get that hatch open!":
    "施展你那“黑客本事”把舱门打开！",
 "Damnit, not now!": "该死，不是现在！",
 "Don't look at me!": "别看我！",
 "Something is screwing up my UI.": "有什么东西在搞坏我的界面。",
 "[to himself] Not good.": "[to himself] 不妙。",
 "{FearB}I can't read the buttons!  They're all... glitched out![beat] Just, uh... I don't know, stay out of their way.":
    "{FearB}我看不清按钮！它们全都……花屏了！[beat] 就，呃……我不知道，别挡他们的路。",
 "[uneasy] That might've been our EMP.": "[uneasy] 那可能是我们的电磁脉冲。",
 "^color:#ffea7f^Con*3nts: ^color:white^1ne SkAg (pi---rcd)).":
    "^color:#ffea7f^内*3容: ^color:white^一 只 异犬（如---所示））。",
 "Hyperions.": "亥博龙的人。",
 "[alt] So many skags.": "[alt] 好多异犬。",
 "Hurry.": "快点。",
 "[alt] We're not safe here.": "[alt] 我们在这儿不安全。",
 "{FearA}[alt] My gun...{FearB}": "{FearA}[alt] 我的枪……{FearB}",
 "Let me tell you something about real partners. They always have each other's backs. Like me and Fiona.":
    "我跟你说说真正的搭档是什么样。他们永远互相照应。就像我和 Fiona。",
 "I can respect that.": "这我尊重。",
 "Whatever works.": "怎么都行。",
 "You're lucky.": "你运气好。",
 "[from the heart] You're lucky to have her. Before Vaughn, I tried not to get too close to anybody. Now I'm not sure what I'd do without him.":
    "[from the heart] 有她是你的运气。在 沃恩 之前，我尽量不跟任何人走太近。现在我不知道没他我会怎样。",
 "[surprised] You mean that.": "[surprised] 你是说真的。",
 "Real friends are hard to come by.": "真朋友可遇不可求。",
 "I respect that. You need each other.": "我尊重这点。你们彼此需要。",
 "It's more than that. It's about trust.": "不止那样。这关乎信任。",
 "Trust doesn't get you far on Hyperion.": "在 亥博龙，信任帮不了你走远。",
 "Well I'm Hyperion, so I wouldn't know anything about that.":
    "这个嘛，我就是 亥博龙的，所以这我一点都不懂。",
 "[sharply] I guess you wouldn't.": "[sharply] 我想你确实不懂。",
 "We don't have to be partners. We choose to because we care about each other.":
    "我们不必当搭档。我们选择这样，是因为我们在乎彼此。",
 "Whatever works. You do what you gotta do.": "怎么都行。你做你该做的。",
 "I knew you wouldn't understand.": "我就知道你不会懂。",
 "Hatch": "舱门",
 "^color:#ffea7f^Ck8ton$$$#: ^color:white^H@tttc--+<:/":
    "^color:#ffea7f^Ck8ton$$$#: ^color:white^H@tttc--+<:/",
 "[re: the skags] They look starving!": "[re: the skags] 它们看起来饿坏了！",
 "Can't you do that any faster?": "你不能弄快点吗？",
 "[under his breath] What the hell?": "[under his breath] 搞什么？",
 "I thought your sister told you not to point that at me.":
    "我以为你妹妹跟你说过别拿那玩意儿指着我。",
 "[alt] [awed] The money's right above us.": "[alt] [awed] 钱就在我们头顶上。",
 "[awed] It's right above us.": "[awed] 就在我们头顶上。",
 "[gentler] If she can trust me, why can't you?":
    "[gentler] 她能信我，你为什么不能？",
 "This doesn't make us friends.": "这不代表我们是朋友。",
 "That's a relief.": "那就好。",
 "{FearA}[alt] Don't do anything stupid.": "{FearA}[alt] 别做蠢事。",
 "{InquireA}[alt] You'll never get away with it.": "{InquireA}[alt] 你不会得逞的。",
 "I'm sorry, what was that?": "抱歉，你说什么？",
 "Whoa whoa whoa, it's just a... just a saying...":
    "哇哇哇，这只是个……只是句俗话……",
 "We should keep moving.": "我们该继续走。",
 "[alt]Skags... I hate skags.": "[alt]异犬……我讨厌异犬。",
 "Whatever it is, figure it out quick. We might have company soon.":
    "不管是什么，快点弄清。我们可能很快就有客人。",
 "{AngryA}[postpax] The pain?": "{AngryA}[postpax] 那些痛苦？",
 "{ShockB}[postpax] The havoc they caused here?":
    "{ShockB}[postpax] 他们在这儿造成的浩劫？",
 "{ShockB}[postpax] It doesn't matter what you do up there... you contributed.":
    "{ShockB}[postpax] 你在上面做什么都不重要……你也出了一份力。",
 "[postpax] You Hyperion guys are all the same...":
    "[postpax] 你们 亥博龙的人全都一个样……",
 "[postpax] How long before he becomes another cost of doing business?":
    "[postpax] 过多久他就会变成另一笔“经营成本”？",
 "[postpax] No problem stabbing your best friend in the back to get a corner office.":
    "[postpax] 为了拿个角落办公室，捅你最好的朋友背后一刀毫无问题。",
 "[postpax] as you make your way up...": "[postpax] 在你往上爬的时候……",
 "[postpax] Just another rung on the ladder...":
    "[postpax] 只是梯子上的又一级……",
 "[postpax] to become king of the assholes.":
    "[postpax] 好当上混蛋之王。",
 "[postpax] Like this Vaughn guy... you're telling me you really plan on sharing your power with him?":
    "[postpax] 比如这个 沃恩……你是说你真打算跟他分享你的权力？",
 "[alt] It'd be weird for that to be the case.":
    "[alt] 要是那样倒挺怪的。",
 "Do what?": "做什么？",
 "Uh, nothing... Just, gimme a sec.": "呃，没什么……就，给我一秒钟。",
 "[postpax] [lots of static, no idea it's Handsome Jack] Do you champ? Do you almost got it?":
    "[postpax] [lots of static, no idea it's Handsome Jack] 你行吗，冠军？你快搞定了吗？",
 "[postpax, vulnerable] I hate skags.": "[postpax, vulnerable] 我讨厌异犬。",
 "[postpax] [lots of static, no idea it's Handsome Jack] Look at you... a real winner.":
    "[postpax] [lots of static, no idea it's Handsome Jack] 看看你……真是个赢家。",
 "[postpax] [freaking out] It's coming! It's gonna make it.":
    "[postpax] [freaking out] 它来了！它快够到了。",
 "[postpax] [freaking out] No. No, no, no, no!":
    "[postpax] [freaking out] 不。不不不不！",
 "[postpax] [freaking out] Get it off me! Get it off me.":
    "[postpax] [freaking out] 弄掉它！弄掉它。",
 "[postpax] [freaking out] Gaah! Aaargh!":
    "[postpax] [freaking out] 嘎！啊啊！",
 "[postpax] I'm just saying if I had a sword...":
    "[postpax] 我只是说，要是我有把剑……",
 "[postpax] Just shut up and thank the man.":
    "[postpax] 你就闭嘴谢谢人家。",
 "[postpax] Could you let me know / if you see a Gortys core / I really need it.":
    "[postpax] 你要是看到 戈提斯 核心 / 能不能告诉我一声 / 我真的很需要它。",
 "Sure... yeah.": "当然……好。",
 "What's it worth to you?": "对你来说值多少？",
 "You're really cool...": "你真酷……",
 "[postpax] You're... you're really cool... I just... I wanted you to know that.":
    "[postpax] 你……你真酷……我只是……我想让你知道。",
 "[postpax] Will you shut your mouth. [to Zer0]Yes. Of course we will let you know.":
    "[postpax] 你能闭嘴吗。[to Zer0]会。我们当然会告诉你。",
 "[postpax] I don't know... what's it worth to you?":
    "[postpax] 我不知道……对你来说值多少？",
 "[postpax] Sure... Yeah. We'll uh, we'll let you know.":
    "[postpax] 当然……好。我们，呃，我们会告诉你的。",
 "Just a... a poor choice of words. Okay?": "只是……用词不当。行吗？",
 "Walk in front of me.": "走我前面。",
 "[postpax] [freaking out] Not now. Not now!":
    "[postpax] [freaking out] 不是现在。不是现在！",
 "{WorryA}[postpax] That's my guess. We just need to pull these pylons up.":
    "{WorryA}[postpax] 我猜是这样。我们只要把这些电力塔拉起来。",
 "[beat] How is it up there, anyway?": "[beat] 话说上面怎么样？",
 "Where?": "哪儿？",
 "Up on that base you're all in. What's it called?":
    "你们都在的那个基地上。它叫什么？",
 "Right. Helios. [beat]I mean, what's it like being an emotionless cog spinning away, day after day, for the most blood thirsty, brutal, soul-crushing, love-defying corporation in the whole wide universe?":
    "对。赫利俄斯。[beat]我是说，当一颗毫无感情的齿轮，日复一日地为全宇宙最好杀、最残暴、最磨灭灵魂、最违背爱的公司空转，是什么感觉？",
 "Everyone's more than happy to climb the corporate ladder even if it means using your face for a rung.":
    "每个人都很乐意爬公司阶梯，哪怕那意味着拿你的脸当一级梯档。",
 "Ugh... sounds awful.": "呃……听着真糟。",
 "All I've ever wanted to do was to run a company, and Hyperion's the biggest company there is, so... Yeah.":
    "我一直想做的就是经营一家公司，而 亥博龙是现存最大的公司，所以……对。",
 "[long beat] Well, that's the saddest thing I've ever heard.":
    "[long beat] 好吧，这是我听过最可悲的话。",
 "I have to make this work, and... I have to get to the top of the Hyperion food chain, or I'll have wasted basically my entire life.":
    "我必须把这事做成，而且……我必须爬到 亥博龙食物链的顶端，否则我这辈子基本上就白过了。",
 "Yup, easy. I'll take the one on the left. You get the one on the right. Oh, do you think you can handle that?":
    "对，简单。左边的我来。右边的你去。哦，你觉得你能搞定吗？",
 "They probably didn't teach you this kind of stuff in finishing school.":
    "他们大概没在淑女/绅士学校教过你这种东西。",
 "I know you Hyperion guys don't like getting your hands dirty.":
    "我知道你们 亥博龙的人不喜欢把手弄脏。",
 "Wow. So you're saying one won't be an issue.":
    "哇。所以你是说一个不成问题。",
 "That's what I'm saying. Yeah.": "我就是这个意思。对。",
 "You're sounding pretty confident.": "你听着挺自信。",
 "Look, I took out a dozen bandits earlier [tuh-DAY]today.":
    "听着，今天早前我干掉了十来个土匪。[tuh-DAY]就今天。",
 "[swagger] Uh, pfft, yeah. No problem.":
    "[swagger] 呃，嗤，是啊。没问题。",
 "Can't we just shoot them?": "我们就不能开枪打他们吗？",
 "Alright, alright, alright. I got it.": "好，好，好。我懂了。",
 "Just shoot them. You have a gun. That's what they're there for, right? You got no problem pointing it at me, and you can't take out a couple guards?":
    "直接开枪打他们。你手上有枪。枪就是干这个用的，对吧？你拿枪指我毫不含糊，却干不掉几个守卫？",
 "Uh, guns make noise. Noise attracts more guards. If we do it quiet, then we won't have all the bang bang sounds that mak--":
    "呃，枪会响。响声会引来更多守卫。我们要是安静点来，就不会有那些砰砰声搞得——",
 "Think YOU can handle it?": "你觉得*你*能搞定？",
 "They're skag skin.": "它们是异犬皮做的。",
 "They're atrocious.": "它们丑毙了。",
 "You just make sure you don't scuff your nice little shoes, okay, Hyperion boy?":
    "你就确保别把你那双漂亮小鞋磨花就行，行吗，亥博龙小子？",
 "Oh, I'm not worried about me. 'Cause I took out a dozen bandits earlier today. Are you sure you can handle it?":
    "哦，我不担心我自己。因为今天早前我干掉了十来个土匪。你确定你能搞定？",
 "[pff] Um, are you serious?": "[pff] 呃，你认真的？",
 "I don't know, you talk a big game, but I haven't seen you in action.":
    "我不知道，你嘴上很能吹，但我还没见过你出手。",
 "Okay... just do your best.": "好吧……尽力就行。",
 "Come on.": "来吧。",
 "[Thumbs Up]": "[竖大拇指]",
 "[Thumbs Down]": "[竖拇指向下]",
 "[Meh]": "[一般]",
 "Ninja Choke": "忍者锁喉",
 "Stun Baton": "电击棒",
 "Whoa, hey, uh, hey, can I help you?": "哇，嘿，呃，嘿，有什么能帮你的？",
 "Oh, come on. You cannot tell me that wasn't cool.":
    "哦，得了吧。你不能说那不够酷。",
 "The \"swing of things\"?": "“事情的节奏”？",
 "Oh, I'm sorry, I was just getting into the swing of things.":
    "哦，抱歉，我只是刚进入状态。",
 "Fine, forget the line, but did you see the distance I got on that guy?":
    "行，台词的事算了，但你看到我把那家伙送出去多远了吗？",
 "[godamn right] Thank you.": "[godamn right] 谢了。",
 "You[,] are not cool. Hyperion tech[,] is cool.":
    "你，不酷。亥博龙的技术，酷。",
 "I see what you're doing. You're copying what I did, even though I clearly had the cooler takedown. That's fine. I don't need your approval.":
    "我看得出你在干什么。你在模仿我做的，尽管显然是我的制服动作更酷。没关系。我不需要你的认可。",
 "Ah ha ha! Nah, I got ya. Get back, man.": "哈哈哈！不，我懂你。退后点，老兄。",
 "[press the button]": "[按下按钮]",
 "Let me, just, get that for you.": "让我来，就，帮你弄那个。",
 "Oh, duh. That's like the one button on th--":
    "哦，废话。那就是那上面唯一一个按钮——",
 "How-- how does this thing work?": "这——这玩意儿怎么用？",
 "Uh, how, uh...": "呃，怎么，呃……",
 "Do you, uh, do you like.... Hmm.": "你，呃，你喜欢……嗯。",
 "[yelling over] I don't need that right now!": "[yelling over] 我现在不需要那个！",
 "[yelling over] Wow, nicely done.": "[yelling over] 哇，干得漂亮。",
 "I got it!": "我搞定了！",
 "Help me!": "帮帮我！",
 "Relax, Sasha!": "放松，萨莎！",
 "Nope, no he doesn't!": "不，他可没有！",
 "Wow, even the bandit's unimpressed.": "哇，连土匪都没被惊艳到。",
 "He does not got it!": "他根本没搞定！",
 "That's not what it looks like from here.": "从这儿看可不是那样。",
 "Uh, a little help?": "呃，帮个忙？",
 "Nah, nah nah, don't help him!": "不，不不，别帮他！",
 "Nah, I think he's right. You should handle it yourself.":
    "不，我觉得他说得对。你该自己搞定。",
 "Come on, let him do it himself! If he can!":
    "得了吧，让他自己做！如果他做得到的话！",
 "You dropped something.": "你掉了东西。",
 "That's gonna leave a mark.": "那会留个印子。",
 "[wind knocked out of him] It... it's... f-ine... Just knocked... the w-ind... out of m-e...":
    "[wind knocked out of him] 我……我……没——事……只是……被……撞得……喘不上气……",
 "[getting up groan]": "[getting up groan]",
 "Yeah, I see that.": "是啊，我看得出来。",
 "I deserve that.": "我活该。",
 "[oh shit] Huh... this is all old Atlas tech.":
    "[oh shit] 嗯……这全是老阿特拉斯技术。",
 "We need to get the lift working.": "我们得把升降台弄好。",
 "[frustrated] Stupid piece of--": "[frustrated] 蠢东西——",
 "Hey! Would you stop that!": "嘿！你能不能停下！",
 "Then do it.": "那就去做。",
 "Oh come on, really? I thought we were past this.":
    "哦得了吧，真的？我以为我们已经过了这一关。",
 "[frustrated] It needs a password.": "[frustrated] 它需要密码。",
 "Hey! I thought you said--": "嘿！我以为你说过——",
 "I'm joking. Relax.": "我开玩笑的。放松。",
 "[that was funny] That's not funny.": "[that was funny] 这不好笑。",
 "Get this to line up with...": "把这个对准……",
 "Boom.": "砰。",
 "And... we are... in.": "然后……我们……进去了。",
 "Just a little end around here...": "在这儿稍微绕一下……",
 "In.": "进去。",
 "\"Past this\"?": "“过了这一关”？",
 "Yes, I get it. We're the worst. So... can you lay off for a bit?":
    "是，我明白。我们最烂。所以……你能歇一会儿吗？",
 "Aww. I guess talking about your evil corporate bosses gets under your skin. Good. It should.":
    "哎呀。看来谈论你们那些邪恶的公司老板会让你不爽。很好。本来就该。",
 "Damnit! It's locked!": "该死！锁着！",
 "I can hack it.": "我能黑开它。",
 "Okay... I'm impressed.": "好……我服了。",
 "Yeah, get the lift moving.": "是啊，让升降台动起来。",
 "[sarcastic]Aww, shucks. You mean it? I really appreciate that.":
    "[sarcastic]哎呀，哪敢当。你说真的？我真的很感激。",
 "I got in, but it didn't give me the right clearances so I'm gonna need a second.":
    "我进去了，但它没给我正确的权限，所以我得再花一秒钟。",
 "Well... hurry up.": "好吧……快点。",
 "Helios.": "赫利俄斯。",
 "[to himself] Okay... okay... now we're getting somewhere... Just... let me in... let me in, right there...  there... Okay, that was the wrong way.":
    "[to himself] 好……好……现在有进展了……就……让我进去……让我进去，就那儿……那儿……好，那是错的方向。",
 "Eh, it mostly is.": "呃，大体上是。",
 "I'm trying to open up here.": "我这儿正试着打开。",
 "Stay closed if the story involves tiny business cards.":
    "要是故事里涉及小小的名片，那就保持关闭吧。",
 "[beat] I'm well aware of your opinion of Hyperion.":
    "[beat] 我很清楚你对 亥博龙的看法。",
 "Uhh... News flash. You did. You wasted your life working for assholes.":
    "呃……新消息。你就是白过了。你把人生浪费在给混蛋干活上。",
 "I, uh... I have to... concentrate.": "我，呃……我得……集中精神。",
 "Absolutely.": "当然。",
 "No way.": "不行。",
 "Okay... I see how it is.": "好……我明白了。",
 "Promise to give it back?": "保证还给我？",
 "Yes.": "嗯。",
 "Pinky promise?": "拉钩保证？",
 "[grudgingly] Yes...": "[grudgingly] 是……",
 "Don't hurt yourself.": "别弄伤自己。",
 "Do you promise to give it back?": "你保证还给我吗？",
 "Look, you asked, and I said no. Anything you're compelled to do after that is on you.":
    "听着，你问了，我说了不。那之后你被迫要做什么，是你自己的事。",
 "[bitter] Get the lift working.": "[bitter] 把升降台弄好。",
 "I said no.": "我说了不。",
 "Who says I can't just take it from you?": "谁说我就不能直接从你这儿拿走？",
 "You need some help over there?": "你那边需要帮忙吗？",
 "[struggling] No, it's not Eric! It's your-- doom! Stop squirming!":
    "[struggling] 不，不是 Eric！是你——的死期！别乱动！",
 "Oh, this is real real!": "哦，这是真的真的！",
 "Wait, wait wait wait, that's not Eric!": "等等，等等等等，那不是 Eric！",
 "Oh, Eric? Aw, is that you?": "哦，Eric？哎呀，是你吗？",
 "Wait wait wait, what is this? Is this real or is this-- is this a joke?":
    "等等等等，这是什么？这是真的还是——是开玩笑？",
 "It looks like you're struggling a bit.": "你看起来有点吃力。",
 "I'm not really doing anything...": "我其实什么都没做……",
 "I already took out mine, so...": "我已经把自己那份解决了，所以……",
 "This is so... awesome.": "这真是……太酷了。",
 "I feel like that's the case with most corporations.":
    "我觉得大多数公司都这样。",
 "Man... You, you might work for the worst corporation in the universe... but they do make some cool stuff.":
    "天哪……你，你可能在为全宇宙最烂的公司干活……但他们确实造了些酷东西。",
 "I suppose you're not completely useless after all.":
    "我想你终究也不是完全没用。",
 "Ooh look at us, we're like best friends now.":
    "哦哦看看我们，我们现在像最好的朋友了。",
 "Not quite.": "不完全是。",
 "That's what I'm talking about.": "这才对嘛。",
 "Uh... no... that was not what I was talking about.":
    "呃……不……我不是说那个。",
 "Great!": "太好了！",
 "Did you mean to do that?": "那是你有意做的吗？",
 "Oh... that guy... again.": "哦……那家伙……又来了。",
 "What if I say please?": "要是我说“请”呢？",
 "Even though I've technically said it twice now.":
    "虽然严格来说我已经说了两遍了。",
 "'Cause I'm not saying please.": "因为我不会说“请”。",
 "Would that make it easier for you?": "那会让你好受点吗？",
 "Can I help you?": "有什么能帮你的？",
 "Your stun baton...": "你的电击棒……",
 "It's the JR4000. Can I... Can I see it? Hold it, I guess I should say.":
    "是 JR4000。我能……我能看看吗？拿着看看，我想我该这么说。",
 "No... it's too late.": "不……太迟了。",
 "We have to get to that lift.": "我们得去那部升降台。",
 "Wait wait, no no no, stop, stop.": "等等等等，不不不，停，停。",
 "[whispered] Crap.": "[whispered] 糟。",
 "[Smack It]": "[拍它]",
 "[Hack It]": "[黑它]",
 "[filtered]\tPassword Override. System online.":
    "[filtered]\t密码覆写。系统上线。",
 "This is gonna be an akward transition for relatively calm, to somewhat panicked":
    "从相对平静到有点慌张，这个过渡会有点生硬",
 "This is who I've always been.": "我一直就是这样的人。",
 "It's not easy.": "这不容易。",
 "I have to make it back.": "我必须回去。",
 "Choke/Attack": "锁喉/攻击",
 "Stun": "电晕",
 "Bandit Guard": "土匪守卫",
 "Press": "按",
 "[whispered]It's not, I-": "[whispered]不是的，我——",
 "[whispered] I've got a shot.": "[whispered] 我有机会开枪。",
 "[whispered] They have the money.": "[whispered] 钱在他们那儿。",
 "Catch": "接住",
 "Very funny Vaughn!": "真好笑，沃恩！",
 "Let us out!": "放我们出去！",
 "Chill out, Sasha!": "冷静点，萨莎！",
 "Hey, Vaughn! Open up, buddy! Hello!?":
    "嘿，沃恩！开门，哥们！喂！？",
 "Ha ha, you are hilarious, now open the damn hatch!":
    "哈哈，你真逗，现在把那该死的舱门打开！",
 "Would you chill out?": "你能不能冷静点？",
 "I'll manage.": "我应付得来。",
 "This is gonna get us killed.": "这会害死我们。",
 "Just shoot them already!": "直接开枪打他们啊！",
 "[sarcastic]Aww, shucks. You mean it?": "[sarcastic]哎呀，哪敢当。你说真的？",
 "I really appreciate that.": "我真的很感激。",
 "Aw, shucks.": "哎呀，哪敢当。",
 "What a relief.": "真让人松口气。",
 "Wait...": "等等……",
 "Hey, relax!": "嘿，放松！",
})

# —— 补漏 ——
T.update({
 "VAUGHN.": "VAUGHN.",
})
