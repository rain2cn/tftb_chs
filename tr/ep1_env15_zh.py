# 批次3-4：第1章 env_15_arenaexterior_rhys（潜入竞技场外围 + ECHO 扫描资料）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
T.update(_load('ep1_env18b_zh.py', '_p18b'))
T.update(_load('ep1_env19_zh.py', '_p19'))
T.update({
 # —— 潜入前的争论 ——
 "Maybe I can boost the signal to get a narrower range so we don't have to traipse around a giant building.":
    "也许我能增强信号、缩小范围，这样就不用绕着这么大的建筑到处跑了。",
 "{body-A}{worryA}There's the case.": "{body-A}{worryA}箱子在那儿。",
 "Some kind of facility.": "某种设施。",
 "What is this...": "这是什么……",
 "[a little nervous] Or, uh, you could just look up.": "[a little nervous] 或者，呃，你抬头看看就行。",
 "The system's working. The money has to be around... or *in* there, I guess.":
    "系统能用了。钱应该就在附近……或者，大概就在*里面*。",
 "Chug! Chug! Chug! Chug! Chug!": "干了！干了！干了！干了！干了！",
 "YeahhhhhhhhhhhhHH!": "耶——！",
 "Yeaahaahhhhh!": "呀哈哈——！",
 "Weeehaaaaaa!": "威哈——！",
 "My kind of scene!": "这才对我的胃口！",
 "What an idiot.": "真是白痴。",
 "What the Hell is going on?": "这他妈怎么回事？",
 "[nervously laughing] Uh.... looks like fun. Right? I mean, this whole thing's... kind of adorable?":
    "[nervously laughing] 呃……看着挺好玩。对吧？我是说，这一整套……还挺可爱的？",
 "[serious] Or a bunch of rabid dogs you want to put down.": "[serious] 或者说一群你想全宰了的疯狗。",
 "Yeah, and shaking it like that really exposes the flavor to overcarbonation.":
    "是啊，这么摇只会让它过度碳酸化、把风味毁掉。",
 "Ugh, I can't *stand* this friggin' guy.": "呃，我*受不了*这家伙。",
 "He's somethin', ain't he.": "他挺有种的，是吧。",
 "Just what in the living Hell is going on?": "到底他妈出什么事了？",
 "But at a-- at a foundry?": "但在一座——铸造厂里？",
 "Looks like a, uh... I don't know what this is.": "看着像个，呃……我也不知道这是什么。",
 "I have no idea.": "我完全不知道。",
 "What is this place? A farm or something?": "这是什么地方？农场之类的？",
 "[tired] Okayyy, soooo....": "[tired] 好吧，那么……",
 "Guys, this will only be a big deal if you *make* it a big deal by freaking out.":
    "各位，只要你们别吓自己，这就不是什么大不了的事。",
 "You don't have to *make* a million psychos in one confined space a big friggin' deal.":
    "你没必要*非得*把一百万疯子挤在一个封锁空间里当成天大的事。",
 "Alright, look, let's not get all \"Hell's Bells, what are we gonna do!\" just yet.":
    "行了，听着，先别急着喊「完了完了，我们怎么办」。",
 "A party? That looked like the schizoid olympics. There were a thousand of those freaks.":
    "派对？那看着像精神病奥运会。那种疯子有一千个。",
 "[trying to talk herself into it] It's just a uhhh... it's a party, it's fine.":
    "[trying to talk herself into it] 就是个，呃……就是个派对，没事的。",
 "And I don't even know how we'll get to him!": "我连要怎么靠近他都不知道！",
 "If he tries to open it before we get to him...": "要是他在我们赶到之前就打开它……",
 "Bossanova has the case.": "Bossanova 拿着箱子。",
 "Alright, listen up! Everybody's just gonna have to suck it up from here.":
    "好了，都听我说！从现在起，大家都得硬着头皮上。",
 "Sasha and I have done *alot* hairier crap than sneaking into.. whatever the Hell this is...":
    "我和 萨莎 干过的*险*事可比溜进……不管这是什么鬼地方……多得多。",
 "How much hairier?": "险多少？",
 "Looney tune prom.": "疯狂的毕业舞会。",
 "Looney tune prom is the only way to get it back, okay? So start pullin' your weight.":
    "疯狂毕业舞会是唯一能把钱拿回来的办法，行吗？那就开始出力吧。",
 "You wanna quit? Wanna leave?": "你想退出？想走？",
 "[to Vaughn] C'mon, it's okay.[to Fiona] We're in, of course we're in.":
    "[to Vaughn] 别这样，没事的。[to Fiona] 我们加入，当然加入。",
 "I wanna... do they-- I mean, do they have to be mutually exclusive?":
    "我想……他们——我是说，这两件事非得二选一吗？",
 "Look, you stick with us, we sneak in there and you get your cut... or you walk out that door, *those* are your options.":
    "听着，跟着我们，我们一起溜进去，你拿你那份……或者你走出那扇门，*就这两个选项*。",
 "We need that money.": "我们需要那笔钱。",
 "Which sun?": "哪颗太阳？",
 "I thought guys from Hyperion were supposed to be the biggest badasses this side of the sun.":
    "我以为 亥博龙来的人该是这颗太阳这边最狠的角色。",
 "[sigh] We can do this, okay? Just... the more of them there are, the easier it will be for us to sneak in.":
    "[sigh] 我们能做到，行吗？只是……他们人越多，我们越好混进去。",
 "Yeah. Jungle law.": "对。丛林法则。",
 "[pshhh] Don't worry about us.": "[pshhh] 别操心我们。",
 "[sarcastic] Well, let's be fair, it was more like three hundred.":
    "[sarcastic] 公平点说，大概也就三百个。",
 "The situation really does the heavy lifting on its own.": "这局面自己就够吓人了，用不着我们添彩。",
 "Look, ya dweebs, the more of them there are, the easier it will be to blend right in.":
    "听着，你们这些呆子，他们人越多，我们越好混进去。",
 "We need the money or we're dead anyways, so it doesn't matter.":
    "反正拿不到钱我们也是死，所以无所谓。",
 "Well, good luck, y'all. Knock three times when you're back so I know you're not a cuckoo person.":
    "那就祝你们好运。回来的时候敲三下，我好知道你们不是疯子。",
 "You can still be getaway and *come*, you know.": "你照样可以当接应，*又能一起进去*，你知道吧。",
 "Yeah, but I can't *watch* our only ride if I come now can I?":
    "是啊，可我要是现在走了，*谁来看着*我们唯一的车？",
 "But what if we need like a lookout or something?": "可要是我们需要个望风的怎么办？",
 "You have four people already.": "你们已经有四个人了。",
 "Figure it out.": "自己想办法。",
 "You should really come. You're not that old that you can't aim a gun and we'll need the help.":
    "你真该一起来。你还没老到举不动枪，而我们需要帮忙。",
 "I *am* helpin'.": "我*就是*在帮忙。",
 "Whatever, if we need someone with a colostomy bag we'll give him a ring.":
    "随便吧，要是我们需要个带造口袋的人，会给他打电话的。",
 "I don't know if it's safe for you out here... by yourself... since you're so old.":
    "我不知道你一个人在外面安不安全……毕竟你年纪那么大了。",
 "Don't worry about me, girl. This thing's a tank.": "别担心我，丫头。这玩意儿是辆坦克。",
 "Yeah, good idea. We'll be comin' out hot, so, just keep the engine runnin'.":
    "对，好主意。我们出来时会很急，所以让引擎一直转着。",
 "I was gonna anyway for the radio, but... sure.": "反正我要听收音机，不过……行。",
 "Alright. Let's get that case, I guess.": "好吧。那就去拿箱子。",
 "I guess we need the money or we're dead anyways, so it really doesn't matter.":
    "反正没钱我们也是死，那就真无所谓了。",
 "That's the spirit!": "这才对嘛！",
 "Alright. Well...[gets cut off]": "好吧。那……[gets cut off]",
 "Oh my God, let's just do this!": "天啊，直接干吧！",
 "I guess this... this is the best way.": "我想这……这是最好的办法。",
 "*This* is the best way? It's a *sewer*, who knows where this thing leads.":
    "*这*是最好的办法？这是*下水道*，鬼知道它通到哪儿。",
 "[flat] I'm a witch.": "[flat] 我是女巫。",
 "How do you know that.": "你怎么知道的。",
 "It's not a sewer, it's like a maintenance shaft or something.": "这不是下水道，像是检修井之类的东西。",
 "For getting in.": "为了进去。",
 "This is probably good enough.": "这个大概够用了。",
 "Good enough? For what?": "够用？用来干什么？",
 "Go to Hell.": "去死吧。",
 "Shut up and just help me.": "闭嘴，来帮我。",
 "No, I got it!": "不用，我行！",
 "I need some help.": "我需要帮忙。",
 "I'm a witch.[beat] And it says right there. \"Maintenance.\"": "我是女巫。[beat] 上面就写着呢。「检修」。",
 "It's *not* a sewer.": "这*不是*下水道。",
 "[mocking] Need some help over there?": "[mocking] 那边需要帮忙吗？",
 "Good thing I worked on my *legs* this morning.": "幸好我今早练过*腿*。",
 "That pickle jar a little *stuck* for you?": "那罐泡菜*拧不开*了？",
 "[hugely obvious fake laughter]": "[hugely obvious fake laughter]",
 "How do you know?": "你怎么知道？",
 "{AngryA}[trying to lift something heavy and failing]": "{AngryA}[trying to lift something heavy and failing]",
 "No, I need somebody a little stronger. Sasha... call Mom.": "不，我需要个更有力气的。萨莎……叫妈来。",
 "Hardy har-har, let's just get this thing open.": "哈、哈、哈，把这家伙弄开吧。",
 "Shut up and just help me before a psycho finds us and I have to *feed* you to him.":
    "闭嘴来帮我，否则等疯子找上我们，我就*把你喂*给他。",
 "No, no, I got it, tough guy, just sit back and watch.": "不不用，我行，硬汉，你就坐着看吧。",
 "Let's just get this thing open.": "把这东西弄开吧。",
 "Ya finished?": "弄完了？",
 "{SmugA}It's like the circus when the twins pull on each other.": "{SmugA}就像马戏团里连体双胞胎互相拉扯。",
 "{AngryA}[heavy lifting]": "{AngryA}[heavy lifting]",
 "{AngryB}[heavy lifting]": "{AngryB}[heavy lifting]",
 "{SmugB}But less graceful.": "{SmugB}只不过没人家优雅。",
 "{AngryC}[lifting something heavy] {RageA}Are you... even... pulling...?":
    "{AngryC}[lifting something heavy] {RageA}你到底……有没有……在拉……？",
 "[lifting something heavy] {RageA}The weight's... {RageB}all... on... my{RageA}... side...!":
    "[lifting something heavy] {RageA}重量……全……压在……我{RageA}……这边……！",
 "Shut uppa ya mouth when you're talkin' to me!": "跟我说话的时候把嘴闭上！",
 "[like an insult] Smoke you!": "[like an insult] 抽死你！",
 "[sincere] Teamwork!": "[sincere] 团队合作！",
 "[flat] Yay.": "[flat] 耶。",
 "Did you ever get that feeling... it's ilke deja vu... but not?": "你有过那种感觉吗……像是既视感……但又不是？",
 "Trust me, I won't.": "放心，我不会。",
 "My underwear's stupid, so don't look up.": "我的内裤很蠢，别往上看。",
 "[confused] Yeahhhh......": "[confused] 是——吧……",
 "Alright.": "好吧。",
 "Are you touching me right now?": "你是在碰我吗？",
 "[sigh] No, you're touching me.": "[sigh] 不，是你在碰我。",
 "Hey!": "嘿！",
 "Guys!": "各位！",
 "Uh? Guys! Joke's over.": "呃？各位！玩笑到此为止。",
 "Ladies first.": "女士优先。",
 "Thank you, I will.": "谢谢，我会的。",
 "You're scared, is that it?": "你怕了，是不是？",
 "Don't mind if I do.": "那我就不客气了。",
 "Fine.": "行吧。",
 "I mean, why *not* ruin a five hundred dollar tie by rubbing it on rat droppings!":
    "我是说，为什么不把五百块的领带蹭在老鼠屎上*毁掉*呢！",
 "Don't mind if I do!": "那我就不客气了！",
 "My thoughts exactly.": "我也这么想。",
 "Being scared of the dark is nothin' to be ashamed of, Fiona.": "怕黑不丢人，Fiona。",
 "[flat] No, it's not.": "[flat] 是不丢人。",
 "Hurry up, guys.": "快点，各位。",
 "Age before beauty.": "长者先请。",
 "It's dark, alright?": "里面很黑，行吗？",
 "It'd help me a bunch if you stopped stepping on my hands.": "你要是不再踩我的手，我会感激不尽。",
 "What is *up* with you, today?": "你今天*怎么回事*？",
 "[sarcastic] Yeah, they're like a litter of puppies you wanna take care of.":
    "[sarcastic] 是啊，他们就像一窝你想照顾的小狗。",
 "Me help!": "我来帮！",
 "Eww.": "噫。",
 "Of all the people to *never* get eaten by crab worms...": "这么多人里，偏偏*就你*没被沙蚕吃掉……",
 "[trying to open something but it's stuck sounds": "[trying to open something but it's stuck sounds",
 "Fine. Go and have fun explaining to your bosses just how a million of their dollars got *misplaced*.":
    "行。去跟你的老板们好好解释那一百万是怎么*弄丢*的吧。",
 "Theoretically.": "理论上。",
 "We need that briefcase, and sneaking into... whatever the Hell this is...":
    "我们需要那个箱子，而溜进……不管这是什么鬼地方……",
 "[whisper] Let's go around.": "[whisper] 我们绕过去。",
 "[whisper] Crap.": "[whisper] 糟了。",
 "Whatever, we won't be here long.": "随便吧，我们不会待太久。",
 "Well, we're boned.": "好吧，我们完了。",
 "{SmugA}Yeah, the giant imposing walls and the guards everywhere really do give this place a {AngryA}'no shooting your way in' sort of vibe.":
    "{SmugA}是啊，高耸的围墙和满地的守卫，确实让这地方透着股{AngryA}「别想硬闯」的气息。",
 "{HappyA}There's a hatch over there.  Every other entrance is guarded, {SlyC}but not that one.":
    "{HappyA}那边有个舱口。其他所有入口都有守卫，{SlyC}就那个没有。",
 "{AngryA}That's something at least.": "{AngryA}那至少算个办法。",
 "{SternA}It is electronically locked -- [gets cut off] {happyA}but I...":
    "{SternA}它装了电子锁——[gets cut off] {happyA}不过我能……",
 "{AngryA}So you've got something useless.": "{AngryA}所以你就是有个没用的办法。",
 "{AngryA}No -- *I* {HappyB}can hack through it.": "{AngryA}不——*我*{HappyB}能黑进去。",
 "{SternA}I see a way in. It's that hatch right down there.": "{SternA}我看到一条进路。就是下面那个舱口。",
 "Huh, where?": "嗯？哪儿？",
 "Right there!": "就在那儿！",
 "{angryA}This is ridiculous. I don't see any hatch or whatever.": "{angryA}胡说。我根本没看到什么舱口。",
 "{SmugA}Of course *you* don't.": "{SmugA}你当然看不到。",
 "You all give up at the wrong moments.": "你们总在该放下的时候不放下。",
 "We give up at the exact right moments. When it's impossible.": "我们放下得恰是时候。就是在不可能的时候。",
 "Ha. I know how we can get in.": "哈。我知道怎么进去了。",
 "{SmugA}We could always... uh...": "{SmugA}我们随时可以……呃……",
 "{HappyA}Give up?": "{HappyA}放弃？",
 "{worryA}Hang on. [beat] {HappyA}I think Rhys spies something with his Echo eye.":
    "{worryA}等等。[beat] {HappyA}我想 瑞斯 用他的 Echo 眼发现什么了。",
 "{AngryA}Quit screwing around. {sternA} You want that money? Then let's go.":
    "{AngryA}别瞎折腾了。{sternA} 你想要那笔钱吗？那就走。",
 "{AngryA}Who even let you wake up?": "{AngryA}谁让你醒过来的？",
 "{ShockA}Hey! Without us you'd {AngryA}never have tracked the case.":
    "{ShockA}嘿！没有我们，你{AngryA}根本找不到那箱子。",
 "{AngryA}Because what I've learned over all my years is that, more so than bandits or psychos, it's always been people like *you* steppin' on people like *me*.":
    "{AngryA}因为这些年我学到的就是：比土匪和疯子更狠的，永远是*你们*这种人踩着*我*这种人。",
 "{AngryB}I don't trust you two.  I don't like you two.": "{AngryB}我不信你们俩。也不喜欢你们俩。",
 "I sure as hell don't want to work with you.": "我更不想跟你们合作。",
 "{AngryA}And we sure as sure as hell aren't following your lead *anywhere.*":
    "{AngryA}我们也绝不会跟着你走*任何地方*。",
 "Let me finish. [beat]Anymore.": "让我把话说完。[beat]我是说，再也不会了。",
 "I'm not Hyperion.": "我不是 亥博龙的人。",
 "Coulda fooled us. What, with your whole get up.": "真看不出来。就你这身打扮？",
 "I burned my bridges. TNTed them, actually.": "我把后路烧了。准确说，是用 TNT 炸了。",
 "So, follow us or not. But don't base your choice on some symbol on our clothing.":
    "所以，跟不跟都行。但别拿我们衣服上的标志当理由。",
 "{ShockA}You hate Hyperion?{sternA} Great. I don't care.": "{ShockA}你恨 亥博龙？{sternA} 很好。我不在乎。",
 "{HappyA}I want that money. You want that money.": "{HappyA}我想要那笔钱。你也想要那笔钱。",
 "{SmugA}I can help us get that money!": "{SmugA}我能帮我们拿到那笔钱！",
 "Stole that money out from underneath the nose of my dick of a boss.":
    "那笔钱是我在我那个混蛋老板眼皮底下偷出来的。",
 "Rhys...": "瑞斯……",
 "{AngryA}Do you hear me throwing out judgments at any of you right now? {SternA} And trust me -- I could.":
    "{AngryA}你听见我现在对你们谁下过判断吗？{SternA} 相信我——我完全可以。",
 "And trust me -- I could.": "相信我——我完全可以。",
 "{SmugA}Just examine your own glass house before you start throwing rocks around.":
    "{SmugA}扔石头之前，先看看自己是不是玻璃房子。",
 "Whoa. What does that have to do with anything?": "哇。这跟这事有什么关系？",
 "{ShockA}What is wrong with you people? {SadA}This isn't about who screwed who anymore.":
    "{ShockA}你们这些人到底怎么回事？{SadA}现在不是追究谁坑了谁的时候。",
 "{AngryA}This is about the growing list of people who will *kill us* if we don't get that money.":
    "{AngryA}而是有一串越来越长的人，会在我们拿不到钱时*杀了我们*。",
 "[proud surprise] That wasn't bad, Vaughn.": "[proud surprise] 说得不错，沃恩。",
 "Can we have a moment, to discuss this? Alone?": "能给我们点时间商量一下吗？单独聊。",
 "What's to discuss?": "有什么好商量的？",
 "I just don't trust them...": "我就是不信他们……",
 "We need that money. Vallory...": "我们需要那笔钱。瓦洛里……",
 "Them! and not... are you really thinking of following them?": "他们！而不是……你真打算跟着他们走？",
 "I'm going.": "我走了。",
 "But uh... we...": "可是呃……我们……",
 "At least I have a plan. It's a plan, the quality of which, hard to tell. But, if you want even a chance at a million dollars, follow me!":
    "至少我有个计划。这计划的好坏嘛，难说。但你要想有那么一丁点机会拿到一百万，就跟我来！",
 "What? Are you all allergic to money or something?": "怎么？你们都对钱过敏吗？",
 "Allergic to the wealth of a million dollars?": "对一百万美元过敏？",
 "You don't trust me. But you should.": "你们不信我。但你们该信。",
 "So, I'm going for it.": "所以，我去试试。",
 "At least for now we have the same goal. Here, in this moment, trust me to do what's best for all of us, because it's also best for me, to get that money.":
    "至少现在我们的目标一样。就眼下这一刻，信我去做对我们大家都最好的事——因为拿到那笔钱对我也是最好的。",
 "I'm not hearing you come up with any ideas.": "我可没听你拿出什么主意。",
 "This is a mistake.": "这是个错误。",
 "[playful, to Felix]{HappyA}If we die, avenge our deaths.": "[playful, to Felix]{HappyA}我们要是死了，记得给我们报仇。",
 "{SadA}Fine. {HappyA}Then I'm in, too.": "{SadA}好吧。{HappyA}那我也加入。",
 "{SmugA}I made a deal with them, and I don't see any better way to get in there and get that money.":
    "{SmugA}我跟他们说好了，而且我也看不出有更好的办法进去拿钱。",
 "{AngryA}You all enjoy being lead to your deaths by this Hyperion boot licker. I'm staying with the trailer.":
    "{AngryA}你们就好好享受被这个 亥博龙舔靴子的家伙带去送死吧。我留在车上。",
 "{AngryA}You come back as ghosts and avenge your own damn deaths.":
    "{AngryA}你们变成鬼回来自己报仇吧。",
 "With like, magnets or something...": "用磁铁之类的……",
 "{body-A}{HappyA}Okay, Rhys, do your thing.": "{body-A}{HappyA}好，瑞斯，看你的了。",
 "{body-A}{SadA}Yup. It's locked all right.": "{body-A}{SadA}嗯。确实锁着。",
 "{SmugA}Just watch this.": "{SmugA}看好了。",
 "Looks like you got it.": "看来你搞定了。",
 "{SadA}Give me a robot hand here, Rhys.": "{SadA}搭把手，瑞斯。",
 "{HappyC}Yes! {smugA}We're in the money.": "{HappyC}成了！{smugA}这下有钱了。",
 "Well, this entrance won't work.": "这个入口行不通。",
 "It's like this place is made of ways not to get in.": "这地方简直就是用「进不去的方法」搭起来的。",
 "Looks like a way in... and no guards. Perfect...": "看着像条进路……而且没守卫。完美……",
 "And what is that? Some kind of hatch.": "那是什么？某种舱口。",
 "{body-A}{SadA}This isn't one of those shanty town bandit camps with the easy to infiltrate tents,{AngryA} Sasha. You can't just shoot your way in.":
    "{body-A}{SadA}这可不是那种帐篷随便钻的土匪棚户营，{AngryA} 萨莎。你没法一路开枪打进去。",
 "I'm going to get that money right now. Anyone who wants to join me is free to.":
    "我现在就去拿那笔钱。谁想跟来都行。",
 "That makes sense.": "有道理。",
 "Ugh... yeah. Vallory. And I punched August. Great. [sigh]": "呃……是啊。瓦洛里。我还揍了 August。好极了。[sigh]",
 "They'll find some way to screw us.": "他们总会找到办法坑我们。",
 "{body-A}{worryA}I thought they'd use a rock to try to open it.": "{body-A}{worryA}我以为他们会拿石头来砸开它。",
 "Magic box has fairy dust!": "魔法盒里有仙尘！",
 "King of boomboom!  He will hurt you!": "轰隆之王！他会伤害你！",
 "{body-A}{HappyA}Alright. [beat] {SternA}I think I've got something.":
    "{body-A}{HappyA}好。[beat] {SternA}我想我有办法了。",
 "{fearA}Got something meaning \"I've found a solution to the{SlyC} swarm of psychos having our money problem\"?":
    "{fearA}「有办法」是指{SlyC}「我找到了从疯子群里夺回我们的钱的办法」？",
 "{fearA}Or are you coming down with some weird Pandoran disease?": "{fearA}还是你染上了什么 潘多拉 怪病？",
 "{angryA}Can you see me now?": "{angryA}现在能看见我了吗？",
 "{happyA}Just follow my lead and do what I say so we can cross this open area without being seen by all the guards.":
    "{happyA}跟着我，照我说的做，这样我们就能不被守卫发现地穿过这片空地。",
 "{AngryA}Just put our lives in the hands of our new Hyperion overlord. [beat] No, thanks.":
    "{AngryA}把命交给我们这位新的 亥博龙主子？[beat] 不了，谢谢。",
 "{AngryA}But if we're going to make it to that money alive enough to spend it, we have to work together.":
    "{AngryA}但要想活着拿到那笔钱并花掉它，我们就得合作。",
 "{SternA}I found us a way in -- that hatch down there.": "{SternA}我找到进路了——下面那个舱口。",
 "{SmugA}One big happy servant family for our Hyperion overlord.":
    "{SmugA}给咱们的 亥博龙主子当一家子快乐的仆人是吧。",
 "Of course you can, you're a soulless Hyperion cyborg.": "你当然能，你是个没心没肺的 亥博龙半机械人。",
 "{happyA}Echo eye implant. I see everything.": "{happyA}Echo 眼球植入体。我什么都看得见。",
 "{sternA}There are guard patrols, but we can definitely get in through that hatch down there if {HappyA}we time it right. [beat] So come on.":
    "{sternA}有守卫巡逻，但只要我们{HappyA}时机抓准，绝对能从下面那个舱口进去。[beat] 所以，走吧。",
 "{SmugA}Fine, you don't want to work with me? Don't.": "{SmugA}行，你不想跟我合作？那就别合作。",
 "{AngryA}But don't expect a single dollar of that money if you don't come along and pull your weight.":
    "{AngryA}但你要是不来出力，就别想拿到那笔钱的一分钱。",
 "{AngryB}Atlas. Hyperion. Torgue. Whatever, you're all the same.":
    "{AngryB}Atlas。亥博龙。Torgue。随便吧，你们都一样。",
 "Look --": "听着——",
 "{AngryA}Anyway -- I'm going to get that money now. You're all free to do as you like.":
    "{AngryA}总之——我现在去拿那笔钱。你们随意。",
 "[processsed: megaphone] Alright scumdogs, we're home, so It's showtime!":
    "[processsed: megaphone] 好了渣滓们，我们到家了，开演！",
 "Open says me.": "芝麻开门。",
 "{WorryA}Oh. You two are still alive. [beat, sarcastic] {sternA}Fantastic.":
    "{WorryA}哦。你们俩还活着。[beat, sarcastic] {sternA}好极了。",
 "{body-A}{AngryA}We're gonna need more bullets.": "{body-A}{AngryA}我们得再多搞点子弹。",
 "{SmugA}It is fantastic, since *I* can probably find us a way in there.":
    "{SmugA}确实好极了，因为*我*大概能给我们找到进路。",
 "{WorryA}Follow *your* lead?": "{WorryA}跟着*你*走？",
 "{SternA}I'm going.": "{SternA}我走了。",
 "{ShockA}But -- [gets cut off] they're...": "{ShockA}可是——[gets cut off] 他们……",
 "Electronic Access Hatch": "电子通行舱口",
 "Panel": "面板",
 "Side Door": "侧门",
 "I can get us in there.": "我能带我们进去。",
 "Just follow my lead.": "跟着我。",
 "We have to work together.": "我们必须合作。",
 "Fine, stay here.": "行，你留下。",
 "Focus on the money.": "专心在那笔钱上。",
 "Don't judge me.": "别评判我。",
 "{InquireA}We've got a way in, but how are we gonna get down there?  {InquireB} Have you forgotten about the bandit parade going by?":
    "{InquireA}进路是有了，可我们要怎么下去？{InquireB} 你忘了旁边还有土匪在游行？",
 "{SmugC} Oh, that's the easy part.": "{SmugC} 哦，那部分简单。",
 "First, we jump down, taking cover behind that rock...": "首先，我们跳下去，躲在石头后面……",
 "Then, Roll under the truck as it passes by": "然后，趁卡车开过时滚到车底",
 "Swipe gun from one of the guards...": "从某个守卫身上顺走枪……",
 "Get the drop on the last guard...": "偷袭最后一个守卫……",
 "Lift up the Hatch cover...": "掀开舱口盖……",
 "Break his neck...": "扭断他的脖子……",
 "Swipe the manhole keys from one of the guards...": "从某个守卫身上顺走井盖钥匙……",
 "{SmugB}...and we are good to go! Everyone got that?": "{SmugB}……然后就能走了！都记住了吗？",
 "[to himself, embarased] {SternA}Damnit.": "[to himself, embarased] {SternA}该死。",
 "[confused]{ThinkA} Guys?": "[confused]{ThinkA} 各位？",
 "{ThinkA}My way would have worked...": "{ThinkA}我那办法本来能成的……",
 "[smug]{SmugA}We found another way down.": "[smug]{SmugA}我们找到别的下去的路了。",
 "After you.": "你先。",
 "[thinking aloud]{ThinkA}No, wait, wait... no... no, that won't work.":
    "[thinking aloud]{ThinkA}不，等等，等等……不……不，那不行。",
 "[nobody's home] {NeutralB} Vaughn? {ThinkA}Where'd everybody go?":
    "[nobody's home] {NeutralB} 沃恩？{ThinkA}人都去哪儿了？",
 "[waking up after being knocked unconscious] {AngryA}Aggghhh...":
    "[waking up after being knocked unconscious] {AngryA}啊啊啊……",
 "[medium-level pain & surprise] {AngryB}OW!": "[medium-level pain & surprise] {AngryB}嗷！",
 "Looks like I found the money. [pointedly] You're welcome.": "看来我找到钱了。[pointedly] 不客气。",
 "{SlyA} Uhh... What happened?": "{SlyA} 呃……发生什么了？",
 "{SmugA}We got tired of looking and learning, so we decided to wander around the desert.":
    "{SmugA}我们看腻了学腻了，就决定去沙漠里逛逛。",
 "Turns out it's really boring.": "结果发现那真的很无聊。",
 "{SmugA} We decided to let you nap while your friend found the money.":
    "{SmugA} 我们决定让你小睡一会儿，你朋友 meanwhile 把钱找到了。",
 "{SmugA}We were still waiting to get a load of that.": "{SmugA}我们还在等你那招呢。",
 "{SmugA}Watching you take a nap just totally blew our minds.": "{SmugA}看你睡觉真是让我们大开眼——界。",
 "[quietly] {WorryA} You okay, Rhys?": "[quietly] {WorryA} 你没事吧，瑞斯？",
 "{AngryA} Quiet. This place is crawling with bandits.": "{AngryA} 小声点。这地方到处都是土匪。",
 "I'm fine.": "我没事。",
 "Thanks for abandoning me.": "谢谢你把我丢下。",
 "Told you I'd find the money.": "我说过我会找到钱。",
 "[quietly] {WorryA}What happened back there?": "[quietly] {WorryA}刚才那边发生了什么？",
 "[quietly] {SternA} No idea, just blacked out.": "[quietly] {SternA} 不知道，就昏过去了。",
 "[quietly] {NeutralB} Yeah. Yeah, I'm fine now.": "[quietly] {NeutralB} 嗯。嗯，我现在没事了。",
 "[quietly] {HappyA} All your... cybernetics still seem to be working, {NeutralA}as far as I can tell.":
    "[quietly] {HappyA} 你那些……机械部件好像都还能用，{NeutralA}至少我看是这样。",
 "[quietly] [excited] {HappyA} Dude, that cable stuck in your head led us straight to the money! {SlyA} We might actually get out of this alive.":
    "[quietly] [excited] {HappyA} 老兄，插在你脑袋上的那根线直接把我们引到钱上了！{SlyA} 我们说不定真能活着出去。",
 "[quietly] {AngryA} Apart from waking up completely alone in a crappy trailer with a cable stuck into my head? {SmugA} I'm great. {SternA}Thanks for the concern.":
    "[quietly] {AngryA} 除了在一个破房车里孤零零醒来、脑袋上插着根线之外？{SmugA} 我好得很。{SternA}谢谢关心。",
 "[quietly] {SternA} Assuming they don't get us killed, of course.": "[quietly] {SternA} 当然，前提是他们别把我们害死。",
 "[quietly] *And* wipe up your drool.": "[quietly] *顺便*把你的口水擦干净。",
 "[quietly] {ShockA} I don't remember you telling me that.": "[quietly] {ShockA} 我不记得你告诉过我。",
 "[quietly] {NeutralB}And I was the one who had to figure out that rust bucket's navigation systems. {SternA}You know, some of that stuff is even older than Atlas tech.":
    "[quietly] {NeutralB}而且那台破车的导航系统是我搞明白的。{SternA}你知道吗，有些东西比 Atlas 的科技还老。",
 "[quietly] {SmugB} See, I told you I'd find the money.": "[quietly] {SmugB} 看吧，我说过我会找到钱。",
 "{NeutralA} We can do a diagnostic on your... {SternA} stuff when we get back to Helios.":
    "{NeutralA} 等我们回 赫利俄斯，可以给你那些……{SternA}部件做个体检。",
 "[getting his attention] {WorryA} Rhys?  Rhys?": "[getting his attention] {WorryA} 瑞斯？瑞斯？",
 "{SternB} I just need you to keep it together until we can get our money back, okay?":
    "{SternB} 我只要你撑到我们把钱拿回来，行吗？",
 "{SternA} And the only reason you're still here is because you're going to lead us to it.":
    "{SternA} 你还能留在这儿，唯一的原因就是你要带我们找到它。",
 "{AngryA} Somewhere.": "{AngryA} 某个地方。",
 "{NeutralB} So the case is in there?": "{NeutralB} 所以箱子就在里面？",
 "It's nice to feel needed.": "被人需要的感觉真好。",
 "We'll talk about terms later.": "条件之后再谈。",
 "I already did my job.": "我的活儿已经干完了。",
 "{HappyA} Aww, you do need me after all.": "{HappyA} 哦，原来你还是需要我。",
 "{SmugB} And all this time I just thought you wanted to murder me.":
    "{SmugB} 我一直以为你们只是想杀了我。",
 "{SternA} And once we've found it, then we can talk about who gets what and how much.":
    "{SternA} 等找到它，我们再谈谁拿多少。",
 "{AngryA}Hey, I showed you where the money was, and you drove us here. {SternA}As far as I'm concerned, we're even.":
    "{AngryA}喂，我告诉你们钱在哪儿，你们开车送我过来。{SternA}在我看来，我们两清了。",
 "{NeutralB} Save it, Rhys. There's no way we can get in there unless we stick together.":
    "{NeutralB} 省省吧，瑞斯。不合作的话我们根本进不去。",
 "{SternB} So you two can spare us having to listen to another tedious argument.":
    "{SternB} 这样你们俩也能省下我们听又一轮无聊争吵的功夫。",
 "{SternB} Look, let's just find the money first, and then we can all argue over it.":
    "{SternB} 听着，先把钱找出来，然后随你们怎么争。",
 "{ShockA} Wow, what is that place?": "{ShockA} 哇，那是什么地方？",
 "Yeah, Rhys. If that is an Atlas building, there might be something you can access with your ECHO Eye.":
    "是啊，瑞斯。如果那是 Atlas 的建筑，说不定有东西能用你的 ECHO 眼接入。",
 "{NeutralA}How about it, Mr. Roboto? {SadA}Do you see any way to get inside?":
    "{NeutralA}怎么样，机器人先生？{SadA}看到进去的办法了吗？",
 "{WorryA}Looks like some kind of abandoned Atlas warehouse.": "{WorryA}看着像废弃的 Atlas 仓库。",
 "{SlyA}Doesn't look abandoned to me.": "{SlyA}在我看可不算废弃。",
 "{SternB}Looks more like every bandit on this side of the planet has shown up.":
    "{SternB}更像是这半颗星球上的土匪全来了。",
 "[alternate dialog idle] Or, you know, we could just sit here.": "[alternate dialog idle] 或者，你知道，我们就坐这儿。",
 "{SmugA} Can't we just go in the same way the Vault Hunter did?": "{SmugA} 我们不能照秘藏猎人进去的方式进去吗？",
 "{SternB} It's that Vault Hunter.": "{SternB} 就是那个秘藏猎人。",
 "{SmugA}Settle down. I got this.": "{SmugA}别急。这个我行。",
 "There's no way we'd get through those bandits. It's impossible.": "我们不可能穿过那群土匪。不可能。",
 "Maybe not, you know, impossible. Look, down there.": "也许不是，那个，不可能。看，下面。",
 "{AngryA} Oh, perfect. As soon as a Vault Hunter finds a case with millions of dollars in it, it's as good as gone. {AngryB} You know how they are! {NeutralA} They're worse than bandits.":
    "{AngryA} 哦，太好了。只要秘藏猎人发现装了百万现金的箱子，那箱子就算没了。{AngryB} 你知道他们什么德行！{NeutralA} 他们比土匪还坏。",
 "{SchemeA} We're not Vault Hunters, Sasha.": "{SchemeA} 我们不是秘藏猎人，萨莎。",
 "That hatch goes down underneath the building.": "那个舱口通向建筑底下。",
 "That hatch doesn't have any guards around it.": "那个舱口周围没有守卫。",
 "There. Unlocked and ready for us.": "好了。解锁了，随时可用。",
 "[alt][groggy]{ThinkA}...I guess Vaughn got the tracker working...":
    "[alt][groggy]{ThinkA}……看来 沃恩 把追踪器弄好了……",
 "If this really is an old Atlas facility, I should be able to unlock the hatch from here.":
    "如果这真是旧的 Atlas 设施，我应该能从这里解开舱口。",
 "[locking an already locked door]Whoops.   Guess I didn't need to do that.":
    "[locking an already locked door]哎呀。看来我不用那么做。",
 "[to himself] [confused]...Oookay?": "[to himself] [confused]……好吧？",
 "Something wrong?": "有问题吗？",
 "No, it's... fine.": "没事，很……好。",
 "{AngryA} We're talking about getting that money back, just like you are.":
    "{AngryA} 我们也在聊怎么把那笔钱拿回来，跟你一样。",
 "[suspicous] {InquireA}What are you guys talking about?": "[suspicous] {InquireA}你们在聊什么？",
 "[like \"no big deal\"] {AngryA} Okay, so you found a way in.": "[like 「没什么大不了」] {AngryA} 好吧，你找到进路了。",
 "{ShockA}You're not coming along?": "{ShockA}你不一起去？",
 "{SternB} Now remember to get in and out of there quickly. We've already taken too many risks today.":
    "{SternB} 记住进去要快、出来也要快。今天我们冒的风险已经够多了。",
 "{NeutralA} I think taking a bullet to the shoulder earns me a night off.":
    "{NeutralA} 挨了一枪肩膀，我觉得够换一晚休息了。",
 "{NeutralA} Somebody needs to stay and protect the getaway car.":
    "{NeutralA} 总得有人留下来看着接应车。",
 "{SternB} And Fiona, Sasha, be prepared, {WorryA} and remember [beat, leans in so Rhys and Vaughn can't hear] don't trust anyone.":
    "{SternB} 还有 Fiona、萨莎，做好准备，{WorryA}记住[beat, leans in so Rhys and Vaughn can't hear] 谁都别信。",
 "And Fiona, Sasha, be prepared, {WorryA} [beat, leans in so Rhys and Vaughn can't hear] don't trust anyone.":
    "还有 Fiona、萨莎，做好准备，{WorryA} [beat, leans in so Rhys and Vaughn can't hear] 谁都别信。",
 "{NeutralB} I'll be waiting for your signal.": "{NeutralB} 我等你们的信号。",
 "Ugh, this ordeal is not helping my complexion.": "呃，这趟折腾对我的皮肤可没好处。",
 "\"Banang\"...? Looks...gross.": "「Banang」……？看着……恶心。",
 "Huh. Nothing.": "嗯。什么都没有。",
 "Nothing in here either...": "这里也没有……",
 "[disgusted] Erg...  Must've been Sasha's choice. No way am I sitting on that.":
    "[disgusted] 呃……肯定是 萨莎 选的。我绝不坐那玩意儿。",
 "But...so, where's the bathroom?": "可……那厕所在哪儿？",
 "Oh hey, real cast iron.  Shame about the kitchen situation.":
    "哦，真铸铁。可惜厨房那情况不怎么样。",
 "{NeutralB} Rhys, if that's Atlas tech, you should be able to scan it.":
    "{NeutralB} 瑞斯，要是那是 Atlas 科技，你应该能扫描它。",
 "[postpax] {NeutralB} ...right after you plugged in...": "[postpax] {NeutralB} ……就在你插上线之后……",
 "[postpax] {NeutralA} Like, a thud but... wet.": "[postpax] {NeutralA} 像是「咚」的一声，但……湿的。",
 "[postpax] {WorryA} You totally whacked your head...": "[postpax] {WorryA} 你脑袋撞得可不轻……",
 "[postpax] {WorryA} It made this gross sound.": "[postpax] {WorryA} 那声音听着很恶心。",
 "[postpax] [beat] {SadA} Are they really that tedious?": "[postpax] [beat] {SadA} 他们真有那么无聊？",
 "[postpax] {NeutralA} They're a little on the tedious side, yeah.": "[postpax] {NeutralA} 是有点无聊。",
 "[postpax] [alt] {smugC}And we looked and learned that you drool all over the floor while you're unconcious.":
    "[postpax] [alt] {smugC}我们看也看了、学也学了：你昏过去的时候会把地板流满口水。",
 "[postpax] [alt] {SmugC} You know, when you said, \"Get a load of this,\" we assumed you were talking about the drool that pooled around your face when you were unconcious.":
    "[postpax] [alt] {SmugC} 你说「看看这个」的时候，我们以为你指的是昏过去时脸边积的那滩口水。",
 "[postpax] I tracked the money while you were... out.": "[postpax] 你昏着的时候……我把钱追踪到了。",
 "[alt] [postpax] {SmugC}Watching you drool all over the floor didn't seem productive.":
    "[alt] [postpax] {SmugC}看着你往地板上流口水，好像没什么意义。",
 "[affronted] Someone could've left a note.": "[affronted] 有人可以留张纸条的。",
 "Wouldn't think they could stand to look at themselves, after all they've done.":
    "干了那些事之后，我还以为他们都不敢照镜子。",
 "Nothing, big surprise.": "什么都没有，真意外。",
 "No fake IDs or lock picks? Huh.": "没有假证件或者开锁工具？嗯。",
 "Their one belonging... Banang? I was expecting at least one head in a jar.":
    "他们唯一的家当……Banang？我还以为至少会有一罐人头。",
 "Those two and their 'uncle' live here? Talk about wackos. They don't even have a bathroom.":
    "那俩和他们的「叔叔」住这儿？真是怪人。连个厕所都没有。",
 "Cast iron steel. Impressive, considering...": "铸铁。挺讲究的，考虑到……",
 "Those two and that old guy live here? My bathroom's bigger then this place.":
    "那俩和那老头住这儿？我家厕所都比这地方大。",
 "Cast iron steel. Impressive... for con artists.": "铸铁。挺讲究……对两个骗子来说。",
 "[disgusted] Erg...vintage, I guess.": "[disgusted] 呃……大概算复古吧。",
 "They got her good side, at least. Reward.... Mental note on that one.":
    "至少拍到了她的好角度。奖金……这条记下来。",
 "No thinning hair for this guy. Thanks, \"Hypergain.\"": "这位头发一点都不稀疏。谢了，「Hypergain」。",
 "Creepy. But kinda.... No, just creepy.": "有点瘆人。不过还挺……不，就是瘆人。",
 "Probably ripped these off of some poor, non-suspecting Pandoran.":
    "大概是从某个倒霉、毫无戒心的 潘多拉 人身上扒下来的。",
 "How many of these things does Fiona need?": "Fiona 需要几副这种东西？",
 "Eck. They can afford this hunk of metal but no cleaning bots?": "呃。买得起这坨铁，却请不起清洁机器人？",
 "If I had to vote for ugliest thing in this place, there it is.": "要投票选这地方最丑的东西，就是那儿。",
 "But that's a tough call.": "不过也很难说。",
 "Don't wanna touch those, I'd probably find a spring loaded fire grenade or something.":
    "那些我不碰，搞不好会摸出个弹簧触发的燃烧弹。",
 "At least they got one thing right on this planet.": "至少这星球上有一件事他们做对了。",
 "{HappyA} Nice to meet you, Miss Moxxi. {SmugA} Not too shabby, in that {NeutralA} crazy Pandora kind of way.":
    "{HappyA} 幸会，莫西 小姐。{SmugA} 以{NegativeA} 潘多拉 式疯狂的标准看，还算不赖。",
 "Purfume, on Pandora? I guess when you're scamming people out of millions of dollars, you want to smell good.":
    "香水？在 潘多拉？大概骗了人家几百万之后，是想闻起来体面点。",
 "Who knows what kinda skeletons that old man's keeping in here. Hm.":
    "谁知道那老头在这屋里藏了什么见不得人的东西。嗯。",
 "Scan": "扫描",
 "Mirror": "镜子",
 "Hand Mirror": "手镜",
 "Pans": "锅具",
 "Cabinet": "橱柜",
 "Privacy Wall": "隔断墙",
 "Mannequin": "人体模型",
 "Pants": "裤子",
 "Jacket": "外套",
 "Fancy Curtains": "讲究的窗帘",
 "Boots": "靴子",
 "Tea Pot": "茶壶",
 "Perfume Bottle": "香水瓶",
 "Navigation Computer": "导航计算机",
 "Couch": "沙发",
 "Family Photo": "全家福",
 "Moxxi Poster": "莫西 海报",
 "Sink": "水槽",
 "Curtains": "窗帘",
 "Next, take out the  psycho...": "接着，干掉那个疯子……",
 "And get the money!": "然后把钱拿到手！",
 "Weapon Crate": "武器箱",
 "Wanted Poster": "通缉海报",
 "...while we casually take our new pal for a stroll.": "……同时若无其事地带着我们的新伙伴散步。",
 "First, we find a crafty hiding spot...": "首先，找个巧妙的藏身处……",
 "Then we make ourselves a new friend.": "然后交个新朋友。",
 "Fiona and Sasha find cover in order to sneak closer...": "Fiona 和 萨莎 找掩体，以便更靠近……",
 "Then we borrow a gun from one of the guards...": "然后向某个守卫「借」把枪……",
 "Making sure that his buddy doesn't feel left out.": "确保他的同伴也不会被冷落。",
 "Then we take the secret entrance...": "然后我们从密道进去……",
 "...where we take a moment to celebrate our swift and easy victory!":
    "……在那里花点时间庆祝我们迅速而轻松的胜利！",
 "[pickup][to himself; reluctant admiration; looking at photo of Felix & Girls] Wow... Guess these three have been together for a long time.":
    "[pickup][to himself; reluctant admiration; looking at photo of Felix & Girls] 哇……看来这三个人在一起很久了。",
 "[pickup][to himself; looking at wanted poster of Fiona] Hmpf. Criminals. I should have seen it coming.":
    "[pickup][to himself; looking at wanted poster of Fiona] 哼。罪犯。我早该看出来的。",
 "[pickup][smug] I don't know if passing out and drooling is what you meant by \"hope this works,\" but if it was... congratulations!":
    "[pickup][smug] 我不知道昏过去流口水是不是你说的「但愿这招管用」，如果是的话……恭喜你！",
 "My way would have worked.": "我那办法本来能成的。",
 "Good job following my instructions.": "照我说的做，干得不错。",
 "[pickup][after montage]I gonna assume you just did everything I was saying so... you know... good work!":
    "[pickup][after montage]我就当你是照我说的全做了，所以……你知道……干得好！",
 "Quit leaving me behind!": "别再把我丢下！",
 "[pickup][after montage] Ya know, I'm getting kind of tired of getting left behind... so, ya know... stop.":
    "[pickup][after montage] 你知道，我有点受够被丢下了……所以，你知道……别这样了。",
 "[quietly] {AngryA} Oh, apart from waking up completely alone in a crappy trailer with drool coming out of my mouth, {SmugA} I'm great. {SternA}Thanks for the concern.":
    "[quietly] {AngryA} 哦，除了在一个破房车里孤零零醒来、嘴角还挂着口水之外，{SmugA} 我好得很。{SternA}谢谢关心。",
 "Ooh, that hatch goes down underneath the building... but... it's... guarded.":
    "哦，那个舱口通向建筑地下……可是……那儿……有守卫。",
 "Not texty yet. Sad face robo face.": "还没写上字呢。哭脸机器人脸。",
 "bandits": "土匪",
 "Upper Cabinets": "上层橱柜",
 "TEMP TEXT": "TEMP TEXT",
 "Lower Cabinets": "下层橱柜",
 "Dressing Screen": "更衣屏风",
 "Travel Poster": "旅游海报",
 "Bumper Sticker": "车贴",
 "Helios": "赫利俄斯",
 "Crane": "起重机",
 "Technical": "技术车",
 "Felix": "菲利克斯",
 "Fiona": "Fiona",
 "Sasha": "萨莎",
 "Vaughn": "沃恩",
 "Coat": "大衣",
 "...which leads us to the briefcase...": "……这就引出了那个手提箱……",
 # —— ECHO 扫描资料卡 ——
 "^color:#ffea7f^Helios\n^color:white^Hyperion Corporation's orbital base of operations\n^color:#ffea7f^Elevation: ^color:white^204,603 miles (329,276 Kilometers)\n^color:#ffea7f^Population: ^color:white^52,072 (not counting robots)\n^color:#ffea7f^Weaponry: ^color:white^ Moonshot Blitz Cannon\n^color:#ffea7f^Armed: ^color:white^Always\n\n^color:white^Hyperion is constantly observing the surface of Pandora because it cares about each and every Pandoran resident. So be on your best behavior.":
    "^color:#ffea7f^赫利俄斯\n^color:white^亥博龙公司的轨道行动基地\n^color:#ffea7f^高度: ^color:white^204,603 英里（329,276 公里）\n^color:#ffea7f^人口: ^color:white^52,072（不含机器人）\n^color:#ffea7f^武器: ^color:white^ 月击闪电炮\n^color:#ffea7f^武装状态: ^color:white^始终\n\n^color:white^亥博龙时刻观察着 潘多拉 表面，因为它关心每一位 潘多拉 居民。所以请注意你的言行。",
 "^color:white^Helios Station\n^color:#ffea7f^Elevation: ^color:white^204,603 miles\n^color:#ffea7f^Population: ^color:white^52,072 \n^color:#ffea7f^Weaponry: ^color:white^Moonshot Blitz Cannon\n\n^color:white^Hyperion is constantly observing the surface of Pandora because it cares about each and every Pandoran resident. So be on your best behavior.":
    "^color:white^太阳神空间站\n^color:#ffea7f^高度: ^color:white^204,603 英里\n^color:#ffea7f^人口: ^color:white^52,072 \n^color:#ffea7f^武器: ^color:white^月击闪电炮\n\n^color:white^亥博龙时刻观察着 潘多拉 表面，因为它关心每一位 潘多拉 居民。所以请注意你的言行。",
 "^color:white^Mining Crane\n^color:#ffea7f^Manufacturer: ^color:white^Atlas: Cranes, Trains, & Automobiles Division\n^color:#ffea7f^Model: ^color:white^Hades Excavation Arm\n^color:#ffea7f^Extended Warranty: ^color:white^No\n\nWhen Atlas abandoned their efforts on Pandora, they left behind hundreds of mining rigs and cranes like this one. Lousy litterbugs.":
    "^color:white^采矿起重机\n^color:#ffea7f^制造商: ^color:white^Atlas：起重机、列车与汽车事业部\n^color:#ffea7f^型号: ^color:white^Hades 挖掘臂\n^color:#ffea7f^延保: ^color:white^无\n\nAtlas 放弃在 潘多拉 的经营时，留下了数百台这样的采矿设备和起重机。真是没素质的乱丢垃圾者。",
 "^color:white^The Local Color\n^color:#ffea7f^Status: ^color:white^Agitated\n^color:#ffea7f^Hygiene: ^color:white^None\n^color:#ffea7f^Armed: ^color:white^Very\n\n^color:white^A diverse range of lunatics, murderers, psychopaths, yahoos, hooligans, roughnecks, madmen, and ne'er-do-wells, all excited about something. Probably murder.":
    "^color:white^本地风情\n^color:#ffea7f^状态: ^color:white^躁动\n^color:#ffea7f^卫生状况: ^color:white^无\n^color:#ffea7f^武装: ^color:white^极其\n\n^color:white^各式各样的疯子、杀人犯、精神病、乡巴佬、混混、粗汉、狂人和无赖，全都为某件事兴奋着。大概是杀人吧。",
 "^color:#ffea7f^Bandit Technical\n^color:#ffea7f^Seats: ^color:white^4\n^color:#ffea7f^Pros: ^color:white^Durable, deadly\n^color:#ffea7f^Cons: ^color:white^Limited agility\n^color:#ffea7f^Weaponry: \n^color:white^-Front-Mounted Machine Gun\n^color:white^-Modular Turret Mount\n\n^color:white^One of Pandora's most popular vehicles, the technical is a great way to say, \"Hi, world! I'm gonna kill you!\"":
    "^color:#ffea7f^土匪技术车\n^color:#ffea7f^座位: ^color:white^4\n^color:#ffea7f^优点: ^color:white^耐用、致命\n^color:#ffea7f^缺点: ^color:white^灵活性差\n^color:#ffea7f^武器: \n^color:white^-前置机枪\n^color:white^-模块化炮塔挂点\n\n^color:white^作为 潘多拉 最流行的载具之一，技术车是说出「嗨世界！我要弄死你！」的好方式。",
 "^color:#ffea7f^Seats: ^color:white^4\n^color:#ffea7f^Pros: ^color:white^Durable, deadly\n^color:#ffea7f^Cons: ^color:white^Limited agility\n^color:#ffea7f^Weaponry: \n^color:white^-Front-Mounted Machine Gun\n^color:white^-Modular Turret Mount\n\n^color:white^One of Pandora's most popular vehicles, the technical is a great way to say, \"Hi, world! I'm gonna kill you!\"":
    "^color:#ffea7f^座位: ^color:white^4\n^color:#ffea7f^优点: ^color:white^耐用、致命\n^color:#ffea7f^缺点: ^color:white^灵活性差\n^color:#ffea7f^武器: \n^color:white^-前置机枪\n^color:white^-模块化炮塔挂点\n\n^color:white^作为 潘多拉 最流行的载具之一，技术车是说出「嗨世界！我要弄死你！」的好方式。",
 "^color:#ffea7f^Weapon Crate\n^color:white^Filled to the brim with implements of Love and Peace.":
    "^color:#ffea7f^武器箱\n^color:white^塞满了「爱与和平」的器具。",
 "^color:white^Homemade Privacy Shield\n^color:#ffea7f^Capacity: ^color:white^1058\n^color:#ffea7f^Recharge Rate: ^color:white^102\n^color:#ffea7f^Recharge Delay: ^color:white^1.29\n\nAlthough ineffective against elemental or standard attacks, ^color:#ffea7f^Dressing Screen ^color:white^grants full immunity to the ^color:#ffea7f^Visual Spectrum^color:white^.":
    "^color:white^自制隐私护盾\n^color:#ffea7f^容量: ^color:white^1058\n^color:#ffea7f^回充速率: ^color:white^102\n^color:#ffea7f^回充延迟: ^color:white^1.29\n\n虽然对元素攻击或常规攻击无效，但^color:#ffea7f^更衣屏风 ^color:white^能提供对^color:#ffea7f^可见光频谱^color:white^的完全免疫。",
 "^color:#ffea7f^A standard cabinet\n^color:#ffea7f^Contents: \n^color:white^  -Canned beans\n^color:white^  -7 plates (Cracked)\n^color:white^  -3 mugs (Chipped)":
    "^color:#ffea7f^一个普通橱柜\n^color:#ffea7f^内容物: \n^color:white^  -罐装豆子\n^color:white^  -7 个盘子（有裂痕）\n^color:white^  -3 个杯子（有缺口）",
 "^color:#ffea7f^A special cabinet*\n^color:#ffea7f^Contents:\n^color:white^  -Guitar picks (Sturdy)\n^color:white^  -Guitar strings (Bass)\n^color:white^  -Sheet music (Not good)\n\n*A comedy joke. It's just a regular-type cabinet.":
    "^color:#ffea7f^一个特别的橱柜*\n^color:#ffea7f^内容物:\n^color:white^  -吉他拨片（结实）\n^color:white^  -吉他弦（贝斯）\n^color:white^  -乐谱（不怎么样）\n\n*一个搞笑梗。它就是个普通橱柜。",
 "color:#ffea7f^Loot Crate\n^color:white^\"Toy Box\"\n^color:#ffea7f^Contents:\n^color:white^  -Coloring books\n^color:white^  -Children's toys\n^color:#ffea7f^Time since last opened:\n^color:white^  -16 years, 4 months, 9 days":
    "color:#ffea7f^战利品箱\n^color:white^「玩具箱」\n^color:#ffea7f^内容物:\n^color:white^  -涂色本\n^color:white^  -儿童玩具\n^color:#ffea7f^距上次开启:\n^color:white^  -16 年 4 个月 9 天",
 "^color:white^\"Toy Box\"\n^color:#ffea7f^Contents:\n^color:white^  -Coloring books\n^color:white^  -Children's toys\n^color:#ffea7f^Time since last opened:\n^color:white^  -16 years, 4 months, 9 days":
    "^color:white^「玩具箱」\n^color:#ffea7f^内容物:\n^color:white^  -涂色本\n^color:white^  -儿童玩具\n^color:#ffea7f^距上次开启:\n^color:white^  -16 年 4 个月 9 天",
 "Hollowpoint Radio\nFrequency: [Unknown]\nHost: [Unknown]\nHypothesized Purpose: Anti-Hyperion propaganda (90% likely)\n\nHyperion has been unable to identify any information about \"Hollow Point Radio\" beyond stray rumors but management has decided that they don't like it.":
    "Hollowpoint 电台\n频率：[未知]\n主播：[未知]\n推测用途：反 亥博龙宣传（90% 可能）\n\n除了零星的传言，亥博龙一直查不到任何关于「Hollowpoint 电台」的信息，但管理层已经决定他们不喜欢它。",
 "Bumper Sticker\nHollowpoint Radio\nFrequency: [Unknown]\nHost: [Unknown]\nHypothesized Purpose: Anti-Hyperion propaganda (90% likely)\n\nHyperion has been unable to identify any information about \"Hollow Point Radio\" beyond stray rumors but management has decided that they don't like it.":
    "车贴\nHollowpoint 电台\n频率：[未知]\n主播：[未知]\n推测用途：反 亥博龙宣传（90% 可能）\n\n除了零星的传言，亥博龙一直查不到任何关于「Hollowpoint 电台」的信息，但管理层已经决定他们不喜欢它。",
 "Hollowpoint Radio\nFrequency: [Unknown]\nHost: (Unknown)\nHypothesized Purpose: Anti-Hyperion propaganda (90% likely)\n\nHyperion has been unable to identify any information about \"Hollow Point Radio\" beyond stray rumors but management has decided that they don't like it.":
    "Hollowpoint 电台\n频率：[未知]\n主播：（未知）\n推测用途：反 亥博龙宣传（90% 可能）\n\n除了零星的传言，亥博龙一直查不到任何关于「Hollowpoint 电台」的信息，但管理层已经决定他们不喜欢它。",
 "^color:white^Hollowpoint Radio\n^color:#ffea7f^Frequency: ^color:white^(Unknown)\n^color:#ffea7f^Host: ^color:white^(Unknown)\n^color:#ffea7f^Purpose: ^color:white^Anti-Hyperion propaganda?\n\n^color:white^Hyperion has been unable to identify any solid information about \"Hollow Point Radio,\" but management has decided that they don't like it.":
    "^color:white^Hollowpoint 电台\n^color:#ffea7f^频率: ^color:white^（未知）\n^color:#ffea7f^主播: ^color:white^（未知）\n^color:#ffea7f^用途: ^color:white^反 亥博龙宣传？\n\n^color:white^亥博龙一直查不到任何关于「Hollowpoint 电台」的确切信息，但管理层已经决定他们不喜欢它。",
 "\"Visit Beautiful Dionysus\"\nPrinted by: Dionysus Board of Tourism\nAge: 12 years\n\nA common poster on the bedroom walls of would-be poets and songwriters, \"Beautiful Dionysus\" is an aspirational location for many wanderlust-stricken Pandorans.":
    "「来美丽的 Dionysus」\n印刷方：Dionysus 旅游局\n年代：12 年\n\n这张海报常见于准诗人和词曲作者卧室的墙上；对许多渴望远行的 潘多拉 人来说，「美丽的 Dionysus」是一个心之所向的地方。",
 "^color:#ffea7f^<<id:362496513>>\"Visit Beautiful Dionysus\"\n^color:#ffea7f^Printed by: Dionysus Board of Tourism\n^color:#ffea7f^Age: 12 years\n\nA common poster on the bedroom walls of would-be poets and songwriters, \"Beautiful Dionysus\" is an aspirational location for many wanderlust-stricken Pandorans.":
    "^color:#ffea7f^<<id:362496513>>「来美丽的 Dionysus」\n^color:#ffea7f^印刷方: Dionysus 旅游局\n^color:#ffea7f^年代: 12 年\n\n这张海报常见于准诗人和词曲作者卧室的墙上；对许多渴望远行的 潘多拉 人来说，「美丽的 Dionysus」是一个心之所向的地方。",
 "^color:white^Travel Poster\n^color:#ffea7f^\"Visit Beautiful Dionysus\"\n^color:#ffea7f^Printed by: ^color:white^Dionysus Board of Tourism\n\nA common poster on the bedroom walls of would-be poets and songwriters, \"Beautiful Dionysus\" is an aspirational location for many wanderlust-stricken Pandorans.":
    "^color:white^旅游海报\n^color:#ffea7f^「来美丽的 Dionysus」\n^color:#ffea7f^印刷方: ^color:white^Dionysus 旅游局\n\n这张海报常见于准诗人和词曲作者卧室的墙上；对许多渴望远行的 潘多拉 人来说，「美丽的 Dionysus」是一个心之所向的地方。",
 "Repurposed Target Practice Dummy\nManufacturer: Local manufacturer? Analysis inconclusive.\nOutfit Composition:\n-72% Rakk Leather\n-22% Maliwan Plasteel\n-06% Duct Tape\nOutfit Analysis: Meh. [See: \"Pandoran Frontierism & Fashion! A Guide for the Layman Pioneer\"]":
    "改装靶场假人\n制造商：本地厂商？分析无结论。\n服装成分：\n-72% 拉克鸟皮革\n-22% Maliwan 塑钢\n-6% 强力胶带\n服装评价：一般。[参见：《Pandora 边疆主义与时尚！外行先驱指南》]",
 "^color:white^Jacket\n^color:#ffea7f^Manufacturer: ^color:white^Local manufacturer? Analysis inconclusive.\n^color:#ffea7f^Outfit Composition:\n^color:white^-72% Rakk Leather\n^color:white^-22% Maliwan Plasteel\n^color:white^-06% Duct Tape\n^color:#ffea7f^Outfit Analysis: ^color:white^Meh. (See: \"Pandoran Frontierism & Fashion! A Guide for the Layman Pioneer\")":
    "^color:white^外套\n^color:#ffea7f^制造商: ^color:white^本地厂商？分析无结论。\n^color:#ffea7f^服装成分:\n^color:white^-72% 拉克鸟皮革\n^color:white^-22% Maliwan 塑钢\n^color:white^-6% 强力胶带\n^color:#ffea7f^服装评价: ^color:white^一般。（参见：“潘多拉 边疆主义与时尚！外行先驱指南”）",
 "\"Midnight at Moxxi's\"\nWho: \nThe White Hot Smooches\nDead or Nearly Dying\nFrostburned Soul\nWhat: A Pandoran \"music\" concert\nWhen: Midnight\nWhere: A Pandoran watering hole\nWhy: Good question":
    "「莫西 家的午夜」\n演出者：\nThe White Hot Smooches\nDead or Nearly Dying\nFrostburned Soul\n内容：一场 潘多拉 的「音乐」演唱会\n时间：午夜\n地点：某家 潘多拉 酒馆\n为何：好问题",
 "^color:#ffea7f^\"Midnight at Moxxi's\"\n^color:#ffea7f^Who: \n^color:white^The White Hot Smooches\n^color:white^Dead or Nearly Dying\n^color:white^Frostburned Soul\n^color:#ffea7f^What: ^color:white^A Pandoran \"music\" concert\n^color:#ffea7f^When: ^color:white^Midnight\n^color:#ffea7f^Where: ^color:white^A Pandoran watering hole\n^color:#ffea7f^Why: ^color:white^Good question":
    "^color:#ffea7f^「莫西 家的午夜」\n^color:#ffea7f^演出者: \n^color:white^The White Hot Smooches\n^color:white^Dead or Nearly Dying\n^color:white^Frostburned Soul\n^color:#ffea7f^内容: ^color:white^一场 潘多拉 的「音乐」演唱会\n^color:#ffea7f^时间: ^color:white^午夜\n^color:#ffea7f^地点: ^color:white^某家 潘多拉 酒馆\n^color:#ffea7f^为何: ^color:white^好问题",
 "^color:white^Photograph\n^color:#ffea7f^Chem. Analysis:\n^color:white^-Printed on instant film\n-Decay indicates picture was taken approx. 15y ago*\n\n*Picture taken on inferior Dahl photo stock. Level of decay would be far less on Hyperion Insta-Film.":
    "^color:white^照片\n^color:#ffea7f^化学分析:\n^color:white^-使用即时成像胶片冲印\n-老化程度显示拍摄于约 15 年前*\n\n*照片使用劣质 Dahl 相纸。若用 亥博龙即时胶片，老化程度会低得多。",
 "^color:white^Modified Weapons Crate\n^color:#ffea7f^Analysis:\n^color:white^-Trace amounts of explosive materials detected\n-Extensive modifications made to crate to make it lighter and more portable\n-Contents and Manufacturer unknown":
    "^color:white^改装武器箱\n^color:#ffea7f^分析:\n^color:white^-检测到微量爆炸物残留\n-箱子经过大量改装，以更轻便易携\n-内容物与制造商未知",
 "^color:white^Vaughn\n^color:#ffea7f^Age: ^color:white^27\n^color:#ffea7f^Hyperion Employee ID: ^color:white^RM-9452\n^color:#ffea7f^Occupation: ^color:white^Accountant\n^color:#ffea7f^Favorite Color: ^color:white^Goldenrod\n^color:#ffea7f^Favorite Book: ^color:white^\"Mind the GAAP: Generally-Accepted Accounting Principles and You!\"\n^color:#ffea7f^Current Status: ^color:white^Dreading Everything":
    "^color:white^沃恩\n^color:#ffea7f^年龄: ^color:white^27\n^color:#ffea7f^亥博龙员工编号: ^color:white^RM-9452\n^color:#ffea7f^职业: ^color:white^会计\n^color:#ffea7f^最喜欢的颜色: ^color:white^金黄\n^color:#ffea7f^最喜欢的书: ^color:white^“小心 GAAP：公认会计准则与你！”\n^color:#ffea7f^当前状态: ^color:white^对一切感到恐惧",
 "^color:white^Fiona\n^color:#ffea7f^Age: ^color:white^29\n^color:#ffea7f^Hometown: ^color:white^Hollow Point\n^color:#ffea7f^Occupation: ^color:white^None/\"Con Artist\"\n^color:#ffea7f^Current Status: ^color:white^Eager\n\n^color:white^This Pandoran is wanted for multiple counts of scamming, conning, forgery, and theft. Treat with caution.":
    "^color:white^Fiona\n^color:#ffea7f^年龄: ^color:white^29\n^color:#ffea7f^家乡: ^color:white^空心弹镇\n^color:#ffea7f^职业: ^color:white^无/「职业骗子」\n^color:#ffea7f^当前状态: ^color:white^跃跃欲试\n\n^color:white^这名 潘多拉 人因多起诈骗、行骗、伪造与盗窃被通缉。接触时请小心。",
 "^color:white^Sasha\n^color:#ffea7f^Age: ^color:white^24\n^color:#ffea7f^Hometown: ^color:white^Hollow Point\n^color:#ffea7f^Occupation: ^color:white^None/\"Con Artist\"\n^color:#ffea7f^Current Status: ^color:white^Trigger-happy\n\n^color:white^Although her rap sheet isn't as long as her older sister's, this Pandoran is still a slippery and dangerous subject in her own right.":
    "^color:white^萨莎\n^color:#ffea7f^年龄: ^color:white^24\n^color:#ffea7f^家乡: ^color:white^空心弹镇\n^color:#ffea7f^职业: ^color:white^无/「职业骗子」\n^color:#ffea7f^当前状态: ^color:white^手痒想开枪\n\n^color:white^虽然她的案底不如姐姐长，但这位 潘多拉 人本身同样滑不留手、十分危险。",
 "^color:white^Felix\n^color:#ffea7f^Age: ^color:white^(DATA NOT FOUND)\n^color:#ffea7f^Hometown: ^color:white^(DATA NOT FOUND)\n^color:#ffea7f^Occupation: ^color:white^=~-Upstanding Citizen\n^color:#ffea7f^Current Status: ^color:white^Elevated Heartrate\n\n^color:white^Felix has a long h1st0ry 0f-~-~-being an upstanding citizen and friend to all who would never even dream of commiting a crime.":
    "^color:white^菲利克斯\n^color:#ffea7f^年龄: ^color:white^（数据未找到）\n^color:#ffea7f^家乡: ^color:white^（数据未找到）\n^color:#ffea7f^职业: ^color:white^=~-正直公民\n^color:#ffea7f^当前状态: ^color:white^心率偏高\n\n^color:white^菲利克斯 有着长久的 1st0ry ——是位正直公民、人人的朋友，绝不会哪怕做梦想到去犯罪。",
})
