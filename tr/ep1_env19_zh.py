# 批次3-3：第1章 env_19_arenabattleground_aftermath（竞技场余波：清点损失、拾荒、发现 Gortys 核心）
# 复用上一批（env_18b）的译文，只补本文件新增内容
import importlib.util as _ilu, os as _os
_p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'ep1_env18b_zh.py')
_s = _ilu.spec_from_file_location('_prev18b', _p)
_m = _ilu.module_from_spec(_s); _s.loader.exec_module(_m)
T = dict(_m.T)
T.update({
 # —— 余波：清点损失 ——
 "Hey, uh, maybe we should, uh, ask the... guy... there?": "呃，我们要不要，呃，问问……那边那位？",
 "Ask him what.": "问他什么。",
 "You know, I dunno, for help? I guess?": "就……我也不知道，问能不能帮忙？大概？",
 "[bitter] {AngryB}*Felix*.": "[bitter] {AngryB}*菲利克斯*。",
 "Their *friend* got himself blown up trying to steal the case.": "他们的*朋友*想偷箱子，结果把自己炸了。",
 "[sighs] Really?": "[sighs] 真的？",
 "Their *friend* stole the case, took off with it into the clear blue night.": "他们的*朋友*偷走箱子，消失在清朗的蓝夜里。",
 "[correcting] Clear black night, but I mean, whatever, we can still just track it, right?": "[correcting] 是清朗的黑夜，不过随便吧，我们还能追踪它，对吧？",
 "Clear black night.": "清朗的黑夜。",
 "[cold] {AngryC}He deserved it what he got.": "[cold] {AngryC}他活该。",
 "{AngryA}I mean... after everything we'd been through? {AngryC}To do something like that? {RageA}Screw him.":
    "{AngryA}我是说……经历了那么多之后？{AngryC}还干出这种事？{RageA}去死吧他。",
 "God *damnit*!": "该死的！",
 "The money's gone. Every bill's burnt to stardust.": "钱没了。每一张都烧成了星尘。",
 "[calming] Fiona...": "[calming] Fiona……",
 "[quietly to herself] {SadA}We were *so* close, it was practically in my {SadB}*hands*...":
    "[quietly to herself] {SadA}就差那么一点点，它几乎就在我{SadB}*手里*……",
 "Nothing's left. It's all gone.": "什么都没了。全没了。",
 "[bitter] {AngryA}It doesn't matter now. {SternA}The money's burnt to a crisp. And so is he.":
    "[bitter] {AngryA}现在说这些没用了。{SternA}钱烧成了灰。他也是。",
 "{SadA}It was tragic. [beat] {FearB}The case was *right* there, {SadB}within reach...":
    "{SadA}太惨了。[beat] {FearB}箱子*就*在那儿，{SadB}伸手就能拿到……",
 "{SternA}I think {AngryA}\"why\" he did it is literally the {SternB}million dollar question.":
    "{SternA}他{AngryA}「为什么」要这么做，这就是那个{SternB}价值百万的问题。",
 "{WorryA}You know, Felix {AngryA}was a real jerk... but... {SadA}I'll still kinda miss him.":
    "{WorryA}你知道，菲利克斯 {AngryA}确实是个混蛋……可是……{SadA}我还是有点想他。",
 "{AngryA}The guy who just extra-ruined our lives?": "{AngryA}那个刚刚把我们的人生彻底毁掉的人？",
 "{WorryA}What can you do with someone like that? {AngryB}Hate him? {SadA}I mean, he's dead.":
    "{WorryA}对这种人你还能怎样？{AngryB}恨他？{SadA}可他人都死了。",
 "I kinda wish you'd told us your buddy was a bit of a klepto *before* he'd try to run off with a million of our dollars.":
    "我真希望你能在你那位朋友拿着一百万跑路*之前*，告诉我们他有顺手牵羊的毛病。",
 "We *can't* track it.": "我们*没法*追踪它。",
 "Now that Vasquez has caught wind of what I was doing with Nakayama's codes... that won't work anymore.":
    "既然 Vasquez 已经知道我用 Nakayama 的代码做了什么……那招不再管用了。",
 "He'd never done anything like this before.": "他以前从没干过这种事。",
 "A professional criminal who'd never stolen before? Really?": "一个职业罪犯从没偷过东西？真的？",
 "{WorryA}You can't trust someone who's got nothin' to lose. {SadA}We just... we just didn't catch it in time with him.":
    "{WorryA}一无所有的人不能信。{SadA}我们只是……我们只是没及时发现。",
 "You'd think we'd run around with people like that if we knew beforehand!":
    "要是早知道，你以为我们会跟这种人混在一起吗！",
 "{SternB}Yeah, really.": "{SternB}是啊，真的。",
 "[bitter] I trusted that guy, I *trusted* him with... I mean, I'd put my life in that frickin' loser's *hands* before.":
    "[bitter] 我信过那个人，我*信*过他……我是说，我以前把命都交到那个废物*手上*过。",
 "I know.": "我知道。",
 "[bitter] {AngryA}It doesn't matter now. {SternB}He's gonna be miles away, and the money with him.":
    "[bitter] {AngryA}现在说这些没用了。{SternB}他早跑远了，钱也跟着他。",
 "[cold] And every dollar he's spent is gonna get repaid in a quart of blood and an inch of skin.":
    "[cold] 他花掉的每一块钱，都得用一夸脱血和一寸皮来还。",
 "Alrighty, uh, easy does it there, sis.": "好啦，呃，悠着点，妹妹。",
 "[cold] {AngryA}If I ever see him again -- and he better hope{AngryC} I don't -- {RageA}he's dead.":
    "[cold] {AngryA}要是我再见到他——他最好祈祷{AngryC}别见着——{RageA}他死定了。",
 "{InquireB}It's called *looting*, {SchemeA}and we've been doin' it since we were in diapers.":
    "{InquireB}这叫*拾荒*，{SchemeA}我们还在穿尿布的时候就在干了。",
 "But if we're gonna do it... we should do it fast.": "但既然要做……就得快点。",
 "Oh God, don't be a goober right now, I can't take it.": "天啊，别在这时候犯傻，我受不了。",
 "Go help the tall one.": "去帮那个高个子。",
 "Hey, look, this isn't-- it's not *all* bad news, okay? This was an Atlas facility, right?":
    "嘿，听着，这也不——不*全是*坏消息，行吗？这里是 Atlas 的设施，对吧？",
 "[plainly] Stuff.": "[plainly] 东西。",
 "Yeah...": "是啊……",
 "Rhys, can you see anything down there?": "瑞斯，下面能看到什么吗？",
 "I'm not doing anything!": "我什么都没干！",
 "Oh, crap. Wait. This isn't...": "哦，糟了。等等。这不是……",
 "Well stop whatever you're not doing!": "那就把你「没在干」的事停下来！",
 "Alrighty. Find anything expensive.": "行。找点值钱的。",
 "If it's heavy or shiny.": "重或者亮就行。",
 "How can I tell what's expensive?": "我怎么知道什么值钱？",
 "{AngryA}Define something.": "{AngryA}你先定义一下「东西」。",
 "{ThinkA}It's... I dunno... What *is* that?": "{ThinkA}那是……我也不知道……那*到底*是什么？",
 "HJAI": "HJAI",
 "[beat] You Suck.": "[beat] 你太烂了。",
 "Oh, that?[beat, then laughs] That's a Vault, baby.": "哦，那个？[beat, then laughs] 那是秘藏，宝贝。",
 "{SmugA}Very funny Vaughn.  I think this... I think this is...": "{SmugA}真好笑，沃恩。我觉得这……我觉得这是……",
 "Ugh. Fine.": "呃。行吧。",
 "C'mon, Sasha, *he* fell in the hole, let *him* scavenge for old... driver ports or whatsidoodles or whatever blows these guys' skirts up.":
    "得了吧 萨莎，是*他*掉进洞里的，让他自己去翻那些旧……驱动接口还是什么鬼玩意儿，随便什么能让这帮人兴奋的东西。",
 "[sarcastic] *Oh* no, I'll need *plenty* of help from the Whining Wench! Please climb down and help me *look* for whatsidoodles.":
    "[sarcastic] *哦*不，我可太需要「哭丧婆」的帮忙了！快爬下来帮我*找*那些鬼玩意儿吧。",
 "Just get in the hole.": "进洞里去。",
 "Anything that, uh, can still turn *on* will do.": "能……还能*开机*的都行。",
 "I wouldn't even know what to look for.": "我连该找什么都不知道。",
 "Huh. Well, it's *shiny* at least.": "嗯。至少它*够亮*。",
 "I have no idea what any of this stuff is.": "这些东西我一个都不认识。",
 "Is it heavy?": "重吗？",
 "Nothing.": "没什么。",
 "Ugh.": "呃。",
 "So... Atlas was what, a competitor or something?": "所以……Atlas 是什么，竞争对手之类的？",
 "Let's go with \"or something.\"": "就当成「之类的」吧。",
 "Huh.": "嗯。",
 "I mean, they never had the clout to really *contend*, you know? But their stuff's worth a bundle on the gray markets now.":
    "我是说，他们从来没那个影响力去真正*竞争*，对吧？可现在他们的东西在黑市上值一大笔钱。",
 "If I had to hazard a guess... his *heart* just wasn't in it anymore.": "要我猜……他是*心*不在这儿了。",
 "What do you think happened to this guy?": "你觉得这人出了什么事？",
 "I thought not.": "我就知道。",
 "This... probably doesn't count as \"gear\", right?": "这个……大概不算「装备」吧？",
 "Mission accomplished.": "任务完成。",
 "We can sell all this shit. A piece at a time. But we can sell it.": "这些破烂我们都能卖。一件一件来。总能卖出去。",
 "That's fracking ridiculous.": "这他妈也太离谱了。",
 "Alright, let's do this!": "好，干吧！",
 "That'll take forever.": "那得花一辈子。",
 "Nothing else to do.": "也没别的可做。",
 "silence": "沉默",
 "{SchemeA}How much money do we have on us? Maybe we can pool it? [beat] {SchemeB}I've got a dollar.":
    "{SchemeA}我们身上有多少钱？凑一凑？[beat] {SchemeB}我有一块。",
 "This. Is. Stupid.": "这。太。蠢了。",
 "We don't have any options. And Rhys here has already started.": "我们没别的选择。而且 瑞斯 已经开始干了。",
 "Time to get dirty.": "该去翻垃圾了。",
 "We can do this.": "我们能做到。",
 "Hyperion Sissy.": "亥博龙的娘娘腔。",
 "Vaughn, time to get that suit of yours dirty.": "沃恩，该把你那身西装弄脏了。",
 "I didn't sign up for this shit. I'm an accountant not a trash picker.": "我可没报名干这种破事。我是会计，不是捡垃圾的。",
 "Vaughn, we, can, do this. It's the life here on Pandora.": "沃恩，我、们、能、做到。潘多拉 的日子就是这样。",
 "You are such a Hyperion sissy. Start picking chump.": "你真是个 亥博龙娘娘腔。开始捡吧，笨蛋。",
 "Nothing but junk here.": "这儿全是破烂。",
 "I can't tell the difference.": "我分辨不出来。",
 "Sasha is right. This is crap. Nothing works.": "萨莎 说得对。这都是废物。没一个能用。",
 "Fiona did you find anything?": "Fiona，你找到什么了吗？",
 "I found a body.": "我找到一具尸体。",
 "A loot chest.": "一个战利品箱。",
 "Nope. Nothing.": "没有。什么都没有。",
 "Fiona find anything?": "Fiona 找到什么了？",
 "Yup.": "嗯。",
 "Nope.": "没有。",
 "Not sure.": "不确定。",
 "[from the other side of the room]Just make sure you don't pick up a booby trapped item.":
    "[from the other side of the room]千万别捡到装了诡雷的东西。",
 "Yeah historically speaking this Atlas guys were tricky.": "是啊，历史上 Atlas 这帮人挺阴的。",
 "Ah.ah.ah. That half is mine.": "哎、哎、哎。那一半是我的。",
 "Rhys?": "瑞斯？",
 "Woah. Rhys what the hell is is?": "哇。瑞斯，这到底是什么？",
 "Man bot are you listening?": "机器人老兄，你在听吗？",
 "What the hell. Looks like the other half of Fiona's.": "搞什么。看起来像 Fiona 那东西的另一半。",
 "I wonder if its broken. Try to join them.": "不知道是不是坏的。试着把两半接上。",
 "Come on Rhys put some elbow grease into it.": "来吧 瑞斯，使点劲。",
 "I'll help you. Sasha help Fiona.": "我来帮你。萨莎 去帮 Fiona。",
 "Pretty lights.": "好漂亮的灯。",
 "[yelling]What's going on?": "[yelling]怎么回事？",
 "woah.": "哇。",
 "[yelling] Oh shiiiiii......": "[yelling] 哦，完——",
 "[yelling] This is  going to get us kiillllled.": "[yelling] 这会害我们被弄死啊。",
 # —— 与 Vallory / Hyperion 摊牌 ——
 "{SternB}The case blew up, as advertised. [beat] {AngryB}Sadly, the dirty thief managed to get away.":
    "{SternB}箱子如约炸了。[beat] {AngryB}可惜那小偷跑掉了。",
 "{SternB}Their *friend* tried to {AngryA}steal the money.": "{SternB}他们的*朋友*想{AngryA}独吞那笔钱。",
 "{WorryA}It's only a matter of time before Vallory catches up with us.": "{WorryA}瓦洛里 追上我们只是时间问题。",
 "{SadA}Or Hyperion. [resigned] {AngryA}We might as well have blown up with that case, {SadB}because we're finished.":
    "{SadA}或者 亥博龙。[resigned] {AngryA}我们还不如跟着那箱子一起炸掉，{SadB}因为我们都完了。",
 "[resigned] We might as well have blown up with that case, because we're finished.":
    "[resigned] 我们还不如跟着那箱子一起炸掉，因为我们都完了。",
 "{SadA}On Pandora? Probably not.": "{SadA}在 潘多拉？大概不会。",
 "{SadA}I bet our deaths won't even be quick and painless.": "{SadA}我赌我们死得既不快也不痛快。",
 "{HappyA}Come on, this is Pandora.": "{HappyA}别这样，这可是 潘多拉。",
 "{SchemeC}There's always another insane and dangerous way to make money out there, {SmugA}we just need to find it.":
    "{SchemeC}总有别的又疯又危险的法子能赚钱，{SmugA}我们只要找到它。",
 "{SadA}Well... maybe we {SternA}*are* overreacting.": "{SadA}好吧……也许我们{SternA}*确实*反应过度了。",
 "{SternA}Maybe we can get that Zer0 guy to shoot us and {SadA}save all the waiting.":
    "{SternA}也许可以让那个叫 Zer0 的家伙直接开枪打死我们，{SadA}省得干等。",
 "{SadA}You're right. We're dead.": "{SadA}你说得对。我们死定了。",
 "{SternA}Can't you two just {doubtfulA}call in some Hyperion robots to fix everything?":
    "{SternA}你们俩就不能{doubtfulA}叫点 亥博龙机器人来把一切搞定？",
 "{AngryA}If we had robots that just gave a million bucks to anyone who asked, {AngryB}we wouldn't be in this mess.":
    "{AngryA}要是有那种开口就给一百万的机器人，{AngryB}我们也不会落到这步。",
 "You're from around here. Isn't there something we can do?": "你是本地人。我们总得能做点什么吧？",
 "{SadA}Or... you know... {HappyA}Slavery seems popular down here.  {SmugA}Maybe we could sell ourselves as slaves.":
    "{SadA}或者……你知道……{HappyA}这地方好像挺流行奴隶制。{SmugA}也许我们把自己卖了当奴隶。",
 "{AngryA}Very funny.": "{AngryA}真好笑。",
 "{SternA}I wasn't being funny.": "{SternA}我没在说笑。",
 "{SchemeA}Well we know the right people.  If you guys can figure out what's valuable, we might be able to pay our debt.":
    "{SchemeA}我们认识对的人。你们要是能分辨什么值钱，我们也许能还上债。",
 "{ShockA}That's old Atlas gear. {HappyA}Some of that stuff is really valuable -- [disappointment] {WorryB}to the right people.":
    "{ShockA}那是旧的 Atlas 装备。{HappyA}有些真的很值钱——[disappointment] {WorryB}当然是对识货的人来说。",
 "{SchemeB}There is a lot of this fancy computer stuff around here. And {HappyA}Rhys knows how to make it work, I saw him do it.":
    "{SchemeB}这附近有好多这种花哨的电脑玩意儿。而且{HappyA}瑞斯 知道怎么让它跑起来，我亲眼见过。",
 "{schemeA}You know... maybe all is not lost after all...": "{schemeA}你知道……也许事情还没到绝路……",
 "{HappyA}I've got twenty bucks. {SmugA}So now we've almost got enough to buy lunch.  {SternC}What about you two?":
    "{HappyA}我有二十块。{SmugA}现在差不多够买顿午饭了。{SternC}你们俩呢？",
 "{SternB}So... between us we owe{WorryA} two million bucks.": "{SternB}所以……我们一共欠{WorryA}两百万。",
 "{WorryB}By finding a bunch of random stuff in piles of rubble?": "{WorryB}靠从瓦砾堆里翻一堆乱七八糟的东西？",
 "Seriously?": "认真的？",
 "I don't have -- oh, never mind.": "我没有——哦，算了。",
 "{SternB}And have you made a {AngryB}million bucks in that time?":
    "{SternB}那这段时间你赚到{AngryB}一百万了吗？",
 "{SchemeA}Alright, we do this Pandoran-style.  {HappyA}Let's find some loot.":
    "{SchemeA}好，按 潘多拉 的方式来。{HappyA}去找战利品。",
 "{SternA}Looting? Seriously?  {AngryA}We'll die of old age or excess bullet holes long before we {SternB}make our money back.":
    "{SternA}拾荒？认真的？{AngryA}我们不是先老死就是先被打成筛子，{SternB}根本等不到回本。",
 "{SmugA}You gotta do what you gotta do.": "{SmugA}该干的就得干。",
 "[sigh] What other choice do we have?  Let's go find expensive things lying around in the garbage...":
    "[sigh] 我们还有别的选择吗？去找垃圾堆里值钱的东西吧……",
 "{sternA}Alright, {HappyA}I found this.": "{sternA}好了，{HappyA}我找到这个。",
 "{InquireA}Fiona?": "{InquireA}Fiona？",
 "{SternA}Hey Rhys, how about you? What'd {FearA}you -- [trails off] find?":
    "{SternA}嘿 瑞斯，你呢？你{FearA}找到——[trails off]什么了？",
 "{NeutralA}Over here. On the other side of the big pile of rubble.":
    "{NeutralA}在这边。那堆大瓦砾的另一侧。",
 "{WorryB}Rhys? [calling out] Rhys, where'd you go?": "{WorryB}瑞斯？[calling out] 瑞斯，你去哪儿了？",
 "{WorryA}At least that's better than what {SadA}we found.": "{WorryA}至少比{SadA}我们找到的强。",
 "[excited] {HappyA}Oooh.  {SchemeB}That does look valuable.": "[excited] {HappyA}哦哦。{SchemeB}那玩意儿看着确实值钱。",
 "RIGHT": "RIGHT",
 "{SternB}I don't think it's broken, {FearA}I think it's two halves of a... something.":
    "{SternB}我觉得它没坏，{FearA}我觉得这是某个……东西的两半。",
 "[disappointed] {SadA}Oh... {AngryA}great, a broken... thing.":
    "[disappointed] {SadA}哦……{AngryA}好啊，一个坏掉的……玩意儿。",
 "COMPUTERVOICE": "COMPUTERVOICE",
 "[filtered] Bioscan, complete. Commence interlock procedure.": "[filtered] 生物扫描完成。开始互锁程序。",
 "[filtered] Interlock esatablished. Init loadscreen.": "[filtered] 互锁已建立。初始化载入界面。",
 "{ShockA}What the ?": "{ShockA}什么鬼？",
 "{FearA}What is going on?": "{FearA}这是怎么回事？",
 "That's a Vault, baby.": "那是秘藏，宝贝。",
 "{HappyA}Cool. [beat] {SternA}I wonder what an Atlas disco ball goes for on the open market.":
    "{HappyA}酷。[beat] {SternA}不知道 Atlas 的迪斯科球在公开市场上能卖多少。",
 "[off screen] That?": "[off screen] 那个？",
 "{ShockA}It's definitely something.": "{ShockA}肯定是个东西。",
 "{SmugA}Sure, I guess.": "{SmugA}行吧，大概。",
 "{SternB}Real nice.  {AngryA}Thanks a lot.": "{SternB}真好啊。{AngryA}多谢了。",
 "{sternA}Will you two cut it out? {AngryA}I'm trying to do something here.":
    "{sternA}你们俩能不能消停点？{AngryA}我这儿忙着呢。",
 "{ShockA}Hey, that dead guy's got{InquireA} the same bracelet as you, Vaughn.":
    "{ShockA}嘿，那死人戴着{InquireA}跟你一样的手环，沃恩。",
 "{SchemeA}At least you still have both hands.": "{SchemeA}至少你两只手都还在。",
 "{ThinkA}The pieces seem to want to... {ShockA}interlock.": "{ThinkA}这两半好像想……{ShockA}互锁。",
 "{AngryA}Hey.": "{AngryA}喂。",
 "{HappyA}What?": "{HappyA}什么？",
 "{AngryA}I was supposed to -- {ThinkA}oh, nevermind.": "{AngryA}我本来该——{ThinkA}哦，算了。",
 "{doubtfulA}So then I guess we should, you know, do that.": "{doubtfulA}那我想我们该……就那个。",
 "{InquireA}I think we're about to find out.": "{InquireA}我觉得马上就能知道了。",
 "{fearA}Then what?": "{fearA}然后呢？",
 "[bigger sigh] So we can go sell them to who knows what sort of people.":
    "[bigger sigh] 然后卖给我们都不知道是什么样的人。",
 "[pregnant pause] Jackpot, muthafuh-- [gets cut off]": "[pregnant pause] 中大奖了，他妈——[gets cut off]",
 "A vault?": "一个秘藏？",
 "[pregnant pause] We are so fuh-- [gets cut off]": "[pregnant pause] 我们完蛋——[gets cut off]",
 "Everyone knows what happens when a vault is in play.": "秘藏一出现会发生什么，人人都知道。",
 "In all the universe there is nothing more beautiful, or valuable.": "整个宇宙里没有比它更美、更值钱的东西。",
 "Seriously.": "真的。",
 # —— 与 STRANGER 的复盘 ——
 "Zer0? A vault? [beat] Handsome Jack?": "Zer0？一个秘藏？[beat] 帅杰克？",
 "Okay... Which one of you wants to tell me what happened next?": "好……你们俩谁来讲讲接下来发生了什么？",
 "Hold it right there.": "打住。",
 "You do know Handsome Jack is dead, right?": "你知道帅杰克已经死了吧？",
 "Everyone does.": "谁都知道。",
 "As a doornail.": "死得透透的。",
 "'Cause I'm sure it's real rich.": "因为那肯定很精彩。",
 "Let me guess... all hell broke loose.": "我猜……一切彻底乱套了。",
 "Jack rose from the grave to haunt us.": "Jack 从坟墓里爬出来缠着我们。",
 "Vasquez happened.": "是 Vasquez。",
 "That's what.": "就是这样。",
 "This one's kinda personal. Can we just leave a few things out?": "这段有点私人。能省掉一些吗？",
 "Jack screwed us, of course.": "当然是 Jack 坑了我们。",
 "Vallory happened.": "是 瓦洛里。",
 "Rhys got all weird on me.": "瑞斯 突然变得怪怪的。",
 "It wasn't the best day of our lives.  Can we just skip over the next bit?":
    "那不是我们人生中最好的一天。能跳过下一段吗？",
 "No. We will hear the whole story.": "不行。全部经过我都要听。",
 "[pickup3] {sternA}Felix is gone. {SadA}Time to worry about ourselves. The money's incinerated, so's the key.":
    "[pickup3] {sternA}菲利克斯 没了。{SadA}该操心我们自己了。钱烧了，钥匙也是。",
 "[pickup3] {AngryA}Fake key.": "[pickup3] {AngryA}假钥匙。",
 "Loot": "战利品",
 "We'll find another way.": "我们会有别的办法。",
 "You're right, we're dead.": "你说得对，我们死定了。",
 "Just call Hyperion.": "叫 亥博龙来就行。",
 "He deserved it.": "他活该。",
 "He lost his mind.": "他疯了。",
 "It doesn't matter now.": "现在说这些没用了。",
 "I'll kill him.": "我要杀了他。",
 "He's out of his mind.": "他脑子不正常。",
 # —— 洞里拾荒 ——
 "[calling out] Rhys! Are you okay?": "[calling out] 瑞斯！你还好吗？",
 "I could use some help.": "我需要点帮忙。",
 "Stay up there.": "待在上面。",
 "What do you see?": "你看到什么了？",
 "I'm fine, I'm fine. Totally meant to do that.": "我没事，我没事。完全是我故意的。",
 "It doesn't look like there's a safe way down.": "看起来没有安全下去的路。",
 "I could use a little help down here.": "我在下面需要点帮忙。",
 "What's down there?": "下面有什么？",
 "Stay up there, and be careful. The floor is... unstable.": "待在上面，小心点。地面……不稳。",
 "Oh yeah, we kinda figured that out.": "哦对，我们大概猜到了。",
 "[calling out] Oh, man! You're totally not dead. He's gonna be alright, everybody.":
    "[calling out] 老天！你居然没死。他会没事的，各位。",
 "[calling out] Rhys!": "[calling out] 瑞斯！",
 "[calling out] What's down there?": "[calling out] 下面有什么？",
 "It's not just weapons, either. Seriously, guys, this is a big deal.": "不只是武器。说真的各位，这是件大事。",
 "[cutting him off, annoyed] Is it worth a lot of money?": "[cutting him off, annoyed] 值很多钱吗？",
 "This is amazing!": "太惊人了！",
 "[confused] How did you get down...? [cut off]": "[confused] 你是怎么下去的……？[cut off]",
 "[calling out] Uh... There's a bunch of old Atlas prototype stuff... some tech... there's like a few weapons and--":
    "[calling out] 呃……有一堆旧的 Atlas 原型货……还有些技术……大概有几把武器，还有——",
 "Sort of. Yeah. I mean, yeah, you know it's not ten million dollars worth, but, ah man, to the right people...":
    "算是吧。对。我是说，这肯定不到一千万，可老天，对识货的人来说……",
 "These models were never even released!": "这些型号根本就没发售过！",
 "All right, Sasha, let's grab what we can and get out of here. Quickly. No telling when those bandits will be back.":
    "好，萨莎，能拿多少拿多少，赶紧离开这儿。要快。那些土匪随时可能回来。",
 "We'd better do the same, Rhys.": "我们也该这么干，瑞斯。",
 "Find anything good?": "找到什么好东西了吗？",
 "It'd be better if any of it actually worked. Still worth a lot.": "要是都能用就更好了。照样很值钱。",
 "You scavengers are incredible. Anything we find, you either want to take it or destroy it.":
    "你们这些拾荒者真行。我们找到什么，你们要么想拿走，要么想毁掉。",
 "Fiona, let's hurry up and get out of here so we can finally get rid of these assholes.":
    "Fiona，快点离开这儿，好把这两个混蛋甩掉。",
 "Yeah, I get it.": "嗯，我懂。",
 "See anything good?": "看到什么好东西了吗？",
 "If I do, I'll make sure Hyperion's the first to know.": "要是我看到了，一定第一个通知 亥博龙。",
 "Thanks.": "谢谢。",
 "I was being sarcastic.": "我在讽刺。",
 "All right, I'll keep looking.": "好，我继续找。",
 "[quietly] Is this stuff really worth anything to us?": "[quietly] 这些东西对我们真能值点钱吗？",
 "[quietly] It's better than anything else I've seen since we came down here. I don't see what better options we have.":
    "[quietly] 这比我们下来之后我见过的所有东西都强。我看不出还有别的选择。",
 "[trying to be nonchalant] So... is it just me, or does that look...":
    "[trying to be nonchalant] 那个……是我多心，还是那东西看起来……",
 "Incredibly valuable? Yeah. [beat] And there's two of them so I don't have to stab you.":
    "值钱得离谱？是啊。[beat] 而且有两半，所以我不用捅你了。",
 "ATLASCOMM": "ATLASCOMM",
 "[process heavy static, almost unintelligible] RESET... IDENTIFICATION REQUIRED.":
    "[process heavy static, almost unintelligible] 重置……需要身份验证。",
 "[context: what is that thing] What is it?": "[context: what is that thing] 这是什么？",
 "No idea.": "不知道。",
 "Well, we got what we came for, so let's go, Sasha.": "我们该拿的都拿到了，走吧，萨莎。",
 "[in wonder] Is that... a map?": "[in wonder] 那是……地图？",
 "JACK": "JACK",
 "[crackled voice from before] [matter-of-factly] That, my friends, is the Gortys project.":
    "[crackled voice from before] [matter-of-factly] 那个，朋友们，就是 戈提斯 计划。",
 "[slight crackle]And now...": "[slight crackle]而现在……",
 "[calling out] [concerned]Rhys! Are you dead?": "[calling out] [concerned]瑞斯！你死了吗？",
 "[calling out] [concerned] If you're dead, say something.": "[calling out] [concerned] 你要是死了，就吭一声。",
 "Good... 'cause it doesn't look like there's a safe way down to help you. So, figure a way out of there.":
    "行……因为看起来没有安全的路下去帮你。所以自己想办法出来吧。",
 "I think... I'm okay.": "我想……我没事。",
 "[to Sasha] He's gonna be alright, everybody.": "[to Sasha] 他会没事的，各位。",
 "[calling out] Where?": "[calling out] 哪儿？",
 "Too dangerous, huh?": "太危险了，是吧？",
 "No way... [beat, awe]Haahahaha! The Atlas Silver. Ah... one of the rarest SMGs on Pandora!":
    "不会吧……[beat, awe]哈哈哈！Atlas Silver。啊……潘多拉 上最稀有的冲锋枪之一！",
 "Look, look look look look. It tells time, and it's a calculator. Just give me a math problem, just give me a math problem.":
    "你看你看你看。它还能看时间，还带计算器。给我出个算术题，给我出个算术题。",
 "[not great]Great a wa- [whoa!]Whoa! Hey! A retro Atlasio! I thought these things were just a rumor.":
    "[not great]好家伙——[whoa!]哇！嘿！一台复古 Atlasio！我还以为这东西只是传言。",
 "[who cares] Cool.": "[who cares] 酷。",
 "[reluctant, looking around] It's the last one... it's only right for us both to reveal it... that's the best part.":
    "[reluctant, looking around] 这是最后一件……该由我们两个一起打开才合适……这才是最棒的部分。",
 "Yeah, I was kinda hoping you'd say that.": "嗯，我还挺希望你会这么说。",
 "Would you like to do the honors?": "要由你来开吗？",
 "Alright... big money...": "好吧……一大笔钱……",
 "That's a bonus... I call the bigger half...": "那是额外奖励……大的那半归我……",
 "[to Vaughn] Hey, Vaughn can you see if there's a crowbar lying around? We're gonna have to pry these apart before we-":
    "[to Vaughn] 嘿 沃恩，看看附近有没有撬棍？我们得把这两半撬开才能——",
 "[clear as day]You're gonna take me to it.": "[clear as day]你要带我去那儿。",
 "Core": "核心",
 "Big Red Button": "大红按钮",
 "It doesn't sound like you are being ripped apart by Skags, so that's good.":
    "听起来你还没被异犬撕碎，那挺好。",
 "There's nothing down there, let's just go.": "下面什么都没有，走吧。",
 "Rhys? You're awfully quiet down there...": "瑞斯？你在下面安静得可疑……",
 "Old Atlas Tech": "旧 Atlas 科技",
 "Old Atlas Stuff": "旧 Atlas 杂物",
 "Atlas Weapon Parts": "Atlas 武器零件",
 "Yeah... that sounds good.": "嗯……听起来不错。",
 "This is so dissapointing, I thought you had more ball than this.": "太让人失望了，我以为你比这更有种。",
 "Yeah, you sure about that, dum-dum?": "是吗，你确定？笨蛋。",
 "Go with that.": "就这么办。",
 "Follow your heart.": "跟着你的心走。",
 "[alt1] [making fun] Is that... a map? I--I--I don't know, it's so confusing.":
    "[alt1] [making fun] 那是……地图？我——我——我不知道，太让人困惑了。",
 "[alt1][off \"It's some kind of map\"] So, she's the brains of the outfit.":
    "[alt1][off 「这是某种地图」] 所以，她才是这伙人的脑子。",
 "[alt3]This, ladies and gentlemen, is the Gortys Project... and it's gonna lead us to a vault...":
    "[alt3]女士们先生们，这就是 戈提斯 计划……它会带我们找到秘藏……",
 "[alt1]Now that is not just a map. My simple, simple friends. That, is the Gortys Project.":
    "[alt1]那可不只是地图。我单纯的朋友们。那是 戈提斯 计划。",
 "You might not believe in yourself...": "你可能不相信自己……",
 "Hey listen, I want you to know that right now...": "嘿听着，我想让你现在就明白……",
 "[alt3]I emphasized us right there cause, uh, you are gonna take me to it...":
    "[alt3]我特意强调「我们」，因为，呃，你要带我去那儿……",
 "[alt3]and then I'll  probably kill you. Surprise.": "[alt3]然后我大概会杀了你。惊喜吧。",
 "[alt1]And you are gonna take me to it...": "[alt1]而你要带我去那儿……",
 "[alt1][beat, matter of fact] And then I'll probably kill you.": "[alt1][beat, matter of fact] 然后我大概会杀了你。",
 "Who cares.": "谁在乎。",
 "Neat.": "不错。",
 "So it's vintage?": "所以这是老古董？",
 "Vintage... I guess.": "老古董……大概吧。",
 # —— 长文本 ——
 "[processed: phone] Nice work, sugar. Now...whenever convenient, simply return Bossanova's ECHO device to me to procure one of my longest, hardest most treasured rocket launchers.":
    "[processed: phone] 干得漂亮，甜心。现在……什么时候方便，把 Bossanova 的 ECHO 设备还给我，就能拿到我最长、最硬、最宝贝的火箭筒之一。",
 "[tired] I'm gonna guess by all of your shining faces that there isn't a briefcase full of money sitting up there waiting for us to climb out and get it?":
    "[tired] 看你们这一张张明媚的脸，我猜上面并没有一个装满钱的手提箱等着我们爬出去拿？",
 "{AngryC}The idiot, he just... {ShockA}he lost his mind, that's the... {SternB}that's the only way I can describe what that {AngryA}damned guy did.":
    "{AngryC}那个白痴，他就是……{ShockA}他疯了，这就是……{SternB}那个{AngryA}该死的家伙干的事，我只能这么形容。",
 "Listen, Atlas gear goes for a *lot* of money and Rhys here is an Atlas knowledge champ, so... I mean, if we scrounge what we can find...we might be able to pay our debt.":
    "听着，Atlas 的装备能卖*大*价钱，而 瑞斯 是 Atlas 知识冠军，所以……我是说，要是我们把能找到的都翻出来……也许就能还上债。",
 "{SternA}According to my estimates, we'll have to loot all day, every day for roughly [beat as he faux-calculates] {AngryC}*forever* {AngryA}in order to make that kind of money.":
    "{SternA}按我的估算，我们得每天从早拾荒到晚，大概持续[beat as he faux-calculates] {AngryC}*永远*，{AngryA}才可能赚到那么多钱。",
 "Anyway, there's no point in worrying about Felix now.  The money's incinerated, so's the fake vault key, and we don't even have our forger anymore to help set-up a new scam.":
    "反正现在担心 菲利克斯 也没意义了。钱烧了，假秘藏钥匙也烧了，我们连伪造师都没了，没法再设计新的骗局。",
 "{HappyA}Alright, that's worth about a hundred bucks. And I found these{SternA} [holds up more components] so now we only need  -- [defeated] {SmugA}well, let's just round it off to two million more dollars.":
    "{HappyA}好，这大概值一百块。我还找到这些{SternA} [holds up more components] 所以现在我们还差——[defeated] {SmugA}算了，就当还差两百万吧。",
 "{SternA}And we can't exactly call-in Hyperion reinforcments when we've just lost a {SadA}million dollars of their {SadB}money. [beat] {SmugA}It's against the rules.":
    "{SternA}我们刚弄丢了他们{SadA}一百万美元，{SadB}可没法叫 亥博龙的增援来。[beat] {SmugA}这不合规矩。",
 "Atlas tech in mint condition like this is worth a hell of a lot to collectors. Some Hyperion execs buy it just to put on their trophy shelves and gloat. And unreleased prototypes at that. I mean, who knows what this is worth?!":
    "这种品相完好的 Atlas 科技对收藏家来说可值大钱了。有些 亥博龙高管买来就为了摆在奖杯柜里炫耀。更别说这还是没发售过的原型。这谁知道值多少啊？！",
 "[crackled voice from before, clearing a bit before the end] Before we beat the hell out of 'em, Atlas found a Vault no human being had ever seen before.":
    "[crackled voice from before, clearing a bit before the end] 在我们把他们揍得满地找牙之前，Atlas 发现了一个从没有人类见过的秘藏。",
 "[alt2][Forboding] And you, lucky bastards, are gonna take me to it... or guess what... you... [breaks out of character] Sorry, I'm sorry, I'm sorry. I was gonna say \"Die\" right there but you know what? That just seems so cliche. Doesn't it? I mean, don't get me wrong, I am totally going to kill you, but you already know that so, I don't know... let's just get on with it.":
    "[alt2][Forboding] 而你们这些走运的混蛋，要带我去那儿……不然你猜怎样……你们……[breaks out of character] 抱歉，对不起，对不起。我刚差点要说「死」，可你知道吗？那也太老套了，对吧？别误会，我确实要杀了你们，可你们本来也知道，所以……算了，我们继续吧。",
 "but I believe in you... I- [laughs, breaks] I almost... I almost did it, I almost got it out of my face there but I can't do it 'cause, no, I can't do it 'cause you're stupid.":
    "但我相信你……我——[laughs, breaks] 我差点……我差点就说出来了，差点就从我这张脸里挤出来了，可我说不出口，因为……不，我说不出口，因为你太蠢了。",
})

T["[weak] {HappyA}Never better.{WorryC}"] = "[weak] {HappyA}从没这么好过。{WorryC}"
T["{WorryB}Rhys! Are you okay!"] = "{WorryB}Rhys！你没事吧！"
T["No, no, no, listen, Atlas gear goes for a *lot* of money, so... I mean, if we scrounge what we can find..."] = "不不不，听着，Atlas 的装备能卖*大*价钱，所以……我是说，要是我们把能找到的都翻出来……"
T["What are you doing?"] = "你在干什么？"
T["I meant to do that."] = "我是故意的。"
T["STRANGER"] = "STRANGER"
