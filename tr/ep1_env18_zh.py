# 批次3-5：第1章 env_18_arenabattleground_actionsequence（竞技场车赛 + Vasquez 电话交易 + Felix 摊牌）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py','_a'), ('ep1_env19_zh.py','_b'), ('ep1_env15_zh.py','_c')):
    T.update(_load(_f, _n))
T.update({
 # —— 玩家选项 / 短句 ——
 "Not a chance.": "想都别想。",
 "What the hell?!": "搞什么鬼？！",
 "Fine, take it.": "行，拿去吧。",
 "I'll go.": "我去。",
 "We should stay here.": "我们该待在这儿。",
 "Sasha, you go.": "萨莎，你去。",
 "I think I can do this!": "我觉得我能行！",
 "I don't think I can do this.": "我觉得我不行。",
 "It's that old guy!": "是那老头！",
 "You have *no idea* what we've been through.": "你*根本不知道*我们经历了什么。",
 "Man, are we lucky you decided to show up when you did.": "老天，你来得可真是时候。",
 "Holy crap, Felix, I have *never* been so happy to see your ugly face. You really saved our asses back there.":
    "我的天，菲利克斯，我*从没*这么高兴见到你这张丑脸。你刚才真救了我们。",
 "I mean, really...[turns to Vaughn] What timing, right?": "我是说，真的……[turns to Vaughn] 这时机也太巧了吧？",
 "Felix?": "菲利克斯？",
 "I thought you were gonna stay outside? Wasn't *that* the plan?": "我以为你会待在外面？*不是说好*这样吗？",
 "*Man*, how'd you-- how'd you even get in here? Or know where to go?":
    "*老天*，你——你怎么进来的？还知道该往哪儿走？",
 "Let's just pick up Rhys and Sasha and go home.": "接上 瑞斯 和 萨莎 就回家吧。",
 "Where are you going? Is there like a plan here?": "你去哪儿？这有什么计划吗？",
 "Hey! There they are again.": "嘿！他们又出现了。",
 "Sasha!": "萨莎！",
 "Hey, Felix, slow down!": "嘿，菲利克斯，慢点！",
 "Our friends are right there!": "我们的朋友就在那儿！",
 "[stern]*Drivers* *drive*.": "[stern]*司机*就该*开车*。",
 "Just one seat belt.": "就系一条安全带。",
 "You remember what I said before, Fiona? [beat] I quit.": "你还记得我之前说的话吗，Fiona？[beat] 我不干了。",
 "Felix! Stop!": "菲利克斯！停车！",
 "What the Hell are you doing?!": "你他妈在干什么？！",
 "You're gonna hit Sasha!": "你要撞到 萨莎 了！",
 "[struggling for the wheel]": "[struggling for the wheel]",
 "Yahhhh!": "呀啊——！",
 "[jumping out of the way yell]": "[jumping out of the way yell]",
 "What the Hell was th--[sees some bandits about to attack them]Ahhhhhhh!":
    "那他妈是什么——[sees some bandits about to attack them]啊啊啊啊！",
 "[in pain moans, then softly, to Fiona] Your uncle is a real asshole.":
    "[in pain moans, then softly, to Fiona] 你叔叔真是个混蛋。",
 "[calling back] You'll be alright, Fiona. You're young... youngish... and... Vallory'll forgive you. [beat] Maybe.":
    "[calling back] 你会没事的，Fiona。你年轻……还算年轻……而且……瓦洛里 会原谅你的。[beat] 也许吧。",
 "Felix!": "菲利克斯！",
 "You'll be... fine.": "你会……没事的。",
 "Trust in that!": "相信这一点！",
 "[furious] Have you lost your *God damned* mind! What in the living *Hell* is wrong with you!":
    "[furious] 你*他妈的*疯了吗！你到底*怎么回事*！",
 "[calling out] What is wrong with me! What's *wrong* with me? Are you kiddin' me, girl!":
    "[calling out] 我怎么回事！我*怎么*回事？你在跟我开玩笑吗，丫头！",
 "[furious] Felix! You asshole bastard prick mother f-- just what-- what in the living *Hell* is wrong with you!":
    "[furious] 菲利克斯！你这混蛋王八蛋狗娘养的——你——你到底*怎么回事*！",
 "[furious] We were *family*, you asswipe! Doesn't that-- doesn't that *mean* anything to you!":
    "[furious] 我们*是一家人*，你这混蛋！那——那对你*一点意义*都没有吗！",
 "[calling out] Oh, *I'm* the prick! *I'm* the bastard?": "[calling out] 哦，*我*是混蛋！*我*是王八蛋？",
 "[calling out] Oh, I'm the one acting crazy?! Huh?!": "[calling out] 哦，是我在发疯？！啊？！",
 "[calling out] Don't you-- *Don't* you look at me like that, alright! This ain't on me!":
    "[calling out] 你别——*别*那么看我，行吗！这不是我的错！",
 "*Felix.* C'mon, we're a team, man. They're gonna write books about us, why would you wanna mess with that?":
    "*菲利克斯。*别这样，我们是一个团队啊老兄。他们以后会写书讲我们的故事，你干嘛要毁掉它？",
 "Because I'm *tired*, that's why.": "因为我*累了*，就这么简单。",
 "You'll be finer without me... trust in that.": "没我你们会更好……相信这一点。",
 "*I'm* the one stuck to Vallory, okay? You know what I wouldn't give to be in your shoes?":
    "被绑在 瓦洛里 身边的是*我*，行吗？你知道我多想跟你换个位置？",
 "If you ran, do you think *anyone* would give two craps about it? No, they wouldn't.":
    "你要是跑了，你觉得*有人*会在乎吗？不，没人会在乎。",
 "So sorry if I don't have any sympathy for this... woe is me act.":
    "所以抱歉，我对这套……「我好可怜」的戏码一点同情都没有。",
 "You have no idea what you're talkin' about.": "你根本不知道自己在说什么。",
 "[light laugh] Gimme a break, Felix. You've retired, what, six times in ten years?":
    "[light laugh] 得了吧，菲利克斯。十年里你退休了，大概六次？",
 "This is your life, this is what you *do*. You'd be back in a week, tops.":
    "这就是你的生活，这就是你*干的*事。你顶多一周就会回来。",
 "Sure, Fiona.": "好啊，Fiona。",
 "I want you to understand it's all been a nice little romp with ya, but...":
    "我想让你明白，跟你一起的这段还算挺开心的，可是……",
 "I'm just too tired for this crap.": "我只是太累了，懒得再折腾这些。",
 "Just stick with you while try to con Vallory *and* Hyperion, and then nearly get us killed trying to clean up that mess? No, thanks.":
    "陪着你一边骗 瓦洛里 *一边*骗 亥博龙，然后为了收拾烂摊子差点把我们都害死？不了，谢谢。",
 "You keep your delusions of grandeur, I'll keep this cash.": "你留着你的宏大幻想，这钱我留着。",
 "We *aren't* a team. We *never* were.": "我们*不是*一个团队。我们*从来都不是*。",
 "You were *wrong* then, and you're *wrong* now.": "你当时*错了*，现在也*错了*。",
 "*You're* the one stuck? Remember? That's what you said, right? That it was *all* on you!":
    "*你*才是被绑住的？记得吗？你是这么说的，对吧？说这*全都*怪你！",
 "This is my life, this what I *do*, remember?": "这就是我的生活，这就是我*干的*事，记得吗？",
 "We worked together when we worked together and it wasn't anythin' more than that... for *either* of us.":
    "我们合作的时候就是在合作，除此之外什么都不是……对*我们两个*都是。",
 "I *told* you I was gonna quit, but... you *never* friggin' listen, do you? [beat] Well listen to this: the money is mine now.":
    "我*告诉过*你我要退出，可……你*从来*不听，是吧？[beat] 那听好这句：钱现在是我的了。",
 "Well listen to this: the money is mine now.": "那听好这句：钱现在是我的了。",
 "Sasha, are you alright!": "萨莎，你没事吧！",
 "[cold] Gettin' old sucks, Fiona.[beat] You still have time, but I-- I *need* this money.":
    "[cold] 变老很糟，Fiona。[beat] 你还有时间，可我——我*需要*这笔钱。",
 "[calling out to him] Felix, stop--[gets cut off]": "[calling out to him] 菲利克斯，等等——[gets cut off]",
 "God! Ugh! Yeah, I'm-- I'm fine, just go get the son of a bitch.": "天！呃！嗯，我——我没事，去把那混蛋抓回来。",
 "Keep back, now. I've been missin' on purpose, but that can change.": "退后。我一直是故意打偏的，但那随时可以变。",
 "You have *not* been missing on purpose!": "你*根本*不是故意打偏的！",
 "You just keep back now.": "你就退后吧。",
 "A retirement needs a pension. You'll understand one day.": "退休需要养老金。你总有一天会明白。",
 "[struggling with it] This... stupid... heavy...\nugh.": "[struggling with it] 这……蠢……重……\n呃。",
 "Felix, stop! It's boobytrapped!": "菲利克斯，别！里面有诡雷！",
 "[quietly] I'm sorry.": "[quietly] 对不起。",
 "[muttering] Hyperion craftmanship...": "[muttering] 亥博龙的做工……",
 "Enjoy the money, while you can.": "趁还能享受，好好享受这笔钱吧。",
 "[struggling] This isn't about... *vanity*, Fiona... this... is about--[gets cut off]":
    "[struggling] 这不是为了……*面子*，Fiona……这是……为了——[gets cut off]",
 "Damn it! [beat] Today sucks.": "该死的！[beat] 今天糟透了。",
 "[happy sigh] *Boy*, am I ever glad to see you!": "[happy sigh] *老天*，见到你真是太好了！",
 "[tired] This seemed easier before [beat] why was that?": "[tired] 之前好像没这么难。[beat] 为什么来着？",
 "Oh yeah, because I had that Loader Bot!": "哦对，因为那时候我有那台装载机器人！",
 "You can get one of those?": "那种东西你也能弄到？",
 "I might be able to use Nakayama's codes...": "也许我能用 Nakayama 的代码……",
 "Connecting...": "正在连接……",
 "[excited, rushed]Oh, Yvette, thank you! Listen, I need you to send me down a--[cut off]":
    "[excited, rushed]哦，Yvette，谢谢你！听我说，我需要你送一台——[cut off]",
 # —— Vasquez 电话（核心场景） ——
 "[processed: phone] Oh, Professor Nakayama!  You sound different.": "[processed: phone] 哦，Nakayama 教授！你的声音变了。",
 "Vasquez.": "Vasquez。",
 "[processed: phone] Glad you're having a pleasant little vaction down on Pandora, buddy.":
    "[processed: phone] 很高兴你在 潘多拉 度假度得愉快，老兄。",
 "Could be worse.": "还不算最糟。",
 "[processed: phone] But look --  I'm not gonna sugar coat things...":
    "[processed: phone] 不过听着——我不打算粉饰太平……",
 "[processed: phone] Unless you bring the Vault Key back here lickety-split, there's not a lot I can do to prevent your *reacquistion* -- and your being boiled down into tanker fuel.":
    "[processed: phone] 除非你赶紧把秘藏钥匙带回来，否则我很难阻止他们*重新接管*你——以及把你煮成油轮燃料。",
 "[processed: phone] But you know what I mean.": "[processed: phone] 不过你懂我意思。",
 "[processed: phone]Not going to really, beat around the bush.": "[processed: phone]我就不绕弯子了。",
 "Vasquez, your entire \"deal\" was a fake, there was *never* any Vault Key!":
    "Vasquez，你那整套「交易」是假的，*从来就*没有什么秘藏钥匙！",
 "[processed: phone] Really...": "[processed: phone] 真的……",
 "Yes! It was a forgery, alright? Made by some grifters who just wanted the money.":
    "对！那是伪造的，行吗？几个只想骗钱的骗子做的。",
 "[processed: phone] Well,[laughing] joke's on me. Or you. As you actually went down there.":
    "[processed: phone] 好吧，[laughing] 那可把我耍了。或者说把你耍了——毕竟真下去的是你。",
 "The key was destroyed, it's gone, so there *isn't* any key to bring back.":
    "钥匙毁了，没了，所以*没有*什么钥匙可带回去。",
 "A Vault Hunter showed up, and... things sorta went to Hell.": "一个秘藏猎人出现了，然后……事情就全乱了。",
 "[processed: phone] Huh.[laughing] Good thing I didn't actually go down there.  Thanks for stepping in front of that bullet for me, chump.":
    "[processed: phone] 呵。[laughing] 幸好我没真下去。谢谢你替我挡了这一枪，笨蛋。",
 "Oh, go screw yourself, buddy, even if I *had* the Key, do you think after all of this *crap* I've been through I'd just *hand* the thing over?":
    "哦，去你的吧老兄。就算我*真有*那把钥匙，你觉得经历这一堆*破事*之后，我会就这么*交出去*？",
 "[processed: phone call]  You don't have it?": "[processed: phone call]  你没有？",
 "Look, I'm a little busy right now  -- so unless you're calling to say you're sorry for being a giant dick, I really can't talk.":
    "听着，我现在有点忙——所以除非你打电话是来为你的混蛋行径道歉，否则我真没法聊。",
 "[processed: phone] So, what i'm saying is...": "[processed: phone] 所以，我要说的是……",
 "[falling into a pit] Aiiiiiiiiigh!": "[falling into a pit] 啊啊啊啊！",
 "[worried] Uhhhh, is that...[gonna come crashing down]?": "[worried] 呃，那个……[会砸下来]吗？",
 "[pickup3] [processed: phone]Your buddy Vaughn signed the expense report.":
    "[pickup3] [processed: phone]你哥们儿 沃恩 在报销单上签了字。",
 "[pickup3] [processed: phone] I spoke with August, and I know about the key. Or, the not key.":
    "[pickup3] [processed: phone] 我跟 August 聊过了，我知道钥匙的事。或者说，那把假钥匙。",
 "What are you talking about?": "你在说什么？",
 "[processed: phone] So, just sell out your ugly weirdo friend.": "[processed: phone] 所以，把你那又丑又怪的哥们儿卖了吧。",
 "[processed: phone] I mean you kind of have to since it's your only option.":
    "[processed: phone] 我是说，你基本上只能这么做，因为这是你唯一的选择。",
 "Ugh. Seriously?": "呃。认真的？",
 "Okay. But I get half the money.": "行。但钱我要一半。",
 "[pickup3] [processed: phone][insincere]Right, sure thing. Sounds like a deal. [beat] Just get that money back up here so we can split it, and throw your friend out an airlock.":
    "[pickup3] [processed: phone][insincere]好，没问题。听起来就这么定了。[beat] 把钱带回来我们分，顺便把你朋友扔出气闸。",
 "Wait wait wait, *why* are you doing this? What's in it for you?":
    "等等等等，你*为什么*要这么做？这对你有什么好处？",
 "Yet!": "还没呢！",
 "Oh c'mon, I haven't even *agreed* to it!": "哦拜托，我根本*还没答应*呢！",
 "[processed: phone]I thought I explained myself pretty well... maybe I should have used smaller words.":
    "[processed: phone]我以为我解释得挺清楚了……也许我该用小一点的词。",
 "I told you to go screw yourself.": "我跟你说过去你的吧。",
 "Go screw yourself!": "去你的吧！",
 "[processed: phone call] Whatever, champ, it's your funeral.": "[processed: phone call] 随便吧，冠军，那是你自己的葬礼。",
 "Thanks!": "谢了！",
 "Oh, give me a break, do you really think I'd just roll over on Vaughn just to get in your good graces? He's like my *best friend*.":
    "哦，得了吧，你真以为我会为了讨好你就把 沃恩 卖了？他可是我*最好的朋友*。",
 "Wow, Rhys. I'm impressed.  Truly.": "哇，瑞斯。我佩服你。真的。",
 "I think I'll stand by my original thought, Vasquez. Go screw yourself.":
    "我还是坚持我最初的想法，Vasquez。去你的吧。",
 "You continue to underestimate me, Sasha.": "你还是低估我了，萨莎。",
 "I'll be honest, I thought you'd give up Vaughn in a heartbeat.": "老实说，我以为你会毫不犹豫地出卖 沃恩。",
 "Yeah, and... wait, *Vaughn's* an asshole?": "是啊，而且……等等，*沃恩* 是混蛋？",
 "What? No, *Vasquez* is an asshole, why would I say that *Vaughn* is an asshole?":
    "什么？不是，*Vasquez* 是混蛋，我干嘛要说 *沃恩* 是混蛋？",
 "I don't know, that's why I asked!": "我不知道，所以才问你啊！",
 "Not that we aren't grateful!": "我们不是不感激你！",
 "That's pretty low, even for someone like you.": "这挺下作的，就算对你这种人来说也是。",
 "I can't believe you'd screw over Vaughn for *that* guy?": "我不敢相信你会为了*那种人*出卖 沃恩？",
 "Yeah, screw Vaughn!": "对，去他的 沃恩！",
 "I was lying to him!": "我是在骗他！",
 "I wanted to figure out his angle!": "我想摸清他的目的！",
 "Screw Vaughn. [beat] Whatever it takes to get off this wretched planet and back to my old life, I'll do it.":
    "去他的 沃恩。[beat] 只要能离开这颗鬼星球、回到我原来的生活，我什么都干。",
 "[cold] Good to know.": "[cold] 知道就好。",
 "Sasha, look...[gets cut off by blast]": "萨莎，你看……[gets cut off by blast]",
 "I dunno. Didn't sound like *lying* to me.": "不知道。听起来可不像是*在骗人*。",
 "Please, I was *lying* to Vasquez! Like I would roll over on anyone for that jerk.":
    "拜托，我是在*骗* Vasquez！我怎么可能为了那个混蛋出卖任何人。",
 "I dunno. It sounded like you were *pretty* open to it...": "不知道。听起来你*挺*愿意的……",
 "Sasha, that is what's called a *negotiation*. I was trying to suss out Vasquez's real motives here.":
    "萨莎，那叫*谈判*。我是想摸清 Vasquez 真正的动机。",
 "*Not* *nice*.": "*不* *厚道*。",
 "Did you hear that \"everyone dies\" part?": "你听到「所有人都会死」那句了吗？",
 "What the hell?": "搞什么鬼？",
 "Fiona?": "Fiona？",
 "Rhys?": "瑞斯？",
 "Sasha?": "萨莎？",
 "Vaughn?": "沃恩？",
 "Damn it Felix!": "该死的 菲利克斯！",
 "You got the money. Good.": "你拿到钱了。很好。",
 "Some \"best friend\".": "好一个「最好的朋友」。",
 "Seems like loyalty only goes one way.": "看来忠诚只是单向的。",
 "I guess all's fair in business and murder.": "看来在生意和谋杀里，什么都算公平。",
 "Whatever it takes to get off this planet and back to my old life, I'll do it.":
    "只要能离开这颗星球、回到我原来的生活，我什么都干。",
 "How do you people live with yourselves?": "你们这种人怎么活得下去？",
 "He's lucky to have you as a friend.": "有你这样的朋友真是他的运气。",
 "And here I thought he was just your little puppet.": "我还以为他只是你的小傀儡。",
 "Lucky for Vaughn it's more profitable for you to keep him around.": "沃恩 运气不错——留着他对你更划算。",
 "I know -- that's exactly what I told him.": "我知道——我就是这么跟他说的。",
 "I'm impressed, Rhys.  Truly.": "我佩服你，瑞斯。真的。",
 "He'd do the same for me.": "换了他也会这么做。",
 "No way I'd sell-out *my guy* to that prick Vasquez.": "我绝不可能把*我的人*卖给 Vasquez 那个混蛋。",
 "Damn right it is. Vaughn's done a lot for me.": "当然不是。沃恩 为我做了很多。",
 "Or if not, it'll all be over soon enough.": "要是不行，反正很快也就结束了。",
 "Well at least I'm gonna die rich.": "至少我会死得很有钱。",
 "You said I was gonna die someday. Well at least I'm gonna die rich.":
    "你说过我总有一天会死。至少我会死得很有钱。",
 "Well [beat] I've looked out for you long enough. Now I'm focusing on *my* job of looking out for number one. [beat]":
    "好吧……[beat] 我照顾你够久了。现在我要专心做*我的*工作——照顾好第一号人物。[beat]",
 "Focus on the job, you said. Well [beat] I've looked out for you long enough. Now I'm focusing on *my* job of looking out for number one.":
    "你说专心干活。好吧……[beat] 我照顾你够久了。现在我要专心做*我的*工作——照顾好第一号人物。",
 "[a little freaked out] Yeah. [beat, more composed] Yeah, I'm fine, he shot at me!":
    "[a little freaked out] 嗯。[beat, more composed] 嗯，我没事——他朝我开枪了！",
 "Aha!": "啊哈！",
 "Damned paranoid Hyperion scumbags!": "该死的多疑 亥博龙渣滓！",
 "Woo hoo! I win the mystery -- [gets cut off] box!": "呜呼！我赢了神秘——[gets cut off] 箱！",
 "Heh... I'll try. I'm gonna miss you kid. Make sure to look after your-- [bomb goes off]sister.":
    "嘿……我会的。我会想你的，孩子。记得照顾好你——[bomb goes off]妹妹。",
 "[betrayed]I can't believe he did that...": "[betrayed]我不敢相信他真这么干了……",
 "Why?": "为什么？",
 "There it is.  Let's go get it.": "就在那儿。去拿吧。",
 "*If*...": "*如果*……",
 "[detached] I do want it.": "[detached] 我确实想要它。",
 "[processed: megaphone] Get set!": "[processed: megaphone] 各就各位！",
 "Well, whatever happens now... It looks like you're gonna have to do *a lot* of paperwork when you get back up there.":
    "不管现在发生什么……看来你回去之后得写*一大堆*报告。",
 "Vasquez is just one guy. I'll get all this sorted out before he can make another move.":
    "Vasquez 只有一个人。我会在他下一步动手之前把事情都处理好。",
 "This is my last trip around the ferries wheel.": "这是我最后一次坐这趟摩天轮了。",
 "Felix come back!": "菲利克斯 回来！",
 "I need enough money to get out and just disappear. I don't have the time, or the energy, to do this again.":
    "我需要足够的钱脱身、彻底消失。我没时间也没精力再来一次了。",
 "It'd last us all a week... if that.": "够我们所有人花一个星期……如果够的话。",
 "You, and Sasha... and those Hyperion lugheads...": "你，还有 萨莎……还有 亥博龙那两个蠢货……",
 "Don't make me break my promise to your father.": "别让我违背对你父亲的承诺。",
 "[pickup3] Look, I'm just going to take the money, and disappear... it's not enough for all of us.":
    "[pickup3] 听着，我打算拿了钱就消失……这钱不够我们所有人分。",
 "...oh god... Felix.": "……天啊……菲利克斯。",
 "[quiet and to herself]He shot at me...": "[quiet and to herself]他朝我开枪了……",
 "You'll be fine. I know it. You're young enough, you still bounce...":
    "你会没事的。我知道。你还年轻，还弹得回来……",
 "[quiet]I'm sorry...": "[quiet]对不起……",
 "You don't give up. You get things *done*. You go for that brass ring every time.":
    "你从不放弃。你能把事*办成*。每次你都会去够那枚金环。",
 "[processed: phone]Together, we could do great things...": "[processed: phone]只要我们联手，能成就大事……",
 "And you... you're the little can do solider, aren't you?": "而你呢……你就是那个「啥都能干」的小兵，对吧？",
 "KNo": "KNo",
 "[processed: phone]I heard about his little *pesky* girl problem. Some chick named Sasha. Broke his heart. I feel for the man, truly.":
    "[processed: phone]我听说了他那点*烦人的*感情问题。一个叫 萨莎 的妞，伤了他的心。我真同情他，真的。",
 "[processed: phone]You know, in talking to my buddy August...": "[processed: phone]你知道，跟我哥们儿 August 聊天的时候……",
 "[processed: phone] Help me find this Sasha chick and maybe I'll cut you *and* Vaughn a break.":
    "[processed: phone] 帮我找到这个叫 萨莎 的妞，也许我就能放*你和* 沃恩 一马。",
 "Millions get lost up here all the time anyways. No skin off my nose.": "反正上面每年都要丢几百万。不关我的事。",
 "[processed: phone]Broke his heart. I feel for the man, truly.": "[processed: phone]伤了他的心。我真同情他，真的。",
 "Yeah?": "是吗？",
 "Rhys... don't do this.": "瑞斯……别这样。",
 "[processed: phone]I take back when I said about the spunk.": "[processed: phone]我之前说的「有种」，我收回。",
 "[processed: phone]You're just dumb, apparently.": "[processed: phone]看来你只是蠢。",
 "[processed: phone] I thought you were supposed to be smart, Rhys.  Yet here I am, extending you the offer of a lifetime and-[CLICK]":
    "[processed: phone] 我以为你挺聪明的，瑞斯。可现在我给你开出这辈子最好的条件，而你——[CLICK]",
 "I hate that guy.": "我讨厌那家伙。",
 "Vasquez, you do your own dirty work.": "Vasquez，脏活你自己干。",
 "I'll track 'em down.": "我会把他们找出来。",
 "You know what, I can do that.": "你知道吗，我能做到。",
 "[processed: phone]Great! As soon as you find 'em, send me an Echo blip and I'll take care of it from there.":
    "[processed: phone]太好了！一找到他们就给我发个 Echo 信号，剩下的我来处理。",
 "You asshole!": "你这混蛋！",
 "And why should I even trust you?": "我凭什么要信你？",
 "Well, you": "好吧，你",
 "Just trying to draw him out and see all he was planning. We found out August had a hit on you. I was *lying* to him.":
    "只是想把他引出来，看看他到底在谋划什么。我们查到 August 对你下了追杀令。我是在*骗*他。",
 "...you...": "……你……",
 "You're all right. [beat] Sometimes.": "你这人还行。[beat] 有时候。",
 "[agreeing]Sometimes.": "[agreeing]有时候。",
 "Screw you. [beat] Whatever it takes to get out form under Hyperion's thumb. You have no idea what they're like.":
    "去你的。[beat] 只要能摆脱 亥博龙的掌控，我什么都干。你根本不知道他们什么样。",
 "*Really*, Rhys? Oh, you are low.": "*真的*，瑞斯？哦，你可真够下作的。",
 "You're--[cutoff]": "你——[cutoff]",
 "And if the key's gone, the key's gone. Gotta look forward my man.": "钥匙没了就是没了。得往前看，老兄。",
 "[processed: phone]Because I like to be forward with people...": "[processed: phone]因为我喜欢对人开诚布公……",
 "[processed: phone]I'll just come out and say this. Okay?": "[processed: phone]我就直说了，行吗？",
 "[processed: phone] What matters though, is you still stole a million dollars from Hyperion's picnic basket... but the only people who know that are *me* and *you.*":
    "[processed: phone] 关键在于，你毕竟从 亥博龙的野餐篮里偷了一百万……而知道这事的只有*我*和*你*。",
 "[processed: phone]You help me pin this whole thing on Vaughn, no more janitorial. You'll be my number two. My left handed man. Key to the executive washroom and everything. [beat] Together, we could do great things...":
    "[processed: phone]你帮我把这事全栽到 沃恩 头上，就不用再打扫卫生了。你就是我的二号人物。我的左膀右臂。高管洗手间的钥匙什么的。[beat] 只要我们联手，能成就大事……",
 "Target Acquired. Termination loop beginning.": "目标已锁定。终止循环开始。",
 "Did Rhys get Yvette to send another loaderbot?": "瑞斯 让 Yvette 又送了一台装载机器人来？",
 "AAAAH!": "啊啊啊！",
 "GAAAH!": "嘎啊啊！",
 "w-w-w-hy am I p-p-p-programed to f-f-f-feel p-p-pain...": "为、为、为什么我、我、我被程序设定成、成、成会感到疼、疼、疼痛……",
 "That... I cannot control.": "那个……我控制不了。",
 "Hey nice, another one.": "嘿不错，又来一台。",
 "What was that?!": "那是什么？！",
 "[processed: phone]We'll figure it out when you get back here.": "[processed: phone]等你回来我们再想办法。",
 "[processed: phone]But this is a limited time offer, Rhys.": "[processed: phone]但这是限时优惠，瑞斯。",
 "[processed: phone]You probably shouldn't. Shows you're smart.": "[processed: phone]你大概不该答应。那才说明你聪明。",
 "[processed: phone]I will scratch your back. With the full might of Hyperion.":
    "[processed: phone]我会帮你这个忙。动用 亥博龙的全部力量。",
 "[processed: phone]The offer stays on the table for a limited time. And if you don't scratch my back?":
    "[processed: phone]这个条件只在限期内有效。而你要是不帮我这个忙？",
 "[processed: phone]It's something I can do now. I have access to like the moon shot cannon a few times a week. Just moon shot anything I want!":
    "[processed: phone]这事我现在就能办到。我一星期能用几次月击炮。想轰什么就轰什么！",
 "[processed: phone]Sp just watch your [beat, as he realizes he's being redundant again] back, Rhys.":
    "[processed: phone]所以，看好你的[beat, as he realizes he's being redundant again] 背后，瑞斯。",
 "What, was *That*!?": "什么，那*是*什么！？",
 "Oh, there is one other thing.": "哦，还有一件事。",
 "[processed: phone]oh, and there's one other thing.": "[processed: phone]哦，还有一件事。",
 "[processed: phone]Favors too, way better than money. The one he really cares about, is some gal type named Sasha.":
    "[processed: phone]人情也算，而且比钱管用得多。他真正在乎的，是个叫 萨莎 的姑娘。",
 "[processed: phone]Help me find this Sasha chick and maybe I'll let you just keep the whole million.":
    "[processed: phone]帮我找到这个叫 萨莎 的妞，也许我就让你独吞那整整一百万。",
 "Still can't believe what you did to your friend.": "还是不敢相信你对自己朋友做的事。",
 "Maybe I was just stringing Vasquez along to see what he'd do.": "也许我只是在吊着 Vasquez，看他下一步做什么。",
 "Maybe. Maybe not.": "也许吧。也许不是。",
 "Unbelievable.": "难以置信。",
 "Good workin' with ya, buddy.": "跟你合作愉快，老兄。",
 "Bring me that girl, and you'll be handsomely rewarded.  If August finds them first, we both miss out.":
    "把那姑娘带来，你会得到丰厚回报。要是 August 先找到他们，我们俩都没份。",
 "You've got a day. Either bring me Vaughn or those girls, or I'll be sending one of our Loaderbot friends down to pay you a visit.":
    "你有一天时间。要么把 沃恩 带来，要么把那两个姑娘带来，否则我就派一台装载机器人下去拜访你。",
 "You're a terrible shot. You have *not* been missing on purpose.": "你枪法烂透了。你*根本*不是故意打偏的。",
 "A million dollars is plenty for all of us. It's more money than we've ever seen!":
    "一百万对我们所有人来说都够多了。那是我们见过最多的钱！",
 "Am I the one who just cut a deal with a couple of Hyperion goons?": "刚跟两个 亥博龙打手做交易的人是我吗？",
 "Hey, get back here!": "嘿，回来！",
 "[pickup3] [processed: phone]Money good. Vaughn bad. Bring back money. Vaughn get dead, Rhys get promotion.":
    "[pickup3] [processed: phone]钱好。沃恩 坏。把钱带回来。沃恩 死，瑞斯 升职。",
 "...I still don't get the why.": "……我还是不明白为什么。",
 "[processed: phone]Does that really matter?": "[processed: phone]那真的重要吗？",
 "[processed: phone]Together we could rule this galaxy you and I--[gets hung up on]as partner and son.":
    "[processed: phone]我们可以一起统治这个星系，你和我——[gets hung up on]像搭档，也像父子。",
 "Eh...": "呃……",
 "You're thinking about it.": "你在考虑了。",
 "I can not *belive* you are thinking about it!": "我*不敢相信*你真在考虑！",
 "What? I...": "什么？我……",
 "Sasha, look...": "萨莎，你看……",
 "[pickup3] Split five ways? Not even close. Even split three it's [considers for a beat] look, I need enough money to get out and just disappear. I don't have the time, or the energy, to do this again.":
    "[pickup3] 五个人分？差得远。就算三个人分也……[considers for a beat]听着，我需要足够的钱脱身、彻底消失。我没时间也没精力再来一次。",
 "[processed: megaphone] Fifi, show the people today's fabulous prize.":
    "[processed: megaphone] Fifi，给大伙看看今天的豪华大奖。",
 "My precious.": "我的宝贝。",
 "[in that sing-songish psycho way, not played straight] Winner is responsible for all taxes!":
    "[in that sing-songish psycho way, not played straight] 获奖者需自行承担全部税费！",
 "Damn. Hyperion's just as cutthroat as Pandora.": "见鬼。亥博龙跟 潘多拉 一样狠。",
 "I haven't even agreed -- [gets cut off] to it.": "我根本还没答应——[gets cut off]这事。",
 "[pickup3] I didn't even agree to it.": "[pickup3] 我根本没答应过。",
 "[pickup3] [processed:phone] Bring back the cash and help me pin the whole debacle on him and no more janitorial. You'll be my number two. My left handed man. Key to the executive washroom and everything.":
    "[pickup3] [processed:phone] 把钱带回来，帮我把这整场烂事栽到他头上，你就不用再打扫卫生。你就是我的二号人物。我的左膀右臂。高管洗手间的钥匙什么的。",
 "[pickup3] [processed:phone] So what matters now is Hyperion being short a million bucks. Of course, the only people who know that right now are *me* and *you.*":
    "[pickup3] [processed:phone] 所以现在关键在于 亥博龙少了一百万。当然，现在知道这事的只有*我*和*你*。",
 "[pickup3] Felix!": "[pickup3] 菲利克斯！",
 "[pickup0][processed: phone] Glad you're having a pleasant little vaction down on Pandora, buddy.":
    "[pickup0][processed: phone] 很高兴你在 潘多拉 度假度得愉快，老兄。",
 "[pickup0][processed: phone] Well,[laughing] joke's on me. Or you. As you actually went down there.":
    "[pickup0][processed: phone] 好吧，[laughing] 那可把我耍了。或者说把你耍了——毕竟真下去的是你。",
 "[pickup0][processed: phone] Huh.[laughing] Good thing I didn't actually go down there.  Thanks for stepping in front of that bullet for me, chump.":
    "[pickup0][processed: phone] 呵。[laughing] 幸好我没真下去。谢谢你替我挡了这一枪，笨蛋。",
 "[pickup0][processed: phone] So, what i'm saying is...": "[pickup0][processed: phone] 所以，我要说的是……",
 "[pickup0][processed: phone]Not going to really, beat around the bush.": "[pickup0][processed: phone]我就不绕弯子了。",
 "[pickup0][processed: phone] I spoke with August, and I know about the key. Or, the not key.":
    "[pickup0][processed: phone] 我跟 August 聊过了，我知道钥匙的事。或者说，那把假钥匙。",
 "[pickup0][processed: phone]Your buddy Vaughn signed the expense report.":
    "[pickup0][processed: phone]你哥们儿 沃恩 在报销单上签了字。",
 "[pickup0][processed: phone][insincere]Right, sure thing. Sounds like a deal. [beat] Just get that money back up here so we can split it, and throw your friend out an airlock.":
    "[pickup0][processed: phone][insincere]好，没问题。听起来就这么定了。[beat] 把钱带回来我们分，顺便把你朋友扔出气闸。",
 "[pickup0][processed: phone]I thought I explained myself pretty well... maybe I should have used smaller words.":
    "[pickup0][processed: phone]我以为我解释得挺清楚了……也许我该用小一点的词。",
 "[pickup0][processed: phone] So, just sell out your ugly weirdo friend.":
    "[pickup0][processed: phone] 所以，把你那又丑又怪的哥们儿卖了吧。",
 "Felix, you saved the day!": "菲利克斯，你救场了！",
 "You were supposed to stay outside!": "你本该待在外面！",
 "How did you get in here?": "你怎么进来的？",
 "Your \"deal\" wasn't real!": "你那笔「交易」是假的！",
 "They key's destroyed!": "钥匙毁了！",
 "Gimme half the money.": "钱分我一半。",
 "Really? Why would you do that?": "真的？你为什么要这么做？",
 "Vaughn's my friend!": "沃恩 是我朋友！",
 "[Hang up]": "[Hang up]",
 "Have you lost your mind?": "你疯了吗？",
 "Felix, you bastard!": "菲利克斯，你这混蛋！",
 "We're family!": "我们是一家人！",
 "Don't do it, it's rigged to explode!": "别碰，它装了引爆装置！",
 "Enjoy it while you can.": "趁还能享受就享受吧。",
 "Keep your eyes on the road!": "看路！",
 "We're doing the best we can.": "我们已经在尽力了。",
 "We're getting that money.": "我们会拿到那笔钱。",
 "You so do not.": "你才不行。",
 "I got this.": "这个我行。",
 "I don't like this.": "我不喜欢这样。",
 "Yeah, no. I really don't like this.": "是啊，不。我真的不喜欢这样。",
 "Nobody likes this! You think I like it?": "没人喜欢这样！你以为我喜欢？",
 "...The Hyperion Mystery Case of Wonder!": "……亥博龙奇妙神秘箱！",
 "Isn't this normal for you?": "这对你来说不算正常吗？",
 "Zer0 has our back.": "有 Zer0 给我们撑腰。",
 "We are so dead.": "我们死定了。",
 "Isn't this what you people do down here? This is cementing everything I assumed about Pandora.":
    "你们这地方的人不就这么干吗？这下我关于 潘多拉 的所有推测都坐实了。",
 "Alright Zer0, you're with us, right, buddy?": "好了 Zer0，你跟我们一伙的，对吧老兄？",
 "*He* can jump. We're screwed.": "*他*能跳。我们完了。",
 "Eh, probably.": "呃，大概吧。",
 "I really, really, really don't like this.": "我真的、真的、真的不喜欢这样。",
 "Okay, let's go. Come on!": "好，走吧。快点！",
 "Okay, so neither of us likes it.": "好吧，那我们俩都不喜欢。",
 "No!  And even if it was, that doesn't mean I like it!": "不！就算真是这样，也不代表我喜欢！",
 "Hurry!": "快！",
 "Rhys, throw it NOW!": "瑞斯，现在扔！",
 "Give me the gun!": "把枪给我！",
 "Fine.": "行。",
 "He's gonna get away!": "他要跑了！",
 "Nice going!": "干得好啊！",
 "Way to go, idiot. Next time...": "干得漂亮，白痴。下次……",
 "...try trusting somebody.": "……试着信个人吧。",
 "Sure, trust a con artist. Great idea.": "当然，信一个骗子。好主意。",
 "Now let's go get--": "现在去把——",
 "You really believe that?": "你真信那话？",
 "See? A little faith goes a long way.": "看到了吧？一点信任能顶大用。",
 "Not really.": "不太信。",
 "[rhetorical]Ugh. Where the hell did the money go? Can't you like, cyborg something up and find it?":
    "[rhetorical]呃。钱到底去哪儿了？你不能像半机械人那样搞点什么把它找出来吗？",
 "No, but I can do you one better.": "不能，但我能给你个更好的办法。",
 "Let's see how these guys deal with a sweet loader bot.": "看看这帮家伙怎么对付一台帅气的装载机器人。",
 ": [pickup 4] You can get one of those?": ": [pickup 4] 那种东西你也能弄到？",
 "Then I'll make this fast.": "那我就快点。",
 "You know what, I really don't have time for--": "你知道吗，我真没时间——",
 "That's right, punchy. I gotta hand it to ya, I didn't think you were capable of something this...*devious*. You might be executive material yet.":
    "没错，硬汉。得承认，我没想到你还能干出这么……*阴*的事。你或许还真有当高管的料。",
 "Screw you.": "去你的。",
 "What money?": "什么钱？",
 "I don't know.": "我不知道。",
 "Because I *heard* that you had a little trouble down there.": "因为我*听说*你在下面遇到点小麻烦。",
 "[menacing]I figure I got a right to know.": "[menacing]我想我有权知道。",
 "And you know. Seeing as IT'S MINE...": "而且你知道。既然那*是*我的钱……",
 "Screw you, Vasquez.": "去你的，Vasquez。",
 "[taken aback]Screw me.": "[taken aback]去我的。",
 "[too loud] SCREW ME?": "[too loud] 去我的？",
 "[Laughs] Oh, Rhys. [laughs again] That's cute. You're like a little baby full of stupid ideas.":
    "[Laughs] 哦，瑞斯。[laughs again] 挺可爱。你就像个满脑子蠢主意的小婴儿。",
 "Gone? I don't know.": "没了？我不知道。",
 "[laughs] Hahaha, good one. Really good. Hilarious.": "[laughs] 哈哈哈，真会说。真会说。太好笑了。",
 "I see.": "我明白了。",
 "It is, Vasquez.": "确实是，Vasquez。",
 "Here's what I'm gonna do, okay buddy? Because I'm a generous guy I'm gonna offer you this, uh, *olive tree.*":
    "我这么办吧，老兄？因为我是个慷慨的人，我要给你这个，呃，*橄榄枝*。",
 "Look, no one else up here needs to know about this little faux pas, all right? So you bring back the money and.. Uh, I'll tell you what... I'll give you your old job back. Before the janitor thing. The respectable job.":
    "听着，上面没别人需要知道这点小失误，行吗？你把钱带回来，然后……呃，这样吧……我把你原来的职位还给你。打扫卫生之前那个。体面的那个。",
 "But I'm just that kinda guy.": "我就是这种人。",
 "It's the kind of spunk gets you places.": "这种「有种」能让你有出息。",
 "I gotta admit, I admire your spunk.": "我得承认，我欣赏你这份「有种」。",
 "*My* kind of spunk.": "*我*欣赏的那种「有种」。",
 "I'm not selling out Vaughn.": "我不会出卖 沃恩。",
 "Why should I trust you?": "我凭什么信你？",
 "[Hang Up]": "[Hang Up]",
 "I want more. Seventy-five percent.": "我要更多。百分之七十五。",
 "Seventy-five? For what?": "七十五？凭什么？",
 "And why would I do that?": "我为什么要那么做？",
 "I want more.": "我要更多。",
 "Okay, I'm in.": "好，我加入。",
 "I don't think so. Vaughn's my friend.": "不行。沃恩 是我朋友。",
 "Hurry up, Rhys. Things are getting tense.": "快点，瑞斯。情况越来越紧张了。",
 "Nope.": "不要。",
 "I know about the Vault key, chum. Okay? I know. So now we've got this problem: a lotta Hyperion cheddar's missing.":
    "我知道秘藏钥匙的事，哥们儿。行吗？我知道。所以现在有个问题：亥博龙少了一大笔钱。",
 "Oh, I don't know, how about putting my best friend on the chopping block?": "哦，我不知道，把我最好的朋友推上案板怎么样？",
 "Okay. Okay, I'm in.": "好。好，我加入。",
 "Sweet. Very sweet.": "爽快。非常爽快。",
 "Oh, you heard all that?": "哦，你全听到了？",
 "Huh, I really thought you'd give him up.": "嗯，我真以为你会把他交出去。",
 "Oh yeah.": "哦对。",
 "Awwww. That's just--I gotta tell ya, that's just adorable. That just warms the cockles.":
    "哦——我得说，这真是太可爱了。暖到人心坎里。",
 "I'll be in touch. You stay safe out there, old buddy.": "我再联系你。你在外面注意安全，老伙计。",
 "Scratch your own nuts.": "你自己挠去吧。",
 "Because one phone call from me and you're in the clear.": "只要我打个电话，你就没事了。",
 "[like a threat]Oh, I'll scratch 'em. I'll scratch 'em hard.": "[like a threat]哦，我会挠的。我会使劲挠。",
 "Really?": "真的？",
 "Come on!": "快点！",
 "There!": "在那儿！",
 "Ack!": "呃啊！",
 "Don't eat--do not, don't-- do not eat the mon--": "别吃——不要，别——别吃那个钱——",
 "Well get it out!": "那就把它弄出来！",
 "You get it out!": "你来弄出来！",
 "[screaming like a girl] Ahhhh!": "[screaming like a girl] 啊啊啊！",
 "Get back here!": "回来！",
 "I'll...stab you!": "我要……捅你！",
 "[screaming like a girl again, but louder] Aaeeeiiiii!": "[screaming like a girl again, but louder] 啊啊啊啊啊！",
 "Don't mention it!": "别客气！",
 "The little one is feeble!": "那个小的很弱！",
 "Say yes to the dress!": "答应这条裙子吧！",
 "How about no, it's half. This ain't a negotiation, twinkle toes.": "不行，就一半。这没得谈，小跳蚤。",
 "I will eat his hair!": "我要吃他的头发！",
 "[scream]": "[scream]",
 "[urgent]Hey, did you get it? Where is it?": "[urgent]嘿，拿到了吗？在哪儿？",
 "[whining]": "[whining]",
 "Oh, there it is. Come on, we have to go--": "哦，就在那儿。快，我们得走——",
 "It's almost as good as having a million dollars. Almost.": "这几乎跟有一百万一样爽。几乎。",
 "But half a million dollars would warm": "但五十万会更暖",
 "I'm gonna just go ahead and assume you're still listening.": "我就当你还听着吧。",
 "You scratch my nuts I scratch yours, that kind of thing.": "你帮我挠，我帮你挠，就这种关系。",
 "Look. I admit it. You screwed me. You really did. Cool moves, Rhys. Cool moves. Hyperion will want my dick in a sling.":
    "听着。我承认。你坑了我。真坑了。好手段，瑞斯。好手段。亥博龙会想把我吊起来。",
 "So... you get your cybernetic rear up here with the money, and I'll split it with you, fifty-fifty.":
    "所以……你带着钱、用你那半机械的屁股爬回这儿，我跟你五五分。",
 "So Vaughn takes the fall... And the two of us?": "所以 沃恩 顶罪……那我们俩呢？",
 "We've got girls sniffing shnae out of our armpits.": "我们俩能让姑娘趴在我们腋下闻味道。",
 "Or whatever. I don--I don't know what you're into.": "或者随便什么。我——我不知道你好哪口。",
 "[exasperated]Yes.": "[exasperated]对。",
 "Is... is that your boss?": "那……那是你老板吗？",
 "I'm just gonna assume you're still there.": "我就当你还在这儿听着。",
 "Get off the phone, Rhys.": "挂电话，瑞斯。",
 "I know it's generous of me.": "我知道我这人很大方。",
 "But I got a feeling you're gonna wanna hear what I'm offering first.":
    "但我有个感觉，你会想先听听我的条件。",
 "Because that's a lot of money. Money I want. Money I don't have. Money you have. Money--":
    "因为那是很大一笔钱。我想要的钱。我没有的钱。你有的钱。钱——",
 "Why on Pandora would I trust you, Vasquez?": "我凭什么信你，Vasquez？",
 "Yeah, okay okay, I get it.": "行，好好好，我懂。",
 "Okay... this is officially the worst day ever.": "好吧……这正式成为史上最糟的一天。",
 "Sad Bossanova/under rubble dead and gone/my sword is righteous.": "悲伤的 Bossanova/埋在瓦砾下死去/我的剑是正义的。",
 "No more phone calls, okay? We have to--": "别再打电话了，行吗？我们得——",
 "[awestruck]Ahh, okay...": "[awestruck]啊，好吧……",
 "We have to get out of here.": "我们得离开这儿。",
 "Come on, come on...": "快，快……",
 "Feel the wrath of my ankle!": "感受我脚踝的怒火！",
 "Take it.": "拿着。",
 "Crane": "起重机",
 "Bandit": "土匪",
 "I'm open to ideas!": "我接受任何主意！",
 "Oh, that's gotta be Yvette! Yes! She can send a Loader Bot!": "哦，那一定是 Yvette！太好了！她能送来一台装载机器人！",
 "[dramatic pause] We'll just have to blame the whole thing on your buddy Vaughn.  Okay?":
    "[dramatic pause] 我们就得把这事全栽到你哥们儿 沃恩 头上。行吗？",
 "I mean, it is his ID associated with the account transfer, and uh...": "毕竟账户转账用的是他的 ID，而且呃……",
 "And he's young...ish.  He'll bounce back.": "而且他还年轻……算年轻。他会缓过来的。",
 "[Thinking]Yeah, I'll see what I can do. It's a deal then!": "[Thinking]好，我看看能做什么。那就这么定了！",
 "Okay, then how about a Loader Bot?": "那好，来台装载机器人怎么样？",
 "You messed up, Rhys.  You coulda been back home, living the good life.  Passing that up for the sake of your little friend? ...Ya have fun dying on that poop chute of of a planet where you belong.":
    "你搞砸了，瑞斯。你本可以回家过好日子。为了你那个小朋友放弃这些？……那你就在你该待的那个厕所坑一样的星球上好好死去吧。",
 "QESTION": "QESTION",
 "Sasha may not have the gun.": "萨莎 可能没拿到枪。",
 "[stilted] Hello Rhys, my coworker and person I occassionally eat lunch around. DIR: Vasquez shoves Yvette out of the way.":
    "[stilted] 你好 瑞斯，我的同事、我偶尔一起吃饭的人。DIR: Vasquez 把 Yvette 推开。",
 "I need a Loaderbot!": "我需要一台装载机器人！",
 "Why are you talking weird?": "你说话怎么这么怪？",
 "Help us!": "帮帮我们！",
 "[postpax]  [frantic] Can you send us a Loaderbot! We need one right now!":
    "[postpax]  [frantic] 能给我们送台装载机器人吗！我们现在就需要！",
 "[postpax] [dropping the weirdness] Don't listen to him Rhys!": "[postpax] [dropping the weirdness] 别听他的，瑞斯！",
 "[postpax] Get outta the way!": "[postpax] 让开！",
 "[postpax] I'm sorry, Rhys, but assisting an employee under HR review would be against section 23b of the Hyperion manual for-":
    "[postpax] 抱歉，瑞斯，但协助一名正在接受人事部审查的员工违反了 亥博龙手册第 23b 条——",
 "[postpax] Get outta the way! I see what's going on here.": "[postpax] 让开！我看明白这是怎么回事了。",
 "[postpax] [stilted] What fun activities are you doing on your vacation?":
    "[postpax] [stilted] 你假期在做什么有趣的活动？",
 "[postpax] [stilted] I am delighted to hear about your escapades.": "[postpax] [stilted] 听到你的经历我很高兴。",
 "[postpax] [stilted] How are you this day?": "[postpax] [stilted] 你今天好吗？",
 "[postpax] [stilted] But I suppose that can wait until you return. I  will speak to you la-":
    "[postpax] [stilted] 不过我想那可以等你回来再说。我回头再跟你——",
 "[postpax] [frantic] We need help down here Yvette! Like right now!":
    "[postpax] [frantic] 我们在下面需要帮忙，Yvette！现在就要！",
 "[postpax] [stilted] I do not know what you mean Rhys. Why would I be talking to you in a weird tone if everything is alrigh-":
    "[postpax] [stilted] 我不明白你的意思，瑞斯。要是一切正常，我干嘛要用怪腔调跟你说话——",
 "[postpax] [frantic] Why- Why are you talking weird?": "[postpax] [frantic] 你——你说话怎么这么怪？",
 "[postpax] Alright, enough of the charade.": "[postpax] 好了，别演戏了。",
 "[Give her the gun]": "[Give her the gun]",
 "[Keep the gun]": "[Keep the gun]",
 "[alt] I'm gonna drum you upside the head, shred you to bits, and de-base your corpse.":
    "[alt] 我要敲烂你的脑袋、把你撕成碎片，再糟践你的尸体。",
 "[alt] Yeah, he's too cool for you Rhys... just... let it go.":
    "[alt] 是啊，他看不上你 瑞斯……就……算了吧。",
 "[double alt] Ouch. That's awkward.": "[double alt] 哎哟。这下尴尬了。",
 "[half whisper] Really don't know what to do with your hand now, do ya?":
    "[half whisper] 现在真不知道该拿你的手怎么办了吧？",
 "[triple alt] You're waving to someone, right? To someone that likes you?":
    "[triple alt] 你是在跟人挥手吧？跟一个喜欢你的人？",
 "[ALT Disgusted] What are you talking about?": "[ALT Disgusted] 你在说什么？",
 "[pickup][PANIC!] The case... He swallowed the case!": "[pickup][PANIC!] 箱子……他把箱子吞了！",
 "He ate the money!": "他把钱吃了！",
})

T["[processed: megaphone] Whoever is the last mongrel still screaming end of the race will get to take home the one, the only...[dramatic pause] ...The Hyperion Mystery Case of Wonder!"] = "[processed: megaphone] 谁在比赛结束时还能嚎出声、成为最后的杂种，就能把独一无二的……[dramatic pause] ……HYPERION 奇妙神秘箱带回家！"
T["[processed: megaphone] Whoever is the last mongrel still screaming at the end of the race will get to take home the one, the only..."] = "[processed: megaphone] 谁在比赛结束时还能嚎出声、成为最后的杂种，就能把独一无二的……"
T["[processed: megaphone] But before we lift those gates -- a reminder..."] = "[processed: megaphone] 但在我们升起闸门之前——提醒一句……"
T["Look, whatever happens... just focus on me."] = "听着，不管发生什么……专心看着我。"
T["[processed: megaphone; spoken as an aside] Also known as That Big Chariot Race Thing Where Everyone Dies!"] = "[processed: megaphone; spoken as an aside] 又名「那场人人都死的大战车赛」！"
T["[processed: megaphone] And now -- maniacs, degenerates and scumdogs  -- it's time for what you've been waiting for:  the first motorized killtacular event of Murder Rally twelve-thousand! [beat, then as an aside] Also known as That Big Chariot Race Thing Where Everyone Dies!"] = "[processed: megaphone] 现在——疯子们、败类们、渣滓们——你们期待的时刻到了：谋杀拉力赛一万二千届的首场机动杀戮盛宴！[beat, then as an aside] 又名「那场人人都死的大战车赛」！"
T["[processed: megaphone] Actually, uh, the last freak standing still gets the mystery box, but whoever kills that guy gets twenty g's cold hard cash."] = "[processed: megaphone] 其实，呃，最后一个还站着的怪胎能拿到神秘箱，但谁能干掉那家伙，就能拿到两万块现钞。"
T["BANDIT 4"] = "BANDIT 4"
T["[processed: a very small voice in the crowd] I'm outta here."] = "[processed: a very small voice in the crowd] 我走了。"
T["[annoyed] Zer0."] = "[annoyed] Zer0。"
T["Ahhhhhh!"] = "啊啊啊啊！"
T["[processed: megaphone] And GO, you scumsuckers -- GO!"] = "[processed: megaphone] 出发，你们这帮舔渣的——跑！"
T["Drivers drive! Drivers drive!"] = "司机就该开车！司机就该开车！"
T["[processed: megaphone] Now-- On your marks!"] = "[processed: megaphone] 现在——各就各位！"
T["I'm gonna drum you upside the head, shred ya to bits, and de-base your corpse [beat] you plastic ninja freak."] = "我要敲烂你的脑袋、把你撕成碎片，再糟践你的尸体[beat] 你这塑料忍者怪胎。"
T["[thankful] Felix!"] = "[thankful] Felix！"
T["ECHOCOMM"] = "ECHOCOMM"
T["VASQUEZ"] = "VASQUEZ"
T["[processed: phone]Or throw him out an airlock."] = "[processed: phone]或者把他扔出气闸。"
T["PSYCHO 2"] = "PSYCHO 2"
T["YVETTE"] = "YVETTE"
