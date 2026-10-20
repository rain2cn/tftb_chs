# 批次3-13：第1章 env_03_prosperityjunction_rhys_opening（Rhys 线开场：降落 Pandora、黑装载机器人、进城问路）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g'), ('ep1_env12_zh.py', '_h'), ('ep1_env01_zh.py', '_i'),
               ('ep1_env09_zh.py', '_j'), ('ep1_env06_zh.py', '_k'), ('ep1_env05_zh.py', '_l')):
    T.update(_load(_f, _n))

T.update({
 "VAUGHN": "VAUGHN",
 "RHYS": "RHYS",
 "YVETTE": "YVETTE",
 "LOADER": "LOADER",
 "VAGRANT": "VAGRANT",
 "RUDIGER": "RUDIGER",
 "TOWNSMAN": "TOWNSMAN",
 "BANDIT": "BANDIT",
 "LOADERBOT": "LOADERBOT",
 "ECHOCOMM": "ECHOCOMM",
 "PROSPERITYVOICE": "PROSPERITYVOICE",
 "QUESTIONS": "QUESTIONS",
 "NWRI": "NWRI",
 "<<ID": "<<ID",
 "361829064>>": "361829064>>",
 "{105D9250-33B4-433A-98C5-D4A314219C96}>>": "{105D9250-33B4-433A-98C5-D4A314219C96}>>",
})

# —— 开场：降落 Pandora ——
T.update({
 "[frustrated with the key to the handcuff lock, under breath] C'mon, you stupid piece of-":
    "[frustrated with the key to the handcuff lock, under breath] 快点，你这愚蠢的破——",
 "[v-o] It all started about a year ago in a little slice of nothing called Prosperity Junction.  I'd come down from the home office to get rich.  My partner was nervous.":
    "[v-o] 一切都始于大约一年前，在一个叫繁荣枢纽的鸟不拉屎的地方。我从总部下来发财。我的搭档很紧张。",
 "[ill] Here!  I gotta- [fights back vomit].": "[ill] 给！我得——[fights back vomit]。",
 "[distraught and ill]Rhys!": "[distraught and ill]瑞斯！",
 "[v-o] Oh, god... [hurling noises]": "[v-o] 哦，天哪……[hurling noises]",
 "You can do that, right?": "你能做到，对吧？",
 "Your assisstant?  How can you tell?": "你的助理？你怎么看出来的？",
 "[v-o] The bad news is, I wasn't able to get a copy of its access codes from IT, so you'll have to hack it open.  Have fun on your mysterious Pandoran adventure!":
    "[v-o] 坏消息是，我没能从 IT 部门拿到它的访问码副本，所以你得自己黑开它。祝你在神秘的 潘多拉 冒险中玩得开心！",
 "In my sleep.": "闭着眼都行。",
 "[v-o] The good news is, I was able to sneak this Loader down to your coordinates from Hyperion HQ.":
    "[v-o] 好消息是，我从 亥博龙总部偷偷把这台装载机送到了你的坐标点。",
 "[v-o]Hello, Boss.  I've got good news and bad news.":
    "[v-o]你好，老板。我有好消息和坏消息。",
 "Who do you think sent the LoaderBot?": "你觉得是谁派来的装载机器人？",
 "Yeah, it's from Yvette.": "是啊，是 Yvette 送来的。",
 "An Echo Recording?": "一段 ECHO 录音？",
 "I'll have to cut the hinges off.   The cutter's in the car.":
    "我得把铰链切掉。切割器在车里。",
 "Is that bad?": "那算坏消息吗？",
 "Without a live interface I can't hack it open... [frustrated] Meh.":
    "没有实时接口我就黑不开它……[frustrated] 啧。",
 "The interface won't open.  Something must've jiggled loose in the fall...":
    "接口打不开。肯定是坠落时震松了什么……",
 "You gonna keep staring at it, or are you gonna cut those wires?":
    "你是要一直盯着它，还是去把那些线切了？",
 "I thought you said you were gonna get a laser cutter out of the trunk?":
    "你不是说要去后备箱拿激光切割器吗？",
 "Yeah, that's great.  Can you get to work hacking open the robot?":
    "是啊，太好了。你能开始动手把机器人黑开了吗？",
 "See that?  That's what I call a clean soldering job.":
    "看到了吗？这才叫干净的焊接。",
 "And you wouldn't like me when I'm queasy.": "而我犯恶心的时候可不好惹。",
 "Stop admiring your handiwork and get hacking already!":
    "别欣赏你的手艺了，赶紧开始黑！",
 "This isn't hardware, this is grade-school electricity.":
    "这不算硬件，这是小学级别的电路。",
 "I thought you were more of a software guy.": "我以为你更偏软件。",
 "All right, stand back and let me work my magic.": "好，退后，让我施展魔法。",
 "I don't believe in magic.": "我不信魔法。",
 "Let's try that again.": "我们再试一次。",
 "This'll just take a second.": "只要一秒钟。",
 "That's what she said.": "她也是这么说的。",
 "[straining] Prying...open...the...interface!": "[straining] 撬……开……这个……接口！",
 "[giving up exhale]": "[giving up exhale]",
 "When are you going to learn that that robot arm of yours is built for hacking, not for feats of strength?":
    "你什么时候才能明白，你那条机器人手臂是用来黑客的，不是用来逞力气的？",
 "[annoyed sound]": "[annoyed sound]",
 "[straining noise]": "[straining noise]",
 "[whistling]": "[whistling]",
 "Yeah, yeah, I know... we \"borrowed\" it.   But we're gonna need every penny of it to buy this so-called alien artifact before those s.o.b's in forensics notice it's missing.":
    "是啊是啊，我知道……我们是“借”来的。但我们要用它的每一分钱去买这件所谓的外星物品，必须赶在取证部那帮狗东西发现钱不见之前。",
 "Vaughn...": "沃恩……",
 "'Cause when that happens we're dead men, y'know?": "因为一旦那样，我们就死定了，懂吗？",
 "You get that, right?": "你明白的吧？",
 "I mean, you saw what they did to that poor guy in marketing last month....":
    "我是说，你看到上个月他们对市场部那可怜虫做了什么……",
 "[pickup1] They'll decorate the office party with my innards.":
    "[pickup1] 他们会拿我的内脏去装点办公室派对。",
 "Be that as it may, when we drag this Eridian artifact back to Helios, Hyperion's gonna forget all about the money we \"borrowed\", and promptly promote us to God!":
    "就算如此，等我们把这件伊瑞德物品拖回 赫利俄斯，亥博龙会彻底忘掉我们“借”的那笔钱，然后把我们提拔成神！",
 "Yeah.  About the \"dragging.\"": "是啊。关于“拖”这个字。",
 "This artifact thing is supposed to, weigh, like,  a ton, right?":
    "这件物品据说重达一吨，对吧？",
 "So, uh, how're we getting it back to the car?": "那，呃，我们怎么把它弄回车上？",
 "[counting down with the display on his arm, which he's shutting off]\t3..2..1":
    "[counting down with the display on his arm, which he's shutting off]\t3……2……1",
 "Agggh!": "啊——！",
 "THAT'S how we're getting it back to the car.": "我们就是这么把它弄回车上的。",
 "A Loader Bot?  Whose butt did you kiss to get access to one of those?":
    "装载机器人？你亲了谁的屁股才弄到一台这种玩意儿？",
 "Um, shouldn't it be running its unbox routine?": "呃，它不是应该跑开箱程序吗？",
 "[concerned] Yeah.": "[concerned] 是啊。",
 "I told you this would be risky.": "我跟你说过这会有风险。",
 "How many times do I have to tell you?  If you want to ride the Rhys Train to the top of Hyperion, you're gonna have to take some risks.":
    "我要跟你说多少遍？你想搭 瑞斯 号列车直达 亥博龙顶峰，就得冒点风险。",
 "Did you just say \"Ride the Rhys Train?\"  This isn't a train you've got us on, it's a rocket.":
    "你刚是说“搭 瑞斯 号列车”？你让我们上的不是列车，是火箭。",
 "Don't worry, Hyperion's gonna love this.": "别担心，亥博龙会喜欢这个的。",
 "You worry too much.  By this time tomorrow, we'll be Hyperion's Golden Boys.":
    "你太爱担心了。明天这个时候，我们就是 亥博龙的黄金男孩。",
 "I just wanna get rich.  You're the one with the Golden Boy issues.":
    "我只想发财。有“黄金男孩”情结的是你。",
 "You're gonna be great.": "你会很棒的。",
 "{SmugA}{alias 361828420} [bucking him up] {SLyB}Hey, pal, you're gonna be great.  I wouldn't have brought you in if I didn't think you could handle a little adventure.":
    "{SmugA}{alias 361828420} [bucking him up] {SLyB}嘿，哥们，你会很棒的。要是我觉得你应付不了一点冒险，我就不会拉你进来了。",
 "[sarcastic] You brought me in because I was the only one who had access to the company's golden parachute accounts.":
    "[sarcastic] 你拉我进来是因为我是唯一能接触到公司高管离职金账户的人。",
 "Y'know, in most friendships it's customary to reassure a buddy before embarking on a dangerous a adventure.":
    "你知道，在大多数友谊里，启程冒险前安抚一下朋友是惯例。",
 "{SlyB}[sighs]But this isn't most friendships, is it?":
    "{SlyB}[sighs]但这不是大多数友谊，对吧？",
 "Is that the soldering iron?": "那是烙铁吗？",
 "Laser cutter.  You don't know the difference?": "激光切割器。你分不出来？",
 "I'm an accountant, Rhys.  I'm lucky I can SPELL \"soldering iron.\"":
    "我是会计，瑞斯。我能*拼出*“烙铁”这个词就算走运了。",
 "There's an 'L' in the middle.": "中间有个“L”。",
 "You're kidding.": "你开玩笑吧。",
 "Um, you gonna pick that up or what?": "呃，你是打算捡起来还是怎么着？",
 "You sure you should be poking the LoaderBot with that?":
    "你确定该拿那玩意儿去戳装载机器人？",
 "It'll be a snap.": "小菜一碟。",
 "[under breath] Of my neck, when it malfunctions and kills us all.":
    "[under breath] 等我脖子断掉的时候——它一故障就把我们全杀了。",
 "[various hurling noises]": "[various hurling noises]",
 "[more hurling noises]": "[more hurling noises]",
 "[wrapping up hurling noises]": "[wrapping up hurling noises]",
 "Thanks for the save.  [sarcastic]It'd be a shame if all our stolen money blew away.":
    "谢谢你救场。[sarcastic]要是我们偷来的钱全被吹走，那可就太可惜了。",
 "[sarcastic, but non-judgemenatal] Stealing money you've already stolen.  I'm not sure if that's ironic or pathological.":
    "[sarcastic, but non-judgemenatal] 偷你已经偷来的钱。我不确定这算讽刺还是病态。",
 "[distressed] Gagh!": "[distressed] 嘎！",
 "[peeved]Is it too much to ask that you DON'T let the stolen money blow away?":
    "[peeved]求你*别*让偷来的钱被吹走，这要求过分吗？",
 "[startled]  Waugh!": "[startled]  哇！",
 "See?  One Mach 3 PWR Loader, with multi-tonnage nullfield lifting arms, ready to rumble.":
    "看吧？一台 3 马赫 PWR 装载机，配多吨级零场起重臂，准备开干。",
 "Great, you found the on switch.  But will it follow us?":
    "好极了，你找到开机键了。但它会跟着我们走吗？",
 "[Dude, why are you even asking] Please.": "[Dude, why are you even asking] 拜托。",
 "Funny.": "好笑。",
 "Let's go buy an artifact.": "我们去买件物品吧。",
 "[vomiting]": "[vomiting]",
 "[vomiting] Oh god, here it comes again! [hurls]":
    "[vomiting] 哦天哪，又来了！[hurls]",
 "All done-[vomits]": "搞定了——[vomits]",
 "[vomiting with dry heaves]": "[vomiting with dry heaves]",
 "[yet more vomting]": "[yet more vomting]",
 "[moaning between vomiting][more vomiting]": "[moaning between vomiting][more vomiting]",
 "[coughining bbetween vomiting][vomiting]": "[coughining bbetween vomiting][vomiting]",
 "I always get squicked out when you plug in like that.":
    "你那样插进去的时候我总是觉得瘆得慌。",
 "Plugging in is what Hyperion pays me for, pal.":
    "插进去就是 亥博龙付我钱的原因，哥们。",
 "Besides,  plugging in is what found us this Eridian artifact.":
    "再说，正是靠插进去我们才发现了这件伊瑞德物品。",
 "Yeah, but it's still a little weird.": "是啊，但还是有点怪。",
 "I don't know why it weirds you out.  You're an accountant... you use computers all the time.":
    "我不知道你为什么会觉得怪。你是会计……你成天用电脑。",
 "That's right, I USE them.  I don't crawl up inside 'em.  I have boundaries with my tools.":
    "没错，我是*用*它们。我不会爬进去。我跟我的工具有界限。",
 "Speaking of accounting-": "说到会计——",
 "Don't worry, the firewalls are fine.": "别担心，防火墙没问题。",
 "I'm just saying... I'm technically the guy who's resposnible for the Widows and Orphans Account... so when that million dollars turns up missing.":
    "我只是说……严格来说我是负责孤儿寡母账户的人……所以当那一百万不见了的时候。",
 "Don't worry.  No one's gonna find out until we're back.":
    "别担心。我们回去之前没人会发现。",
 "Soooo, what's going on betwen you and Yvette, anyway?":
    "那么……你和 Yvette 之间到底怎么回事？",
 "'Cause not to many assistants would go out of their way to steal a company, Loader Bot, know what I mean?":
    "因为没几个助理会特意去偷一台公司装载机器人，懂我意思吗？",
 "Nothing's going on with Yvette, Vaughn.": "我跟 Yvette 没什么，沃恩。",
 "Are you sure?  'Cause I think she's got a serious case of boss-crush going on.":
    "你确定？因为我觉得她有严重的“迷上司”症状。",
 "There's an old saying Vaughn...here, let me personalize it for you: \"You don't projectile vomit where you eat.\"":
    "有句老话，沃恩……来，我给你个性化一下：“别在你吃饭的地方喷吐。”",
 "I know what you mean about trouble.": "我知道你说的麻烦是什么意思。",
 "I once asked out Alexis over in Sales, and she had me fill out ten forms, swab my cheek, and submit a stool sample.":
    "我有一次约市场部的 Alexis，她让我填十份表、做口腔拭子，还交了一份粪便样本。",
 "[epiphany] Of course, now that I think about it, maybe she just didn't want to go out with me...":
    "[epiphany] 当然，现在想想，也许她只是不想跟我约会……",
 "{NeutralB}Is it me, or is everyone here {SmugC}kind of scared of us?":
    "{NeutralB}是我多心，还是这儿所有人都{SmugC}有点怕我们？",
 "{SmugA}Or angry.  {SmugB}Or maybe agoraphobic.": "{SmugA}或者生气。{SmugB}或者也许患有广场恐惧症。",
 "{SmugC}It's kind of hard to tell behind all the slamming doors.":
    "{SmugC}在那么大的摔门声后面很难分辨。",
 "Y'know, It's not too late to do this through regular channels.":
    "你知道，现在走正规渠道还不算太晚。",
 "I mean, I get that you're still pissed off about that Vasquez thing, but you've gotta, I dunno, sleep with his wife and move on.":
    "我是说，我明白你还在为 Vasquez 那事生气，但你得，我不知道，睡他老婆然后翻篇。",
 "Why don't you just send a note over to Vault Acquistions...":
    "你干嘛不干脆给秘藏收购部发个条子……",
 "I bet you'd get a nice bonus out of it.": "我打赌你还能拿笔不错的奖金。",
 "\"Hey Chet.  Was doing some routine data mining today when I got a lead on a priceless alilen artifact.  By the way, how're the kids?\"":
    "“嘿 Chet。今天做例行数据挖掘时，我摸到了一件无价外星物品的线索。顺便问一句，孩子们好吗？”",
 "They'd probably even give you your own parking space.":
    "他们说不定还会给你配个专属车位。",
 "We're here.": "我们到了。",
 "You sure?": "你确定？",
 "The arm doesn't lie.": "这条手臂不会说谎。",
 "So, we knock on the door, show him the money, buy the Artifact, and go back to the moonbase, right?":
    "所以，我们敲门、给他看钱、买下物品，然后回月球基地，对吧？",
 "Right.  And it's not a moonbase.": "对。而且那不是月球基地。",
 "In, out, and no one gets hurt.": "进去、出来，没人受伤。",
 "'Cause I'm just in this for the money.": "因为我纯粹为了钱。",
 "And maybe the ladies.": "也许还有姑娘们。",
 "But definitely the money.": "但肯定是为了钱。",
 "Can't get to the top without hurting someone.": "不想伤人就爬不到顶。",
 "No one gets to the top without hurting SOMEONE, Vaughn.":
    "没人能不伤到*某个*人就爬到顶端，沃恩。",
 "That's a Handsome Jack quote isn't it? [louder] You know he's dead, right?":
    "那是帅杰克的名言吧？[louder] 你知道他死了吧？",
 "Don't worry, it'll be fine.": "别担心，会没事的。",
 "Trust me Vaughn, the only thing that's gonna get hurt are everyone's necks... when they look up at us... [struggles to complete metaphor] getting promoted... over their heads.":
    "相信我 沃恩，唯一会受伤的就是所有人的脖子……当他们仰头看我们……[struggles to complete metaphor] 一飞冲天……越过他们的头顶。",
 "That one kind of got away from you there, didn't it?":
    "那个比喻有点跑偏了，对吧？",
 "[annoyed] Just watch the robot.": "[annoyed] 看着机器人就行。",
 "[louder] I'm feeling very reassured now!": "[louder] 我现在感到非常安心！",
 "I don't want any violence either.": "我也不想要任何暴力。",
 "Trust me, Vaughn.  The last thing I want is some sort of cliched Pandoran bloodbath.  Now watch the robot.":
    "相信我，沃恩。我最不想要的就是那种老套的 潘多拉 血洗场面。现在看着机器人。",
 "[to the robot] [nervous] Pandoran bloodbaths...":
    "[to the robot] [nervous] 潘多拉 血洗场面……",
 "[pointedly]  No one gets hurt, right?": "[pointedly]  没人会受伤，对吧？",
 "[louder] That wasn't the reassurance I was looking for!":
    "[louder] 那不是我想听到的安慰！",
 "But then YOU wouldn't get rich.": "但那样*你*就发不了财。",
 "Sure, I COULD just take my [sarcastic] way cool bonus while the guys in Vault Acquistions get all the glory , but where would that leave YOU?  Stuck staring at numbers for the rest of your life?":
    "当然，我大可以拿着我[ sarcastic]超酷的奖金，让秘藏收购部那帮人拿走所有荣耀，但那样*你*会怎样？余生都在盯着数字发呆？",
 "Hey, I LOVE staring at numbers... I just wanna stare at some bigger ones.":
    "嘿，我*爱*盯数字……我只是想盯一些更大的。",
 "Don't wuss out.": "别怂。",
 "You can't wuss out now, man.  Corporate immortality is just a few steps down the street.":
    "你现在不能怂，老兄。企业不朽就在街那头几步路。",
 "Y'know who else is immortal?  Ghosts.": "你知道还有谁不朽吗？鬼。",
 "Together we can do this.": "我们一起能做到。",
 "Don't worry.  As long as we've got each other's backs, we'll be fine.":
    "别担心。只要我们互相照应，就会没事。",
 "I always worry when you start getting genuine on me, Rhys.":
    "你一对我掏心掏肺我就开始担心，瑞斯。",
 "Orrrr, we could silently stroll headlong into danger without talking it over one last time.":
    "或者……我们可以一声不吭地一头扎进危险里，不做最后一次商量。",
 "You BETTER be scared of Hyperion!": "你们*最好*怕 亥博龙！",
 "[loudly]  Yeah, you better be scared!  Hyperion's in town, baby!":
    "[loudly]  是啊，你们最好怕！亥博龙来了，宝贝！",
 "[a little freaked] Are you crazy!?": "[a little freaked] 你疯了吗！？",
 "Hyperion operatives on official business don't skulk, pal.":
    "执行公务的 亥博龙特工不鬼鬼祟祟，哥们。",
 "But we're not here on official business.": "但我们不是来执行公务的。",
 "They don't know that.": "他们不知道。",
 "Can you blame them?": "你能怪他们吗？",
 "You can't really blame 'em.  After all that anti-Hyperion propaganda, they probably think we're here to wipe 'em out with our orbital death ray.":
    "你还真不能怪他们。听了那么多反 亥博龙宣传，他们大概以为我们是来用轨道死光把他们清掉的。",
 "Do we still have one of those?  I could swear they all got sold off in the last re-org.":
    "我们还有那种东西吗？我发誓上次重组时它们全被卖掉了。",
 "Ignore the locals.": "别理当地人。",
 "The locals aren't important.  Just pretend they're all in their underwear and focus on the job.":
    "当地人不重要。就当他们都只穿着内裤，专注干活。",
 "Are you trying to make me throw up again?": "你是想让我再吐一次吗？",
 "Guess that's what you get when a couple of Hyperion employees power walk down main street with a killer robot.":
    "两个 亥博龙员工带着一台杀人机器人快步走过主街，会这样也是活该。",
 "How'd you requisition this beast, anyway?": "你到底是怎么申请到这头猛兽的？",
 "Yvette.": "Yvette。",
 "A Loader Bot, a company vehicle... why isn't SHE in on this deal?":
    "一台装载机器人、一辆公司车……她怎么不参与这笔交易？",
 "The less people that know about this, the better.": "知道这事的人越少越好。",
 "Your assistant?  Man, she's good.": "你的助理？老兄，她真厉害。",
 "Tell me about it.  In a few years, we'll all be working for her.":
    "还用你说。过几年我们都得给她打工。",
 "We didn't \"steal it,\" Vaughn-": "我们不是“偷”它，沃恩——",
 "Just in case things get hairy.": "以防事情变得棘手。",
 "D'oh! [not Homer]  I almost forgot!  Here.": "哎呀！[not Homer]  我差点忘了！给。",
 "A Hyperion stun rod?": "一根 亥博龙电击棒？",
 "Dance": "跳舞",
 "Voice Test": "语音测试",
 "Anti-Theft System": "防盗系统",
 "System Controls": "系统控制",
 "Follow User": "跟随用户",
 "Walk Mode": "行走模式",
 "Motor Control": "电机控制",
 "Activates the System Controls of the Loader Bot, allowing the user full control.":
    "激活装载机器人的系统控制，让用户获得完全控制权。",
 "Suplies power to the LoaderBot.": "为装载机器人供电。",
 "Commands the Loader bot to dance.": "命令装载机器人跳舞。",
 "Activates the motor of the Loader Bot.": "启动装载机器人的电机。",
 "Commands the Loader Bot to walk.": "命令装载机器人行走。",
 "Tests the voice capabilities of the Loader Bot.": "测试装载机器人的语音功能。",
 "Sets the Loader Bot to follow the user.": "让装载机器人跟随用户。",
 "Prevents the Loader Bot from making any unauthorized actions.":
    "阻止装载机器人做出任何未经授权的动作。",
 "Rhys' car": "瑞斯 的车",
 "Open trunk": "打开后备箱",
 "Briefcase": "手提箱",
 "Command": "指令",
 "Close Briefcase": "合上手提箱",
 "Skim Some Money": "私吞一些钱",
 "Take Money": "拿走钱",
 "Unrecognised user. What do you think you're doing?":
    "无法识别的用户。你以为你在干什么？",
 "Do you even know what you are doing?": "你到底知不知道你在干什么？",
 "Be careful in there.": "在里面小心点。",
 "I'm not comfortable with this.": "我对这个不太放心。",
 "Knock it off already.": "别闹了。",
 "I don't even know what you are trying to accomplish.": "我甚至不知道你想达成什么。",
 "[annoyed] Just give me a second here.": "[annoyed] 给我一秒钟。",
 "Impressed?": "佩服吗？",
 "[Asked if he's impressed] Hardly. This coding is a hack job. Probably Willcocks's work.":
    "[Asked if he's impressed] 谈不上。这代码写得乱七八糟。大概是 Willcocks 的活儿。",
 "Take a picture, it will last longer.": "拍张照片吧，能留得久一点。",
 "That's my cousin.": "那是我表弟。",
 "[irritated] What are you, comment-bot?": "[irritated] 你是什么，注释机器人吗？",
 "Linking...": "正在连接……",
 "[talking loudly over noise]Turn it off!": "[talking loudly over noise]关掉它！",
 "Alarm protocol activated.": "警报协议已激活。",
 "I do! [trying to come up with a lie, talking loudly over noise] I'm just checking... uh... I was trying to...":
    "我知道！[trying to come up with a lie, talking loudly over noise] 我只是在检查……呃……我本来想……",
 "[hearing an alarm go off, talking loudly] What the hell, man!? I thought you knew what you were doing!?":
    "[hearing an alarm go off, talking loudly] 搞什么，老兄！？我以为你知道自己在干什么！？",
 "Motor Controls activated.": "电机控制已激活。",
 "Engaging Walk Mode.": "启动行走模式。",
 "[excited, accomplishing a goal] Yes! So far so good.":
    "[excited, accomplishing a goal] 太好了！到目前为止一切顺利。",
 "[slightly exasperated] Just... warn me next time you're going to do that!":
    "[slightly exasperated] 就……下次你要那么做之前先警告我一声！",
 "Low power.": "电力不足。",
 "Not enough power. Unlink a node first.": "电力不足。请先断开一个节点。",
 "Are you listening?  I don't have enough power jerk.": "你在听吗？我电力不够，蠢货。",
 "Encrypted Node.": "加密节点。",
 "No kidding. I'll have to crack it.": "还用你说。我得破解它。",
 "That node is protected.": "该节点受保护。",
 "[emphasis on UN] So, I'll un-protect it.": "[emphasis on UN] 那我就*解除*它的保护。",
 "That node is protected, dummy.": "那个节点受保护，笨蛋。",
 "Node De-Linked. Take that.": "节点已断开。接招吧。",
 "De-linking Node. In your face.": "正在断开节点。当面打脸。",
 "Node de-linked. Ha ha ha.": "节点已断开。哈哈哈。",
 "Please don't make me dance. I'm shy.": "请别让我跳舞。我害羞。",
 "You suck.": "你真差劲。",
 "Stop tormenting me.": "别折磨我了。",
 "If I had a face, I'd be scowling so hard right now.":
    "如果我有脸，我现在肯定皱着眉头皱得很厉害。",
 "Node Locked. Try again later.": "节点已锁定。请稍后再试。",
 "That node is locked. You can't access it yet.": "那个节点已锁定。你还不能访问它。",
 "You aren't very good at this. That node is inaccessible right now.":
    "你这方面不太行。那个节点现在无法访问。",
 "Higher System Controls accessed. Hey, wait. Get out of there.":
    "已访问高级系统控制。嘿，等等。从那儿出去。",
 "Higher System Controls accessed. Seriously, stay out.":
    "已访问高级系统控制。说真的，别动。",
 "Executing voice test. Test, test, is this thing on?":
    "正在执行语音测试。测试，测试，这玩意儿开着吗？",
 "Executing voice test.": "正在执行语音测试。",
 "[doing a voice check] Jackdaws love my big sphinx of quartz. The quick brown fox jumps over the lazy dog. The five boxing wizards jump quickly. Wafting zephyrs quickly vexed Jumbo. Brawny gods just flocked up to quiz and vex him.":
    "[doing a voice check] （语音测试句）寒鸦爱我那块巨大的石英狮身人面像。敏捷的棕色狐狸跃过懒狗。五个拳击巫师跳得飞快。飘荡的微风迅速惹恼了 Jumbo。健壮的神祇刚聚起来考问他、烦扰他。",
 "Security protocols bypassed. Quit it.": "安全协议已绕过。别闹了。",
 "Node decrypted. That was encrypted for a reason.": "节点已解密。它加密是有原因的。",
 "That was my favorite secure node and you ruined it.": "那是我最喜欢的安全节点，被你毁了。",
 "Engaging Manual Control. Wait, what? OOoooooooohhhh nooooooo [warps into digital noise and fades off as Rhys takes control]":
    "启动手动控制。等等，什么？哦哦哦哦哦哦不不不不[warps into digital noise and fades off as Rhys takes control]",
 "[irritated] Not you best effort there, Captain Hacker.":
    "[irritated] 这可不是你的最好水平，黑客队长。",
 "Damnit.": "该死。",
 "[frustrated] I can get this. I just... need a breath.":
    "[frustrated] 我能搞定。我只是……需要喘口气。",
 "Get all your breathing in now, before Hyperionkills us.":
    "现在就一次喘够，趁 亥博龙还没杀了我们。",
 "[frustrated] Ugh.": "[frustrated] 呃。",
 "Any day now...": "随便哪天都行……",
 "{body-CarryCase}[whistles to self]": "{body-CarryCase}[whistles to self]",
 "Have you seen my laser cutter?": "你看到我的激光切割器了吗？",
 "{body-CarryCase}I thought you said it was in the trunk.":
    "{body-CarryCase}我以为你说在后备箱里。",
 "Uh huh. How about you get that panel open first?": "嗯哼。不如你先把那块面板打开？",
 "[Snapping out of it] What? No. [Wistful] Just thinking about how rich we're going to be.":
    "[Snapping out of it] 什么？不。[Wistful] 只是在想我们会多有钱。",
 "{body-CarryCase}Something wrong with the laser cutter?":
    "{body-CarryCase}激光切割器有问题？",
 "Don't look at me - I can't hack that thing.": "别看我——我黑不了那玩意儿。",
 "Big deals require big risks/dicks.": "大买卖要大风险／大胆量。",
 "Don't worry, Vaughn.": "别担心，沃恩。",
 "Funny retort.": "回嘴真好笑。",
 "Only an idiots get killed over alien artifacts.  I'm not.":
    "只有傻子才会为外星物品送命。我不是。",
 "This is a unique, relatively safe way to do this":
    "这是做这件事独一无二、相对安全的方式",
 "Dude, I'm adorably funny.": "老兄，我可爱又好笑。",
 "Silence.": "沉默。",
 "[this is a snip of 361828396] Yeah, yeah, I know... we \"borrowed\" it.":
    "[this is a snip of 361828396] 是啊是啊，我知道……我们是“借”来的。",
 "Maybe if this deal goes sour, we can \"borrow\" our way out of an corporate embezzlement charge, too.":
    "也许要是这交易黄了，我们也能“借”出一条路，摆脱挪用公款的指控。",
 "'Course, knowing your luck, you'll probably get off scott free...":
    "当然，照你的运气，你大概能全身而退……",
 "Big deals mean big risks": "大买卖意味着大风险",
 "Try not to vomit again.": "尽量别再吐了。",
 "But I think they're still gonna call it \"embezzlement\" if this deal falls through, y'know?":
    "但我觉得要是这交易泡汤，他们还是会管它叫“挪用公款”，你知道吗？",
 "What can I say?  It's a big opprtunity.": "我能说什么？这是个大好机会。",
 "You know they revised Hyperion Company Handbook after Handsome Jack died, right?":
    "你知道帅杰克死后他们修订了“亥博龙公司手册”吧？",
 "{SlyA}Borrowing, embezzling... an opportunity this enormous is worth breaking a few rules.":
    "{SlyA}借、挪用……这么大的机会值得破几条规矩。",
 "Heck, that's right out of our Hyperion employee handbook.":
    "见鬼，这可完全是照我们 亥博龙员工手册来的。",
 "... while I'm left holding the secret Hyperion account numbers.":
    "……而我却要抱着那些机密的 亥博龙账号。",
 "Dude, relax.": "老兄，放松。",
 "Silence": "沉默",
 "[sigh] We never shou": "[sigh] 我们从来就不该",
 "You know how Hyperion feels about embezzlers, right?":
    "你知道 亥博龙对挪用公款的人是什么态度吧？",
 "How's the stomach?": "胃怎么样了？",
 "I told you not to eat the breakfast burritos in the Hyperion cafeteria.":
    "我跟你说过别吃 亥博龙食堂的早餐卷饼。",
 "Inside out.   I should've taken those pills before we left the Hyperion moonbase.":
    "翻江倒海。我真该在离开 亥博龙月球基地前吃那些药的。",
 "It's not a moonbase.  And I guarantee you'll feel better after we seal the deal on this Key.":
    "那不是月球基地。而且我保证，我们把这把钥匙的交易敲定之后你会好受些。",
 "Yeah, but": "是啊，但是",
 "Whatever.  That risky briefcase full of borrowed money's about to buy us a priceless alien artifact.":
    "随便吧。那个装着“借来的钱”的冒险手提箱，马上要给我们换来一件无价的外星物品。",
 "[reflective]Flying down to dangerous planets,  buying priceless alien artifacts...":
    "[reflective]飞往危险的星球，购买无价的外星物品……",
 "[a little to himself] Of course, they're only \"priceless\" because everyone's so OBSESSED with alien technology.":
    "[a little to himself] 当然，它们之所以“无价”，只是因为所有人都对 Alyen 技术*着迷*得不行。",
 "[back to confronting Rhys] Seriously, do you know how many Hyperion employees have gotten KILLED looking for this ancient alien stuff?":
    "[back to confronting Rhys] 说真的，你知道有多少 亥博龙员工在寻找这些古老外星玩意儿时*丧命*了吗？",
 "Try swaggering more.": "试试多摆点气场。",
 "They're scared of us.": "他们怕我们。",
 "They're the least of our problems.": "他们是我们最小的麻烦。",
 "I told you it would be risky.": "我跟你说过这会有风险。",
 "It'll all be worth it.": "这一切都会值得。",
 "They were idiots.  We're not.": "他们是傻子。我们不是。",
 "We're taking a safer route thatn they did.": "我们走的路比他们安全。",
 "[listing off roll call of the dead] Johnson, Sherman, Clarkwood...":
    "[listing off roll call of the dead] Johnson、Sherman、Clarkwood……",
 "Adamson, DeBarger, the OTHER Johnson...": "Adamson、DeBarger，还有*另一个* Johnson……",
 "And that's not even including our dearly departed CEO...":
    "这还没算上我们那位已故的 CEO……",
 "Only an idiot gets himself killed chasing after secrets if the universe.  And we're not idiots.":
    "只有傻子才会在追寻宇宙秘密时把自己搞死。我们不是傻子。",
 "We're not?": "我们不是？",
 "Those guys all took the dangerous path..": "那些人都走了危险路线……",
 "But us? WE'RE just gonna BUY an alien artifact, drag it back to Hyperion, and stand back as we're showered with long-overdue promotions and raises!":
    "但我们？我们只是*买*一件外星物品，把它拖回 亥博龙，然后站着等早该给我们的升职加薪往身上砸！",
 "Vault Hunting.  Riling up the Bandits.  Making a lot of noise about looking for the secrets of the Universe.":
    "猎秘藏。招惹土匪。到处嚷嚷着要找宇宙的秘密。",
 "Yeah, about that...": "是啊，关于那个……",
 "Look at the bright side.": "看看好的一面。",
 "Look at the bright side, Vaughn.  Our fellow employees' deaths have given us an abject lesson in how NOT to do this.":
    "看看好的一面，沃恩。同事们的死给了我们一堂惨痛的反面教材。",
 "No, we're not.  And when we drag this artifact back to Hyperion, we're gonna get promoted out of our dead end jobs once and for all.":
    "不，我们不是。等我们把这件物品拖回 亥博龙，我们就会彻底摆脱这些没前途的工作、升上去。",
 "Then we'll drag it back to Hyperion for our well-deserved bonuses, raises, and promortions!":
    "然后我们把它拖回 亥博龙，领取我们应得的奖金、加薪和晋升！",
 "It'll follow ME.": "它会跟着*我*。",
 "Well, it'll follow ME.  You... not so much.": "它会跟着*我*。你……就不太会了。",
 "Under my control?  It'll go anywhere.": "在我的控制下？它哪儿都能去。",
 "With me in control, this robot'll follow us to the gates of hell.":
    "有我控制，这台机器人会跟着我们走到地狱之门。",
 "[mess with Vaughn]": "[逗弄 Vaughn]",
 "See?  Totally under control... [fakes being out of control]  Whoah!  Stop!":
    "看吧？完全在控制之中……[fakes being out of control]  哇！停下！",
 "Definitely.": "绝对。",
 "Hell is other people.": "他人即地狱。",
 "Psyche.": "开玩笑啦。",
 "Sterlize!  Sterilize!": "灭菌！灭菌！",
 "Ha.  Ha.": "哈。哈。",
 "Following... following...": "跟随中……跟随中……",
 "[slightly derisive] Golden Boys.": "[slightly derisive] 黄金男孩。",
 "Just for the record, I still think this is really really risky.":
    "顺便说一句，我还是觉得这非常非常冒险。",
 "It'll be a piece of cake.": "小菜一碟。",
 "Trust me, this'll be a piece of cake.  [looking for an example] Like a Lady Baltimore.":
    "相信我，这会是小事一桩。[looking for an example] 就像巴尔的摩女士蛋糕。",
 "[derisively]Rhys train.": "[derisively]瑞斯 号列车。",
 "On": "开",
 "I've had dinner dates that were more dangerous than this.":
    "我约过的晚餐都比这危险。",
 "Lady Baltimore?": "巴尔的摩女士蛋糕？",
 "'Cause If we get caught...": "因为要是我们被抓到……",
 "They're gonna shoot us right into the sun. Poof.": "他们会把我们直接射进太阳。砰。",
 "Or worse, lose the money...": "或者更糟，把钱丢了……",
 "[confidentially] Sometimes he shuts me out.": "[confidentially] 他有时候会把我关在外面。",
 "[sarcastic] You're right, that IS a bright side.": "[sarcastic] 你说得对，这*确实*是好的一面。",
 "An yeah, I suppose if we DO manage to purchase this little chunk of Pandora's \"mysterious alien past\" we'll FINALLY be showered with raises and promotions, and, I don't know, the keys to the executive bidet, but-[has an epiphany] waaaaitaminute.":
    "是啊，我想要是我们真买下了这一小块 潘多拉 的“神秘外星过去”，我们*终于*会迎来加薪和晋升，还有，我不知道，高管智能马桶的钥匙，但——[has an epiphany] 等……等等。",
 "Let' get this over with quickly, man.": "我们快点把这事了结，老兄。",
 "You don't think they saw the money pop open, do you?":
    "你不觉得他们看到钱箱弹开了吧？",
 "...with their greedy little violent eyes.": "……用他们那贪婪的小暴力眼睛。",
 "Does it stun bullets? Gimme that! NEVER pull a weapon on Pandora unless you want to get shot!":
    "它能电晕子弹吗？给我！在 潘多拉 上永远别掏武器，除非你想挨枪！",
 "[being surprised by a suspicious sound]Agh!": "[being surprised by a suspicious sound]啊！",
 "A stun baton.": "一根电击棒。",
 "[annoyed] What is THAT?": "[annoyed] 那是什么？",
 "[nervous] Any time you want to get this thing moving, that would be just fine by me.":
    "[nervous] 你什么时候想让这玩意儿动起来，我都完全没意见。",
 "[nervous] You know I'm standing in the middle of town with a million bucks, right?":
    "[nervous] 你知道我正站在镇中央、身上带着一百万吧？",
 "[nervous, frustrated] Is it broken? Aww, it's broken, isn't it? I KNEW it.":
    "[nervous, frustrated] 它坏了吗？唉，它坏了对吧？我*就知道*。",
 "[reassuring, but secretly nervous] It's not broken; the syntax is just a little... different than I expected.":
    "[reassuring, but secretly nervous] 它没坏；只是语法有点……跟我预期的不一样。",
 "Power active.": "电源已激活。",
 "Just gotta get it to follow us, and we'll be ready to go.":
    "只要让它跟着我们，我们就准备好了。",
 "[surprised by a mistake. short, clipped] Uh oh.": "[surprised by a mistake. short, clipped] 哦哦。",
 "[irritated] So much for low-key.": "[irritated] 低调就别提了。",
 "I've got it under control.": "我能控制住。",
 "And it's not a moon base.": "而且那不是月球基地。",
 "[surprise] What the hell?": "[surprise] 搞什么？",
 "[defensive] Just checking its servos.": "[defensive] 只是在检查它的伺服。",
 "You heard the robot, Rhys.  Stop playing with your toys and get on with it.":
    "你听到机器人了，瑞斯。别玩你的玩具了，继续干活。",
 "[pissed at Rhys] You and me both, pal.": "[pissed at Rhys] 我也一样，哥们。",
 "[success hacking a robot] There!": "[success hacking a robot] 成了！",
 "Command accepted. Preparing to follow user 'RHYS-IS-COOL'":
    "指令已接受。准备跟随用户“RHYS-IS-COOL”",
 "[frustrated sigh]": "[frustrated sigh]",
 "[smirky] Well, the grippers work.": "[smirky] 好吧，夹钳还能用。",
 "[deadpan, upset] Are you kidding me?": "[deadpan, upset] 你在逗我吗？",
 "[deadpan exasperated] Dude. Get this thing to follow us already.":
    "[deadpan exasperated] 老兄。让这玩意儿跟着我们吧。",
 "[deep exasperated sigh]": "[deep exasperated sigh]",
 "(over the Voice Test) You don't know what you're doing, do you?":
    "(over the Voice Test) 你根本不知道自己在干什么，对吧？",
 "(over the voice test) Hacking is more art than science Vaughn.":
    "(over the voice test) 黑客与其说是科学，不如说是艺术，沃恩。",
 "They probably heard that all the way up on the moon base!":
    "他们大概在月球基地上都能听到！",
 "Should I be concerned about those elite hacking firewalls you put up around those accounts we plundered?":
    "我们洗劫的那些账户，你给它们装的那些顶级黑客防火墙，我该担心吗？",
 "{AngryA}I don't think Hyperion's Coroporate Punishment division is gonna agree with that.":
    "{AngryA}我觉得 亥博龙的企业惩处部不会同意这个说法。",
 "{SlyB}Yeah, well, after we seal the deal on the Key, we can BUY the Corporate Punishment division.":
    "{SlyB}是啊，不过等我们把钥匙的交易敲定，我们就能*买下*企业惩处部。",
 "We're thousands of miles from our orbiting Hyperion bosses, it's a beautiful day, and that little briefcase of cash is about to buy us a priceless alien artifact.":
    "我们离轨道上的 亥博龙老板有几千英里，天气好得很，而那个小手提箱里的现金马上要给我们换来一件无价的外星物品。",
 "What's there to relax about?": "有什么好放松的？",
 "Maybe you should, like, poke it or something.": "也许你该，呃，戳它一下什么的。",
 "[pinch of 361828519] You can't really blame 'em.  They probably think we're here to wipe 'em out with our orbital death ray.":
    "[pinch of 361828519] 你还真不能怪他们。他们大概以为我们是来用轨道死光把他们清掉的。",
 "[pinch of 361828520] Do we still have one of those?":
    "[pinch of 361828520] 我们还有那种东西吗？",
 "I love it when you get it all dorky.  You sure it'll follow us?":
    "我就喜欢你一本正经地说傻话。你确定它会跟着我们？",
 "This artifact of yours is supposed to weigh a ton... so how're we getting it back to the car?":
    "你这件物品据说重达一吨……那我们怎么把它弄回车上？",
 "Is it me, or is everybody staring at us?": "是我多心，还是所有人都在盯着我们？",
 "'Cause that would be bad.": "因为那会很糟。",
 "Like, feeding frenzy bad.": "就是那种被围猎的糟。",
 "[mildly nervous][through teeth]  That's it... nothing to see here... just a couple of guys with a killer robot and a kajillion dollars...":
    "[mildly nervous][through teeth]  没什么……这儿没什么可看的……只是两个带着杀人机器人和千百来万块钱的家伙……",
 "A LoaderBot, a company vehicle... why isn't SHE in on this deal?":
    "一台装载机器人、一辆公司车……她怎么不参与这笔交易？",
 "Good assistants are hard to come by.   Besides, the less people that know about this, the better.":
    "好助理可遇不可求。再说，知道这事的人越少越好。",
 "Open": "打开",
 "Car Trunk": "汽车后备箱",
 "Test Grippers": "测试夹钳",
})

# —— Rhys/Vaughn 增补对白 ——
T.update({
 "[pickup1][v-o] It all started about a year ago in a little slice of nothing called Prosperity Junction. I had come down from the home office to make the score of a lifetime. It was all going smooth as whipped butter.":
    "[pickup1][v-o] 一切都始于大约一年前，在一个叫繁荣枢纽的鸟不拉屎的地方。我从总部下来，想干一票这辈子最大的买卖。一切顺利得像打发的黄油。",
 "[pickup1][he's pretty nervous]Thanks. I think I'm OK now, sort of. Kind of. Maybe.":
    "[pickup1][he's pretty nervous]谢了。我想我现在还行，算是吧。差不多。也许。",
 "[pickup1][accusing but still nervous]Y'know, if you need money, you can just ask.":
    "[pickup1][accusing but still nervous]你知道，你要是缺钱，直接问我就行。",
 "[pickup1][peeved and agitated]Is it too much to ask that you DON'T let the money blow away?":
    "[pickup1][peeved and agitated]求你*别*让钱被吹走，这要求过分吗？",
 "[pickup1]{HappyA}I know, but can't help thinking about the {AngryB}EMBEZZLEMENT, and how happy Hyperion will be to hollow out our gorgeous intestines.":
    "[pickup1]{HappyA}我知道，但我忍不住想那桩{AngryB}挪用公款案，还有 亥博龙把咱们漂亮内脏掏空时会有多高兴。",
 "[pickup1]{SlyB}Let's focus on the deal, Vaughn. Think about how happy Hyperion will be when we come back with a gorgeous Vault Key!":
    "[pickup1]{SlyB}我们专注这笔交易，沃恩。想想我们带着一把漂亮的秘藏钥匙回去时 亥博龙会有多高兴！",
 "[pickup1]Cause if Finance forensics gets onto this we are DEAD.":
    "[pickup1]因为要是财务取证部查到这事，我们就*死定了*。",
 "[pickup1]Except that's not gonna happen, because we're coming back with a Vault Key.":
    "[pickup1]但那不会发生，因为我们会带着秘藏钥匙回来。",
 "[pickup1]Especially me. It's my name on the accounts.":
    "[pickup1]尤其是我。账户上写的是我的名字。",
 "[pickup1]Remember that poor shmuck from marketing? And that was just over a computer.":
    "[pickup1]还记得市场部那个可怜虫吗？那还只是因为一台电脑。",
 "[pickup1]This has got to be the stupidest thing I've ever done.":
    "[pickup1]这绝对是我这辈子干过最蠢的事。",
 "[pickup1][slightly calmed]Did you just say \"Ride the Rhys Train?\" [warm]You might want to workshop that one a little bit.":
    "[pickup1][slightly calmed]你刚是说“搭 瑞斯 号列车”？[warm]这句你也许该再打磨打磨。",
 "[pickup1]I'm with you a hundred percent. But shouldn't we at least have some backup?":
    "[pickup1]我百分之百支持你。但我们至少该有点后援吧？",
 "[pickup1]Solution to that coming in 3...2...1...": "[pickup1]解决方案 3……2……1……到。",
 "[pickup1]I used my natural gifts.": "[pickup1]我用了我的天赋。",
 "[pickup1][faux eloquent]Anything else I can get for you, good sir?":
    "[pickup1][faux eloquent]还需要我为您做点别的吗，先生？",
 "[pickup1]I think it'll be scarier if it stays quiet.":
    "[pickup1]我觉得它安静着更吓人。",
 "[pickup1]Where're the guns?": "[pickup1]枪呢？",
 "[pickup1]The base model's all I could get. [spit out the name]Vasquez requisitioned all the weaponized Loaders.  [looking for reassurance] But hey, it should still be enough to intimidate the locals, right?":
    "[pickup1]我只能弄到基础款。[spit out the name]Vasquez 把所有武装型装载机都调走了。[looking for reassurance] 但嘿，吓吓当地人应该还是够的，对吧？",
 "[pickup1]I am equipped with extra-long vibrating pistons for versatile thrusting movements.":
    "[pickup1]我配备了超长振动活塞，可进行多种方式的推顶动作。",
 "[pickup1]Vasquez'll be here in a couple of hours. [grin][Rhys has snapped off his display, and begun walking]":
    "[pickup1]Vasquez 几小时后到。[grin][Rhys has snapped off his display, and begun walking]",
 "[pickup1][Deep breath, mustering his courage.]": "[pickup1][Deep breath, mustering his courage.]",
 "[pickup1][get a bunch of different versions]Let's go buy a Vault Key.":
    "[pickup1][get a bunch of different versions]我们去买一把秘藏钥匙吧。",
 "We're not embezzling, we're investing.": "我们不是挪用公款，我们是在投资。",
 "{SlyB}[pickup1]Listen, try not to vomit while we're talking to the seller, OK? Weakens our bargaining position.":
    "{SlyB}[pickup1]听着，跟卖家谈话的时候尽量别吐，行吗？这会削弱我们的谈判地位。",
 "[pickup1][disgusted noise, as though considering that is distasteful]":
    "[pickup1][disgusted noise, as though considering that is distasteful]",
 "We got this.": "我们搞得定。",
 "[pickup1][arched eyebrow]Did you just say \"Ride the Rhys Train?\"":
    "[pickup1][arched eyebrow]你刚是说“搭 瑞斯 号列车”？",
 "[neutral]It sounds like \"restraint.\" The irony is pleasing.":
    "[neutral]听起来像“自制”。这讽刺感令人愉悦。",
 "[neutral]Actually, Carbon steel has superior load-bearing capabilities.":
    "[neutral]其实，碳钢的承重能力更强。",
 "Thanks a lot.": "多谢了。",
 "No, I didn't mean you...": "不，我不是说你……",
 "Man is the cruelest animal.": "人是最残忍的动物。",
 "[pickup1]You know this is how I found the Vault Key, right?  Accessed Vasquez's personal transponder, intercepted his encrypted conversation, wham, bam, here we are.":
    "[pickup1]你知道我就是这么找到秘藏钥匙的，对吧？接入 Vasquez 的私人应答器，截获他的加密通话，砰，啪，我们就到这儿了。",
 "[pickup1]I'm just saying... I'm technically the guy who's resposnible for the Hyperion Golden Parachute Account... so when that million dollars turns up missing...":
    "[pickup1]我只是说……严格来说我是负责 亥博龙高管离职金账户的人……所以当那一百万不见了的时候……",
 "[pickup1]Well I take it back. You are a beautiful snowflake. [Long Pause] Who makes weird arm love to computers.":
    "[pickup1]好吧，我收回。你是朵美丽的雪花。[Long Pause] 一个用奇怪手臂对电脑做爱的家伙。",
 "[pickup1][nervous]I can't feel my kneecaps.": "[pickup1][nervous]我感觉不到我的膝盖骨了。",
 "Visual weight estimate indicates exactly one million dollars.":
    "目测重量估计：正好一百万美元。",
 "Visual weight estimate indicates only nine hundred ninety-nine thousand, eight hundred dollars.":
    "目测重量估计：只有九十九万九千八百美元。",
 "Could you not broadcast that please?": "你能不能别那样播报？",
 "[pickup1][nervous]We're being watched.": "[pickup1][nervous]我们被盯上了。",
 "[to vaughn]Try swaggering it up a little. Let 'em know who's boss.":
    "[to vaughn]试着多摆点气场。让他们知道谁是老大。",
 "[pickup1]They won't do anything, they're petrified of us. Probably think we're gonna wipe 'em out with our orbital death ray.":
    "[pickup1]他们什么都不会做，他们被我们吓僵了。大概以为我们要用轨道死光把他们清掉。",
 "[pickup1]Don't sweat the locals, they're not what we should be worried about. Just pretend they're all in their underwear and focus on the job.":
    "[pickup1]别管当地人，他们不是我们该担心的。就当他们都只穿着内裤，专注干活。",
 "Eleven.": "十一。",
 "Old models, with buggy software. Not to be trusted.":
    "老型号，软件一堆毛病。不能信。",
 "Wait, what DO you think we should be worried about?": "等等，那你觉得我们该担心什么？",
 "[nervous, not fantastic]Fantastic.": "[nervous, not fantastic]太好了。",
 "Do not bring a stick to a gunfight.": "别拿棍子去参加枪战。",
 "Well, it's all arranged, right? We give him the money, we take the key.":
    "嗯，都安排好了，对吧？我们给他钱，我们拿钥匙。",
 "Hyperion Mobile Ordnance Regulation 2471: Do not bring a stick to a gunfight.":
    "亥博龙机动武器条例第 2471 条：别拿棍子去参加枪战。",
 "This isn't about Vasquez, it's about us. This is our chance at the brass ring. But I do have to admit it's going to feel really good to scoop that greedy, lying, two-faced...oh!":
    "这跟 Vasquez 无关，这关乎我们。这是我们抓住那枚金环的机会。但我得承认，能抢先一步搞掉那个贪婪、满嘴谎言、两面三刀的……哦！",
 "Speaking of bringing a stick to a gunfight, Rhys...":
    "说到拿棍子去参加枪战，瑞斯……",
 "Rhys, I have to ask, and don't take this the wrong way... this isn't just to get back at Vasquez, is it? Cause a normal person would just, sleep with his wife or something, and move on.":
    "瑞斯，我得问一句，别误会……这事不只是为了报复 Vasquez 吧？因为正常人只会，睡他老婆之类的，然后翻篇。",
 "And before Hyperion finds out we stole their money.":
    "还要赶在 亥博龙发现我们偷了他们的钱之前。",
 "All before Vasquez shows up, burns the town to the ground, and grabs the key for himself.":
    "全都要赶在 Vasquez 出现、把镇子烧成灰、自己把钥匙抢走之前。",
 "And without any screw-ups.": "而且不能出任何岔子。",
 "[pickup1]Really?": "[pickup1]真的？",
 "{HappyB}[pickup1]What gave you the impression that I have control over my vomit?":
    "{HappyB}[pickup1]是什么让你觉得我能控制住我的呕吐？",
 "[pickup1]Not bad! How'd you pull this off? I mean, ganking a million bucks is one thing, but walking off with a Loader Bot is unheard of.":
    "[pickup1]不错嘛！你是怎么弄成的？我是说，搞到一百万是一回事，但顺走一台装载机器人可是闻所未闻。",
 "[pickup1]Of course you did.": "[pickup1]你当然用了。",
 "[geeking out] Presto: one Mach 3 PWR Loader, with multi-tonnage nullfield lifting arms, fully articulated Thompson fine-motor manipulators, jet-assist locomotion, PBX slow-fusion power plant, satellite uplink module, anti-corrosive paint, and holographic status indicator. Ready to rumble.":
    "[geeking out] 变——一台 3 马赫 PWR 装载机，配多吨级零场起重臂、全关节汤姆森精密电机机械手、喷气辅助行进、PBX 慢聚变动力装置、卫星上行模块、防腐蚀涂层和全息状态指示器。准备开干。",
 "[attempting swagger]Y-yeah! And we ain't here for no BIRTHDAY PARTY!":
    "[attempting swagger]对——对！我们可不是来参加*生日派对*的！",
 "I think he'll be scarier if he stays quiet.": "我觉得他安静着更吓人。",
 "[triumphant]This is the place!": "[triumphant]就是这儿！",
 "Yep, and whatever goes down it'll be worth it. By this time tomorrow, we'll be Hyperion's Golden Boys.":
    "没错，不管发生什么都是值得的。明天这个时候，我们就是 亥博龙的黄金男孩。",
 "Yeah. Must be from Yvette.": "是啊。肯定是 Yvette 送来的。",
 "I supervised.": "我监督的。",
 "Remotely.": "远程监督。",
 "Your assistant?": "你的助理？",
 "But preferably not.": "但最好用不上。",
 "I mean what if something happened and we had to put the money back?":
    "我是说，万一出了什么事，我们得把钱还回去怎么办？",
 "[pickup1][v-o] MY bottom line was adjusted about a year ago in a speck of dirt called Prosperity Junction.  I'd flown down to Pandora for the score of a lifetime.":
    "[pickup1][v-o] 我的底线在大约一年前，在一个叫繁荣枢纽的小土点上被调整了。我飞到 潘多拉，想干一票这辈子最大的买卖。",
 "[defensive] I'm a naturally gifted supervisor.  Shh.":
    "[defensive] 我天生就是个有天赋的监督者。嘘。",
 "[arched  eyebrow] Natural gifts, huh?": "[arched  eyebrow] 天赋，是吗？",
 "[pickup1]People here aren't very friendly, are they?": "[pickup1]这儿的人不太友好，对吧？",
 "Ignoring you.": "不理你。",
 "How is it that you can make hacking an authorization server sound dirty?":
    "你怎么能把黑一台授权服务器说得那么下流？",
 "I am naked and unashamed.": "我赤身裸体，毫不羞愧。",
 "Keep your skeevy skivvy fantasies to yourself, okay?":
    "把你那些猥琐的内衣幻想留给自己，行吗？",
 "Eyes on the prize, buddy. Guys like us NEVER get their hands on a Vault Key, and with Handsome Jack dead and Hyperion in turmoil, this is our chance to ride it to the top!":
    "盯着目标，哥们。像我们这种人*永远*摸不到秘藏钥匙，而帅杰克死了、亥博龙一片混乱，这是我们一飞冲天的机会！",
 "[concerned]Yes. Yes it should.": "[concerned]对。确实应该。",
 "It just seemed smart to be carrying something. 'Cause we really don't know squat about the seller.":
    "带点东西在身上显得聪明。因为我们压根不了解那个卖家。",
 "[hopeful]Right?": "[hopeful]对吧？",
 "But you never know.": "但说不准。",
 "[less mumbly] Also Vasquez is going to turn up sooner or later and you KNOW he won't be happy about being punked...":
    "[less mumbly] 而且 Vasquez 迟早会出现，你*知道*他不会喜欢被耍……",
 "Not that a stun baton would do much good against his army of Loader Bots.":
    "倒不是说一根电击棒对他那支装载机器人军队有什么用。",
 "No. I mean, Vasquez is a grasping, two-faced weasel, but this is about us, our future. This is our shot. I could be the next Handsome Jack, Vaughn, and you could be...Vice President in Charge of Unbelievable Spending. And the guy who's going to make all that happen for us is... [Rhys looks up, is confused] right here?":
    "不。我是说，Vasquez 是个贪得无厌、两面三刀的黄鼠狼，但这关乎我们、关乎我们的未来。这是我们的机会。我可能是下一个帅杰克，沃恩，而你可能是……“难以置信开销”副总裁。而将为我们实现这一切的人就是……[Rhys looks up, is confused] 这儿？",
 "[matter of fact]These are the coordinates I lifted from Vasquez.":
    "[matter of fact]这是我从 Vasquez 那儿偷来的坐标。",
 "No accounting for taste, I guess.": "品味这东西没法计较，我想。",
 "You two wait here. I'll check it out.": "你们两个在这儿等着。我去看看。",
 "[mumbly] Apart from the fact that he's got a Vault Key and lives in the ass end of NOWHERE.":
    "[mumbly] 除了他有一把秘藏钥匙，而且住在鸟不拉屎的地方这个事实。",
 "[pickup1] I was excited.": "[pickup1] 我当时很兴奋。",
 "[pickup1] My partner was positively gushing.": "[pickup1] 我的搭档简直滔滔不绝。",
 "[pickup1] ...": "[pickup1] ……",
 "[pickup1]And then nothing else will matter.": "[pickup1]然后其他一切都不重要了。",
 "[pickup1]Right?": "[pickup1]对吧？",
 "{HappyB}I've always wanted a private army.": "{HappyB}我一直想要一支私人军队。",
 "{HappyB}Don't worry about me, I'm fine with adventure.":
    "{HappyB}别担心我，我不怕冒险。",
 "{SlyA}[pickup1]  Seriously, next time, I'LL drive to the once-in-a-lifetime deal, okay?":
    "{SlyA}[pickup1]  说真的，下次这种一辈子一次的交易，*我*来开车，行吗？",
 "[pickup1]{SlyC}You know, in most friendships, it's customary to buck up your pal before embarking on a dangerous adventure.":
    "[pickup1]{SlyC}你知道，在大多数友谊里，启程冒险前给朋友打打气是惯例。",
 "Fine. Then I want to be the loose cannon with a sensitive side.":
    "行。那我要当那个内心敏感的火炮。",
 "{SLyA}I think you brought me along because I got drunk and told you about the company's golden parachute accounts and how easy it would be poach the money.":
    "{SLyA}我觉得你带上我，是因为我喝醉了，跟你讲了公司的离职金账户，还有挪用那笔钱有多容易。",
 "I'll have her hacked and running in no time.": "我很快就能把她黑进去、让她跑起来。",
 "{body-CarryCase}Great!": "{body-CarryCase}太好了！",
 "{body-CarryCase}I'll, uh... watch.": "{body-CarryCase}我，呃……看着。",
 "No. Just strategizing about the best way to open the panel with it.":
    "不。只是在盘算用它打开面板的最佳方式。",
 "{body-CarryCase}Pandora's not such a bad place, is it?":
    "{body-CarryCase}潘多拉 也没那么糟，对吧？",
 "I'd better get working, I think you're getting a sunstroke.":
    "我最好开始干活，我觉得你中暑了。",
 "{body-CarryCase}You know, wealth and power is going to be awesome, but right now all I really want is a cheeseburger.":
    "{body-CarryCase}你知道，财富和权力会很棒，但现在我真正想要的只是一个芝士汉堡。",
 "Dare to dream, my friend.": "敢于梦想，我的朋友。",
 "Nope. Everything's hunky dory.": "没有。一切都好得很。",
 "{body-CarryCase}\tIs there something wrong?": "{body-CarryCase}\t出什么问题了吗？",
 "{body-CarryCase}OK. Just wasn't sure what the holdup was, but I'm sure you're working as fast as you can.":
    "{body-CarryCase}好。只是不确定卡在哪儿了，但我相信你已经尽力快了。",
 "Not that I have any money...": "倒不是说我有钱……",
 "When we bring them the Vault Key they'll GIVE us the  Corporate Punishment division.":
    "等我们把秘藏钥匙带给他们，他们会*主动把*企业惩处部交给我们。",
 "We're not EMBEZZLING the money, we're INVESTING IT. In Hyperion's future.":
    "我们不是在*挪用*这笔钱，我们是在*投资*。投资 亥博龙的未来。",
 "[bucking him up] {SLyB}Pal, we got this, you're gonna be great.  You think I brought you along just because we're friends?":
    "[bucking him up] {SLyB}哥们，我们搞得定，你会很棒的。你以为我带你一起来只是因为我们是朋友？",
 "That's a very cynical attitude, Vaughn.": "这态度太愤世嫉俗了，沃恩。",
 "I feel like we don't talk as much now that we're on Pandora. Are you reinventing yourself as thestrong, silent type?":
    "我觉得到了 潘多拉 之后我们话少了很多。你是不是在把自己重塑成那种沉默硬汉？",
 "Because hacking is a sensual art that--I'll tell you when you're older.":
    "因为黑客是一门感官艺术，它——等你长大点我再告诉你。",
 "You know what I meant!": "你知道我什么意思！",
 "[v-o] Nobody thought that!": "[v-o] 没人那么想过！",
 "[under breathe] I told you, I'm a loose cannon now.":
    "[under breathe] 我跟你说过，我现在是个失控的火炮。",
 "I told you, buddy, If you want to ride the Rhys Train to the top of Hyperion, you're gonna have to take a few risks.":
    "我跟你说过，哥们，你想搭 瑞斯 号列车直达 亥博龙顶峰，就得冒点风险。",
 "You really need to tell me what you're feeling more often.":
    "你真该多跟我说说你的感受。",
 "The less people who know about this deal the better.  Besides, good assisstants are hard to come by.":
    "知道这笔交易的人越少越好。再说，好助理可遇不可求。",
 "If I can get to the Loader's interface port, I can force it to unfold, but the access panel is jammed shut.":
    "只要我能接触到装载机的接口端口，就能强行让它展开，但检修面板卡死了。",
 "{body-CarryCase}Don't look at me.  If it's not an expense report, I can't hack it.":
    "{body-CarryCase}别看我。要不是费用报销单，我黑不了。",
 "That's right, I USE them I don't have intimate physical relations with them.  It's a little something called \"boundaries.\"":
    "没错，我是*用*它们，不是跟它们发生亲密肉体关系。这东西叫“界限”。",
 "I don't know why this weirds you out.  You're an accountant... you use computers all the time.":
    "我不知道你为什么会觉得怪。你是会计……你成天用电脑。",
 "I'm not going to let anything happen to you, buddy.":
    "我不会让你出任何事的，哥们。",
 "Yeah, yeah, I hear you.": "是啊是啊，我听见了。",
 "She never did get back to me...": "她一直没回我……",
 "[pickup1][peeved] Come on man, help me out here.  I can't watch the cash and cough up":
    "[pickup1][peeved] 拜托，老兄，帮我一把。我不能一边看着钱一边吐啊吐",
 "And I appreciate you letting me know. Every. Time. I do it.":
    "而我很感谢你每次都告诉我。每一。次。都是。",
 "[almost ashamed under breath] That's what she said.":
    "[almost ashamed under breath] 她也是这么说的。",
 "That robot arm really isn't good for anything but hacking, is it?  You know what, if it is, don't tell me.  That's private.":
    "那条机器人手臂除了黑客真的什么都干不了，对吧？你知道吗，要是能干别的，别告诉我。那是隐私。",
 "[walking away] It's a type of cake.": "[walking away] 是一种蛋糕。",
 "[sotto voce] You're a type of cake.": "[sotto voce] 你才是一种蛋糕。",
 "Does the moonbase have a top?": "月球基地有顶吗？",
 "It's not a moonbase.  The point is, somebody's going to wind up on top at Hyperion, and I pick us.":
    "那不是月球基地。重点是，亥博龙总会有人爬到顶上，我选我们。",
 "Shouldn't we get some-": "我们不该弄点——",
 "(<<author>>Harrison Pink, Wed Mar 05 10:40:59 2014<<date:1394044859>>) Suggest peppering in Vaughn pushing expediency in the entire sequence before bot opens. We don't need to know why, but we also want to really get the player to do what we want ASAP.":
    "(<<author>>Harrison Pink, Wed Mar 05 10:40:59 2014<<date:1394044859>>) 建议在机器人打开前的整段流程里，穿插 沃恩 催促赶紧动手的台词。我们不需要解释原因，但也要真正推着玩家尽快按我们的意图行动。",
 "[to himself] The hinges must've melted in the descent.":
    "[to himself] 铰链肯定是在降落时熔掉了。",
 "You gonna keep staring at it, or are you gonna cut those hinges?":
    "你是要一直盯着它，还是去把那些铰链切了？",
 "Now THAT'S a clean cut.": "这才叫干净的切口。",
 "Hmmm... not sure where they put the interface port on this model.":
    "嗯……不确定这个型号的接口端口放在哪儿。",
 "Bet my cyber eye can find it.": "我打赌我的电子眼能找到。",
 "There the port... under that access panel.": "端口就在那儿……在那块检修面板下面。",
 "Your assisstant?": "你的助理？",
 "[v-o] The good news is, I was able to sneak a surface-shipment request for this Loader down to your coordinates from Hyperion HQ.":
    "[v-o] 好消息是，我从 亥博龙总部偷偷提交了一份地表运输申请，把这台装载机送到了你的坐标点。",
 "ECHO Recording": "ECHO 录音",
 "Pry Open": "撬开",
 "[pickup2][v-o] I had everything totally under control.":
    "[pickup2][v-o] 一切都在我完全掌控之中。",
 "[pickup2][nervous and talking fast]Like I said, it's some kind of stomach flu, and- yes, I know you don't care about my stomach, Mr. Vasquez.  Yes, I'll come in early tomorrow towork on those firewall upgrades.  Thank you, sir.":
    "[pickup2][nervous and talking fast]就像我说的，是某种肠胃流感，而且——是的，我知道您不关心我的胃，Vasquez 先生。是的，我明天早点来弄那些防火墙升级。谢谢您，先生。",
 "[pickup2][nervous and talking fast]  No sir, Mr. Vasquez.  I'm sorry, but I can't come in today, sir.":
    "[pickup2][nervous and talking fast]  不，先生，Vasquez 先生。抱歉，我今天来不了，先生。",
 "[pickup2][frustrated noise] God, what an asshole.":
    "[pickup2][frustrated noise] 天哪，真是个混蛋。",
 "[pickup2] You gonna get that?": "[pickup2] 你要接吗？",
 "[pickup2] You and me both, brother.  But it's not gonna come to that, 'cause the Key that's gonna Vault us out from under Vasquez once and for all is right about... here?":
    "[pickup2] 我也一样，兄弟。但不会走到那一步，因为那把能让我们彻底摆脱 Vasquez 的钥匙就在……这儿？",
 "[pickup2] I swear, I'd almost PREFER disembowelment to working another week under that back-stabbing chumwad.":
    "[pickup2] 我发誓，比起在那个背后捅刀的混账手下再干一周，我几乎*宁愿*被掏空肚子。",
 "[pickup2]  Hell no.  It's Vasquez.  Bastard's trying to use me to check up on you.":
    "[pickup2]  才不接。是 Vasquez。那混蛋想利用我监视你。",
 "[pickup2] These are the coordinates I intercepted on V":
    "[pickup2] 这是我在 V 上截获的坐标",
 "[pickup2] Strange place for a fate-altering rendevous.":
    "[pickup2] 改变命运的会面选在这种地方，真怪。",
 "[pickup2] So, we walk up to the creepy building, buy the Vault Key, and take it back to the moonbase.":
    "[pickup2] 所以，我们走到那栋瘆人的建筑前，买下秘藏钥匙，然后带回月球基地。",
 "[pickup2] Y'know, it's only a matter of time before he figures out what we're up to,  and when he does-":
    "[pickup2] 你知道，他迟早会发现我们在干什么，而等他发现了——",
 "[pickup2] He won't, and even if he does, I don't give a crap anymore.  Pricks like Vasquez have been sucking the life out of us ever since we started at Hyperion.  If we don't make our move NOW, we're gonna die in our cubes.":
    "[pickup2] 他不会，就算他发现了，我也不在乎了。自从我们进 亥博龙以来，Vasquez 那种混蛋就一直在吸我们的血。我们现在不动手，就会死在工位里。",
 "[pickup2][perking up and ignoring Vaughn] And the Key to Vaulting over those bastards into the Hyperion big leagues is right... about... here?":
    "[pickup2][perking up and ignoring Vaughn] 而那把能让我们越过那些混蛋、闯进 亥博龙大联盟的钥匙就在……这……儿？",
 "[pickup2] Sorry about that... Vasquez probably thinks you'll rat me out.":
    "[pickup2] 抱歉……Vasquez 大概觉得你会出卖我。",
 "[pickup2] Oh great, now your psycho supervisor is calling ME.":
    "[pickup2] 哦好极了，现在你那个精神病主管打给*我*了。",
 "[pickup2]": "[pickup2]",
 "[pickup2] Or foolhardy...": "[pickup2] 或者是鲁莽……",
 "[pickup2] Or dangerous...": "[pickup2] 或者危险……",
 "[pickup2] Not TOO risky...": "[pickup2] 不是*太*冒险……",
 "[pickup2][cheerfully sarcastic] Assuming we don't get killed down here first.":
    "[pickup2][cheerfully sarcastic] 前提是我们没先在这下面被弄死。",
})

# —— 行车 + 进城问路（Rudiger）——
T.update({
 "{worryA}Ugh, shhhhhhcrap.[beat; sad]  I think we-- {SadB}I think we killed it.":
    "{worryA}呃，糟……糟了。[beat; sad] 我想我们——{SadB}我想我们把它撞死了。",
 "It's, uh....": "这个，呃……",
 "[sad] Maan, I didn't want to start the trip like this.":
    "[sad] 唉，我不想以这种方式开始这趟旅程。",
 "Put a dent in the car...": "把车撞了个坑……",
 "It died quick.": "它死得很快。",
 "Look, everything here wants to kill us, alright? Remember that.":
    "听着，这儿什么都想弄死我们，行吗？记住这点。",
 "{WorryC}Yeah, but you wouldn't brake for monster birds, {FearB}that thing was a... a nightmare creature.":
    "{WorryC}是啊，但你不会为几只怪鸟刹车，{FearB}那东西是个……噩梦般的生物。",
 "[a little annoyed by the look] {SternD}What.": "[a little annoyed by the look] {SternD}怎么了。",
 "{WorryB}Sooooo.... this looks... not good.": "{WorryB}那么……这看起来……不太妙。",
 "{SternD}Just drive.": "{SternD}开车就行。",
 "{SternA}It's Pandora, what did you expect?": "{SternA}这是 潘多拉，你还指望什么？",
 "Yeah, I, uh, I guess this, but... this is just... really not good.":
    "是啊，我，呃，我猜是这样，但……这真的……不太妙。",
 "[growl]": "[growl]",
 "{FearB}In a neighborhood, I might add, of backplanet nutjobs.":
    "{FearB}顺便说一句，还是在一个满是落后星球疯子的街区里。",
 "{fearA}I'm just getting a vibe, ya know?": "{fearA}我只是有种感觉，你知道吗？",
 "{sternA}Just keep your eyes open for the place, okay? {SternB}I don't wanna be here any longer than we have to.":
    "{sternA}盯紧点找那地方，行吗？{SternB}我不想在这儿多待一秒。",
 "[quietly] {WorryA}Yeah.": "[quietly] {WorryA}嗯。",
 "{SternA}And watch the money.": "{SternA}还有看好钱。",
 "I'm serious. Pandora's dangerous. Everything here wants to kill us.":
    "我是认真的。潘多拉 很危险。这儿什么都想弄死我们。",
 "[sarcastic] {smugC}Oh, really?": "[sarcastic] {smugC}哦，是吗？",
 "\"What am I afraid of?\" {SmugC}Oh, I don't know, {RageA}old mining communities stranded on a planet getting prospecter madness and eating us for one...":
    "“我怕什么？”{SmugC}哦，我不知道，{RageA}比如那些困在星球上的老矿工社区得了淘金疯，把我们吃掉……",
 "{slyC}What the Hell are you afraid of, huh? It's a town, like any other, {SmugB}just a little more dust.":
    "{slyC}你到底怕什么，啊？这就是个镇子，跟别的没两样，{SmugB}只是灰多一点。",
 "They would be stranded and they'd have to eat each other.":
    "他们会被困住，然后不得不互相吃。",
 "Why not eat the skags?": "干嘛不吃异犬？",
 "That's a good question, actually.": "这问题其实问得好。",
 "[laughing] {HappyB}Get the Hell outta here.": "[laughing] {HappyB}滚一边去。",
 "{SmugC}[laughs] {sternD}I'm not kidding!": "{SmugC}[laughs] {sternD}我没开玩笑！",
 "Sure, okay.": "行吧。",
 "{NeutralB}Vaughn, don't be such a wuss.": "{NeutralB}沃恩，别这么怂。",
 "You know, when you say things like that, I sometimes forgot that you're pretending to be the guy who would say things like that.":
    "你知道，你说这种话的时候，我有时会忘了你是在假装自己是会说这种话的人。",
 "[playful] You forget your dress back at the station.": "[playful] 你的裙子忘在站上了。",
 "[not believing] {SternD}Sure.": "[not believing] {SternD}行。",
 "{SmugB}[pretending to be Rhys] \"Yeah, Vaughn, I agree.\"[beat, then as himself] {HappyA}Yeah, this place is a garbage land of sand and sadness.":
    "{SmugB}[pretending to be Rhys] “对，沃恩，我同意。”[beat, then as himself] {HappyA}对，这地方就是一片沙子与悲伤的垃圾之地。",
 "{NeutralB}Rhys?": "{NeutralB}瑞斯？",
 "{HappyA}Listen, one tap on the arm and Yvette can send down a Loader Bot if things get too entertaining.":
    "{HappyA}听着，往手臂上一敲，Yvette 就能派台装载机器人下来，以防事情变得太“有趣”。",
 "[becoming content] {SlyA}That's true.": "[becoming content] {SlyA}那倒是。",
 "{smugA}God, I can't wait to be in that chair. You and me, Yvette...":
    "{smugA}天哪，我迫不及待想坐上那把椅子。你和我，Yvette……",
 "{NeutralB}That guy ran this company into the ground.":
    "{NeutralB}那家伙把这家公司搞垮了。",
 "{SmugB}He makes all this noise, wastes all this money.":
    "{SmugB}他闹出这么大动静，浪费这么多钱。",
 "{SternD}Runs around with nutcases like Wilhelm...": "{SternD}跟 Wilhelm 那种疯子混在一起……",
 "All just to get himself killed.": "结果只是把自己搞死。",
 "{SternB}That's what you think?": "{SternB}你是这么想的？",
 "[almost to himself] {SmugC}That's what I know.": "[almost to himself] {SmugC}这是我确定的。",
 "{ThinkB}Boy, you and I see things very differently.[beat] {SlyC}Handsome Jack made Hyperion.":
    "{ThinkB}天哪，你和我看事情的眼光差太远了。[beat] {SlyC}是帅杰克造就了 亥博龙。",
 "{FearA}Yeah, but--[gets cut off]": "{FearA}是啊，但是——[gets cut off]",
 "{SmugA}No, more than that.[beat] {SmugC}He's the industrialist of the century.":
    "{SmugA}不，不止如此。[beat] {SmugC}他是世纪工业家。",
 "{HappyB}He's the model of interplanetary success, {slyC}I mean, no one else comes close.":
    "{HappyB}他是星际成功的典范，{slyC}我是说，没人能比。",
 "[to himself] {SternD}Calling himself \"Handsome Jack\" for starters...":
    "[to himself] {SternD}首先，管自己叫“帅杰克”这一点……",
 "{HappyB}But we're smarter than he was.": "{HappyB}但我们比他聪明。",
 "{WorryB}Jack... look, he did a lot of good things for the company, but... he made a lot of mistakes, too.":
    "{WorryB}Jack……听着，他为公司做了很多好事，但……他也犯了很多错。",
 "{slyA}Uh huh.": "{slyA}嗯哼。",
 "Not us, though.": "但我们不会。",
 "[to himself] {SternD}Or a Vault Hunter will.": "[to himself] {SternD}或者某个秘藏猎人会。",
 "{SmugC}Look, Jack's dead, he lost, he couldn't make it.":
    "{SmugC}听着，Jack 死了，他输了，他没能成。",
 "He was a loser, and I don't care if you're a trillionaire or a janitor or whatever... your true nature will always catch up to you.":
    "他是个失败者，不管你是万亿富翁还是清洁工还是什么……你的本性迟早会追上你。",
 "{HappyA}That's not gonna be us.": "{HappyA}那不会是我们。",
 "{NeutralB}Yeah, do you see it?": "{NeutralB}是啊，你看到了吗？",
 "{AngryA}The tracker's beep beep beeping but I don't see the place.":
    "{AngryA}追踪器嘀嘀嘀响个不停，但我没看到那地方。",
 "{thinkB}It's \"The World of Curiosities,\" right?":
    "{thinkB}叫“奇珍世界”，对吧？",
 "{SternD}Could ask one of them...": "{SternD}可以问问他们中的一个……",
 "{WorryA}Normalish enough, anyway.": "{WorryA}总之，还算正常。",
 "And we need to find it before Vasquez comes down.":
    "而且我们得在 Vasquez 下来之前找到它。",
 "{SmugB}They seem... {FearA}normalish.": "{SmugB}他们看起来……{FearA}还算正常。",
 "All in one day's work.": "都是一天的活儿。",
 "Then it's kick back on the moon beach time.": "然后就是躺在月球海滩上放松的时间。",
 "{slyA}They'll send in a crew to use the key...":
    "{slyA}他们会派一队人来使用钥匙……",
 "What's this \"we\" stuff?": "这个“我们”是怎么回事？",
 "Don't think so small.": "别想得那么小。",
 "First things first.": "先办正事。",
 "{SmugC}Take you and Yvette out of that sentence and it's almost true.":
    "{SmugC}把你和 Yvette 从这句话里拿掉，它就差点成真了。",
 "{AngryA}You're joking.": "{AngryA}你在开玩笑。",
 "No, I'm not, when we get back, I'm running things, not you, and definitely not Yvette.":
    "不，我没开玩笑，回去之后是我管事，不是你，更绝对不是 Yvette。",
 "{SlyC}And I got the stun button.": "{SlyC}而且电击按钮在我手上。",
 "{slyb}You are unbelievable.": "{slyb}你真是难以置信。",
 "{SmugC}I got the money.": "{SmugC}钱在我手上。",
 "{HappyB}You can count on two fingers the number of people who have even gotten close to that.":
    "{HappyB}接近过那一步的人，你两只手的手指都数得过来。",
 "{SlyC}Don't think so small, my friend. We're not just gonna run Hyperion, we're gonna be responsible {SlyB}for plundering a Vault.":
    "{SlyC}别想得那么小，我的朋友。我们不只要掌管 亥博龙，我们还要{SlyB}负责洗劫一个秘藏。",
 "{SlyC}Yeah.": "{SlyC}对。",
 "{smugA}Ah c'mon, it's in the bag.": "{smugA}哎呀拜托，稳稳的。",
 "{SternA}Yeah, yeah, we'll pop champagne and everything after we get back with the key.":
    "{SternA}是啊是啊，等我们带着钥匙回来就开香槟，什么都来。",
 "{WorryA}Please don't jinx us.": "{WorryA}求你别乌鸦嘴。",
 "{SmugA}All in a day's work.": "{SmugA}都是一天的活儿。",
 "[thinking] {SlyA}I mean we gotta do a better job than Handsome Jack.":
    "[thinking] {SlyA}我是说，我们得干得比帅杰克好。",
 "{SmugC}What an excellent idea.": "{SmugC}多棒的主意。",
 "{SmugA}I thought so myself.": "{SmugA}我也这么觉得。",
 "{ThinkA}Or you could ask one of them.": "{ThinkA}或者你可以问问他们中的一个。",
 "{AngryB}Cause I'm strapped to a million Goddamned dollars, that's why.":
    "{AngryB}因为我身上绑着一百万该死的美元，就是这样。",
 "{SternD}You're the closer, right. {SlyA}So close. Get us some direction.":
    "{SternD}你是那个负责谈成的人，对吧。{SlyA}那就去谈成。给我们弄点方向来。",
 "Yeah, I guess that wouldn't be good.": "是啊，我想那不会好。",
 "{worryA}We're on a very strict time limit, here, Rhys. If Vasquez comes down before we're finished... I mean... I don't even...":
    "{worryA}我们时间非常紧，瑞斯。要是 Vasquez 在我们办完之前下来……我是说……我都不敢……",
 "{worryB}I don't know... we can still just find it... I hate asking for help.":
    "{worryB}我不知道……我们还是能自己找到……我讨厌求人帮忙。",
 "{worryA}Time's a wastin', let's figure out where we're going.":
    "{worryA}时间不等人，我们弄清该往哪儿走。",
 "{ThinkB}Not a very handsome fellow, is he?": "{ThinkB}长得可不太俊，对吧？",
 "{WorryA}We don't have all day here, Rhys.": "{WorryA}我们没一整天时间，瑞斯。",
 "Hi, excuse me, uh, sir, do you know where the, uh, \"World of Curiosities\" is?":
    "你好，打扰一下，呃，先生，你知道那个，呃，“奇珍世界”在哪儿吗？",
 "{SmugB}[throat clearing]": "{SmugB}[throat clearing]",
 "You know where the \"World of Curiosities\" is, cause my buddy and I, we gotta be there like, you know, like right now.":
    "你知道“奇珍世界”在哪儿吧，因为我哥们和我，我们得赶到那儿，你知道，就是现在。",
 "{smugC}Hey! Yo Grease face. You know, the guy with the, weird... meat thing.":
    "{smugC}嘿！喂，油脸。你知道，就那个带着个怪……肉乎乎东西的家伙。",
 "{ThinkB}Do you know  where the World of Curiosities is?":
    "{ThinkB}你知道奇珍世界在哪儿吗？",
 "Just kidding, fella.": "开玩笑的，老兄。",
 "What? You got a greasy face.": "怎么？你脸就是油。",
 "I'm sorry, okay?": "对不起，行吗？",
 "Say that again.": "再说一遍。",
 "Repeat what you said.": "把你说的重复一遍。",
 "{WorryB}Rhys, what are you doing?": "{WorryB}瑞斯，你在干什么？",
 "Yeah, Rhys... what are you doing?": "是啊，瑞斯……你在干什么？",
 "{SmugA}I was just kidding, fella, c'mon now.": "{SmugA}我开玩笑的，老兄，别这样。",
 "{SmugC}We're new to-[to Vaughn] {SmugA}It's alright, it's alright.[back to Rudiger] {Worryb}We're new here,  okay, passing through, and we just thought you might be able to give us some directions.":
    "{SmugC}我们是新来——[to Vaughn] {SmugA}没事，没事。[back to Rudiger] {Worryb}我们是新来的，行吗，路过而已，我们只是觉得你也许能给我们指个路。",
 "Look! Get some lotion, get some gel, do a wrap or something... I mean, if you wanna lash out, you know, blame your genes, it's not your fault.":
    "听着！买点润肤乳、发胶、做个敷脸什么的……我是说，你要想发泄，你知道，怪你的基因吧，不是你的错。",
 "{FearB}Oh, look, fella, um, my friend is really, really sorry.":
    "{FearB}哦，听着，老兄，呃，我朋友真的真的很抱歉。",
 "{SlyC}What? You got a greasy face.": "{SlyC}怎么？你脸就是油。",
 "{WorryA}He's got some kind of, uh, condition where he says really stupid crap just to see what'll happen.":
    "{WorryA}他有某种，呃，毛病，会说些特别蠢的废话，就为了看会发生什么。",
 "{worryC}Woah, oh- okay hey, look, you know what, I'm sorry, okay?":
    "{worryC}哇，哦——好，嘿，听着，这样，对不起，行吗？",
 "Do you not speak my language? Ooga booga? Crab got your tongue?":
    "你不会说我的话吗？呜嘎布嘎？螃蟹夹住你舌头了？",
 "What're you lookin' for?": "你在找什么？",
 "Uh...": "呃……",
 "{FearA}It should be around here.": "{FearA}应该就在这附近。",
 "You lost?": "你迷路了？",
 "A simple business deal.": "一笔简单的生意。",
 "{WorryA}Um...": "{WorryA}呃……",
 "What are you here for?": "你们来这儿干什么？",
 "Why do you care?": "关你什么事？",
 "{slyC}Look, guy, it's none of your business why we're here.":
    "{slyC}听着，老兄，我们来这儿干什么不关你的事。",
 "Now if you don't know, you can stop wasting our time and just tell us so we can move on to the next hole of garbage you people call a suburb and see if their morons know any better.":
    "你要不知道，就别浪费我们时间，直接说一声，我们好去下一个你们管它叫郊区的垃圾坑，看看那儿的傻子知不知道。",
 "{Thinkb}Oh my God, {SmugA}who called in the whaaambulance, huh?":
    "{Thinkb}我的天，{SmugA}是谁叫的救护车啊，啊？",
 "{AngryB} Look, if you don't know where the World of Curiosities is, stop wasting our time and just tell us so we can move on to the next hole of garbage that you people call a suburb and see if their morons know any better.":
    "{AngryB} 听着，你要不知道奇珍世界在哪儿，就别浪费我们时间，直接说一声，我们好去下一个你们管它叫郊区的垃圾坑，看看那儿的傻子知不知道。",
 "Oh, you're a right kitten, aren't ya? It's none of my business why you're drivin' your wagon through my town?":
    "哦，你还真是只小猫呢，是吧？你们开着车在我镇上横冲直撞不关我事？",
 "{SmugA}It's just a simple business deal... a few papers to sign, and then we're out, easy.":
    "{SmugA}就是笔简单的生意……签几份文件，然后我们就走，轻松。",
 "Huh. Those the \"papers?\"": "嗯。那些就是“文件”？",
 "[quietly] {FearA}Of a sort.": "[quietly] {FearA}算是吧。",
 "{smugA}Uhhh, why do you even care?": "{smugA}呃，你干嘛在乎？",
 "Because you're drivin' your ass wagon all through my town, kickin' up earth, stirrin' up spiderants, and when the spiderants come, people get killed.":
    "因为你们那辆破车在我镇上到处开，扬起尘土、惊动蛛蚁，而蛛蚁一来，就会有人死。",
 "{FearB}Sorry, um, we didn't...": "{FearB}抱歉，呃，我们不是……",
 "What. are. you. here. for.": "你。们。来。这。儿。干。什。么。",
 "[cold] What are you doin' with a Hyperion car.": "[cold] 你们开着一辆 亥博龙的车干什么。",
 "[cold] You're Hyperion?": "[cold] 你们是 亥博龙的？",
 "You egg-suckers ruined this town, you know that?": "你们这帮吸蛋的毁了这镇子，知道吗？",
 "Everything turned to smoke.": "一切都化成了烟。",
 "Atlas were bastards, but at least they had the good sense to fail.":
    "阿特拉斯是混蛋，但至少他们还有点自知之明，倒掉了。",
 "When Jack came in he turned everything to smoke.":
    "Jack 来了之后，他把一切都化成了烟。",
 "[sigh] {ThinkB}Listen, all we want are directions to the World of Curiosities, that's it, okay? We get that, and we're gone.":
    "[sigh] {ThinkB}听着，我们只想要去奇珍世界的路，就这样，行吗？知道了我们就走。",
 "{ThinkB}[sigh] Okay.": "{ThinkB}[sigh] 好。",
 "{SmugA}What's it gonna take. Huh? How much? Twenty? Fifty?":
    "{SmugA}要多少才行。啊？多少钱？二十？五十？",
 "And it's you and assholes like you that made it happen.":
    "而正是你和你这样的混蛋造成了这一切。",
 "{worryb}Look, man, we really don't know anything about that.":
    "{worryb}听着，老兄，我们真的完全不知道那事。",
 "I think maybe... reparations are in order.": "我觉得也许……该有赔偿。",
 "You know... I thought today was gonna be boring.":
    "你知道……我还以为今天会很无聊。",
 "\"Gone,\" huh?": "“没了”，是吗？",
 "It'd take a lot more than that.": "那可得要多得多。",
 "{FearB}Rhys. Do the...": "{FearB}瑞斯。做那个……",
 "The bot. Yvette. Prime it.": "那台机器人。Yvette。叫它下来。",
 "Hey little man, what's in the case?": "嘿，小家伙，箱子里是什么？",
 "We got a couple Hyperion warmongers, gentlemen.":
    "先生们，我们这儿来了两个 亥博龙好战分子。",
 "You know what we got here?": "你知道我们这儿有什么吗？",
 "{SternA}Okay, now, look... before we get all...[trails off]":
    "{SternA}好，听着……在我们把事情搞……[trails off] 之前。",
 "{FearB}Oh, uh.[beat] Bandits.": "{FearB}哦，呃。[beat] 土匪。",
 "[cold] Ooh. Got quiet all of a sudden.": "[cold] 哦。突然安静了。",
 "{ThinkB}Like I said, I think it's called the World of Curiosities?":
    "{ThinkB}就像我说的，我记得它叫奇珍世界？",
 "[about to run over something] {ShockB}AHHH CRAP!": "[about to run over something] {ShockB}啊啊糟了！",
 "[trying to calm down] {ShockC}Holy freakin' crap, what was... {ShockD}why in a desert world would you cross right there?":
    "[trying to calm down] {ShockC}我的天，那是——{ShockD}在这沙漠星球上你干嘛偏偏从那儿横穿？",
 "[trying to calm down] {ShockB}What did we even-- what did we even hit? {WorryB}I hope that wasn't like a really ugly person.":
    "[trying to calm down] {ShockB}我们到底——我们到底撞到了什么？{WorryB}希望那不是什么很丑的人。",
 "{ShockB}What?": "{ShockB}什么？",
 "{SadA}Ughhh.": "{SadA}呃……",
 "{AngryB}I guess I'm just now acutely aware that I have a million dollars chained to me is all.":
    "{AngryB}我只是刚刚强烈地意识到有一百万美元拴在我身上，就这样。",
 "And she gave me this.{SmugB}[beat] {ThinkA}It is a stun baton. I do not know how it works, but{SlyA} it's definitely neat.":
    "而她还给了我这个。{SmugB}[beat] {ThinkA}这是根电击棒。我不知道它怎么工作，但{SlyA}它绝对很酷。",
 "[blankly] {SmugB}Yeah, a stick. Neato.": "[blankly] {SmugB}是啊，一根棍子。真酷。",
 "I mean, we bring this key back, {HappyC}and they're gonna make us the once and future kings of that place for sure.":
    "我是说，我们把这钥匙带回去，{HappyC}他们肯定会封我们为那地方的千古一帝。",
 "{HappyB}And then that's it.": "{HappyB}然后就这样了。",
 "{NeutralB}Hey, do you know where the \"World of Curiosities\" is?":
    "{NeutralB}嘿，你知道“奇珍世界”在哪儿吗？",
 "{ThinkB}[sigh]Okay.": "{ThinkB}[sigh]好。",
 "{SmugB}Hi, sir, yes, do you... I think I'm gonna just skip this guy.":
    "{SmugB}你好，先生，是的，你……我想我还是跳过这家伙吧。",
 "{SmugB}Well we won't know until you try, will we?":
    "{SmugB}你不试试怎么知道呢，对吧？",
 "{worryB}Good odds.": "{worryB}胜算不错。",
 "{WorryB}I have a feeling he's somewhat inebriated.":
    "{WorryB}我觉得他有点醉了。",
 "{ThinkB}Excuse me, but do you know where the \"World of Curiosities\" is?":
    "{ThinkB}打扰一下，你知道“奇珍世界”在哪儿吗？",
 "Right, well... don't trouble yourself.": "好，那……不劳你费心了。",
 "[quietly] {WorryB}Is there... like a... convention or something...?":
    "[quietly] {WorryB}这是有什么……像那种……集会还是什么……？",
 "{ShockA}[quietly to himself] Bent... huuohhh...":
    "{ShockA}[quietly to himself] 弯的……呼哦哦……",
 "{FearA}Just, we need a Loader Bot, okay? {SternB}Give me the menu.":
    "{FearA}就，我们需要一台装载机器人，行吗？{SternB}把菜单给我。",
 "[processed: cyber talk] [sighs] Already? Really?": "[processed: cyber talk] [sighs] 又要？真的？",
 "And for what?": "为了什么？",
 "then looks up at the crowd, now dangerously encroaching upon them.":
    "然后抬头看向人群，他们现在正危险地逼近。",
 "{SmugB}{SternA}It's... Wait, what? Okay look, it's a boring dusty old town, {HappyA}nothing more, alright?":
    "{SmugB}{SternA}这是……等等，什么？好吧听着，这就是个无聊多灰的老镇子，{HappyA}没别的，行吗？",
 "{AngryA}You know, when you say things like that, I sometimes forget you're pretending to be the guy who would say things like that.":
    "{AngryA}你知道，你说这种话的时候，我有时会忘了你是在假装自己是会说这种话的人。",
 "Just so there's no... misunderstanding.": "只是免得有什么……误会。",
 "do we hear the skag, if so please tag it": "我们能听到异犬的叫声吗，如果能，请打标签",
 "Keep your eyes open.": "睁大眼睛看着。",
 "It's just a town.": "就是个镇子。",
 "Don't be such a wuss.": "别这么怂。",
 "Jack MADE Hyperion.": "是 Jack*造就*了 亥博龙。",
 "We're smarter than he was.": "我们比他聪明。",
 "Jack's nature caught up with him.": "Jack 的本性追上了他。",
 "Excellent idea.": "好主意。",
 "Or, you could ask them.": "或者，你可以问问他们。",
 "I hate asking for help.": "我讨厌求人帮忙。",
 "Excuse me, sir...": "打扰一下，先生……",
 "Hey! Grease face!": "嘿！油脸！",
 "Where is the World of Curiosities?": "奇珍世界在哪儿？",
 "We just want directions.": "我们只想要个方向。",
 "Who called the whaaambulance?": "是谁叫的救护车啊？",
 "Okay, how much will this cost me?": "好，这要我花多少钱？",
 "Talk To": "交谈",
 "Kabob Man": "烤串男",
 "It's a town like any other.": "这就是个跟别处一样的镇子。",
 "Not us, just me.": "不是我们，只有我。",
 "Let's just get the key first.": "我们先拿到钥匙。",
 "Just we need a Loader Bot, okay?": "就是我们需要一台装载机器人，行吗？",
 "Give me the menu.": "把菜单给我。",
 "Loot Container": "战利品容器",
 "Unconscious Man": "昏迷的男人",
 "[pickup1][ALT} So, this looks... interesting.": "[pickup1][ALT} 那么，这看起来……挺有意思。",
 "[pickup1] Not just any stick, a badass Hyperion stick.":
    "[pickup1] 可不是普通的棍子，是根狠角色的 亥博龙棍子。",
 "[pickup1] I don't think Bobby Boy can hold that much weight.":
    "[pickup1] 我觉得小鲍比扛不住那么重。",
 "[pickup1] You know what I mean...": "[pickup1] 你懂我意思……",
 "[pickup1] You're joking. [beat] Right?": "[pickup1] 你在开玩笑。[beat] 对吧？",
 "[pickup1] There's only room at the top for one.": "[pickup1] 顶上只有一个位置。",
 "[pickup1] And next time you need a favor... [beat] I'll totally make you apologize.":
    "[pickup1] 下次你需要帮忙的时候……[beat] 我一定会逼你道歉。",
 "[pickup1] I'll retain this conversation.": "[pickup1] 我会记住这段对话的。",
 "[pickup1] Don't worry, you'll still be my loyal retainer.":
    "[pickup1] 别担心，你依然会是我忠实的随从。",
 "[pickup1][ALT] That guy ran Hyperion -- and Pandora -- into the ground.":
    "[pickup1][ALT] 那家伙把 亥博龙——还有 潘多拉——都搞垮了。",
 "[pickup1][deadpan] Curious.": "[pickup1][deadpan] 有意思。",
 "[pickup1] You're the closer, right?  So go close.":
    "[pickup1] 你是负责谈成的那个人，对吧？那就去谈成。",
 "[pickup1]If I weren't strapped to ten million goddamned dollars.":
    "[pickup1]要不是我身上绑着一千万该死的美元。",
 "[pickup1]I could...": "[pickup1]我可以……",
 "[pickup1] Better hurry. If Vasquez comes down here before we're finished... we'll be... well, finished.":
    "[pickup1] 最好快点。要是 Vasquez 在我们办完之前下来……我们就……嗯，完蛋了。",
 "[pickup1] What is it with sociopaths and asking for directions?":
    "[pickup1] 反社会人格怎么都爱问路？",
 "[pickup1] Yvette. Bot. Now.": "[pickup1] Yvette。机器人。现在。",
 "[pickup1][ALT][pig-Latin] Vette-Ee-ay. Oaderbot-Lay. Ow-Nay.":
    "[pickup1][ALT][pig-Latin] Vette-Ee-ay。Oaderbot-Lay。Ow-Nay。",
 "[pickup1] I hate asking for directions.": "[pickup1] 我讨厌问路。",
})

# —— ECHO 资料卡 + 车内问答 ——
T.update({
 "^color:#ffea7f^Suspended Monorail\n^color:white^Manufacturer: Atlas\n^color:white^Analysis: Structural weakpoints. Susceptible to explosives.*\n\n^color:white^*Hyperion does not endorse or condone inter-corporate sabotage. On a totally and completely unrelated note, please remember that employees who take initiative are often most prized for management positions.":
    "^color:#ffea7f^悬挂式单轨列车\n^color:white^制造商: 阿特拉斯\n^color:white^分析: 结构弱点。易受爆炸物破坏。*\n\n^color:white^*亥博龙不赞同也不纵容企业间破坏行为。在一件完全、彻底无关的事情上，请记住：主动做事的员工往往最受管理岗青睐。",
 "^color:#ffea7f^ Dahl Ammunitions Box\n^color:#ffea7f^Loot outlook: good":
    "^color:#ffea7f^ 达尔弹药箱\n^color:#ffea7f^战利品前景: 良好",
 "^color:#ffea7f^Dahl Ammunitions Box\n^color:white^ So empty inside":
    "^color:#ffea7f^达尔弹药箱\n^color:white^ 里面空空的",
 "^color:#ffea7f^Dahl Ammunitions Box\n^color:white^Loot Outlook: Good":
    "^color:#ffea7f^达尔弹药箱\n^color:white^战利品前景: 良好",
 "^color:#ffea7f^Kebab composition:\n^color:white^69% Skag Meat\n^color:white^28% Wood\n^color:white^3% ????":
    "^color:#ffea7f^烤串成分:\n^color:white^69% 异犬肉\n^color:white^28% 木头\n^color:white^3% ？？？？",
 "^color:#ffea7f^\"Dook Hut\"\n^color:white^Portable Chemical Toilet\n^color:#ffea7f^Manufacturer: ^color:white^Dahl\n^color:#ffea7f^Model: ^color:white^109VE \"Titan Class\"\n^color:#ffea7f^Probability of Containing Loot: ^color:white^Weirdly High\n\n^color:white^\"For the Pandoran with a Titan ass, make sure your toilet is Titan Class.\"":
    "^color:#ffea7f^“大便小屋”\n^color:white^便携式化学马桶\n^color:#ffea7f^制造商: ^color:white^达尔\n^color:#ffea7f^型号: ^color:white^109VE“泰坦级”\n^color:#ffea7f^含战利品概率: ^color:white^高得离谱\n\n^color:white^“献给屁股如泰坦的 潘多拉 人，务必确认你的马桶是泰坦级。”",
 "^color:#ffea7f^ Skag Kebabs, a staple and delecacy of Pandora.":
    "^color:#ffea7f^ 异犬烤串，潘多拉 的主食兼美味。",
 "[postpax] Yeah, no, I know... I--I guess I'm just now more acutely aware that I have 10 million dollars chained to me is all.":
    "[postpax] 是啊，不，我知道……我——我只是刚更强烈地意识到有一千万美元拴在我身上，就这样。",
 "You do know we're getting out of the car eventually...":
    "你知道我们最终是要下车的吧……",
 "[distracted] [postpax] What do you mean?": "[distracted] [postpax] 你什么意思？",
 "[postpax] I mean what do we tell people? We should have a story.":
    "[postpax] 我是说我们跟人怎么说？我们该有个说法。",
 "So... What do we say if someone asks where we got the money?":
    "那……要是有人问我们钱哪儿来的，我们怎么说？",
 "[postpax] I would prefer not to tell them that we stole it from Hyperion.":
    "[postpax] 我更倾向于不要告诉他们我们是从 亥博龙偷的。",
 "[postpax] I just think we need a plan of some sort.":
    "[postpax] 我只是觉得我们需要某种计划。",
 "[postpax] That would not go over well.": "[postpax] 那不会有好结果。",
 "Vasquez gave it to us.": "是 Vasquez 给我们的。",
 "It's for a charity.": "这是给慈善机构的。",
 "The truth. We stole it.": "说实话。我们偷的。",
 "[postpax] [sigh] Uh, ok--okay, I guess we just say we're his personal assistants...  I mean, he's got enough of those, it wouldn't surpise anyone.":
    "[postpax] [sigh] 呃，好——好吧，我想我们就说我们是他的私人助理……我是说，他那种人多得是，没人会奇怪。",
 "[postpax] Let's just say Vasquez gave it to us to make the deal. It's easier that way.":
    "[postpax] 我们就说 Vasquez 把钱给我们去做这笔交易。这样说省事。",
 "[postpax] Yeah... I guess I wanted a cooler plan, but I suppose that'll work.":
    "[postpax] 是啊……我本来想要个更酷的说法，但我想这样也行。",
 "[postpax] We say it's some sort of \"Open a Vault for Pandorans,\" kind of deal. People love stuff when it's attached to a charity. They hardly ever question their intentions.":
    "[postpax] 我们就说这是某种“为 潘多拉 人开秘藏”之类的项目。人们一听到慈善就喜欢，几乎从不质疑动机。",
 "[postpax] We can just say it's for charity.": "[postpax] 我们就说是做慈善的。",
 "[postpax] What does that even mean?": "[postpax] 那到底是什么意思？",
 "[postpax] Okay, that makes sense.": "[postpax] 好，这说得通。",
 "[postpax] Hey, we're on Pandora. We'll actually get more street cred if it seems like we're bigger criminals than we are.":
    "[postpax] 嘿，我们在 潘多拉。要是我们显得比实际更像大罪犯，反而更有江湖地位。",
 "[postpax] How is that a good idea?": "[postpax] 那怎么就算好主意了？",
 "[postpax] We just tell 'em the truth... that we stole it.":
    "[postpax] 我们就跟他们说实话……是我们偷的。",
 "Create a distraction.": "制造点骚动。",
 "[postpax] Oh, hey, your fly's down. Eh? Eh?": "[postpax] 哦，嘿，你拉链开了。嗯？嗯？",
 "[postpax] I don't think that's gonna work.": "[postpax] 我觉得那不管用。",
 "[postpax] What? How?": "[postpax] 什么？怎么不行？",
 "[postpax] We just need to create some sort of distraction.":
    "[postpax] 我们只需要制造某种骚动。",
 "^color:#ffea7f^Vasquez's Car\n^color:white^Hyperion Bolt 4600 S series.\n^color:white^Damage: \n^color:white^  Rugged detailing (Minor scratches and dents)\n^color:white^  Paint effects (Skag residue)\n\n^color:white^\"No one cares if you're overcompensating when it looks this good.\"":
    "^color:#ffea7f^Vasquez 的车\n^color:white^亥博龙Bolt 4600 S 系列。\n^color:white^损伤: \n^color:white^  粗犷细节（轻微划痕与凹痕）\n^color:white^  涂装效果（异犬残留物）\n\n^color:white^“只要看起来这么帅，没人在乎你是不是在过度补偿。”",
 "^color:white^Vaughn\n^color:#ffea7f^Age: ^color:white^27\n^color:#ffea7f^Hyperion Employee ID: ^color:white^RM-9452\n^color:#ffea7f^Occupation: ^color:white^Accountant\n^color:#ffea7f^Favorite Color: ^color:white^Goldenrod\n^color:#ffea7f^Favorite Book: ^color:white^\"Mind the GAAP: Generally-Accepted Accounting Principles and You!\"\n\n^color:#ffea7f^Current Status: ^color:white^Sweaty":
    "^color:white^沃恩\n^color:#ffea7f^年龄: ^color:white^27\n^color:#ffea7f^亥博龙员工编号: ^color:white^RM-9452\n^color:#ffea7f^职业: ^color:white^会计\n^color:#ffea7f^最喜欢的颜色: ^color:white^金菊黄\n^color:#ffea7f^最喜欢的书: ^color:white^“谨守 GAAP：公认会计原则与你！”\n\n^color:#ffea7f^当前状态: ^color:white^一身汗",
 "^color:#ffea7f^Atlas Logo\n^color:white^Atlas Mining Company\n\n^color:white^After kicking off the Vault arms race, Atlas royally dropped a steamer in their drawers when they tried to pull one over on Hyperion. Those losers got booted off Pandora so hard I lost a shoe. HA. I rule. -HandsomeJack69\n\n^color:red^[ADMIN:Can someone please reset admin privileges so we can revise this? It's highly inappropriate.]":
    "^color:#ffea7f^阿特拉斯标志\n^color:white^阿特拉斯矿业公司\n\n^color:white^在引爆秘藏军备竞赛之后，阿特拉斯想坑 亥博龙，结果彻底拉了一裤裆。那帮废物被踢出 潘多拉 的力度之大，我连鞋都掉了。哈。我最强。——帅杰克69\n\n^color:red^[管理员：能有人重置一下管理员权限让我们改这条吗？这内容非常不合适。]",
 "^color:#ffea7f^Kebab\n^color:#ffea7f^Contents:\n^color:white^  -64% Skag Meat\n^color:white^  -35% Other Meat\n\n^color:white^\"A big, full-bodied kebab that is excellent as a before -- or after -- murder meal. Rudiger's deeply-colored kebab, consisting of skag meat and other meat, is sweet and aromatic. Its delectable smoothness is due to a low acid content, delivering a rich earthy flavor.\" - Mayhew Pontifex, Local Kebabisseur":
    "^color:#ffea7f^烤串\n^color:#ffea7f^内容物:\n^color:white^  -64% 异犬肉\n^color:white^  -35% 其他肉\n\n^color:white^“一串硕大饱满的烤串，作为谋杀前——或谋杀后——的餐点都极佳。Rudiger 这串色泽深浓的烤串由异犬肉和其他肉组成，香甜芬芳。其可口的顺滑感来自低酸度，带来浓郁的土地风味。”——Mayhew Pontifex，本地烤串行家",
 "^color:white^Suspended Monorail\n^color:#ffea7f^Manufacturer: ^color:white^Atlas\n^color:#ffea7f^Analysis: ^color:white^Structural weakpoints. Susceptible to explosives.*\n\n*Hyperion does not endorse inter-corporate sabotage. On a completely unrelated note, remember that taking initiative is a great trait for management material!":
    "^color:white^悬挂式单轨列车\n^color:#ffea7f^制造商: ^color:white^阿特拉斯\n^color:#ffea7f^分析: ^color:white^结构弱点。易受爆炸物破坏。*\n\n*亥博龙不纵容企业间破坏行为。在一件完全无关的事情上，请记住：主动做事是管理人才的一大优点！",
 "^color:white^Hyperion Bolt 4600 S series.\n^color:#ffea7f^Manufacturer: ^color:white^Hyperion  \n^color:#ffea7f^Analysis: ^color:white^Super awesome\n^color:#ffea7f^Top speed: ^color:white^Super fast\n^color:#ffea7f^Cost: ^color:white^If you have to ask...\n\n\"No one cares if you're overcompensating when it looks this good.\"":
    "^color:white^亥博龙Bolt 4600 S 系列。\n^color:#ffea7f^制造商: ^color:white^亥博龙 \n^color:#ffea7f^分析: ^color:white^超级棒\n^color:#ffea7f^最高时速: ^color:white^超级快\n^color:#ffea7f^价格: ^color:white^这还要问的话……\n\n“只要看起来这么帅，没人在乎你是不是在过度补偿。”",
 "^color:white^Atlas\n^color:#ffea7f^Primary Industries: \n^color:white^-Weapons\n-Mining\n-Finding Vaults\n-Getting beaten by Handsome Jack\n\n^color:white^HA. I rule.\n^color:#CC1919^ \\<last edited by user ~HJack69~ 342 days ago\\>":
    "^color:white^阿特拉斯\n^color:#ffea7f^主要产业: \n^color:white^-武器\n-采矿\n-寻找秘藏\n-被帅杰克打败\n\n^color:white^哈。我最强。\n^color:#CC1919^ \\<最后由用户 ~HJack69~ 于 342 天前编辑\\>",
 "^color:white^Local \"food\"\n^color:#ffea7f^Contents:\n^color:white^-64% Skag Meat\n-35% Other Meat\n-01% Smoke\n^color:#ffea7f^Nutrition: ^color:white^(Awaiting results - Assigned food tester in hospital)":
    "^color:white^本地“食物”\n^color:#ffea7f^内容物:\n^color:white^-64% 异犬肉\n-35% 其他肉\n-01% 烟尘\n^color:#ffea7f^营养: ^color:white^（待结果——指定试吃员已送医）",
 "Skag Cart": "异犬摊车",
 "Porto-Potty": "移动厕所",
 "Vasquez Mobile": "Vasquez 座驾",
 "Vaughn": "沃恩",
 "Atlas Logo": "阿特拉斯标志",
})

# —— 补漏：撞死斯凯格后的对话变体 ——
T.update({
 "Power": "电源",
 "{WorryC}I don't know, it looks like a...": "{WorryC}我不知道，它看起来像一只……",
 "Like some kind of alien dog or something.": "像某种外星狗之类的。",
 "It's only a skag.": "只是只异犬而已。",
 "{SadA}Still. It's kinda sad.": "{SadA}还是啊。有点难过。",
 "[uncaring]{SmugA}Yeah.[beat] \"Kinda.\"": "[uncaring]{SmugA}是啊。[beat] “有点。”",
 "{ShockA}Relax, {HappyB}Vaughn, it's a skag. {SlyC}They breed like hostile rabbits down here.":
    "{ShockA}放松，{HappyB}沃恩，这就是只异犬。{SlyC}它们在这下面像敌意兔子一样繁殖。",
 "[annoyed]{AngryA}Vaughn...[quick sigh] I'm more worried about the dent in the car, okay.":
    "[annoyed]{AngryA}沃恩……[quick sigh] 我更担心车上的那个坑，行吗。",
 "{AngryA}First of all, it's Vasquez's company lease, and second, I'm sorry that I... brake for birds or whatever, but...":
    "{AngryA}第一，那是 Vasquez 的公司租赁车；第二，我很抱歉我……为鸟刹车还是怎么着，但……",
 "{ShockA}Well... {WorryB}at least it didn't suffer.": "{ShockA}好吧……{WorryB}至少它没受苦。",
 "[quietly] {SadA}Yeah, I guess.": "[quietly] {SadA}是啊，我想是。",
 "Sucks, though.": "不过真糟。",
 "[to himself] {worryA}Yeah.[beat] Sucks.": "[to himself] {worryA}是啊。[beat] 真糟。",
 "{ThinkA}I didn't say anything.": "{ThinkA}我什么都没说。",
 "What about the car?": "那车怎么办？",
 "{ShockC}[about to run over something] Aggggghhh!": "{ShockC}[about to run over something] 啊啊啊啊啊！",
 "Just keep your eyes open.": "盯紧点看着。",
})
