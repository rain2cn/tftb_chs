# 第2章 env_04（空心镇 Scooter 车库，Fiona 线：讨价还价修车 → Hodunk 敲诈 → Rhys/Vaughn 车内闲谈）
T = {
 # —— 说话人 ——
 "FIONA": "FIONA", "SASHA": "SASHA", "SCOOTER": "SCOOTER", "AUGUST": "AUGUST",
 "RHYS": "RHYS", "VAUGHN": "VAUGHN", "JACK": "JACK", "VALLORY": "VALLORY",
 "TECTOR": "TECTOR", "JIMBO": "JIMBO", "FINCH": "FINCH", "KROGER": "KROGER",
 "[Silence]": "[Silence]", "...": "……",
 # —— 选择 / 交互标签 ——
 "[Offer Cash]": "[给现金]", "[Offer General's Ring]": "[给将军的戒指]",
 "[Offer War Medal]": "[给军功章]", "[Shoot August]": "[朝 August 开枪]",
 "[Surrender]": "[投降]", "[shrug sorry]": "[耸耸肩，抱歉]",
 "[Stare down]": "[对视]", "[Crumple photo]": "[揉皱照片]",
 "[Squeeze Sasha's hand]": "[捏紧 Sasha 的手]", "[Throw bucket]": "[扔水桶]",
 "[Wave Sasha Over]": "[招手让 Sasha 过来]", "[Motion to Stay Put]": "[示意别动]",
 "[Deadstick]": "[装死]", "[Sell Out]": "[出卖自己]",
 "[Retain Dignity]": "[保住尊严]", "[Happy squeak]": "[开心地吱一声]",
 "Catch-A-Riiiiiiiiiiiiiiide!": "Catch-A-Riiiiiiiiiiiiiiide！",
 # —— 让 Scooter 免费修车的对白选择 ——
 "I changed my mind.": "我改主意了。",
 "Let's trade.": "我们做个交换。",
 "You are so paranoid!": "你也太疑神疑鬼了！",
 "No. I did not make a deal.": "不。我没做交易。",
 "Yeah. I made a deal.": "是啊。我做了交易。",
 "I'm keeping my badge.": "我要留着我的证件。",
 "Let's be safe and remove them.": "保险起见，把它们摘了吧。",
 "Ok. But I'm Hyperion at heart.": "好。但我心里还是 亥博龙的人。",
 "Dood. Bros for life.": "哥们。一辈子的兄弟。",
 "I'm going to punch Vasquez.": "我要去揍 Vasquez。",
 "I said I didn't make a deal!": "我说了我没做交易！",
 "Man, I had to make a deal.": "天哪，我不得不做交易。",
 "She's can handle herself.": "她能照顾好自己。",
 "Yeah Vasquez was listening.": "是啊，Vasquez 在听。",
 "What do you want from me?": "你想让我怎样？",
 "I don't need friends.": "我不需要朋友。",
 "You're right Vaughn.": "你说得对，沃恩。",
 "On Pandora, Friends kill Friends.": "在 潘多拉，朋友杀朋友。",
 # —— Fiona / Sasha 抵达车库 ——
 "This is Vallory's turf. We have to be careful.": "这是 瓦洛里 的地盘。我们得小心。",
 "Sit tight.": "别动。",
 "Jeez. It's gonna be spendy.": "天哪。这得花不少钱。",
 "Hey Fioner. Glad to be of service.": "嘿 Fioner。很高兴为你效劳。",
 "It's all we got.": "我们就只有这个了。",
 "No trouble. But you're gonna need parts. And those ain't easy to find.":
    "不麻烦。但你需要零件。而那些可不好找。",
 "Thanks, but I can fix my own van.": "谢了，但我能自己修我的车。",
 "Please. Take it.": "拜托。拿着吧。",
 "I insist.": "我坚持。",
 "Don't worry. I'll give you the Scooter discount.": "别担心。我给你走 斯库特 折扣。",
 "Naw, you know me better'an that.": "不，你该知道我比那强。",
 "Nice and shiny. You keep it.": "又漂亮又闪。你留着吧。",
 "What a purdy medal. But that' s somethin' a man's gotta earn.":
    "多漂亮的勋章。但那得是男人挣来的东西。",
 "You could alway catch-a-ride with me to my garage, but this ain't no oil change we're talkin 'bout. No, ma'am, this here's a biggun'.":
    "你随时可以搭我的车去我车库，但咱们这可不是换换机油的事。不，女士，这可是大活儿。",
 "Hope you brought plenty of money, because I can tell from here that everthing's broken. Kaput. Fi-ni-to.":
    "希望你带够了钱，因为我从这儿就能看出来，一切都坏了。完蛋。彻——底。",
 "By the looks of it, you need major repairs.": "看样子，你需要大修。",
 "The kind that cost major mula.": "那种要花大钱的。",
 "I'd love to give you the Scooter discount, but no amount I take off would cover all the repairs.":
    "我很想给你走 斯库特 折扣，但我减掉多少都不够覆盖全部修理费。",
 "I appreciate yer kindly offer, but yer gonna need way more for all the parts.":
    "我感谢你的好意，但买齐这些零件你需要多得多。",
 "We're talkin' a tappet head, a knurled piston, maybe a hill holder, prolly a harmonic compensator, definitely a hog trough...":
    "咱们说的是一个挺杆头、一个滚花活塞、也许一个坡道辅助器、大概一个谐波补偿器、肯定还有一个猪食槽……",
 "Aw, Sasha. You know I'm always at your service. [to Fiona] And you.":
    "哦，萨莎。你知道我随时为你效劳。[to Fiona] 你也一样。",
 "Help you think I can?": "帮你们？我想我能。",
 "Think you can help us out?": "你觉得你能帮我们吗？",
 "I'll get my tools.": "我去拿工具。",
 "That's a beaut.": "这可真漂亮。",
 "It's nuthin'.": "没什么。",
 "Oh, right. Yer van.": "哦，对。你们的车。",
 "Thanks a bunch.": "多谢。",
 "Get off me!": "别压着我！",
 # —— August 的人绑走 Fiona/Sasha ——
 "Don't look surprised. Mama's got eyes everywhere.":
    "别装惊讶。妈到处都有眼睛。",
 "You're coming with us. Mama always gets the truth.":
    "你们跟我们走。妈总能拿到真相。",
 "Ooph.": "呃。",
 "[re: Sasha] How many times I gotta tell you to stay away from my girl?":
    "[re: Sasha] 要我跟你说多少遍离我的姑娘远点？",
 "The hell we are.": "去你的。",
 "Sack 'em!": "把他们套起来！",
 "[desperate] We'll go with you.": "[desperate] 我们跟你走。",
 "Sack 'em! \nAn extremely intimidating Henchman #2, heretofore unseen, emerges from August's racer. Cut to a black hood pulled over player's view, and sounds of scuffling and tazer zaps.":
    "把他们套起来！\n一个此前未出场、极其吓人的二号打手从 August 的赛车中现身。镜头切到玩家视野被黑布罩住，伴随着扭打声与电击枪的啪啪声。",
 "No!\nAn extremely intimidating Henchman #2, heretofore unseen, emerges from August's racer. Cut to a black hood pulled over player's view, and sounds of scuffling and tazer zaps.":
    "不！\n一个此前未出场、极其吓人的二号打手从 August 的赛车中现身。镜头切到玩家视野被黑布罩住，伴随着扭打声与电击枪的啪啪声。",
 "No. \nAn extremely intimidating Henchman #2, heretofore unseen, emerges from August's racer. Cut to a black hood pulled over player's view, and sounds of scuffling and tazer zaps.":
    "不。\n一个此前未出场、极其吓人的二号打手从 August 的赛车中现身。镜头切到玩家视野被黑布罩住，伴随着扭打声与电击枪的啪啪声。",
 "[to Fiona] Don't make this hard.": "[to Fiona] 别把事情搞复杂。",
 "They're not friends. And we ditched them.": "他们不是朋友。而且我们甩掉他们了。",
 "Where's your new friends?": "你们的新朋友呢？",
 "I'm sure it's not that bad. Let's check it out.": "我确定没那么糟。我们去看看。",
 "[re: the van] Let's check it out.": "[re: the van] 我们去看看。",
 "We're going to Felix's safehouse to find his contact list. We'll be back soon.":
    "我们去 菲利克斯 的安全屋找他的联系人名单。我们很快回来。",
 "Nothing we can't handle.": "没什么我们应付不了的。",
 "At least we know it can't get worse.": "至少我们知道不可能更糟了。",
 "Is it weird that I kinda like the smell? At least we know it can't get worse.":
    "我有点喜欢这味道，这算怪吗？至少我们知道不可能更糟了。",
 "We died and went to hell.": "我们死了，下地狱了。",
 "I knew there was a tiny little optimist drowning inside you somewhere.":
    "我就知道你心里某个地方淹着一个小小的乐观主义者。",
 "[giddy] It's so dark, I almost feel safe here.": "[giddy] 这么黑，我在这儿几乎感觉安全。",
 "Has anyone seen Vaughn? Is Vaughn in there?": "有人见到 沃恩 了吗？沃恩 在里面吗？",
 "Hey! I'm still fully capable of being miserable.": "嘿！我完全还有能力悲惨下去。",
 "This place is disgusting, and suddenly you're okay with everything.":
    "这地方恶心死了，而你突然对一切都无所谓了。",
 "It's not that I'm okay, it's just that it's so dark and breezy, it's refreshing in a revolting way.":
    "不是我无所谓，只是这儿又黑又通风，以一种令人作呕的方式让人觉得清爽。",
 "What's the matter with you?!": "你有什么毛病？！",
 "I hate it, all right? It's cold, it reeks, and I'm miserable. Happy?":
    "我讨厌这儿，行吗？又冷又臭，我难受死了。满意了？",
 "Relieved. For a minute I thought I'd lost you.": "是放心。刚才有一分钟我以为我把你弄丢了。",
 "I think the moonshots killed us and we're in hell.": "我觉得月球投射把我们炸死了，我们在地狱里。",
 "It's not that bad.": "没那么糟。",
 "Oh. my. God. Somebody stole Vaughn and replaced him with a person!":
    "我的。天。哪。有人把 沃恩 偷走了，换成了一个真人！",
 "It means suddenly you're exhibiting human qualities like hope and optimism. I dare say you're even a tad cheerful.":
    "意思是突然之间你表现出了希望、乐观这类人类特质。我敢说你甚至有点愉快。",
 "Vaughn's back.": "沃恩 回来了。",
 "It's so dank and murky I feel like no one could ever find us.":
    "又潮又暗，我感觉没人能找到我们。",
 "Say what you will, this place has character. It's not as bad as I thought.":
    "随你怎么说，这地方有个性。没我想的那么糟。",
 "I get it. It smells. There's rats everywhere. But you could also blend in. You could be anything you want and no one would care.":
    "我懂。它有味儿。到处都是老鼠。但你也可能混进去。你可以当任何你想当的人，而且没人在乎。",
 "I don't know about you, but this town makes me feel kinda free.":
    "我不知道你怎么想，但这镇子让我觉得有点自由。",
 "I can't believe I'm saying this, but I actually don't hate it.":
    "我不敢相信我居然说这话，但我其实不讨厌它。",
 # —— Jack AI 抱怨 Pandora 人恨他 ——
 "Death to Hyperion? Is this some kind of joke? I'm a hero to all Pandorans. What's wrong with these people?":
    "亥博龙去死？这是个玩笑吗？我是所有 潘多拉 人的英雄。这些人怎么回事？",
 "You were misunderstood.": "你被误解了。",
 "You were a tyrant.": "你是个暴君。",
 "They've moved on.": "他们已经翻篇了。",
 "They didn't realize that everything you did was for them. If you don't mind my saying, they weren't worthy of your gifts.":
    "他们没意识到你所做的一切都是为了他们。恕我直言，他们配不上你的馈赠。",
 "No, no, no. Everyone is worthy. My brilliance should be shared by all.":
    "不不不。人人都配得上。我的光辉该由所有人共享。",
 "I couldn't agree more.": "我完全同意。",
 "This guy's a keeper.": "这家伙值得留下。",
 "I'm gonna lay it out cause you're dead. Pandorans hated you. They thought you were a murderous tyrant.":
    "我直说吧，因为你已经死了。潘多拉 人恨你。他们以为你是个嗜杀的暴君。",
 "I was the savior of Pandora and the glory of Hyperion!":
    "我是 潘多拉 的救世主，是 亥博龙的荣光！",
 "[re: Vaughn] What's wrong with him?": "[re: Vaughn] 他怎么了？",
 "You were the worst of the worst. A vicious homicidal dictator who destroyed anything and anyone that got in your way. \nHJAI [flattered] Really?":
    "你是最坏里的最坏。一个恶毒的、嗜杀的独裁者，毁掉了任何挡你路的东西和人。\nHJAI [flattered] 真的？",
 "They're worthless bottom feeders. They have no idea what you tried to do for the good of Pandora.":
    "他们是不值一提的底层蛀虫。他们根本不知道你为了 潘多拉 的利益想做什么。",
 "Thank you. Can I get an Amen?": "谢谢你。能给我个“阿门”吗？",
 "Amen, brother.": "阿门，兄弟。",
 "Don't brown nose.": "别拍马屁。",
 "I am so sorry.": "我非常抱歉。",
 "You're doing it again.": "你又来了。",
 "[genuinely disturbed] Since I died, nothing makes sense...":
    "[genuinely disturbed] 自从我死了之后，一切都说不通了……",
 "How could they not revel in my magnificence? My pure unadulterated Handsome Jackness? Has the world gone mad?":
    "他们怎么能不沉浸在我的伟大里？我那纯粹无杂质的帅杰克本色？这世界疯了吗？",
 "There's got to be an explanation.": "肯定有个解释。",
 "How could they be so blind?": "他们怎么能这么瞎？",
 "I don't get it. Everybody loves me. I'm a gift to Pandora.":
    "我不懂。人人都爱我。我是给 潘多拉 的礼物。",
 "This must be a mistake. Somebody's spreading lies. I'm like a god to these people. I am a god.":
    "这肯定是个错误。有人在散布谣言。对这些人来说我就像神。我就是神。",
 "To hell with Athena. We should get you to a shrink.": "雅典娜 去死吧。我们该带你去看心理医生。",
 "Not again.": "别又来。",
 "Who's moved on?": "谁翻篇了？",
 "Forget Athena. We need to find you a shrink.": "别管 雅典娜 了。我们得给你找个心理医生。",
 "We've passed these dumpsters ten times already.": "这些垃圾箱我们已经走过十遍了。",
 "Not so proud to be Hyperion now, huh? [to the henchmen] Sack'em.":
    "现在没那么以 亥博龙为傲了吧，哈？[to the henchmen] 把他们套起来。",
 "Howdy.": "你好啊。",
 "[motioning to their shirts] But for godsakes, take off your Hyperion badges.":
    "[motioning to their shirts] 但看在上帝份上，把你们的 亥博龙证件摘了。",
 "No, seriously, you should take them off. It's a 100% surefire way to get yourself killed.":
    "不，说真的，你们该摘了。这是 100% 保证送命的办法。",
 "It's up to you. I mean if you really feel it's worth dying over your ungrateful, lameass corporate overlords then by all means.":
    "看你们自己。我是说，你要是真觉得为你们那些不知感恩、烂透了的公司主子去死值得，那就请便。",
 "You'd have to be suicidal to keep those things on.": "想死才留着那些玩意儿。",
 "It's your call.": "你决定。",
 "I just think you'd have to be crazy or have balls of steel to walk around with what's basically a target painted on your face.":
    "我只是觉得，身上顶着个基本等于脸上画了靶子的东西到处走，你要么疯了，要么胆大如钢。",
 "It stays.": "留着。",
 "I hate to do it.": "我很不情愿。",
 "Not a problem.": "没问题。",
 "These logos represent everything we stand for. Without them, we're nothing.":
    "这些标志代表着我们所主张的一切。没有它们，我们什么都不是。",
 "It's your funeral.": "那是你自找的。",
 "Maybe she has a point.": "也许她说得对。",
 "Don't say it.": "别说。",
 "This badge represents years of stepping on the heads of the weak and the slow. It stays.":
    "这证件代表着多年来踩在弱者和慢者的头上。留着。",
 "[re: Vaughn] I just threw up a little.": "[re: Vaughn] 我刚吐了一点点。",
 "[heading the opposite way] Excellent.": "[heading the opposite way] 太好了。",
 "I feel so naked. So free.": "我觉得好赤裸。好自由。",
 "We need this vault.": "我们需要这座秘藏。",
 "The docks are the other way.": "码头在另一边。",
 "Athena awaits. To the docks.": "雅典娜 在等我们。去码头。",
 "My nipple!": "我的乳头！",
 "Not a problem. Hyperion's in the past.": "没问题。亥博龙已是过去。",
 "To the docks. Athena awaits.": "去码头。雅典娜 在等。",
 "It's better when you don't talk.": "你不说话的时候更好。",
 "You can take the man out of Hyperion, but you can't take Hyperion out of the man.":
    "你能把人带出 亥博龙，但没法把 亥博龙从人心里带走。",
 "That's in the past. We're all about the vault now.":
    "那是过去了。我们现在只关心秘藏。",
 "I thought Hyperion meant something to us.": "我以为 亥博龙对我们有点意义。",
 "Hyperion to the end, huh?": "亥博龙到死方休，哈？",
 "Not so proud to be Hyperion now, eh?": "现在没那么以 亥博龙为傲了，嗯？",
 "Sit tight, I'll pop the hood while we wait for Scooter.":
    "别动，等 斯库特 的时候我把引擎盖掀开。",
 "[glancing back to make sure Sasha can't hear] You know what? I can fix my own van. Sorry for the trouble.":
    "[glancing back to make sure Sasha can't hear] 你知道吗？我能自己修我的车。抱歉添麻烦了。",
 "Don't hurt him.": "别伤他。",
 "[oblivious]<<id:362795093>> Is it weird that I kinda like the smell? At least we know it can't get worse.":
    "[oblivious]<<id:362795093>> 我有点喜欢这味道，这算怪吗？至少我们知道不可能更糟了。",
 "And no one can take that away from you.": "而没人能把这个从你身上拿走。",
 "If you don't mind my saying, they weren't worthy of your gifts.":
    "恕我直言，他们配不上你的馈赠。",
 "You were a homicidal dictator who destroyed everything and everyone that got in your way. \nHJAI [flattered] Really?":
    "你是个嗜杀的独裁者，毁掉了任何挡你路的东西和人。\nHJAI [flattered] 真的？",
 "Times change. They've moved on.": "时代变了。他们翻篇了。",
 "Amen!": "阿门！",
 "Death to Hyperion? Is this a joke? I'm a hero to Pandorans. What's wrong with these people?":
    "亥博龙去死？这是个玩笑吗？我是 潘多拉 人的英雄。这些人怎么回事？",
 "If you don't mind my saying, they're not worthy of your gifts.":
    "恕我直言，他们配不上你的馈赠。",
 "Death to Hyperion? Is this a joke? I'm a hero to all Pandorans. What's wrong with these people?":
    "亥博龙去死？这是个玩笑吗？我是所有 潘多拉 人的英雄。这些人怎么回事？",
 "You were the worst of the worst. A homicidal dictator who destroyed everything and everyone that got in your way. \nHJAI [flattered] Really?":
    "你是最坏里的最坏。一个嗜杀的独裁者，毁掉了任何挡你路的东西和人。\nHJAI [flattered] 真的？",
 "[re: Rhys] Thank you. Can I get an amen?": "[re: Rhys] 谢谢你。能给我个“阿门”吗？",
 "Awg!": "嗷！",
 "We're getting Felix's contact list. It shouldn't take long.":
    "我们去拿 菲利克斯 的联系人名单。应该不会太久。",
 "I'm gonna lay it out cause you're dead. You were a murderous tyrant.":
    "我直说吧，因为你已经死了。你是个嗜杀的暴君。",
 "This must be a mistake. I'm like a god to these people. What am I saying? I am god.":
    "这肯定是个错误。对这些人来说我就像神。我在说什么？我就是神。",
 "[incredulous] Somebody lied to these people. My Handsome Jackness is there for the taking and they're missing it. Can I get an Amen?":
    "[incredulous] 有人骗了这些人。我的帅杰克本色就在那儿任人取用，而他们居然错过了。能给我个“阿门”吗？",
 "[Winces, burned hand]": "[Winces, burned hand]",
 "Whoops. That's not good.": "哎呀。这可不好。",
 "Yeah. I'm guessing that's not factory standard.":
    "是啊。我猜那不是原厂标准配置。",
 "Take them to the Purple Skag.": "把他们带到紫异犬。",
 "Take them to The Purple Skag.": "把他们带到紫异犬。",
 "Where's Sash at?": "Sash 在哪儿？",
 "Here's how to impress her.": "这就是讨好她的办法。",
 "Sasha stepped out.": "萨莎 出去了。",
 "If you want to impress her, you'll fix the van.": "你想讨好她，就把车修了。",
 "She's in the van.": "她在车里。",
 "Think it'd be alright if I said howdy?": "我说声“你好”应该没关系吧？",
 "I got supplies. I got ever'thin' in mah truck. Even a pimen-taco if you're hankerin for some grub.":
    "我有补给。我卡车里什么都有。你要是想垫点肚子，连辣椒塔可都有。",
 "Scooter. The Van. Focus.": "斯库特。车。专注。",
 "She went to get some supplies.": "她去买补给了。",
 "She doesn't want to see you.": "她不想见你。",
 "I'm sorry, but it's the truth.": "抱歉，但这是实话。",
 "Them there's painful words.": "这话可真扎心。",
 "I won't bite. Hard. Just kiddin'. [to himself] Guess I ain't helpin' mah cause.":
    "我不咬人。不使劲咬。开玩笑的。[to himself] 看来我这是在自己拆自己的台。",
 "I just wanna talk.": "我就想聊聊。",
 "Looky here. I'll fix your van. But I gotta see Sasha first. I know she's in there!":
    "你瞧。我给你们修车。但我得先见 萨莎。我知道她在里面！",
 "No deal.": "不行。",
 "Shame on you.": "你真不害臊。",
 "Then help.": "那就帮忙。",
 "That's not happening.": "不可能。",
 "I wanna help, I really do...": "我想帮忙，真的想……",
 "I just gotta see her!": "我就是得见她！",
 "Fine. But no drooling.\nSCOOTER [wiping his mouth] I don't know what yer talkin' bout.":
    "行。但不许流口水。\nSCOOTER [wiping his mouth] 我不知道你在说什么。",
 "[to Sasha] Your gentleman caller awaits.": "[to Sasha] 你的绅士访客在等你。",
 "I'm surprised at you. The Scooter I know would help a friend no matter what.":
    "我对你很失望。我认识的 斯库特 不管怎样都会帮朋友。",
 "I want to, I really do...": "我想，真的想……",
 "But I gotta see her, I just gotta!": "但我得见她，我就是得见！",
 "So fix the van.": "那就把车修了。",
 "Oh, I get it. I'm not good enough for the great Fion'er.":
    "哦，我懂了。我配不上伟大的 Fioner。",
 "[trying to look in] I will, I will. But I just wanted to say howdy first.":
    "[trying to look in] 我会的，我会的。但我就是想先打个招呼。",
 "Talkin' ain't against the law.": "说话不犯法。",
 "I'll behave. You have my solemn word.": "我会守规矩。我郑重保证。",
 "I'll pop the hood while we wait for Scooter.": "等 斯库特 的时候我把引擎盖掀开。",
 "...and if Vallory's people show up?": "……那要是 瓦洛里 的人出现了呢？",
 "I mean we're not exactly on her \"nice\" list.": "我是说我们可不在她的“好”名单上。",
 "[Aside] Not that she'd even have one...": "[Aside] 倒不是说她会有那种名单……",
 "Please. It'll be a quick patch job - We'll be long gone before Vallory even gets a whiff of us being in town.":
    "拜托。就是个快速补修——等 瓦洛里 闻到我们在镇上的味儿之前，我们早走了。",
 "You worry too much, sis. It's just a quick patch job. Get in, fix it, get out.":
    "你太爱担心了，妹妹。就是个快速补修。进去，修好，出来。",
 "In that case we'll just have to improvise.": "那我们就只能随机应变了。",
 "So be safe.": "那就注意安全。",
 "[Unsure] Okay...": "[Unsure] 好吧……",
 "Whatever, let's just be fast and blow this pop stand.":
    "随便，我们就快点办完然后赶紧离开这鬼地方。",
 "[Sigh] Of course.": "[Sigh] 当然。",
 "[To herself] Pleeease let it be a little problem.": "[To herself] 求——你了，让它只是个小问题吧。",
 "[Muttering] Well I don't know what I expected.": "[Muttering] 好吧，我也不知道我期待什么。",
 "Okay. Just going to... check the oil?": "好。就去……检查一下机油？",
 "I got customers!": "我有客人！",
 "How can I give you more money, if I can't get to my customers?":
    "我要是到不了我的客人那儿，怎么给你更多钱？",
 "Mmmff!": "唔呣！",
 "Awwg.": "嗷。",
 "[correcting himself] Howdy, name's Scooter! What can I do to ya--for ya?":
    "[correcting himself] 你好，我叫 斯库特！我能为你做点——为你效劳什么？",
 "We can't let them inside.": "我们不能让他们进去。",
 "I'll do the talking.": "我来说话。",
 "No worries.": "别担心。",
 "Use your charm.": "用你的魅力。",
 "I'm sure August told them about the deal.": "我确定 August 跟他们说了那笔交易。",
 "They know we'd only come back if we had a damn good reason. Like a big score.":
    "他们知道我们回来肯定有十足的理由。比如一大笔进账。",
}

T.update({
 # —— Hodunk 一家上门敲诈 ——
 "You two have some nerve showin' yer faces back here.": "你们俩还敢回来露面，胆子不小。",
 "We just need repairs.": "我们只需要修车。",
 "It's none of your concern.": "不关你的事。",
 "[spit]": "[spit]",
 "Them's purdy words. [turning to Jimbo] Pa, you believe'em?":
    "话说得真好听。[turning to Jimbo] 爹，你信他们吗？",
 "No, I don't think. And Scooter ain't fixin' this van.":
    "不，我不信。而且 斯库特 不会修这辆车。",
 "You always do.": "你总是这样。",
 "I'm gonna take that as a compliment.": "我就当这是夸奖了。",
 "They're still gonna want to know what we're doing here.":
    "他们还是会想知道我们在这儿干什么。",
 "We're here to fix the van.": "我们是来修车的。",
 "There's nothing to worry about. They're not exactly sharp.":
    "没什么好担心的。他们不太灵光。",
 "Come on now, she's got a point -- even if I were to consider it, which I never ever would -- I can't *lend* y'all money if you keep scarin' away my customers.":
    "得了吧，她说得有道理——就算我会考虑（可我绝不会考虑）——你们一直把我的客人吓跑，我就没法*借*钱给你们。",
 "Open them doors.": "把那些门打开。",
 "Since when am I charming?": "我什么时候有魅力了？",
 "Perfect. Just do the opposite of that.": "完美。就做与之相反的事。",
 "You're kidding, right?": "你开玩笑吧？",
 "Since now. Let's see a smile.": "从现在起。笑一个看看。",
 "We'll bank on your charm.": "我们就押在你的魅力上。",
 "[to Scooter] Can you fix our van or what?": "[to Scooter] 你到底能不能修我们的车？",
 "Yeah! On your way *where*?": "是啊！去*哪儿*？",
 "Yes, ma'am, I surely can. [to Sasha] Especially for a purdy lady like you. [to Fiona] Oh, gosh. Not that you're not purdy. I mean you're both purdy. [to himself] Shut up, Scooter!":
    "是的女士，我当然能。[to Sasha] 尤其是对像你这么漂亮的女士。[to Fiona] 哦，天。不是说你就不漂亮。我是说你们俩都漂亮。[to himself] 闭嘴，斯库特！",
 "We need repairs first. Then we'll be on our way.":
    "我们先要修车。然后我们就上路。",
 "Our business here is none of your concern.": "我们在这儿的事不关你的事。",
 "Ain't nuthin here happens that's NOT my concern.": "这儿发生的事没有一件不关我的事。",
 "Tector, I already told you this here's *mah* new garage.":
    "Tector，我已经跟你说过这儿是*我*的新车库。",
 "[to Scooter] So you can fix it?": "[to Scooter] 那你能修吗？",
 "Why don't you run along and let Scooter fix our van?":
    "你干嘛不走开，让 斯库特 修我们的车？",
 "Well you ain't in charge.": "你说了可不算。",
 "[smiling at Sasha] My pleasure.": "[smiling at Sasha] 乐意效劳。",
 "Can'tcha see we're talkin'?": "你没看到我们在说话吗？",
 "Back off. I'm not in the mood. Not today.": "退后。我没心情。今天没心情。",
 "You sure did get August mad, I tell you what.": "你们确实把 August 惹火了，我跟你说。",
 "Gotta be somethin' big goin' on for you to come back here.":
    "能让你们回来，肯定有什么大事。",
 "You should leave.": "你们该走了。",
 "That's bad for business.": "这对生意不好。",
 "We're not going anywhere.": "我们哪儿都不去。",
 "I hope you've got a plan.": "我希望你有计划。",
 "Charm don't work on me.": "魅力对我不管用。",
 "I know yer up to somethin'.": "我知道你们在搞鬼。",
 "Happy?": "满意了？",
 "[proudly] That one of you is me. [to himself] Aw jeez...":
    "[proudly] 你们当中那个就是我。[to himself] 哦天……",
 "[exasperated] Can one of you fix our van already?":
    "[exasperated] 你们哪位能不能赶紧把我们的车修了？",
 "Go ahead. Look.": "来吧。看吧。",
 "Then you won't mind if I take a look.": "那让我看一眼你不介意吧。",
 "Mind you own damn business.": "管好你自己的破事。",
 "You got all the time in the world.": "你有的是时间。",
 "Whoa, whoa, whoa. Ain't nobody gettin' hurt.": "哇哇哇。没人会受伤。",
 "You should leave, unless you want to scare off all the customers.":
    "你们该走了，除非你们想把客人全吓跑。",
 "This ain't over.": "这事没完。",
 "He's not that cute.": "他没多可爱。",
 "We're not going anywhere until Scooter's fixing our van.":
    "在 斯库特 修好我们的车之前我们哪儿都不去。",
 "[angry] But pa!": "[angry] 可是爹！",
 "Aw, I seen a lot worse damage than this before. I'll have 'er patched up like new before you even know what happened!":
    "哦，比这糟得多的损伤我都见过。等你们还没反应过来，我就把她补得跟新的一样！",
 "Sure you can fix it?": "你确定你能修好？",
 "Dang it!": "该死！",
 "You bet. I can fix anything.": "当然。我什么都能修。",
 "Don't go inside.": "别进去。",
 "'Cept me.": "除了我。",
 "I know it!": "我就知道！",
 "'Less you want me to tell August you're back in town!":
    "除非你想让我告诉 August 你们回镇上了！",
 "Them's fightin' words.": "这是要打架的话。",
 "We'll handle this. Remember *everyone* hates you here.":
    "这事我们来处理。记住这儿*所有人*都恨你们。",
 "Keep an eye on them.": "盯着他们。",
 "We're in this together.": "我们是一条船上的。",
 "You're holding out on us.": "你在对我们藏着掖着。",
 "I guess you know best.": "我想你是最懂的。",
 "Maybe we should help.": "也许我们该帮忙。",
 "They can handle it.": "他们应付得了。",
 "She said hang back.": "她说了别上前。",
 "Ok. Let's kick some ass.": "好。我们去揍人。",
 "If they kill them, we'll never get the vault.": "他们要是杀了他们，我们就再也拿不到秘藏了。",
 "They might need us.": "他们可能需要我们。",
 "[re: Rhys and Vaughn] Make sure they don't touch anything.":
    "[re: Rhys and Vaughn] 确保他们什么都别碰。",
 "She does have a point.": "她确实说得有道理。",
 "If anybody spots two fancy Hyperion guys walking around Hollow Point, you'll be as good as dead. Not to mention the fact that you almost got us killed already.":
    "要是有人看到两个穿得体面的 亥博龙家伙在空心镇晃悠，你就等于死了。更别说你已经差点害死我们了。",
 "I thought we were in this together.": "我以为我们是一条船上的。",
 "It looks like you might need our help.": "看来你可能需要我们帮忙。",
 "Have it your way.": "随你。",
 "Not a good idea.": "不是好主意。",
 "Be careful out there.": "在外面小心点。",
 "We will. Thanks.": "我们会的。谢了。",
 "We'd only make things worse.": "我们只会把事情弄得更糟。",
 "That's a first.": "这倒是头一回。",
 "[suspicious] Agreed. Sit tight.": "[suspicious] 同意。别动。",
 "I guess you know how it works here.": "我想你知道这儿的规矩。",
 "Good. Stay out of sight. Hyperions are as good as dead here.":
    "好。别露脸。亥博龙的人在这儿等于死人。",
 "Whose side are you on?!": "你站哪边？！",
 "What was that about?": "那是怎么回事？",
 "Now's our chance to take a look.": "现在我们有机会看看了。",
 "He's hiding something, and I bet it's in this van.":
    "他在隐瞒什么，我打赌就在这车里。",
 "When I scanned Felix's heart rate near the arena, it was off the charts.":
    "我在竞技场附近扫描 菲利克斯 的心率时，那数值高得离谱。",
 "Because that's always worked out so well.": "因为这一向都很成功嘛。",
 "She said hang back. It's their problem.": "她说了别上前。那是他们的问题。",
 "But it's gonna be our problem if they get themselves killed.":
    "但他们要是把自己搞死，那就会变成我们的问题。",
 "This is Pandora. Killing each other is practically a form of greeting here. They'll be fine.":
    "这是 潘多拉。互相残杀在这儿基本上算一种问候方式。他们会没事的。",
 "They can handle themselves. They're from this godforsaken hole.":
    "他们能应付自己。他们就是从这鬼地方出来的。",
 "Better them than us.": "是他们总比是我们好。",
 "It's not looking good.": "看着不太妙。",
 "Yeah, but we need them alive.": "是啊，但我们需要他们活着。",
 "They know what they're doing. We'd only mess it up.":
    "他们知道自己在干什么。我们只会搞砸。",
 "You're right. Let's kick some ass.": "你说得对。我们去揍人。",
 "Then what do you propose?": "那你提议怎么做？",
 "A distraction.": "制造点骚动。",
 "I didn't say that.": "我没那么说。",
 "Do that thing where you don't talk.": "用你那招——不说话。",
 "I could run from the van screaming, and you could chase me.":
    "我可以从车里跑出来尖叫，你可以追我。",
 "We need them alive.": "我们需要他们活着。",
 "Deal with it.": "忍着吧。",
 "Suit yourself. But if anyone catches you, you're dead.":
    "随你。但要是有人抓到你，你就死定了。",
 "Hear, hear!": "说得好！",
 "Open your mouth.": "张开嘴。",
 "Stand by the window so that moron can't see inside.":
    "站到窗边去，这样那个白痴就看不到里面。",
 "I'll search the van.": "我来搜车。",
 "They said not to touch anything.": "他们说什么都别碰。",
 "You fellers better quit snoopin', or you'll catch-a-ride on my foot.":
    "你们几位最好别乱翻，不然就搭我的脚一程吧。",
 "Don't make me come in.": "别逼我进去。",
 "What're you doin' in there?": "你在里面干什么？",
 "I see you.": "我看见你了。",
 "Candy. Who knew Felix had such a sweet tooth?": "糖。谁知道 菲利克斯 这么爱吃甜？",
 "The guy loved his tech, I'll give him that.": "这家伙爱他的技术，这点我承认。",
 "Crumbs and coins. Big surprise.": "碎屑和硬币。真意外。",
 # —— Vallory 的 VO 留言 ——
 "[VO] [suddenly sinister] Did you think you could stay hidden?":
    "[VO] [suddenly sinister] 你以为能一直躲着？",
 "[VO] I know you're in Hollow Point. I know about your cozy little hideaway above Emmit's Pawn Shop. I wouldn't go back there if I were you.":
    "[VO] 我知道你们在空心镇。我知道你们在 Emmit 当铺楼上那个舒服的小窝。我要是你们就不会回去。",
 "[VO] I know where you live.": "[VO] 我知道你们住哪儿。",
 "[VO] You're only way out is to deliver the money to your Bleeker and Kreb Street drop. And come alone.":
    "[VO] 你们唯一的出路，是把钱送到你们在 Bleeker 街和 Kreb 街的投放点。而且单独来。",
 "It seems like they're really growing on you.": "看来他们还真让你上心了。",
 "We have to get to Felix's safehouse before it's too late.":
    "我们得趁还来得及，赶到 菲利克斯 的安全屋。",
 "I care about the vault.": "我在乎的是秘藏。",
 "We need them.": "我们需要他们。",
 "And since when were you such a hardass?": "你什么时候变得这么硬了？",
 "Or not.": "或者不是。",
 "That doesn't mean I want them dead.": "那不代表我想让他们死。",
 "I do believe you're getting soft.": "我看你是变软了。",
 "I care about finding the vault. That's it.": "我在乎的是找到秘藏。就这样。",
 "Right on, interns! Let's track them down!": "好样的，实习生们！我们去追踪他们！",
 "Your face. It has that effect on me sometimes.": "你的脸。它有时候对我有那种效果。",
 "Right on, intern!": "好样的，实习生！",
 "Mr. Marshmallow. Senor cream-puff. Madame Muffin-":
    "棉花糖先生。奶油泡芙先生。松饼夫人——",
 "Keep going. I dare you.": "继续。我赌你不敢。",
 "I can't breathe.": "我喘不上气。",
 "Mrs. Manners...": "礼貌夫人……",
 "We need them right now.": "我们现在需要他们。",
 "I agree.": "我同意。",
 "[off Vaughn's look] I'm not being sentimental.": "[off Vaughn's look] 我不是在感伤。",
 "You do care. I knew it.": "你就是在乎。我就知道。",
 "That wasn't about me, right? Because I didn't hear it prefaced with his divine Jackness.":
    "那不是关于我的，对吧？因为我没听到前面加上他那神圣的“Jack 性”。",
 "You gotta love his enthusiasm.": "你得喜欢他这股热情。",
 "Too bad we don't know where that is.": "可惜我们不知道那在哪儿。",
 "Lucky for you, I'm a genius. Check the GPS on Felix's phone. Wherever he received the most calls is probably his safehouse.":
    "算你走运，我是天才。查一下 菲利克斯 手机上的 GPS。他接到电话最多的地方大概就是他的安全屋。",
 "Who are you calling a hologram?": "你说谁是全息像？",
 "Best AI hologram ever.": "史上最棒的 AI 全息像。",
 "I'll check the GPS on his phone. We can trace where he received the most calls. That's probably his safehouse.":
    "我来查他手机上的 GPS。我们能追踪他接到电话最多的地方。那大概就是他的安全屋。",
 "I'm a genius.": "我是天才。",
 "How'd you know that?": "你怎么知道的？",
 "On second thought, don't do that. I'll do it. Don't you touch her!":
    "再想想，别那么做。我来。你别碰她！",
 "Where you headed?": "你们去哪儿？",
 "If you see Sasha, give her a big 'ol hug for me.": "你要是见到 萨莎，替我好好抱抱她。",
 "Don't worry about that. Just mind the van.": "别操心这个。看着车就行。",
 "Way to go, Scoot-": "干得好，Scoot——",
 "AAAAAAAAAAAHHHG!": "啊啊啊啊啊啊！",
 "Says you.": "你才这么说。",
 "I don't. But that doesn't mean I want them dead.":
    "我没有。但那不代表我想让他们死。",
 "Welcome to our future.": "欢迎来到我们的未来。",
 "Just our luck. Tector's shaking down the mechanic and we need to get these repairs started now.":
    "真是我们的运气。Tector 正在勒索那个修车工，而我们现在就得开始修车。",
 "That's exactly what we're gonna do.": "我们正是要这么做。",
 "Yeah, thanks to you!": "是啊，多亏了你！",
 "Just havin' some fun with my kin.": "只是跟我亲戚玩玩。",
 "[to Jimbo] Hey. There are ladies present.": "[to Jimbo] 嘿。这儿有女士在场。",
 "Lost your job at The Purple Skag?": "在紫异犬丢了工作？",
 "A little old to be takin' orders from your pa, don't ya think?":
    "听你爹的命令，年纪是不是有点大了，你不觉得吗？",
 "Damn right.": "他妈没错。",
 "Unless you want to stand around all night, scaring away the customers. 'Cause it looks like you and Jimbo could use all the business Scooter can get.":
    "除非你想整晚站在这儿，把客人都吓跑。因为看来你和 Jimbo 需要 斯库特 能招来的每一单生意。",
 "I say it is. Right, Scooter?": "我说就是。对吧，斯库特？",
 "That's funny, because I thought you were here on business. But guess what? No customers, no business. So back off.":
    "真有意思，因为我还以为你们是来做生意的。可你猜怎么着？没客人就没生意。所以退后。",
 "Not on my wach he ain't.": "在我盯着的时候他可不行。",
 "It's not your call. This is Scooter's garage and he wants to fix our van.":
    "这不由你说了算。这是 斯库特 的车库，他想修我们的车。",
 "That' s bad for business. And it looks like you and Jimbo could use all the business Scooter can get.":
    "那对生意不好。而看来你和 Jimbo 需要 斯库特 能招来的每一单生意。",
 "So back off and let him get to work.": "所以退后，让他干活。",
 "No one's fixin' nuthin'!": "谁都不许修任何东西！",
 "'Cause it looks like you and Jimbo could use all the customers Scooter can get.":
    "因为看来你和 Jimbo 需要 斯库特 能招来的所有客人。",
 "Shouldn't Tector be at the Purple Skag?": "Tector 不该在紫异犬吗？",
 "Just our luck. The day he decides to visit his kin, our van is broken and we're with two Hyperions he'd kill on sight.":
    "真是我们的运气。偏偏在他决定来看亲戚的这天，我们的车坏了，而我们身边还有两个他一见就会杀的 亥博龙。",
 "I hate to do it, but better safe than sorry.": "我很不情愿，但小心总比后悔好。",
 "Damn straight.": "他妈没错。",
 "We're heading to Felix's safehouse to find his contact list.":
    "我们去 菲利克斯 的安全屋找他的联系人名单。",
 "If you value your life, you'll stay in the van.": "要是你珍惜性命，就待在车里。",
 "It's too dangerous for you out there.": "外面对你来说太危险了。",
 "He was up to something in here before the race, and we're gonna find out what it was.":
    "比赛之前他在这车里搞了什么名堂，我们要查出来。",
 "Remember, the safest spot for you is in the van.": "记住，对你来说最安全的地方是车里。",
 "So stay put.": "所以别动。",
 "Logos or not, Hollow Pointers can sniff out Hyperions from a mile off.":
    "不管有没有标志，空心镇人一英里外就能闻出 亥博龙的人。",
 "It shouldn't take us long at Felix's safehouse.": "在 菲利克斯 的安全屋应该不会花太久。",
 "They won't hesitate to kill you.": "他们会毫不犹豫地杀了你。",
 "All right, then. See you soon.": "那好。回头见。",
 "But you're in danger too.": "但你也有危险。",
 "We should go together.": "我们该一起去。",
 "Be careful.": "小心点。",
 "We grew up on these streets. We can handle ourselves.":
    "我们是在这些街上长大的。我们能照顾好自己。",
 "But you're in danger too. You screwed over August, and this is his turf.":
    "但你也有危险。你坑了 August，而这是他的地盘。",
 "It's gonna be our problem if anything happens to you.": "你要是出了事，那就会变成我们的问题。",
 "That's our problem.": "那是我们的问题。",
 "It's too dangerous to go without us.": "不带上我们去太危险了。",
 "What about strength in numbers? We've got a vault on the line here.":
    "那“人多力量大”呢？我们这儿可押着一座秘藏。",
 "Together is way worse.": "一起去糟得多。",
 "Most Hollow Pointers would like nothing more than to lovingly mount your heads on their wall.":
    "大多数空心镇人最想做的事，就是把你们的头深情地挂在他们墙上。",
 "I'm sorry, but you'll just have to trust us.": "抱歉，但你们只能信我们。",
 "We'll worry about August. You focus on staying out of sight.":
    "August 的事我们来操心。你专心别露脸。",
 "But this is August's turf and he wants you dead.": "但这是 August 的地盘，而他想让你死。",
 "Vallory said \"your\" drop on Bleeker and Kreb street.":
    "瓦洛里 说的是*你们*在 Bleeker 街和 Kreb 街的投放点。",
 "[excited] Greed is good.": "[excited] 贪婪是好事。",
 "I bet it's Felix's safehouse.": "我打赌那是 菲利克斯 的安全屋。",
 "Which is why you need to stay in the van. We can't let them see you.":
    "所以你们得待在车里。我们不能让他们看到你们。",
 "Well, be careful.": "好吧，小心点。",
 "I know you're from here, but they seem dangerous even by Pandoran standards.":
    "我知道你们是这儿的人，但就算按 潘多拉 的标准，他们看着也很危险。",
 "Like it or not, we're partners. We're supposed to share the risk.":
    "不管你喜不喜欢，我们是搭档。我们应该共担风险。",
 "We can't take that risk again.": "我们不能再冒那个风险。",
 "I'm sorry, but you're staying.": "抱歉，你们得留下。",
 "That's right. Taking two fancy Hyperion guys into Hollow Point would be suicide.":
    "没错。带两个穿得体面的 亥博龙家伙进空心镇等于自杀。",
 "Sit tight for now.": "先别动。",
 "We won't take long.": "我们不会太久。",
 "Just stay quiet. No one can know you're here.": "保持安静。没人能知道你在这儿。",
 "I don't like it. We're sitting targets.": "我不喜欢这样。我们是活靶子。",
 "*Hidden* targets. And it's the best we can do.": "*藏起来的*靶子。而我们只能这样。",
 "We just teamed up, and you're already holding out on us.":
    "我们才刚合作，你就已经对我们藏着掖着了。",
 "You don't need to. All you need to know is that everyone in Hollow Point hates Hyperion. They'd shoot you on sight. And from recent experience, I can see they're not the only ones.":
    "你不需要知道。你只要知道空心镇所有人都恨 亥博龙。他们会一见你就开枪。而根据最近的经验，我看不止他们如此。",
 "We'll be back soon.": "我们很快回来。",
 "We'll hurry back.": "我们尽快回来。",
 "It's not just you abandoning us. Felix betrayed you, and you're heading to his safehouse?":
    "不只是你们抛下我们。菲利克斯 背叛了你们，而你们还要去他的安全屋？",
 "It wouldn't surprise me.": "我不会意外。",
 "We can defend ourselves if we have to. And your *help* almost got us killed.":
    "必要时我们能自卫。而你的*帮忙*差点害死我们。",
 "You think it might be a trap?": "你觉得那可能是个陷阱？",
 "This is a bad idea.": "这是个烂主意。",
 "We're risking the vault.": "我们在拿秘藏冒险。",
 "Fine. You guys go.": "行。你们去吧。",
 "We can handle it. [incredulous] And Felix isn't the only one who blindsided us.":
    "我们能应付。[incredulous] 而且打我们措手不及的不只是 菲利克斯。",
 "Felix blindsided you once and you barely survived.":
    "菲利克斯 打你们措手不及一次，你们就差点没活下来。",
 "It still seems too risky.": "还是太冒险了。",
 "We're leaving.": "我们走了。",
 "We've got an equal stake in finding this Vault, remember.":
    "找这座秘藏我们有一份同等的权益，记得吗。",
 "We'll deal with it.": "我们会处理。",
 "That's not reassuring considering how much is on the line.":
    "考虑到押上了多少东西，这可不太让人安心。",
 "It's the best you're gonna get.": "这是你能得到最好的了。",
 "There isn't one. Vault hunting's all or nothing.":
    "没有。猎秘藏是全有或全无。",
 "That's not reassuring.": "这不安心。",
 "So if you go out and get yourselves killed-": "所以你们要是出去把自己搞死——",
 "Fine. Go. I just hope you don't regret it if you run into trouble.":
    "行。去吧。我只希望你们遇到麻烦时不会后悔。",
 "We're ready for anything.": "我们准备好了应对一切。",
 "You're just gonna have to trust us.": "你们只能信我们。",
 "But most importantly, stay put. If August finds out you're in Hollowpoint, he'll tear you to pieces.":
    "但最重要的是，别动。要是 August 发现你们在空心镇，他会把你们撕成碎片。",
 "With them, you'll be dead.": "跟他们一起，你会死。",
 "Stay in the van, and don't do anything that could attract attention.":
    "待在车里，别做任何可能引人注意的事。",
 "Okay, good. Then that's settled.": "好，很好。那就这么定了。",
 "August ain't gonna be happy if you've been helpin' them out.":
    "你要是帮他们，August 可不会高兴。",
 "[sarcastic] Okay great, we'll just sit here and scan-- [cut off]":
    "[sarcastic] 好极了，那我们就坐在这儿扫描——[cut off]",
 "When he kills ya, I get first dibs on your tools.": "他杀了你之后，你的工具我先挑。",
 "[quiet, panicked] Well, find out what *is* beeping, before that bullymong comes in here!":
    "[quiet, panicked] 好吧，在那边那头恶霸兽进来之前，赶紧查清楚*什么*在响！",
 "I'm working on it!": "我在弄！",
 "What's that beepin? Sounds like it's coming from somewhere close.":
    "那是什么在响？听着像是从很近的地方传来。",
 "Sounds like it might be coming from the van.": "听着可能是从车里传来的。",
 "It's real close.": "非常近。",
 "Ain't you the least bit curious about that noise, Scooter?":
    "你对那声音一点都不好奇吗，斯库特？",
 "Ain't no way to treat family. Even if we do kill each other sometimes...":
    "对家人不该这样。就算我们有时候会互相残杀……",
 "[VO] [faux jovial] Felix! It's Vallory. It feels like forever since we talked. Too bad you skipped town.":
    "[VO] [faux jovial] 菲利克斯！我是 瓦洛里。感觉我们好久没聊了。可惜你跑出了城。",
 "[VO] You know where to find me.": "[VO] 你知道去哪儿找我。",
 "[VO] I also know about those two young ladies you've got running your scams. Do you really want anyone else to die?":
    "[VO] 我也知道你手底下那两个替你跑骗局的年轻姑娘。你真的还想再死人吗？",
 "August is gonna love this.": "August 会喜欢这个的。",
 "If they die, we lose our one shot at this.": "他们要是死了，我们就丢掉这一次唯一的机会。",
 "[giddy] Greed is good.": "[giddy] 贪婪是好事。",
})

T.update({
 # —— Jimbo 的含糊嘟囔 + Scooter 被撞晕 ——
 "JIMBO": "JIMBO",
 "*suspicious mumbling*": "*怀疑地嘟囔*",
 "*muttered reprimand*": "*低声斥责*",
 "No, *I* am.": "不，*我*才是。",
 "You want me to go back to Sanctuary, and leave y'all with nothin'?":
    "你想让我回避风港，把你们丢下一无所有？",
 "*resentful gibberish*": "*怨恨的胡话*",
 "*scolding gibberish*": "*训斥的胡话*",
 "Sure as I can -- [acidentally hurts himself] Oww!": "当然能——[acidentally hurts himself] 哎哟！",
 "[feebly] Catch-a-ride.": "[feebly] Catch-a-ride。",
 "Tector? You know this guy?": "Tector？你认识这家伙？",
 "He's a bouncer at the Purple Skag. And he hates Hyperion even more than we do, so keep your heads down.":
    "他是紫异犬的看门人。他比我们还恨 亥博龙，所以你们把头低着。",
 "*offended mumbling*": "*被冒犯地嘟囔*",
 "*threatening mumbling*": "*威胁地嘟囔*",
 "We don't even know where you're going.": "我们连你们要去哪儿都不知道。",
 "We told you, anybody Hyperion is as good as dead -- [cut off]":
    "我们说过了，亥博龙的人等于死人——[cut off]",
 "What's that beepin'?": "那是什么在响？",
 "[quiet, panicked] Don't look at me!": "[quiet, panicked] 别看我！",
 "[quiet, panicked] Are you beeping?": "[quiet, panicked] 是你在响吗？",
 "*scheming gibberish*": "*盘算的胡话*",
 "I don't give a flyin' flip what makes August happy. Now skee-daddle 'less you wanna meet my *boomstick.*":
    "我才他妈不管什么让 August 高兴。现在赶紧滚，除非你想见见我的*大炮*。",
 "*nagging gibberish*": "*唠叨的胡话*",
 "Shut yer face! You're loiterin' on private property!": "闭上你的嘴！你在私人产业上闲荡！",
 "Maybe I should look inside if you ain't gonna.": "你要是不去，也许该我进去看看。",
 "I don't care where it's coming from. You can't be here.": "我不管那声音从哪儿来。你们不能在这儿。",
 "That's right. Don't ever come back.": "没错。别再回来。",
 "Well if it ain't that couple of Hyperion assholes.": "哎，这不是那两个 亥博龙混蛋嘛。",
 "[realizing] They're walking right into a trap....":
    "[realizing] 他们正一头撞进陷阱里……",
 "Well, this just got interesting.": "好吧，这刚变得有意思了。",
 "I KNEW this was a bad idea! That bastard tried to make off with the money but they STILL trusted him.":
    "我*就*知道这是个烂主意！那混蛋想卷钱跑路，可他们*还是*信他。",
 "Put your shoes on, kids. You have to go warn them.":
    "穿上鞋，孩子们。你们得去警告他们。",
 "[to Handsome Jack] You're actually worried about those two?":
    "[to Handsome Jack] 你居然真担心那两个？",
 "[correcting himself] I'm worried about me -- us.":
    "[correcting himself] 我担心的是我自己——我们。",
 "If she gets herself killed, we lose the Vault. We're not going to lose the Vault.":
    "她要是把自己搞死，我们就丢了秘藏。我们不会丢掉秘藏。",
 "[disbelief] Wait -- is Handsome Jack saying we should go *help* them?":
    "[disbelief] 等等——帅杰克是在说我们该去*帮*他们？",
 "No, I think this proves your \"stick together\" plan was a bad idea.":
    "不，我觉得这证明了你的“待在一起”计划是个烂主意。",
 "[mumbling to himself] Once she sees this she's gonna be all \"Scooter I had no idea you had the magic touch take me now right here\" and I'm gonna be all \"Can I keep my boots on?\" and she'll say \"I wouldn't have it any other way 'cause this is true love.\"":
    "[mumbling to himself] 等她看到这个，她就会说“斯库特 我都不知道你有这魔力，现在就带我走就在这儿”然后我就会说“我能留着靴子吗？”然后她会说“我不会让你有别的选择，因为这就是真爱。”",
 "[quietly] Coast is clear. Let's go.": "[quietly] 没人了。我们走。",
 "We're partners now.": "我们现在是搭档了。",
 "They don't deserve to die.": "他们不该死。",
 "She's got the Gortys core.": "她手上有 戈提斯 核心。",
 "You're not really thinking about walking into that... hellhole?":
    "你不会真想着走进那个……地狱洞吧？",
 "Come on, Rhys. Tell your buddy to sack up and let's get Gortys.":
    "得了吧，瑞斯。让你哥们硬气点，我们去拿 戈提斯。",
 "Like it or not, they're our partners. We've got to help them.":
    "不管你喜不喜欢，他们是我们的搭档。我们得帮他们。",
 "[sarcastic] Great. We're going after assassins now. Why not?":
    "[sarcastic] 好极了。我们现在去追刺客了。为什么不呢？",
 "They'll never see us coming.": "他们绝不会看到我们来。",
 "Come on, Vaughn. Like them or not, they don't deserve to die.":
    "得了吧，沃恩。不管你喜不喜欢他们，他们不该死。",
 "Oh, so I'm the bad guy now?": "哦，所以现在我是坏人了？",
 "We've got to help them.": "我们得帮他们。",
 "Quote, Handsome Jack. That's okay, you don't have to give me credit.":
    "这是帅杰克的原话。没关系，你不用给我署名。",
 "Whether you like her or not, Fiona's got the other part of the Gortys Core.":
    "不管你喜不喜欢她，Fiona 手上有 戈提斯 核心的另一半。",
 "We lose her, we lose our way to the Vault.": "丢了她，我们就丢了通往秘藏的路。",
 "I didn't say anything!": "我什么都没说！",
 "Exactly. You're just staring at me, making me feel guilty.":
    "正是。你就盯着我看，让我觉得愧疚。",
 "Okay, fine. We'll go warn them.": "好，行。我们去警告他们。",
 "All right, then. Let's find \"Emmit's Pawn Shop.\"": "那好。我们去找“Emmit 当铺”。",
 "[defensive] We're not \"fancy.\"": "[defensive] 我们不算“体面”。",
 "[agreement] Yeah!": "[agreement] 是啊！",
 "Just our luck. We need repairs and Scooter almost kills himself.":
    "真是我们的运气。我们需要修车，而 斯库特 差点把自己搞死。",
 "[softly] Catch-a-riiide...": "[softly] Catch-a-riiide……",
 "Damn it, Scooter!": "该死，斯库特！",
 "[mumbling re: Sasha] I musta died and gone to heaven, cause yer an angel.":
    "[mumbling re: Sasha] 我肯定死了上天堂了，因为你是天使。",
 "[mumbling] What in the sam hill?": "[mumbling] 这到底怎么回事？",
 "Sure. Soon as everthin' stops spinnin'.": "当然。等一切不转了就修。",
 "I'm tryin'. Gimme a minute, will ya?": "我在试。给我一分钟，行吗？",
 "[re: the van] Think you can patch up our van?": "[re: the van] 你觉得能补好我们的车吗？",
 "How many of 'em are there?": "他们有多少人？",
 "HEY. Snap out of it.": "嘿。清醒过来。",
 "Just the one.": "就一个。",
 "Think you can patch up our van?": "你觉得能补好我们的车吗？",
 "Scooter, are you all right?": "斯库特，你没事吧？",
 "My head hurts somethin' awful.": "我的头疼得要命。",
 "I was distracted is all.": "只是分了神。",
 "Sure. Soon as everthin' stops spinning.": "当然。等一切不转了。",
 "Damn it, Scooter. You need to be more careful.": "该死，斯库特。你该小心点。",
 "Everthin's spinnin' so fast. I wish I could help, but I'm too dang dizzy.":
    "一切转得太快了。我希望我能帮忙，但我晕得太厉害了。",
 "We've gotta help him.": "我们得帮他。",
 "Take my hand.": "抓住我的手。",
 "Follow my finger.": "跟着我的手指。",
 "Try a deep breath.": "试着深呼吸。",
 "Here. Take my hand.": "来。抓住我的手。",
 "[to Sasha] Thank you kindly. [to Fiona] And you.\n.":
    "[to Sasha] 太谢谢你了。[to Fiona] 还有你。\n。",
 "Try to follow my finger.": "试着跟着我的手指。",
 "There ya go.": "这就对了。",
 "That's a little better. The world's slowin' back down.":
    "好一点了。世界又慢下来了。",
 "Whaddaya know. I'm startin' to feel better already.": "你猜怎么着。我已经开始感觉好些了。",
 "Try taking a deep breath.": "试着深呼吸。",
 "What'd you do that for?! Let a feller catch his wind. Jeez.":
    "你干嘛那么做？！让人家缓口气。天哪。",
 "I'm out to lunch...": "我魂都飞了……",
 "I'll be with y'all in a minute...": "我一会儿就过来……",
 "Scooter, at yer service: [to Sasha] Especially yours. What can I do to ya--for ya?":
    "斯库特，听候差遣：[to Sasha] 尤其是你的。我能为你做点——为你效劳什么？",
 "As low as it takes.": "多低都行。",
 "And you'll have no business at all if you help these backstabbers. First they duped me, then they double-crossed my boss. That's why he had us follow 'em.":
    "你要是帮这些背后捅刀的家伙，你就一点生意都没有了。他们先骗了我，然后又背叛了我老板。所以他才让我们跟着他们。",
 "Well dead or alive, kin or no kin, you ain't shakin' me down and y'all got no business tresspassin' on mah franchise.":
    "不管死的活的，不管是不是亲戚，你别想勒索我，你们也无权闯进我的地盘。",
 "After they double-crossed August, he had me": "他们背叛 August 之后，他让我",
 "Workin' for the mob now? How low you gonna go?": "现在给黑帮干活了？你还能堕落到什么地步？",
 "And what would that be?": "那是什么？",
 "This here's your last chance. Clear out now if you know what's good for ya.":
    "这是你最后的机会。识相就现在滚。",
 "[to Fiona and Sasha] Never mind them. I can damn well fix it.":
    "[to Fiona and Sasha] 别管他们。我他妈当然能修。",
 "YOW'll take care now. I'm gonna fix'er up real sweet, you'll see. I'll get'er purrin' in no time. Hehe. [to himself] That's enough.":
    "你们放心。我会把她修得漂漂亮亮的，你等着看。我很快就能让她咕噜咕噜跑起来。嘿嘿。[to himself] 够了。",
 "*angry mumbling*": "*愤怒地嘟囔*",
 "I thought I told you to scram.": "我以为我叫你滚了。",
 "Maybe I should call my vault hunter friends from Sanctuary to deal with you! How'd you like that?!":
    "也许我该把我在避风港的秘藏猎人朋友叫来处理你！你觉得怎么样？！",
 "We ain't family, okay?! Not now, not ever!": "我们不是家人，行吗？！现在不是，永远不是！",
 "Pull your finger? I can barely see it.": "拉你的手指？我几乎看不见它。",
 "*Follow* my finger.": "*跟着*我的手指。",
 "I don't care where it's comin' from, y'all need to get gone!":
    "我不管它从哪儿来，你们得赶紧走！",
 "You two have some nerve showin' yer faces back in Hollow Point. August'll have yer hides.":
    "你们俩还敢回空心镇露面，胆子不小。August 会扒了你们的皮。",
 "[to Jimbo] I heard you was dead. It's a damn shame yer still kickin'.":
    "[to Jimbo] 我听说你死了。可惜你还在喘气。",
 "*furious mumbling denial*": "*愤怒地嘟囔否认*",
 "What're the stars doin' out? I thought we was in a cave.":
    "星星怎么出来了？我以为我们在山洞里。",
 "You best unhand me friendo 'fore I shove a pipin' hot pimentaco up your tail pipe, ya hear.":
    "你最好把我放开，哥们，不然我就把一个滚烫的辣椒塔可塞进你的排气管，听到了吗。",
 "You best unhand me friendo 'fore I shove a pipin' hot pimentaco up your tail pipe.":
    "你最好把我放开，哥们，不然我就把一个滚烫的辣椒塔可塞进你的排气管。",
 "Yeah, beat it, unless you want this to get *ugly* and by ugly I mean I'll rearrange your faces with my wrench and make you uglier than you already are, which, if we're all being honest, would be really hard to do. So, yeah...":
    "是啊，滚吧，除非你想把事情搞得*难看*，我说的难看我是指我用扳手把你们的脸重新排一遍，让你们比现在更丑——说实话，那可真挺难的。所以，是啊……",
 "You best get lost 'fore I shove two pipin' hot pimentacos up your tailpipes, ya hear.":
    "你最好滚蛋，不然我就把两个滚烫的辣椒塔可塞进你们的排气管，听到了吗。",
 "Y'all must be outta yer damn heads draggin' yer hairy knuckles up to my new place.":
    "你们拖着毛手毛脚到我新地盘来，肯定是脑子坏了。",
 "Mind yer lip, Scooter. You know we'd only come here for a damn good reason.":
    "注意你的嘴，斯库特。你知道我们来这儿肯定有十足的理由。",
 "[VO] Awwg.": "[VO] 嗷。",
 "[VO] Have a nice ride.": "[VO] 坐车愉快。",
 "[VO] Ooof!": "[VO] 呃！",
 "*angry shouting*": "*愤怒地喊叫*",
 "Well whaddaya know. Gravity and such. I think my brain's broke.":
    "你猜怎么着。重力什么的。我觉得我脑子坏了。",
 "You've already caused us enough trouble.": "你已经给我们惹了够多麻烦。",
 "Not to mention the targets you already have on your backs that almost got us killed.":
    "更别说你们背上已经有的、差点把我们害死的靶子。",
 "You might need our help.": "你们可能需要我们帮忙。",
 "Sounds like a trap.": "听着像个陷阱。",
 "Exactly. If Felix was hiding something, chances are it'd be here. [re: Rhys's ECHOeye] You might catch something we never could.":
    "正是。要是 菲利克斯 藏了什么，很可能就在这儿。[re: Rhys's ECHOeye] 你也许能看出我们从来看不出的东西。",
 "If you want to make yourselves useful, try to find out what Felix was doing in the van before he crashed the arena.":
    "你们想有点用的话，就查查 菲利克斯 在把竞技场搞砸之前在这车里干什么。",
 "You want us to look through your stuff?!": "你想让我们翻你们的东西？！",
 "Guess who's back to hisself?": "猜猜谁恢复正常了？",
 "I'm back to myself and in a whole lotta pain.": "我恢复正常了，而且疼得要命。",
 "This ain't yogi, is it?": "这不是瑜伽吧？",
 "Just breathe.": "呼吸就行。",
 "And don't break anything!": "还有别弄坏任何东西！",
 "Whatever happens, we'll deal with it. Just like we always do.":
    "不管发生什么，我们都会处理。就像我们一直做的那样。",
 "Then good luck out there.": "那外面祝你好运。",
 "Y'all got no business tresspassin' on mah franchise.": "你们无权闯进我的地盘。",
 "[to FIona and Sasha]<<id:362795934>> You two have some nerve showin' yer faces back in Hollow Point. August'll have yer hides.":
    "[to FIona and Sasha]<<id:362795934>> 你们俩还敢回空心镇露面，胆子不小。August 会扒了你们的皮。",
 "*mencing jibberish*": "*威胁的胡话*",
 "[to Fiona and Sasha]:": "[to Fiona and Sasha]：",
 "You better not be lyin'. August says, if Strauss, or two Hyperion double-crossers turn up, you come get us lickety-split.":
    "你最好别撒谎。August 说，要是 Strauss，或者两个 亥博龙叛徒出现，你就赶紧来叫我们。",
 "I done told ya. I ain't seen no Lydia Strauss, archay-ologist or otherwise. Now get the hell off mah property.":
    "我跟你说过了。我没见过什么 Lydia Strauss，考古学家还是别的什么。现在滚出我的地盘。",
 "He's hurt. We gotta help him.": "他受伤了。我们得帮他。",
 "Aaawg.": "嗷。",
 "He's hurt.": "他受伤了。",
 "We can't just leave him here.": "我们不能就这么把他扔在这儿。",
 "It's too dangerous. The Hodunks could come back any minute.":
    "太危险了。Hodunk 一家随时可能回来。",
 "I'll keep an eye out.": "我来盯着。",
 "He's just a mechanic.": "他只是个修车工。",
 "We don't know if we can trust him.": "我们不知道能不能信他。",
 "I'm willing to take that risk.": "我愿意冒这个风险。",
 "That doesn't mean he's *our* friend.": "那不代表他是*我们的*朋友。",
 "I always do.": "我一向如此。",
 "Okay, we'll help him. But stay alert.": "好，我们帮他。但保持警惕。",
 "I say we give him a hand.": "我说我们帮他一把。",
 "And I can't risk a vault because you feel sorry for him.":
    "而我不能因为你同情他就拿一座秘藏冒险。",
 "If you can't make up your mind, I say we give him a hand.":
    "你要是决定不了，我说我们帮他一把。",
 "All right, fine. We'll help him. But stay alert.": "好，行。我们帮他。但保持警惕。",
 "Lead the way.": "带路。",
 "Howdy, ladies. At yer service. [to Sasha] Especially yers.":
    "你好啊，女士们。听候差遣。[to Sasha] 尤其是你的。",
 "Well, with all the moonshots too close fer comfort, and rumors of Hyperions snoopin' around, not to mention the dozen loader-bots I heard destroyed Prosperity Junction, it's like someone stepped on an ant hill.":
    "这个，月球投射近得让人不安，还有 亥博龙的人在附近打探的传言，更别说我听说有十几台装载机器人把繁荣枢纽给毁了，简直像有人踩了蚂蚁窝。",
 "You wanna tell us what happened with the Hodunks?": "你想跟我们说说 Hodunk 一家是怎么回事吗？",
 "All the li'l buggers are mad as hell.": "所有小虫子都气疯了。",
 "First we've heard of it.": "这我们还是头一回听说。",
 "Sounds scary.": "听着挺吓人。",
 "I reckon yer right.": "我想你说得对。",
 "That's Pandora for you.": "潘多拉 就是这样。",
 "Yeah, we know. Must be another crackdown.": "是啊，我们知道。肯定又是一次镇压。",
 "Well ain't that perfect. I open mah new franchise in the middle of a shitstorm.":
    "这可真完美。我在一场屎风暴中间开了我的新加盟店。",
 "We don't know anything about it.": "我们什么都不知道。",
 "Then you must'a been livin' under a rock. [glancing around] Guess I shouldn't be talkin'.":
    "那你肯定是住在石头底下。[glancing around] 我想我不该说。",
 "You don't know the half of it.": "你知道的连一半都不到。",
 "All right. Let's skip the small talk.": "好。我们别闲聊了。",
 "If you know anythin', spill the beans.": "你要是知道什么，就都说出来。",
 "Maybe you two travelers have some idea 'bout what's goin' on.":
    "也许你们两位旅人知道点什么正在发生的事。",
 "It's hard enough openin' a new business without yer crazy family threatenin' ya every second.":
    "开新店本来就够难了，还要被你那个疯家人时时刻刻威胁。",
 "I'm startin' to hate this town.": "我开始讨厌这镇子了。",
 "Tell me about it.": "还用你说。",
 "So what happened to yer van?": "那你们的车怎么了？",
 "Can you fix it or not?": "你到底能不能修？",
 "Just an accident.": "只是个意外。",
 "It's a long story.": "说来话长。",
 "Wow, that's heavy. Sorry fer yer troubles.": "哇，这可真沉重。为你们的遭遇感到抱歉。",
 "It's a long story, but this is all because our partner betrayed us. We almost died.":
    "说来话长，但这一切都是因为我们搭档背叛了我们。我们差点死了。",
 "Fixin's this here van's the least I can do.": "修好这辆车是我起码能做的。",
 "Just your typical accident. I got distracted and hit another car.":
    "就是普通的意外。我分了神，撞了另一辆车。",
 "Looks more like ya hit a spiderant.": "看着更像是你撞了只蛛蚁。",
})

T.update({
 # —— Scooter 谈价钱 / Fiona 讨价 ——
 "Jeez louise, no need to get mad. I can fix anything, given half a chance.":
    "天哪，别生气。给我个机会，我什么都能修。",
 "Don't worry about it. Can you fix it or not?": "别管那个。你到底能不能修？",
 "It was an accident, that's all.": "是个意外，就这样。",
 "That's what we're giving you.": "我们给你的就是这个。",
 "By the looks of it, y'all we're involved in something serious.":
    "看样子，你们卷进什么严重的事里了。",
 "It's a miracle ya got here at all.": "你们能开到这儿都是奇迹。",
 "Now I'm gonna be honest.": "那我就直说了。",
 "We're not in trouble.": "我们没惹上麻烦。",
 "Mind your own business.": "管好你自己的事。",
 "You're right. The Hodunks are after us.": "你说得对。Hodunk 一家在追我们。",
 "I knew it! You cain't fool 'ol Scooter!": "我就知道！你骗不过老 斯库特！",
 "If you say so. But I got my suspicions.": "你要是这么说那就好。但我有我的怀疑。",
 "It is if I fix yer van and they come after me.": "要是我修了你们的车，他们来找我，那就有关系了。",
 "Look, we don't need to tell you anything.": "听着，我们什么都不用告诉你。",
 "I'm just sayin' it'd be nice to know what I'm gettin' into.": "我只是说，知道我要掺和进什么事会挺好。",
 "You need to stay out of our business.": "你得离我们的事远点。",
 "That's none of your concern.": "不关你的事。",
 "You're gonna have to trust us.": "你们只能信我们。",
 "Trust? In Hollow Point? That's a good one.": "信任？在空心镇？这笑话不错。",
 "I hope you'll still help us.": "我希望你还是会帮我们。",
 "I hate those fellers. I'll help you all right.": "我讨厌那帮家伙。我会帮你们的，没问题。",
 "Y'all can be honest with me.": "你们可以跟我说实话。",
 "I know somethin's goin' on.": "我知道有事在发生。",
 "That's all right. You don't have to tell me. But I got my suspicions.":
    "没关系。你不必告诉我。但我有我的怀疑。",
 "Besides, he's obviously no friend of the Hodunks.": "再说，他显然不是 Hodunk 一家的朋友。",
 "He needs us.": "他需要我们。",
 "I tell you what. An enemy of Tector is a friend of mine. I'm highly inclined to fix yer van.":
    "我跟你说。Tector 的敌人就是我的朋友。我非常倾向于修你们的车。",
 "Tector would hate it!": "Tector 会气死的！",
 "It would impress Sasha.": "那会让 萨莎 印象深刻。",
 "What with yer arrival right after all these goings-on, the sorry state of yer van, and the Hodunks warnin' me to look out for two lady grifters, I think you might be in some kinda trouble.":
    "你们偏偏在这一切发生之后出现，车又是这副惨样，Hodunk 一家还警告我留意两个女骗子，我想你们可能惹上什么麻烦了。",
 "What's this going to cost?": "这要花多少钱？",
 "We can't risk it.": "我们不能冒这个险。",
 "Oh, I'll fix'er up all right. Especially if it pisses off that sumbitch.":
    "哦，我会把她修好的。尤其是如果能气死那狗娘养的。",
 "I'm in!": "我加入！",
 "Tector would be furious if you suped-up our van.": "你要是改装我们的车，Tector 会气疯的。",
 "I know if you suped-up our van, Sasha would be really impressed.":
    "我知道你要是改装我们的车，萨莎 会印象深刻的。",
 "I'll make her purr like a kitten.": "我会让她像小猫一样咕噜咕噜叫。",
 "[winking at Sasha] And I'll fix yer van too!": "[winking at Sasha] 我也会把你们的车修好！",
 "I'll fix'er up good. Y'all don't worry 'bout a thing.": "我会把她修得妥妥的。你们一点不用操心。",
 "That's a nice chunk 'a change.": "这可不是一笔小钱。",
 "How much is this going to cost me?": "这得花我多少钱？",
 "Y'all don't worry 'bout a thing.": "你们一点不用操心。",
 "That's all I right. I feel ya. I'll fix'er up good.": "就这些了。我懂。我会把她修好的。",
 "If it makes the Hodunks mad, sounds good to me.": "要是能让 Hodunk 一家不爽，我没意见。",
 "I'd like to help you out.": "我想帮你们一把。",
 "Uh-huh. Yes'm. Oh my.": "嗯哼。是的女士。哦天。",
 "She's cryin' out for a new tappet head, her knurled piston's busted, and cleanin' up that harmonic compensator would do her a world 'a good.":
    "她正急需一个新的挺杆头，她的滚花活塞也坏了，再清理一下那个谐波补偿器，对她会有天大的好处。",
 "Thanks, Scooter. You're amazing.": "谢谢你，斯库特。你太厉害了。",
 "Where y'all goin'?": "你们去哪儿？",
 "S'cuse me ladies.": "失陪了女士们。",
 "Okay, I get it. Secret mission and such. Be careful.": "好，我懂了。秘密任务什么的。小心点。",
 "It's not safe out there for you.": "外面对你们来说不安全。",
 "At least gimme me a hint.": "至少给我点提示。",
 "It's safer not to know.": "不知道更安全。",
 "Our old partner's place.": "我们老搭档的地方。",
 "Focus on the van.": "专心修车。",
 "To our old partner's place.": "去我们老搭档的地方。",
 "Y'all be careful, ya hear.": "你们小心点，听到了吗。",
 "We've learned to be ready for anything.": "我们学会了随时准备应对一切。",
 "We'll": "我们会",
 "You will come back, and that's all there is to it.": "你会回来的，就这样。",
 "I'm gonna. I was worried about you is all.": "我会的。我只是担心你而已。",
 "We can handle ourselves. [re: the van] Just make sure she's ready by the time we get back.":
    "我们能照顾自己。[re: the van] 只要确保我们回来的时候她准备好了。",
 "Focus on fixing the van.": "专心修车。",
 "The less you know the better.": "你知道得越少越好。",
 "I was worried about you is all.": "我只是担心你而已。",
 "We can handle ourselves, but it's safer for you to pretend we never met.":
    "我们能照顾自己，但你假装我们从没见过会更安全。",
 "All right. Just come back in one piece.": "好。平安回来就行。",
 "See ya soon, ladies.": "回头见，女士们。",
 "Watch yer backs.": "注意背后。",
 "I hope Felix doesn't have any more nasty surprises at his safehouse.":
    "我希望 菲利克斯 的安全屋里没有更多恶心的惊喜了。",
 "I guess we're gonna find out.": "我想我们马上就会知道。",
 "*Whistling*.": "*吹口哨*。",
 "You better not be lyin'.  If Strauss, or two Hyperion double-crossers turn up, you come get us lickety-split.":
    "你最好别撒谎。要是 Strauss，或者两个 亥博龙叛徒出现，你就赶紧来叫我们。",
 "He's hurt. We should help him.": "他受伤了。我们该帮他。",
 "They're looking for us! We should cut our losses and go.":
    "他们在找我们！我们该及时止损走人。",
 "We'll just grab a couple things before we go.": "我们走之前拿几样东西就行。",
 "Take yer time. I got lots to do.": "你们慢慢来。我有很多活要干。",
 "And I can't risk everything because you feel sorry for him.":
    "而我不能因为你同情他就拿一切冒险。",
 "Hey, uh... you wasn't travelling with no one else, was you?":
    "嘿，呃……你们没跟别人一起旅行吧？",
 "We're alone.": "只有我们。",
 "Can you keep a secret?": "你能保守秘密吗？",
 "Yer actin' kinda funny.": "你表现得有点怪。",
 "Like yer hidin' somethin' else. Or someone.": "像是还在藏着别的什么。或者藏人。",
 "Y'all don't gotta worry 'bout me. Do what ya gotta do.":
    "你们不用担心我。做你们该做的。",
 "Okay, okay, you don't gotta tell me nuthin'.": "好，好，你什么都不用告诉我。",
 "I'll just do mah job.": "我就干我的活。",
 "It's just us.": "就我们俩。",
 "I thought maybe you was talking with somebody when ya'll first got here.":
    "你们刚来的时候，我还以为你们在跟什么人说话。",
 "Nope. My sister and I travel alone.": "没有。我和我妹妹独自旅行。",
 "Enough with the damn questions.": "该死的，问题别问了。",
 "Whoo boy, I done stepped in it.": "哎呀天，我这可踩进屎里了。",
 "I sure am sorry for givin' offense.": "我真抱歉冒犯了你。",
 "Just mind your own business and we'll be fine.": "管好你自己的事，我们就相安无事。",
 "Hyperions. Blech! But a vault?! WOOOEEEE!": "亥博龙人。呸！但一座秘藏？！呜——！",
 "If we tell you something, can you keep it to yourself?": "我们要是告诉你点什么，你能保密吗？",
 "Mah lips are sealed.": "我的嘴封上了。",
 "Sorry, it's just so excitin'. And dangerous.": "抱歉，只是这太让人兴奋了。而且危险。",
 "Remember not to tell anyone.": "记住别告诉任何人。",
 "Yer secret's safe with me. Hot damn.": "你的秘密在我这儿很安全。他妈的。",
 "All right. We're traveling with two Hyperions. They're helping us find a vault.":
    "好。我们在跟两个 亥博龙人一起旅行。他们帮我们找一座秘藏。",
 "I guess mah mind is playin' tricks on me. Not the first time.":
    "我想是我脑子在跟我开玩笑。也不是第一次了。",
 "They're after us! Maybe we should cut our losses and go.":
    "他们在追我们！也许我们该及时止损走人。",
 "But it looks like he needs help.": "但看起来他需要帮助。",
 "Okay, we'll help.": "好，我们帮。",
 "What if you're being set up?": "要是你被设局了呢？",
 "He was the only person we could trust. What happened back there?":
    "他是我们唯一能信的人。刚才到底发生了什么？",
 "The way Felix used to fix'er up, I thought she'd last forever.":
    "照 菲利克斯 以前修她的方式，我以为她能撑到永远。",
 "Think we'll make it to Hollow Point?": "你觉得我们能开到空心镇吗？",
 "We got away from those Hyperion losers.": "我们甩掉了那些 亥博龙废物。",
 "I guess there's one small silver lining.": "我想总算还有一点点好的一面。",
 "But what happened to Felix was the result of his own choices. The sooner we accept that, the better.":
    "但 菲利克斯 的遭遇是他自己选择的结果。我们越早接受越好。",
 "It's possible we'll never know.": "我们可能永远不会知道。",
 "I'll always wonder if he *ever* cared about us.": "我会一直想知道他到底*有没有*在乎过我们。",
 "You did the best you could.": "你已经尽力了。",
 "I'm sorry he put you in that position.": "抱歉他让你陷入那种境地。",
 "Maybe he was in trouble.": "也许他是遇上麻烦了。",
 "But we counted on each other.": "但我们彼此依靠。",
 "Maybe he didn't want to get us involved.": "也许他不想把我们牵扯进来。",
 "Then he should've told us.": "那他该告诉我们。",
 "He could've been in trouble.": "他可能是遇上麻烦了。",
 "I guess he got greedy.": "我想他是贪心了。",
 "Maybe it was too big to resist.": "也许那太诱人，难以抗拒。",
 "But we were in it together.": "但我们是一起做的。",
 "He was always after the big score.": "他一直在追大买卖。",
 "My guess is he got greedy.": "我猜他是贪心了。",
 "I still can't believe he's gone.": "我还是无法相信他走了。",
 "I don't care about his reasons. We could've been killed.":
    "我不在乎他的理由。我们本来可能会死。",
 "We don't know that! He must've had his reasons.": "我们不知道！他肯定有他的理由。",
 "It doesn't matter. He betrayed us.": "无所谓。他背叛了我们。",
 "He was the closest thing we had to a father.": "他是我们最接近父亲的存在。",
 "I'll never get over it.": "我永远放不下。",
 "You could've done it another way.": "你本可以用别的方式。",
 "You don't understand. I had to protect us.": "你不明白。我必须保护我们。",
 "We were supposed to look out for each other.": "我们本该互相照应。",
 "I don't get it.": "我不明白。",
 "He got what he deserved.": "他得到了他应得的。",
 "[softening] I still can't believe he's gone.": "[softening] 我还是无法相信他走了。",
 "He deserved what he got.": "他得到了他应得的。",
 "I loved him too.": "我也爱他。",
 "We were a family.": "我们曾是一家人。",
 "I did it for you.": "我是为了你。",
 "You're all I've got.": "你是我唯一的亲人。",
 "The thought of anybody hurting you...": "一想到有人会伤害你……",
 "I can protect myself!": "我能保护自己！",
 "I did it to protect you.": "我那么做是为了保护你。",
 "He left me no choice.": "他让我别无选择。",
 "He brought it on himself.": "他自作自受。",
 "What you did is unforgiveable.": "你做的事不可原谅。",
 "There's always a choice.": "总有选择。",
 "The point is you don't know.": "重点是你不知道。",
 "Who's to say he wouldn't have betrayed us again?": "谁能说他不会再背叛我们一次？",
 "We could've given him another chance.": "我们本可以再给他一次机会。",
 "Maybe he got greedy.": "也许他贪心了。",
 "You should've given him a chance to explain himself.":
    "你本该给他一个解释的机会。",
 "Hi, my name's Rhys. I wanna be like Handsome Jack when I grow up, and I'm so slick I tried to buy a fake vault key.":
    "嗨，我叫 瑞斯。我长大了想成为帅杰克那样的人，而且我机灵到去买了一把假秘藏钥匙。",
 "Sanctuary's too far.": "避风港太远了。",
 "We should go to Scooter's garage.": "我们该去 斯库特 的车库。",
 "I don't know no Libia Strauss, archay-ologist or otherwise. Now get the hell off mah property.":
    "我不认识什么 Libia Strauss，考古学家还是别的什么。现在滚出我的地盘。",
 "I never heard of no Livia Strauss, archay-ologist or otherwise. Now get the hell off mah property.":
    "我从没听过什么 Livia Strauss，考古学家还是别的什么。现在滚出我的地盘。",
 "Felix wrecked it.": "菲利克斯 把它弄坏的。",
 "Moonshots.": "月球投射。",
 "Well, tell ya what.  I'll give ya some options...":
    "这个，我跟你说。我给你几个选择……",
 "Now, the basic repair package, I'll give that to ya'll for free, but if ya got the cash, I can add a few upgrades!":
    "那么，基础维修套餐，我免费给你们，但要是你们有钱，我可以加几项升级！",
 "Think we'll even make it to Old Haven?": "你觉得我们还能开到老避风港吗？",
 "We need to get this thing to a garage.  Maybe Scooters?":
    "我们得把这东西弄到车库去。也许 斯库特 那儿？",
 "He just opened one in Hollow Point, we're still not too far from there.":
    "他刚在空心镇开了一家，我们离那儿还不算太远。",
 "[laughs]": "[laughs]",
 "We were hit by moonshots.": "我们被月球投射炸了。",
 "Dang! Y'all must be in some serious trouble.": "该死！你们肯定惹上大麻烦了。",
 "You could say that.": "可以这么说。",
 "I don't gotta say it, I can see it!": "我不用说，我看得出来！",
 "Alrighty, then. I'll get started.": "那好。我这就开工。",
 "We're cool with the basic package.": "基础套餐我们就行。",
 "Hey, wake up...": "嘿，醒醒……",
 "Is he okay?": "他没事吧？",
 "I know, I know. You're dazzled by the options. Tell you what, I'll give you the basic package, and we'll go from there.":
    "我知道，我知道。这些选择让你眼花。这样吧，我给你基础套餐，然后我们再往下谈。",
 "If you don't want to get too splashy, but are desirin' some extra oomph, ya can't go wrong with option B, the Scooter Value Package.":
    "你要是不想太张扬，但想要点额外马力，选 B 套餐准没错——斯库特 实惠包。",
 "But if shock and awe is what yer after, it's Option C - The Scooter Special. I get the shivers just thinkin' 'bout it. So, what'll it be for you today?":
    "但你要是追求震撼与敬畏，那就选 C 套餐——斯库特 特装。光是想想我就浑身发抖。那，今天你们要哪个？",
 "We'll take Option B.": "我们要 B 套餐。",
 "Suh-weet. You won't be disappointed.": "妙——啊。你不会失望的。",
 "We want Option C. The works.": "我们要 C 套餐。全套。",
 "Woo-hoo! Get ready to have yer minds blown!": "呜——呼！准备好被震撼吧！",
 "It just seems like yer not alone.": "只是感觉你们不是一个人。",
 "I got a feelin' for these kinda things.": "我对这种事有感觉。",
 "Sounds dangerous.": "听着挺危险。",
 "[under his breath] What an honor.": "[under his breath] 真是荣幸。",
 "Just past the docks, you'll find Emmit's Shop. He'll have the tech, and he sells to Hyperions.":
    "过了码头，你会找到 Emmit 的店。他那儿有那种技术，而且他卖给 亥博龙人。",
 "Listen up. While we deal with the van, we're gonna need you to get a jammer to shield us from more attacks.":
    "听好了。我们处理车的时候，需要你们去弄个干扰器，好让我们免受更多攻击。",
 "It is dangerous.": "那确实危险。",
 "Just be careful.": "小心点就行。",
 "Not if you lay low.": "你低调点就不会。",
 "Terrific.": "太好了。",
 "Hollow Point was founded by cutthroats, criminals, and refugees from Hyperion tyranny.":
    "空心镇是由割喉者、罪犯，以及逃离 亥博龙暴政的难民建立的。",
 "Pandorans may hate you, but in Hollow Point, that hatred is the blood in their veins. It keeps them alive.":
    "潘多拉 人也许恨你们，但在空心镇，那份恨是他们血管里的血。正是它让他们活着。",
 "That's because it is dangerous.": "因为那确实危险。",
 "I'm beginning to think we're not welcome here.": "我开始觉得我们在这儿不受欢迎。",
 "Stay alert and stick to the shadows.": "保持警惕，贴着阴影走。",
 "Just be careful. You're no good to us dead.": "小心点。你死了对我们没用。",
 "Just don't do anything that could draw attention to us.": "别做任何可能引来注意的事。",
 "The key is to stay out of sight. You've caused us enough trouble.":
    "关键是不露脸。你已经给我们惹了够多麻烦。",
 "I know you'd never intentionally endanger us.": "我知道你绝不会故意危害我们。",
 "I'm not sure I like this plan.": "我不太喜欢这个计划。",
 "Sounds like we'll be walking targets.": "听起来我们会是走动的靶子。",
 "So it's settled then. Just stay alert and stick to the shadows.":
    "那就这么定了。保持警惕，贴着阴影走就行。",
 "Fine. Vaughn and I can handle anything this dump throws at us.":
    "行。这垃圾堆扔给我们什么，沃恩 和我都应付得了。",
 "Good luck getting to Emmit's. And keep a low profile!": "祝你们顺利到 Emmit 那儿。低调点！",
 "Attacks *you* brought on us.": "是*你们*招来的攻击。",
 "They live for the day that Helios burns.": "他们活着就为了等 太阳神烧起来的那天。",
 "[re: Sasha] Someone call the waaambulance.": "[re: Sasha] 谁去叫辆哭哭车。",
 "Tyranny? I brought order to chaos. A thank you would be nice.":
    "暴政？我给混乱带来了秩序。道声谢会不错。",
 "I shoulda crushed every last one of these cockroaches.":
    "我早该把这些蟑螂一个个碾死。",
 "Oooh. Scary.": "哦哦。好吓人。",
 "Tyranny? We brought order to chaos. A thank you would be nice.":
    "暴政？我们给混乱带来了秩序。道声谢会不错。",
 "I hope he'll fix it. We're low on funds.": "我希望他能修好。我们资金紧张。",
 "Stay here. I'll do the talking.": "待在这儿。我来说话。",
})

# —— Scooter 车库：讨价还价主干对白（带表情标签）——
T.update({
 "{ShockA}Aw hey man {HappyA}welcome to Scooter's Catch-A-Ride. {SmugA}What can we do for you today?":
    "{ShockA}哦嘿，老兄{HappyA}欢迎来到 斯库特 的 Catch-A-Ride。{SmugA}今天能为你们做点什么？",
 "This ain't my first rodeo, I'll tell you that much.":
    "这可不是我第一回上马，这点我可以告诉你。",
 "[Appraisingly] {InquireA}{Body-A}This is a really nice looking place {SchemeB}{Body-HipR}you have here, Scooter.":
    "[Appraisingly] {InquireA}{Body-A}你这地方看着真不错{SchemeB}{Body-HipR}，斯库特。",
 "Why thank you. Built it mah self. Now all I need is Springs to run it.":
    "谢谢夸奖。我自己盖的。现在就差 Springs 来管店了。",
 "Well, from the looks of things, you obviously know what you're doing.":
    "这个，从这情形看，你显然很懂行。",
 "{InquireA}{Body-A}My ride's {WorryB}trashed - {SchemeB}{Body-HipR}Think you could help me out?":
    "{InquireA}{Body-A}我的座驾{WorryB}废了——{SchemeB}{Body-HipR}你觉得能帮我一把吗？",
 "Judgin' by the looks 'a things, it ain't gonna be cheap.":
    "照这情形看，便宜不了。",
 "I'm just hoping you can fix it.": "我只希望你能修好它。",
 "I can dang near fix anything. For the right price.":
    "给够了钱，我他妈什么都能修。",
 "{InquireA}{Body-A}\"New proprieter{Body-HipR}?\"": "{InquireA}{Body-A}“新老板{Body-HipR}？”",
 "It's nuthin really.": "真没什么。",
 "Looks pretty complicated.": "看着挺复杂。",
 "For the average layman maybe, but for 'ol Scooter, puttin' together engines is as easy as pie.":
    "对普通外行也许吧，但对老 斯库特 来说，组装引擎就跟吃派一样容易。",
 "I can tell.": "我看得出来。",
 "This here's where the magic is.": "魔法就在这儿。",
 "I'm no psychic. You gotta tell me what kind of repairs you need.":
    "我不是算命的。你得告诉我你需要什么修理。",
 "I'd luv to be 'a service to ya.": "我很乐意为你效劳。",
 "If yer needin' repairs, I got everthin' to do the job.":
    "你要是需要修车，干活的家伙我全都有。",
 "Say, don't I know you? You look pretty darn familiar. And I never forget a face. Except sometimes.":
    "我说，我是不是认识你？你看着特别眼熟。我从不忘记一张脸。除了有时候。",
 "Wanted, huh. You must be in a world 'a trouble. A life 'a danger and derrin' do. Sounds cray-zey!":
    "通缉，哈。你肯定陷进天大的麻烦里了。刀口舔血、出生入死的日子。听着可真疯！",
 "You ain't lyin'. I want ya and I hardly even know ya. Jus' kiddin. Sorta.":
    "你没说谎。我都没怎么认识你就想要你了。开玩笑的。算是吧。",
 "That's because I'm a wanted woman.": "因为我是个被通缉的女人。",
 "Of course. That's what I thought you thought I meant. I think.":
    "当然。我就是想你以为我以为的那个意思。我想。",
 "I mean you've probably seen my wanted poster all over town.":
    "我是说你大概在镇上到处都见过我的通缉海报。",
 "Where you been all mah life? I can't believe it. A gal who loves cars as much as I do.":
    "我这一辈子都在哪儿找的你？我不敢相信。一个像我一样爱车的姑娘。",
 "Best on Pandora.": "潘多拉 上最棒的。",
 "Oooweee. I never met a real life celebrity. And a racer to boot. Damn.":
    "哦——喂。我从没见过活生生的名人。而且还是赛车手。该死。",
 "{SmugC}You watched the latest Bossanova Arena Death Race... thing?":
    "{SmugC}你看过最近那场 Bossanova 竞技场死亡竞速……玩意儿吗？",
 "Girl, we have so much in common it ain't funny. Yer like me but a woman. Guess that means I'm attracted to mah self. Suh-weet!":
    "姑娘，我们的共同点多得都不好笑了。你就像我，只不过是个女的。那我猜我是被我自己吸引了。妙——啊！",
 "I don't feel alive unless I'm behind the wheel.":
    "不坐在方向盘后面，我就感觉不到自己活着。",
 "No kiddin.' You must be all sorts 'a fearless.": "不开玩笑。你肯定各种天不怕地不怕。",
 "I live for danger.": "我为危险而活。",
 "A bona fide vault hunter. Well I'll be. Sexiest dang Vault Hunter I ever seen.":
    "货真价实的秘藏猎人。哎呀我的天。我见过最性感的秘藏猎人。",
 "Because I'm a vault hunter.": "因为我是秘藏猎人。",
 "Wow. You got me shakin' in mah boots, and that ain't easy. Unless I gotta drain mah iguana.":
    "哇。你把我吓得靴子都在抖，而这可不容易。除非我得去给我的鬣蜥放水。",
 "That's what they tell me.": "他们都这么说。",
 "You don't have to tell me nuthin'. But you can't fool Scooter. I know I know you from somewheres.":
    "你什么都不用告诉我。但你骗不过 斯库特。我知道我肯定在哪儿见过你。",
 "Wait a minute. It's comin' to me...dang!": "等等。我想起来了……该死！",
 "I can't quite place yer face, but I seen it before.":
    "我一时想不起你这张脸在哪儿见过，但我肯定见过。",
 "Well, listen, chit-chattin' with you has been a real pleasure, but let's talk business. Fixin' this here van will cost ya about two thousand five hunerd. It don't take an expert to tell you how messed up it is.":
    "好吧，听着，跟你闲聊真的很愉快，但我们谈生意吧。修这辆车大概要花你两千五。这车有多烂，用不着专家也能看出来。",
 "Well ain't that a damn shame.": "这可真他妈可惜。",
 "I hear ya. But that's how much it is.": "我懂。但就是这个价。",
 "That's way beyond our budget.": "那远超我们的预算。",
 "Parts is parts and labor's labor. Yer also gettin' mah years of ex-per-tise.":
    "零件是零件，工时是工时。你还在享受我多年的专业经验。",
 "It's just way too much money.": "这实在是太多了。",
 "{FearA}Okay. {HappyC}How about a down payment. {DoubtfulA}Just to get you started?":
    "{FearA}好。{HappyC}付个定金怎么样。{DoubtfulA}就让你能开工？",
 "Fine, but a little cash should get you started.":
    "行，但一点现金应该能让你开工。",
 "I dunno...you seem real sincere and all...I don't normally do this...":
    "我不知道……你看着挺真诚的……我平时不这么做……",
 "I usually need the full amount to get goin'. And don't forget yer gettin' Scooter-quality work.":
    "我通常要收全款才开工。别忘了你得到的是 斯库特 品质的活儿。",
 "Great. When you do, come back to me and I'll fix yer van.":
    "好。等你拿到钱，回来找我，我就给你修车。",
 "But I really will have it.": "但我真的会拿到。",
 "I hear what yer sayin, but it's not mah normal way 'a doin' things. Ya feel me? That's okay, you don't have to. Unless you want to. Feel away.":
    "我听到你说的了，但这不是我平时的做法。懂我意思吗？没关系，你不必懂。除非你想懂。随便感受。",
 "I'll get the money soon.": "我很快就会拿到钱。",
 "I ain't gonna lie. I heard that one before. It's not that I don't wanna believe you...":
    "我不撒谎。这话我听过。不是我不想信你……",
 "{FearA}Will you do it on credit? {HappyC}I'll pay you later. I swear.":
    "{FearA}你能赊账做吗？{HappyC}我以后再付，我发誓。",
 "I got the skillz to fix'er up real good.": "我有本事把她修得妥妥的。",
 "And the best don't come cheap.": "而最好的可不便宜。",
 "But real good ain't the same as real cheap.": "但“挺好”跟“挺便宜”可不是一回事。",
 "'Guess you could say I been blessed.": "可以说我是被上天眷顾的。",
 "But it'll cost ya.": "但那得花你的钱。",
 "Between you and me, I got a big score coming my way. Help me out now, and you definitely won't regret it.":
    "你我之间说，我马上有一大笔进账。现在帮我一把，你绝对不会后悔。",
 "Well, I guess if you're a fugitive from the law, you could be cookin' up all kind 'a highly illegal but lucrative plots. Whatcha got in mind? I won't squeal. Loud. Hehe.":
    "这个，我想你要是逃犯，那你可能正在策划各种高度违法但很赚钱的勾当。你打算干什么？我不会告密。大声的那种。嘿嘿。",
 "You sure know how to bend a feller's ear, I tell you what.":
    "你还真会跟人唠，我跟你说。",
 "I'm gonna pull a major heist. Money. Jewels. You name it.":
    "我要做一票大的。钱。珠宝。随你说。",
 "You'll like it more when I bring you your share.":
    "等我把我那份给你带来，你会更喜欢的。",
 "Keep talkin' 'bout them shiny things. I like what I'm hearing.":
    "继续说那些亮闪闪的东西。我喜欢我听着的。",
 "Just 'cause I'm coming into money doesn't mean I'm gonna break the law.":
    "我要进账了，不代表我要犯法。",
 "If you ain't a criminal, and you ain't hatchin' no illicit schemes, I don't understand where you're gonna get the money to pay me.":
    "你要不是罪犯，也没在策划什么非法勾当，我就不明白你上哪儿弄钱付我。",
 "It does on Pandora.": "在 潘多拉 就是。",
 "Depends who's making the laws.": "得看是谁在定法律。",
 "Law abidin' citizens don't usually end up on wanted posters.":
    "守法公民一般不大会出现在通缉海报上。",
 "I know what it must look like, but I'm not really a criminal.":
    "我知道这看起来像什么，但我真的不是罪犯。",
 "What I do or don't do is none of your business.": "我做什么不做什么不关你的事。",
 "Ooh, boy. I done stepped in it now. But I don't believe a damn thing yer sayin'.":
    "哦，天。我这下可踩进屎里了。但你说的我他妈一个字都不信。",
 "Easy now. I just wanna know how you're gonna pay me.":
    "别急。我只是想知道你打算怎么付我钱。",
 "With cold hard cash. And how I come by it is none of your concern.":
    "用冷冰冰的硬现金。至于我怎么弄来的不关你的事。",
 "Yer awful quiet for someone on the verge of the score of a lifetime. That's prolly 'cause yer full of it.":
    "一个即将做成一笔一生一次大买卖的人，你可真够沉默的。大概是因为你在放屁。",
 "Well, I guess if yer a racing celebrity and all, you'll make a ton 'a money with yer winnings.":
    "这个，我想你要是赛车名人什么的，靠奖金能赚一大笔钱。",
 "Yeah, I got a big race coming up.": "是啊，我马上有场大赛。",
 "I love racin'. Which one?": "我爱赛车。哪一场？",
 "Well I'll be damned. I'm talkin' to a real Old Haven 500 driver. I gotta pinch myself. [Scooter pinches himself] Ouch. Damn it.":
    "我他妈的。我在跟一个真正的老避风港 500 车手说话。我得掐自己一下。[Scooter pinches himself] 哎哟。该死。",
 "Nothing except a brand new track. [off Scooter's look] Let me guess. You haven't been there in ages.":
    "除了是条全新赛道，没什么特别的。[off Scooter's look] 我猜猜。你好多年没去那儿了。",
 "Whoa. You must be amazin'...to race against ghosts! There's nuthin' out there.":
    "哇。那你肯定特别厉害……跟鬼比赛！那儿什么都没有。",
 "It's the Old Haven 500.": "是老避风港 500。",
 "There's big money to be had if yer willin' to steal.":
    "只要你肯偷，就有大钱可赚。",
 "And it sure seems like you're willin'.": "而看来你确实肯。",
 "With all this talk 'a criminal shenanigans, you seem awful sure you won't get caught.":
    "嘴上说着这些犯罪勾当，你好像特别确定自己不会被抓。",
 "If you pull off your cons as good as you talk, ain't no fool stands a chance.":
    "你要行骗的本事有嘴皮子一半好，就没哪个傻子挡得住你。",
 "Let's just say I love what I do, and I do it well.":
    "可以说我喜欢我的本行，而且干得好。",
 "Yer certainly got sass, I'll give ya that.": "你确实有股泼劲，这点我承认。",
 "That's 'cause I'm the best.": "因为我是最棒的。",
 "It's easy when you know what you're doing.": "懂行了就容易。",
 "Yer sure awful confident. But I wonder if you can back it up.":
    "你可真是自信。但我好奇你撑不撑得住。",
 "This job'll be like taking candy from a baby.": "这活儿就跟从婴儿手里抢糖一样。",
 "If you can steal as good as you talk, ain't no fool stands a chance.":
    "你要偷的本事有嘴皮子一半好，就没哪个傻子挡得住你。",
 "So yer a thief, AND a liar.": "所以你是小偷，*还是*骗子。",
 "That's 'cause there is no job.": "因为根本没什么活儿。",
 "And I'm done with your bullcrap. Ain't no way I can trust that you'll pay me. No ma'am.":
    "你的狗屁我听够了。我绝不可能信你会付我钱。不行，女士。",
 "I'm whatever I have to be.": "需要我是什么，我就是什么。",
 "Well, you don't have to tell me, I guess. Just figured I'd try and make conversation, man.":
    "这个，我想你不必告诉我。我只是想着聊两句而已，老兄。",
 "I wonder what yer hidin'.": "我很好奇你在藏什么。",
 "You must be pretty darn crafty to avoid the strong arm of the law.":
    "能躲过法律的铁腕，你肯定挺狡猾。",
 "*The* Hollow Point Drags?! That's the best dang race there is!":
    "*就是* 空心镇直线加速赛？！那是最好的一场比赛！",
 "The Hollow Point Drags of course.": "当然是空心镇直线加速赛。",
 "I must be dreamin'. Yer 'a force 'a nature.": "我肯定在做梦。你是一股自然之力。",
 "When you live for speed like me, it's the only race that matters.":
    "像这样为速度而活的人，只有那场比赛才算数。",
 "Wait there just a minute. That don't sound right. As matter 'a fact, it sounds like a big 'ol pile of stinkin' bullcrap.":
    "你等等。这听着不对。事实上，听着像一大坨臭烘烘的狗屁。",
 "With so many races, they all blur together.": "比赛太多了，全都混在一起了。",
 "Any racer worth their salt knows what race they're in. I think the only thing yer runnin' is yer lip.":
    "有点本事的车手都知道自己在跑哪场。我看你唯一在跑的就是你那张嘴。",
 "I can't remember the name is all.": "我就是想不起名字而已。",
 "I been a fan forever.": "我一直是个粉丝，一直。",
 "Must be excitin' all those races.": "那些比赛肯定很刺激。",
 "Well, don't keep me guessin'. How'd it go?": "这个，别让我猜。结果怎么样？",
 "Truth is, I only raced once.": "实话是，我只赛过一次。",
 "Yer my kinda gal. Wish I coulda seen it.": "你就是我那型姑娘。真希望我看到了。",
 "It was amazing. Not even close.": "太惊人了。简直毫无悬念。",
 "I could tell just by lookin' at ya! You got the bones for racin'.":
    "我光看你就看得出来！你有赛车的骨相。",
 "Oh I won. By a mile. Asses kicked all around.":
    "哦我赢了。赢了一英里。把别人屁股都踹遍了。",
 "I did all right.": "我还行。",
 "Sounds to me like you owned that track.": "听来你把那条赛道收归己有了。",
 "What can I say?": "我能说什么？",
 "You showed them, girl. Yer amazin'.": "你给他们看了，姑娘。你太厉害。",
 "I was the last woman standing. No one else left.":
    "我是最后站着的女人。再没别人了。",
 "Not to be unkind, but you don't sound like much of a racer.":
    "不是想刻薄，但你听着不太像个车手。",
 "Let's just say it wasn't my finest hour.": "就说那不是我最好的时刻吧。",
 "Ain't much to brag about then, I guess.": "那我想也没什么好吹的了。",
 "It was a mess.": "一团糟。",
 "Ya can't even tell me if you won? Sounds like a pretty lameass race to me.":
    "你连自己赢没赢都说不出来？在我看来这场比赛挺烂的。",
 "'Specially if you was in only one race.": "尤其在你就赛过一场的情况下。",
 "I mean you're standin' right here so clearly you didn't die.":
    "我是说你现在就站在这儿，所以显然你没死。",
 "And yer pretty damn nervy to waltz in here with your fancy racing stories and expect me to work for free.":
    "而且你带着你的花哨赛车故事大摇大摆进来，指望我免费干活，脸皮可真厚。",
 "You ask way too many questions.": "你问题太多了。",
 "They are if you expect me to fix yer van, lady.":
    "你要是指望我修你的车，那就关我的事，女士。",
 "My winnings are none of yer business.": "我的奖金不关你的事。",
 "If you can't even tell me what yer gonna win, I can't trust that you'll pay me.":
    "你连自己能赢什么都说不出，我就没法信你会付我钱。",
 "Well, if yer a vault hunter like you say, you might well be on the path to makin' a killin', am I right?":
    "这个，你要真像你说的那样是秘藏猎人，那你很可能正走在赚大钱的路上，对吧？",
 "Hell, you find a vault, you can buy vans by the fleet.":
    "天哪，你要是找到一座秘藏，你能按车队买面包车。",
 "Vault hunters that don't get dead, get rich.":
    "没死的秘藏猎人，都发财了。",
 "You find a vault, I'll be fixin' yer space yacht, not some crap ass van. [off Fiona's look] No offense.":
    "你要是找到一座秘藏，我给你修的就是太空游艇，不是什么烂面包车。[off Fiona's look] 无意冒犯。",
 "Just think about the money I could pay you if I found a vault.":
    "你就想想，我要是找到一座秘藏，能付你多少钱。",
 "You got some major cojones for a purdy lady.": "作为一个漂亮女士，你胆子可真大。",
 "You're damn right.": "你说得他妈对。",
 "Them's just more words.": "那不过是又一堆话。",
 "Hey, I'm working on it.": "嘿，我在想办法。",
 "So basically yer nuthin' but a double-talkin' windbag.":
    "所以基本上你就是个满嘴跑火车的吹牛大王。",
 "I'm not quite a vault hunter yet.": "我还不算是个秘藏猎人。",
 "Yer the one that was spoutin'  about how you was a vault hunter and such.":
    "是你在那儿大谈你是秘藏猎人什么的。",
 "That's none of your business.": "不关你的事。",
 "Suit yourself, but I'm startin' to think the only way you'll make a fortune is if bullshit turns to gold.":
    "随你。但我开始觉得你唯一发财的路子是等狗屁变成金子。",
 "Whether I strike it rich or not is *my* concern.": "我发不发财是*我*的事。",
 "If you ain't willin' to even talk about yer vault huntin' spoils, I ain't willin' to fix yer van.":
    "你要是连你猎秘藏的战利品都不肯谈，那我也不肯修你的车。",
 "The other problem with yer stated vocation is that most folks die on the job.":
    "你说的这职业还有个问题，就是大多数人都会在工作中送命。",
 "That doesn't bode well fer ya payin' me later.": "这对我以后收到你的钱可不是好兆头。",
 "The, ah, let's say \"survival rate\" for vault hunters ain't exactly high man, hah.":
    "那个，啊，我们就说秘藏猎人的“存活率”不怎么样，老兄，哈。",
 "Sounds purdy sweet to me. Maybe too sweet.": "听起来挺美。也许太美了。",
 "That's because it's the only one of its kind.": "因为它是独一无二的。",
 "Well, then, maybe you are actually on to sumthin'. But I ain't never heard of a vault like that.":
    "这个，那也许你真摸到了点什么。但我从没听过那样的秘藏。",
 "Special in that a giant monster doesn't come out and kill ya?":
    "特别在于不会钻出个巨型怪物把你杀掉？",
 "This vault is special.": "这座秘藏很特别。",
 "I like yer spirit, but I still think it's gonna be separated from yer body.":
    "我喜欢你的精神，但我还是觉得它会跟你的身体分开。",
 "You got nerve, I'll give ya that. It's just that vaults are littered with the corpses of spunky folk who thought they were smarter and braver than everbody else.":
    "你有胆，这点我承认。只是秘藏里到处都堆着那些自以为比别人更聪明、更勇敢的机灵鬼的尸体。",
 "Hey. I'": "嘿。我",
 "It usually does.": "通常都是。",
 "You're right. It could end badly.": "你说得对。可能会很糟。",
 "With that attitude, I'd say they're about zero. You got no business huntin' flies, let alone vaults.":
    "就这态度，我得说大概是零。你连打苍蝇的胆子都没有，更别说猎秘藏。",
 "I know the odds aren't great.": "我知道胜算不大。",
 "If yer too timid to talk about the grisly demise that most likely awaits ya, you ain't got no business huntin' vaults.":
    "你要是胆小到连大概率等着你的惨死都不敢谈，那就没资格猎秘藏。",
 "Look, I know the odds aren't great.": "听着，我知道胜算不大。",
 "Hey, cant'cha see we're talkin-": "嘿，你没看到我们在说话——",
 "{WorryB}Hey guys?": "{WorryB}嘿各位？",
 "About what a fine lookin' lady you are. Anyways, we was  just concludin' our business. So here's my final offer. I'll make all the repairs for free right now, and throw in some upgrades.":
    "在聊你是位多好看的女士。总之，我们刚在收尾了。所以我开最后价：我现在免费做全部修理，还附送几项升级。",
 "Y'all are gonna have the best lookin' van on Pandora. Catch-a-riiide!":
    "你们的车会是整个 潘多拉 最好看的。Catch-a-riiide！",
 "You can't go wrong.": "错不了。",
 "So what package y'all want? I'll throw in the Blaupunkt stereo for free.":
    "那你们要哪个套餐？我免费附送 Blaupunkt 音响。",
 "Than this baby will fly.": "那这宝贝就能飞了。",
 "We'll take option A.": "我们要 A 套餐。",
 "Time for me to get to work.": "我该开工了。",
 "I best get to work.": "我最好去干活了。",
 "It'll be like driving Fort Knox. Only a little faster.":
    "就像开着诺克斯堡上路。只是稍微快点。",
 "Extra shields sound good. We could use the protection.":
    "额外护盾听着不错。我们能多点保护。",
 "But I gotta get started.": "但我得开工了。",
 "Dang, girl! You got amazin' taste!": "该死，姑娘！你品味真惊人！",
 "We'll go with option C.": "我们要 C 套餐。",
 "She's an angel.": "她是个天使。",
 "Damn.": "该死。",
 "If I was you, I'd take it.": "我要是你，我就接受。",
 "So that's my last offer. Best I can do.": "那就是我最后的出价。我能做到最好的了。",
 "{WorryA}Man, I really wish I could help you out... {WorryB}But I can't be working for free.":
    "{WorryA}老兄，我真希望能帮你一把……{WorryB}但我不能白干活。",
 "I been called plenty 'a things, but a doll ain't one 'a them.":
    "我被叫过很多外号，但“宝贝”不在其中。",
 "You're a doll.": "你人真好。",
 "Thanks, Scooter!": "谢谢你，斯库特！",
 "Whoa, whoa, whoa. Let's not be hasty. Yer credit's good here. [glancing at Sasha] As a matter of fact, it's mighty fine.":
    "哇哇哇。别急。你的信用在我这儿没问题。[glancing at Sasha] 事实上，好得很。",
 "[re: Scooter] {SadB}He says he can't help us.": "[re: Scooter] {SadB}他说他帮不了我们。",
 "All you gotta do is ask.": "你只要开口就行。",
 "Yeah, well, maybe you should do the flirting once in awhile.":
    "是啊，也许你偶尔也该负责去调情。",
 "'Cause you do it so well.": "因为你干得那么好。",
 "I'm kinda used to it by now.": "我现在算是习惯了。",
 "Thanks, Sash. Much appreciated.": "谢了，Sash。非常感激。",
 "[sly grin]: I'm the closer. Deal with it.": "[sly grin]： 我是负责收尾的。忍着吧。",
 "You should've let me finish.": "你该让我把话说完。",
 "A few more minutes, I woulda had him.": "再几分钟，我就把他拿下了。",
 "Really? We don't have all the time in the world.":
    "真的？我们可没有无限的时间。",
 "{SternA}You didn't have to do that. {NeutralA}I had it under control.":
    "{SternA}你不用那么做的。{NeutralA}我搞得定。",
 "I'm not so sure about that.": "我不太确定。",
 "I can't believe you thought I might be into him.": "我不敢相信你居然以为我可能对他有意思。",
 "Seriously? It's an act.": "认真的？那是演的。",
 "Please tell me you don't actually like this guy.": "求你别告诉我你真的喜欢这家伙。",
 "You can be very convincing when you want to be.": "你想的话可以非常有说服力。",
 "{SternB}Y'know what? {SadA}Never mind. He's coming back.":
    "{SternB}你知道吗？{SadA}算了。他回来了。",
 "{InquireA}Maybe we should switch places for awhile.":
    "{InquireA}也许我们该换换位置一阵子。",
 "{AngryA}I'm getting a little tired of being{SternA}[ sigh] the {SmugA}flirty one {AngryA}all the time.":
    "{AngryA}我有点厌倦了总是{SternA}[ sigh] 当那个{SmugA}负责调情的{AngryA}。",
 "{ShockA}Oh we're blown.": "{ShockA}哦，我们暴露了。",
 "{FearB}Oh, no-": "{FearB}哦，不——",
 "Looks like trouble. Better clamp it down.": "看着像麻烦。最好压低声音。",
 "Follow me. I'll show you where the magic happens. And I'l show you mah garage too. Hehe.":
    "跟我来。我带你们看看魔法在哪儿发生。也带你们看看我的车库。嘿嘿。",
 "I ain't seen nuthin' and nobody! Now unhand me friendo!": "我什么都没看见，谁也没看见！现在把我放开，哥们！",
 "*grunts*": "*咕哝*",
 "Maybe this'll jog your memory, friend.": "也许这能帮你想想，朋友。",
 "{SternA}...Yeah that'll teach 'em... {WorryB}Hope you ladies weren't too scared.":
    "{SternA}……对，这下能给他们点教训了……{WorryB}希望你们两位女士没被吓着。",
 "{AngryA}Most.": "{AngryA}大部分。",
 "{NormalA}If we find out you're lying, the consequences will be most unpleasant.":
    "{NormalA}要是我们发现你撒谎，后果会非常不愉快。",
 "*Grunting*": "*咕哝*",
 "Just some two-bit thugs tryin' to shake me down. No biggie.":
    "就是几个三流混混想勒索我。没什么大不了。",
 "{SternA}Who were those guys?": "{SternA}那些家伙是谁？",
 "Ya  gotta stand up to 'em is all. Teach'em a lesson in pain.":
    "你就得跟他们硬碰硬。给他们上一堂痛苦的课。",
 "They looked pretty dangerous to me.": "在我看来他们挺危险的。",
 "Why did you protect us?": "你为什么要保护我们？",
 "This here's mah garage. Ain't no miscreants gonna come in and harangue mah lovely guests. Hell, no!":
    "这儿是我的车库。没有什么混账能进来辱骂我可爱的客人。绝不！",
 "But they could've killed you.": "但他们本来可能杀了你。",
 "If a man ain't prepared to defend his turf, he ain't no kinda man. [to himself] Wow, Scooter, that beautiful.":
    "一个男人要是不准备守住自己的地盘，就不算个男人。[to himself] 哇，斯库特，这话真美。",
 "Thank you, Scooter.": "谢谢你，斯库特。",
 "I was jus' doin' what's right.": "我只是做了对的事。",
 "But you didn't have to.": "但你本不必这么做。",
 "Ain't no way I was gonna let those miscreants get their hands on you.":
    "我绝不可能让那些混账碰到你们。",
 "We're really grateful.": "我们真的非常感激。",
 "Never you mind. [smiling at Sasha] It's all in a day's work. I ain't no hero.":
    "别在意。[smiling at Sasha] 都是份内的事。我不是什么英雄。",
 "No reason to be scared. They're gone now.": "没什么好怕的。他们现在走了。",
 "I had them runnin' like scalded apes in a hailstorm!": "我让他们跑得像冰雹里被烫到的猿猴！",
 "I gave'em the Scooter special.": "我给他们上了“斯库特 特餐”。",
 "If you don't mind, we have some business to discuss.": "你不介意的话，我们有些事要谈。",
 "I hear ya. Just holler if you need me.": "我懂。需要我就喊一声。",
 "{WorryA}I say we hit the safehouse. {SternA}If Felix hasn't already been there first, it'll have {SternB}everything we need... {SadA}Money, gear, new IDs...":
    "{WorryA}我说我们就去安全屋。{SternA}要是 菲利克斯 没先去那儿，那里面会有{SternB}我们需要的一切……{SadA}钱、装备、新证件……",
 "{FearA}It's too risky. {SternA}I think we should stay put.":
    "{FearA}太冒险了。{SternA}我觉得我们该待着不动。",
 "{SadA}Well you can do whatever you want. {SternA}I'm going.":
    "{SadA}那你想怎么做都行。{SternA}我要去。",
 "Our wanted posters are everywhere. August is after us-":
    "我们的通缉海报到处都是。August 在追我们——",
 "That's exactly why we need it.": "正因如此我们才需要那些东西。",
 "I can't let you go alone.": "我不能让你一个人去。",
 "{FearA}Okay, but {SternA}let's be fast.": "{FearA}好，但{SternA}我们动作要快。",
 "I'm glad you see it my way.": "很高兴你能听我的。",
 "It's more that I don't want you to get killed. Our wanted posters are everywhere. August is after us.":
    "更该说是不想让你被杀。我们的通缉海报到处都是。August 在追我们。",
 "{SternA}I'm not a little girl anymore - {SmugA}I can handle myself.":
    "{SternA}我不再是小女孩了——{SmugA}我能照顾好自己。",
 "I know. But we're a team.": "我知道。但我们是一队。",
 "We can't be 100% it's still there.": "我们不能百分百确定东西还在那儿。",
 "That's a risk I'm willing to take.": "那是我愿意冒的风险。",
 "{SternA}Then I'm going with you.": "{SternA}那我就跟你一起去。",
 "I know you may not understand, but It's just something I have to do.":
    "我知道你也许不理解，但这是我必须做的事。",
 "If there's even a chance it's there,  we should go.":
    "只要有一丝可能东西还在，我们就该去。",
 "We need it.": "我们需要它。",
 "We need to go to Felix's safehouse. I want answers.":
    "我们得去 菲利克斯 的安全屋。我要答案。",
 "I need to see his place for myself. I'm going.": "我要亲眼看看他的地方。我要去。",
 "Felix is gone, Sasha. You have to accept it.": "菲利克斯 不在了，萨莎。你得接受。",
 "It's too dangerous. Our wanted posters are everywhere. August is after us.":
    "太危险了。我们的通缉海报到处都是。August 在追我们。",
 "It's just something I have to do.": "这是我必须做的事。",
 "Then I'm going with you.": "那我就跟你一起去。",
 "If there's even a chance we could find out what he was thinking, it's worth it.":
    "只要有一丝可能弄清他在想什么，就值得。",
 "I have to know.": "我必须知道。",
 "We'll cut across the docks to get to Felix's. But we have to stay alert. August will have every goon on the lookout.":
    "我们穿过码头去 菲利克斯 那儿。但我们得保持警惕。August 会让所有打手都盯着。",
 "Y'all be careful now. Come' back in one piece.": "你们小心点。完整地回来。",
 "{HappyB}We barely made it. [beat] {SchemeB}Not like I care or anything, but {SmugA}you think the guys are okay?":
    "{HappyB}我们勉强撑过来了。[beat] {SchemeB}倒不是我在乎什么的，但{SmugA}你觉得那两位没事吧？",
 "{SchemeA}I'm sure they'll figure something out.": "{SchemeA}我确定他们会想办法的。",
 "{SmugA}But {WorryA}the Badlands are practically a graveyard.":
    "{SmugA}但{WorryA}恶地基本上就是片坟场。",
 "They'll be fine.": "他们会没事的。",
 "They have a chance.": "他们有机会。",
 "They won't last the night.": "他们撑不过今晚。",
 "{HappyA}They'll be all right.": "{HappyA}他们会没事的。",
 "{SmugA}In the heat? With the Skags? {SmugB}I'm not so sure.":
    "{SmugA}在那种高温下？还有异犬？{SmugB}我不太确定。",
 "{FearA}They probably {SchemeB}called for help and had someone pick them up.":
    "{FearA}他们大概{SchemeB}叫了救援，有人接走他们了。",
 "{SmugA}Yeah, probably.": "{SmugA}是啊，大概吧。",
 "{SchemeB}If they're smart they have a chance.": "{SchemeB}他们要是有脑子就有机会。",
 "{SmugA}I'm not convinced two {AngryA}Hyperion desk jockeys {SchemeB}know the first thing about survival in the Badlands.":
    "{SmugA}我不信两个{AngryA}亥博龙坐办公室的{SchemeB}懂什么恶地生存。",
 "{DoubtfulA}All they have to do is find a shelter and build a fire.":
    "{DoubtfulA}他们只要找个掩体、生个火就行。",
 "{SadA}They're dead.": "{SadA}他们死了。",
 "{SadA}I hate to say it, but {SternA}they're not gonna last the night.":
    "{SadA}我不想这么说，但{SternA}他们撑不过今晚。",
 "{WorryA}Yeah... that's what I {SadA}kinda thought.": "{WorryA}是啊……我也{SadA}大概这么想。",
 "{SternA}Between the exposure, the Skags, and the psychos, {InquireB}I'd say they're screwed.":
    "{SternA}暴晒、异犬、还有疯子加起来，{InquireB}我得说他们完了。",
 "[conflicted] {WorryB}They knew what they signed up for...":
    "[conflicted] {WorryB}他们知道自己在签什么……",
 "The only way we can is to get the van fixed, but I don't think we'd make it back to them in time.":
    "我们唯一的办法就是把车修好，但我觉得我们赶不回去救他们。",
 "{WorryA}That bad, huh? {SadA}That's what I thought. {WorryB}They don't stand a chance out there.":
    "{WorryA}那么糟，哈？{SadA}我就知道。{WorryB}他们在外面一点机会都没有。",
 "{SternA}With the caravan like this, {SadA}we couldn't help them if we wanted to.":
    "{SternA}车这样，{SadA}我们就算想帮也帮不了。",
 "{WorryA}I hope he'll fix it. {SadA}We're not exactly rolling in cash right now.":
    "{WorryA}我希望他能修好。{SadA}我们现在可不算钱多得能打滚。",
 "{DoubtfulA}We'll figure it out, {HappyA}don't worry.": "{DoubtfulA}我们会想办法的，{HappyA}别担心。",
 "{SadB}Wouldn't have{SmugB} it any other way.": "{SadB}换别的方式{SmugB}我还不要呢。",
 "[Hit in stomach] {AngryA}...sumbitch...": "[Hit in stomach] {AngryA}……狗娘养的……",
 "{NormalA}You're sure you haven't seen them?": "{NormalA}你确定没见过他们？",
 "I wouldn't mind 'a piece 'a that. And yer racing money too!":
    "我倒也不介意分一份。还有你的赛车奖金！",
 "Racers sure do get rich quick.": "车手确实发财快。",
 "Springs should be here any minute. I wonder what's holdin' her up.":
    "Springs 随时会到。不知道什么事把她绊住了。",
 "If you don't got it, I ain't sayin' we can't figure sumthin' out. But it's not mah normal way 'a operatin'.":
    "你要是没钱，我也不是说不能想办法。但那不是我平时的做法。",
 "A damn fine choice if I say so mahself.": "恕我自夸，这选择真不错。",
 "We want option B.": "我们要 B 套餐。",
 "She's gonna be a real beaut.": "她会变得非常漂亮。",
 "Now these here fixes are gonna take some time. I was just wonderin' if you ladies had any place to lay low while I work mah miracles.":
    "这些修理要花点时间。我刚想问你们两位女士，在我施展奇迹的时候有没有地方躲一躲。",
 "{SternA}Fine. Then we go together.": "{SternA}行。那就一起去。",
 "I just don't want you getting hurt.": "我只是不想你受伤。",
 "The place might be empty.": "那地方可能是空的。",
 "{SadA}I know it's dangerous, {SternA}but getting that stash is our best {WorryA}shot at survival.":
    "{SadA}我知道这很危险，{SternA}但拿到那批东西是我们{WorryA}活下去最好的机会。",
 "We should go to the safehouse to get our stash: money, IDs, gear. It's our only way out. Now that Felix is gone, it's the perfect time.":
    "我们该去安全屋拿我们的存货：钱、证件、装备。那是我们唯一的出路。既然 菲利克斯 不在了，现在正是时候。",
 "Then we go together.": "那就一起去。",
 "It might not be there.": "东西可能不在了。",
 "Fix the van, or else..": "把车修好，不然……",
 "Please help us.": "求你帮帮我们。",
 "I've got a big score lined up.": "我有一大笔进账在等着。",
 "Look man, it doesn't matter what the race is called, it only matters that I drive fast.  And I always drive fast.":
    "听着老兄，比赛叫什么名字不重要，重要的是我开得快。而我永远开得快。",
})

# —— Scooter 的“连锁店老板 / 实习生”版对白（带标签）——
T.update({
 "[Re: his clipboard] {HappyA}Sorry if I seem a little{WorryA} distracted - Hopefully{HappyA} handing the place over to the new proprieter today and I gotta get all these numbers {WorryB}and stuff in order and, {WorryC}uh, it's a lot.":
    "[Re: his clipboard] {HappyA}抱歉我看起来有点{WorryA}分心——希望今天能把这地方交给新老板，我得把这些数字{WorryB}之类的东西都理清楚，而且，{WorryC}呃，太多了。",
 "[Mumbling to self] {InquireA}Alright, carry the three... {SternA}divide by 12... {AngryA}What the hell man I gotta cut down my {WorryB}wrench budget...":
    "[Mumbling to self] {InquireA}好，进三……{SternA}除以十二……{AngryA}搞什么鬼老兄，我得削减我的{WorryB}扳手预算了……",
 "[Thinks to himself] {WorryB}Hope none of that was {WorryA}too much information.":
    "[Thinks to himself] {WorryB}希望那些不算{WorryA}说得太多。",
 "{WorryC}I don't know {InquireA}if you know this, {HappyA}but the transition from \"small business owner\" to \"franchise owner\" is surprisingly difficult.":
    "{WorryC}我不知道{InquireA}你知不知道，{HappyA}但从“小业主”到“加盟店老板”的转变出人意料地难。",
 "Anyway, what you need man?": "总之，你需要什么，老兄？",
 "{HappyA}Aw thanks man that means a lot. {SmugA}Business has been a little slow so far - {WorryB}y'know being in a hidden cave town and everything - {SmugA}but it'll pick up, haha.":
    "{HappyA}哦谢谢老兄，这话很重要。{SmugA}生意目前有点清淡——{WorryB}你知道，毕竟是在个隐蔽的洞穴镇里——{SmugA}但会好起来的，哈哈。",
 "[Quiet dread] ...{WorryA}Hope it picks up.": "[Quiet dread] ……{WorryA}希望会好起来。",
 "{SmugA}Yeah man. I got too many locations now - {WorryA}I can't work all of 'em.":
    "{SmugA}是啊老兄。我现在店面太多了——{WorryA}我做不过来。",
 "{WorryA}Eeeyep yep yep. {HappyA}Hopin' to hand this ol' girl off to Janey Springs? You know her? {SlyA}She used to fix buggies and crap on the moon so I figure it'll be like ridin' a bike for her. {WorryA}Figuratively speaking. {WorryB}I don't really do bikes, {SmugA}haaha.":
    "{WorryA}是——是是是。{HappyA}希望把这老姑娘交给 Janey Springs？你认识她吗？{SlyA}她以前在月球上修越野车什么的，所以我想对她来说就跟骑自行车一样简单。{WorryA}比喻意义上。{WorryB}我其实不骑自行车，{SmugA}哈哈。",
 "{HappyA}As much as I'd love to be one of them {SlyA}mind readers, I can't {WorryB}actually tell what you're thinking so, uh, how about we do it the o{SmugA}ld fashioned way and use our mouths? [Trails off with awkward laugh] {HappyA}Haha.":
    "{HappyA}虽然我很想当那种{SlyA}读心的人，但我{WorryB}真看不出你在想什么，所以，呃，不如我们用{SlyA}老办法——用嘴说话？[Trails off with awkward laugh] {HappyA}哈哈。",
 "{WorryB}Can you fix it?": "{WorryB}你能修吗？",
 "{HappyA}Hey man that's what the sign says I do, {SmugA}doesn't it?":
    "{HappyA}嘿老兄，招牌上写的就是我干这个，{SmugA}对吧？",
 "{SternA}No seriously does it {WorryB}I can't remember what I put on that new billboard.":
    "{SternA}不，说真的，是吗，{WorryB}我记不得我在新广告牌上写了什么。",
 "{HappyA}Point is I can fix her up for ya, {SmugA}hah.":
    "{HappyA}重点是我能把她给你修好，{SmugA}哈。",
 "{ShockA}Aw crap man that girl is not looking too good. {WorryB}Least I'm assuming it wasn't designed with that whole, uh, \"hole\" thing in the side.":
    "{ShockA}哦操，老兄，那姑娘看着不太妙。{WorryB}至少我猜它设计的时候没有那个，呃，侧面的“洞”。",
 "Like I said, I still got some time before the":
    "就像我说的，我还有时间，在……之前",
 "{HappyA}I still got a few minutes before Springs shows up - my manager-to-be that is - {SlyA}so I figure we can at least take a look.":
    "{HappyA}在 Springs 出现之前我还有几分钟——就是我未来的经理——{SlyA}所以我想我们至少可以先看看。",
 "{HappyA}She should be along in a few minutes but I figure we at least got time to take a look.":
    "{HappyA}她应该几分钟后就到，但我想我们至少有时间先看看。",
 "{SlyA}I can never resist peekin' under a {SmugA}hood, haaa.":
    "{SlyA}我从来抗拒不了掀开{SmugA}引擎盖偷看，哈哈哈。",
 "{InquireA}Hey man do I know you? Maybe from {WorryA}Sanctuary or something?":
    "{InquireA}嘿老兄，我认识你吗？也许在{WorryA}避风港什么的？",
 "{InquireA}I'm just getting a feeling that I've seen your face before - {SternA}Some kind'a {WorryA}deja vu or something.":
    "{InquireA}我就是有种感觉，以前见过你那张脸——{SternA}某种{WorryA}既视感什么的。",
 "{HappyA}Help me out, {ShockA}man.": "{HappyA}帮我想想，{ShockA}老兄。",
 "{ShockA}Aw, wait wait wait wait. {HappyA}I got it.":
    "{ShockA}哦，等等等等。{HappyA}我想到了。",
 "{WorryA}Nope. It's gone.": "{WorryA}不。又忘了。",
 "That's, uh. That's the plan.": "那个，呃。那就是计划。",
 "[Boasting] {SmugB}{Body-A}I'm a wanted woman. {SmugC}{Body-X}Maybe you've seen my poster?":
    "[Boasting] {SmugB}{Body-A}我是个被通缉的女人。{SmugC}{Body-X}也许你见过我的海报？",
 "{HappyA}Badass man, badass. So long {SmugA}as, you know, {WorryA}don't end up dead {HappyA}right?":
    "{HappyA}狠，老兄，狠。只要你，你知道，{WorryA}最后别死掉，{HappyA}对吧？",
 "[Proudly] Yup.": "[Proudly] 对。",
 "Aw crap man yeah that's it! That's a good poster! I was just over at the poster wall getting photos for my family album and saw one of yours. \"Dead or Alive,\" right?":
    "哦操，老兄，对就是它！那张海报不错！我刚在通缉墙那边给我家相册拍照，看到你那张了。“死活不论”，对吧？",
 "{ShockA}Badass.": "{ShockA}狠。",
 "{HappyB}Uh, yeah. Great. Lemme know. {SchemeB}I'll sign one or {AngryA}something.":
    "{HappyB}呃，是啊。挺好。跟我说一声。{SchemeB}我给你签一张还是{AngryA}怎么着。",
 "{ShockA}Aw crap that's {HappyA}awesome man! I get repair jobs from 'Nova for weeks after one of his big race death things - {SmugA}I'll have to keep an eye out for car parts with your blood on 'em!":
    "{ShockA}哦操，{HappyA}太棒了老兄！每次 Bossanova 办那种死亡大赛之后，我能接到好几周的修车活儿——{SmugA}我得留意带着你血的汽车零件！",
 "{SchemeD}Winner.": "{SchemeD}赢家。",
 "{HappyA}Aw cool man, that's cool. {SmugA}Congrats on not-dyin' so far. {WorryA}That's a good first step.":
    "{HappyA}哦酷，老兄，酷。{SmugA}恭喜你到目前为止还没死。{WorryA}这是很好的第一步。",
 "{HappyA}I've helped out loads'a Vault Hunters before - {WorryA}Feel like I should get one of those little punch cards, {HappyA}haaha.":
    "{HappyA}我以前帮过好多秘藏猎人——{WorryA}感觉我该弄张那种小打卡券，{HappyA}哈哈。",
 "{InquireA}I'm a Vault Hunter.": "{InquireA}我是秘藏猎人。",
 "{ShockA}You're all {SlyA}mysterious and crap, huh man? That's cool, that's cool. {HappyA}I'll just let the old imagination fill in the blanks for me. {WorryC}Or the gas fumes, {HappyA}haaa. {WorryA}Seriously I've probably damaged my brain.":
    "{ShockA}你一副{SlyA}神秘兮兮的样子，哈老兄？酷，酷。{HappyA}那就让我的老想象力替我补空白吧。{WorryC}或者让汽油味来补，{HappyA}哈哈。{WorryA}说真的我脑子大概已经坏了。",
 "{HappyA}Well man, I don't have to tell you how much I enjoy a good chat but we should {SlyA}probably be gettin' down to business, amirite?":
    "{HappyA}这个老兄，我多喜欢好好聊天不用我说，但我们{SlyA}大概该谈正事了，对吧？",
 "{ShockA}That thing's beat up to hell and back, man. {HappyA}I can fix it, but it's probably gonna run you {InquireA}about {NeutralA}twenty-five hundred cold ones.":
    "{ShockA}那玩意儿被打得遍体鳞伤，老兄。{HappyA}我能修，但大概要花你{InquireA}大约{NeutralA}两千五冷钞。",
 "{WorryB}We're talkin' a lot parts, lotta labor... And that's just to get her runnin' again.":
    "{WorryB}我们说的是大量零件、大量工时……而这还只是让她重新能跑。",
 "[Uncomfortable] {WorryA}And, man, that's bein' pretty generous.":
    "[Uncomfortable] {WorryA}而且，老兄，这已经算挺大方了。",
 "{WorryB}Aw crap man, really? How \"little\" is it {WorryA}out of there? {SmugA}I mean I could maybe wiggle a bit for ya...":
    "{WorryB}哦操，老兄，真的？比那“少”多少？{WorryA}我是说我也许能给你松动一点……",
 "{FearA}Twenty-five {ShockA}hundred? That's a little {DoubtfulA}out of my price range.":
    "{FearA}两千{ShockA}五？那有点{DoubtfulA}超出我的价格范围了。",
 "{WorryB}Ah man I hate to be the bad guy... {WorryA}Just if I do it for any less than that I'll be payin' for it myself, {WorryC}nawmean? Getting parts down here{WorryB} in this damn cave don't come cheap.":
    "{WorryB}啊老兄，我不想当坏人……{WorryA}只是我要少收一分，就得我自己贴，{WorryC}懂我意思吗？在这该死的洞穴里{WorryB}弄零件可不便宜。",
 "Sorry, it's just way too much.": "抱歉，实在是太多了。",
 "{FearA}A few... {HappyC}thousand?": "{FearA}几……{HappyC}千？",
 "{AngryA}But maybe {WorryA}I could work something out...":
    "{AngryA}但也许{WorryA}我能想出个办法……",
 "{HappyC}Please? {DoubtfulA}I swear I'm good for it.":
    "{HappyC}求你？{DoubtfulA}我发誓我付得起。",
 "{WorryB}I dunno man, that kinda thing makes me a little uncomfortable.":
    "{WorryB}我不知道老兄，那种事让我有点不自在。",
 "{SternA}I mean I {WorryB}trust you and all, but I kinda need the cash to get the{WorryC} job goin' y'know man?":
    "{SternA}我是说{WorryB}我信你什么的，但我需要现金才能{WorryC}开工，你懂吗老兄？",
 "{NeutralA}You only have to walk out to a \"hiding spot\" in the \"desert\" to get your \"payment\" {InquireA}three times before you start reassessing your life choices.":
    "{NeutralA}你只要走到“沙漠”里一个“藏钱点”去拿你的“报酬”{InquireA}三次，就会开始重新审视自己的人生选择了。",
 "{WorryB}Man you seem real nice and all,{WorryB} but I've had bad things happen when I did that before.":
    "{WorryB}老兄你看着人很好什么的，{WorryB}但我以前那么干的时候出过坏事。",
 "[Wince] {WorryB}Sorry.": "[Wince] {WorryB}抱歉。",
 "{WorryB}I mean, I really wanna figure something out, {NeutralA}but you gotta {WorryA}work with me here man.":
    "{WorryB}我是说，我真的很想找出办法，{NeutralA}但你也得{WorryA}配合我一下，老兄。",
 "{WorryA}Help me to help you man, haa.": "{WorryA}帮我，我才能帮你，老兄，哈。",
 "{WorryB}Okay. Okay okay okay. {NeutralA}What can we work with here?":
    "{WorryB}好。好好好。{NeutralA}我们这儿能拿什么来周转？",
 "{WorryA}Course, heh, I think they think {SmugA}\"bartering\" means \"drinking and scratchin' their {HappyA}nethers on the porch,\" haaa. {WorryA}I'm just kiddin', just kiddin'.":
    "{WorryA}当然，嘿，我想他们以为{SmugA}“以物易物”是指“在门廊上喝酒挠{HappyA}裆”，哈哈。{WorryA}我开玩笑的，开玩笑的。",
 "{WorryB}Maybe... {WorryA}Somethin' to trade?": "{WorryB}也许……{WorryA}有什么可以交换的？",
 "{HappyA}But they're moron scumbags. For serious.":
    "{HappyA}但他们是一帮白痴渣滓。说真的。",
 "{InquireA}I ain't too proud to barter, man. {WorryA}My grandpappy and his grandpappy been barterin' {ShockA}for years.":
    "{InquireA}我可不至于骄傲到不肯以物易物，老兄。{WorryA}我爷爷和他爷爷都易了好多年{ShockA}了。",
 "[Scoff] Or else what, man? You gonna threaten me here in my own place of business? I'm more than just a pretty face y'know. If you try and step to me I will bite back man, swear to god.":
    "[Scoff] 不然怎样，老兄？你要在我自己的店里威胁我？你知道我不只是张好看的脸。你要是敢冲我来，我会咬回去的，我向上帝发誓。",
 "I'm more than just a pretty face y'know. If you try and step to me I will bite back man, swear to god.":
    "你知道我不只是张好看的脸。你要是敢冲我来，我会咬回去的，老兄，我向上帝发誓。",
 "Fix the van. Or else.": "把车修好。不然。",
 "I'm a businessman and this is a business, man!":
    "我是生意人，这是一门生意，老兄！",
 "[Conflicted] Maaaaan you are tuggin' at my heartstrings like crazy but I just can't do it.":
    "[Conflicted] 老——兄，你这样死命拽我的心弦，但我真做不了。",
 "Please Scooter. I'm begging you. We need your help.":
    "求你 斯库特。我求你了。我们需要你帮忙。",
 "Alright. You wanna know a secret? Because here comes a tasty one.":
    "好。你想知道一个秘密吗？因为要来一个带劲的。",
 "Yeah. I've got a lead on a big score. You help me out... I can cut you in on it.":
    "是啊。我有一笔大买卖的线索。你帮我一把……我可以算你一份。",
 "{SternA}Stay here. {SchemeB}I'll do the talking.":
    "{SternA}待在这儿。{SchemeB}我来说话。",
 "Oof. Sorry. I saw red there for a minute. What were we talkin' about?":
    "呃。抱歉。我刚刚有点上火。我们说哪儿了？",
 "Hey man I do hear crime is fairly lucrative.":
    "嘿老兄，我听说犯罪确实挺赚钱。",
 "Aw yeah? I *have* heard that the life of crime can be fairly lucrative... What you got cookin'?":
    "哦是吗？我*确实*听过犯罪生涯可以挺赚钱……你在搞什么名堂？",
 "I mean, just cuz I spend seemingly most of my gosh-dang life inside one of these garages doesn't mean I'm not interested in exciting true-crime hijinks and crap.":
    "我是说，虽然我这一辈子好像大部分都泡在车库里，但不代表我对刺激的真实犯罪勾当什么的没兴趣。",
 "Like, uh, robberies? Or murderings? Kidnappings? Breakin'-an'-enterings? Forgeries?":
    "比如，呃，抢劫？还是杀人？绑架？入室盗窃？伪造？",
 "Hey. All you need to know is that I'm the best there is at what I do.":
    "嘿。你只要知道，我干这行是最棒的。",
 "Wow. Y'know man there might be some folks that view that as over-confident, but I just find it dang impressive.":
    "哇。你知道老兄，也许有人会觉得那是过度自信，但我只觉得特别让人佩服。",
 "And what I do is make money.": "我干的就是赚钱。",
 "How this job will be no problem.": "这活儿不会有问题。",
 "I dunno man. Some babies hold onto things real tight. Especially candy. Sticky fingers, y'know? Sorry. I got off topic. What were we talking about?":
    "我不知道老兄。有些婴儿抓东西抓得特别紧。尤其是糖。黏手，你知道吗？抱歉。我跑题了。我们说什么来着？",
 "Right. Right. I mean... You sound pretty damn confident. What could go wrong, right?":
    "对。对。我是说……你听着特别自信。能出什么岔子，对吧？",
 "Please - This will be a cinch. Like taking candy from a baby.":
    "拜托——这易如反掌。就跟从婴儿手里抢糖一样。",
 "[Considering] ...I do have a lot of loved ones...":
    "[Considering] ……我确实有很多爱的人……",
 "You must be the real deal, huh man? Dangerous classified jobs and all...":
    "你肯定是真的行家，哈老兄？危险的机密任务之类的……",
 "If I told you... it could put you and your loved ones in danger.":
    "我要是告诉你了……可能会让你和你爱的人陷入危险。",
 "I don't know Scooter. It's pretty dangerous. Classified even.":
    "我不知道 斯库特。这挺危险的。甚至是机密的。",
 "Makes sense to me, man. I hear those cups and whatnot rake in the dough.":
    "我懂，老兄。我听说那些奖杯什么的很能捞钱。",
 "You promising me a slice of that money pie?": "你是承诺分我一块那张钱饼？",
 "Love all them races.": "我爱所有那些比赛。",
 "Lemme tell you when I was a kid all I wanted to be was a racer.":
    "我跟你说，我小时候唯一想当的就是车手。",
 "Still all I wanna be. All I'm missing is the reflexes, the bowel control, the short term memory, the reflexes...":
    "现在还是我唯一想当的。我缺的只是反应能力、肠道控制力、短期记忆、反应能力……",
 "Aw yeah? That's great! Which one?": "哦是吗？太好了！哪一场？",
 "Yeah, well when you've got a need for speed like I do...":
    "是啊，当你像我一样渴望速度的时候……",
 "Can't wait to see you in that one!": "我迫不及待想看你跑那场！",
 "Aw crap man that's one of the best there is! All those underground tunnels and what not? Awesome.":
    "哦操老兄，那是最好的比赛之一！那些地下隧道什么的？太棒了。",
 "Except a brand new race track.": "除了是条全新赛道。",
 "Huh. Well I'll have to keep an eye out for that one when it happens.":
    "嗯。那它办的时候我得留意。",
 "\"Old Haven 500?\" Haaaa. Good comedy joke man - There hasn't be anything in Old Haven for liiike ten years.":
    "“老避风港 500？”哈哈。老兄这笑话真好——老避风港都大概十年没什么东西了。",
 "Naw that makes sense to me man. If you're as much of a racer as you say you've probably seen a lot. It's like me with all the women that come through here, haaaa. Naw I'm just kidding.":
    "不，这对我来说说得通，老兄。你要是像你说的那么爱赛车，肯定见过很多。就像我见过所有经过这儿的女人一样，哈哈。不，我开玩笑的。",
 "[Afterthought] I'm real alone.": "[Afterthought] 我真的很孤独。",
 "You know how it is. With so many races they all start to blur together.":
    "你知道的。比赛太多，全都开始混在一起了。",
 "Naw I mean... Not answering a question's a way to do it too. I can just keep talking. Filllllll the silence, man. Ha. Just, y'know, good times with social interactions.":
    "不，我是说……不回答问题也是一种办法。我可以一直说。填——满沉默，老兄。哈。就是，你知道，社交互动的好时光。",
 "Ain't no shame in that, man. That still makes you a racer to me! How'd it go?":
    "这没什么可耻的，老兄。对我来说你还是个车手！结果怎么样？",
 "Alright if you want to know the truth I've only ever been in the one race.":
    "好，你要是想知道实话，我只赛过一场。",
 "You do good? Top 3 at least?": "你跑得好吗？至少前三？",
 "So, A+ for that right there, haa.": "所以，就冲这个给你打个 A+，哈。",
 "Well I hope you have lots more great racers in your career then, man. Awesome.":
    "那希望你的职业生涯里还有更多精彩的比赛，老兄。太棒了。",
 "Thank you, thank you.": "谢谢，谢谢。",
 "Well that's god-dang awesome then! Congratulations, congratulations.":
    "那可真他妈的棒！恭喜，恭喜。",
 "Badass man. Badass.": "狠，老兄。狠。",
 "Left, right, and center.": "左中右到处都是。",
 "Aww man it was one of them races huh? Crashes everywhere?":
    "哎呀老兄，那是那种比赛哈？到处都是撞车？",
 "Then that's badass man!": "那真是狠，老兄！",
 "It's my face.": "是我的脸。",
 "Yeah?? That sounds badass man! 'Specially since you've clearly got your face where it started! Unless you stole someone else's face!":
    "是吗？？听着挺狠啊老兄！尤其你那张脸显然还在原位！除非你偷了别人的脸！",
 "It was a MASSACRE. Giant skags! Explosions! Gunfire everywhere! Lil' psychos trying to tear my face off!":
    "那是一*场*屠*杀*。巨型异犬！爆炸！到处都是枪声！小疯子想把我脸撕下来！",
 "Hey. The winnings are just part of it.": "嘿。奖金只是其中一部分。",
 "You've heard about the endorsement deals us racers get, right?":
    "你听说过我们车手拿的代言合同吧？",
 "No way man. You're of them endorsed racers? Commercials and everything?":
    "不可能吧老兄。你就是那种拿代言的车手？还拍广告什么的？",
 "Yeah. Just haven't filmed 'em yet.": "是啊。只是还没拍。",
 "I mean that makes sense - You Vault Hunters are always chasing after, y'know, Vaults. Hah.":
    "我是说那说得通——你们秘藏猎人总是在追，你知道，秘藏。哈。",
 "You really think you got what it takes?": "你真觉得你有那本事？",
 "Course I seen a lot of Vault Hunters just end up dead, man and some of them were way scarier than you. No offense.":
    "当然我见过很多秘藏猎人最后就死了，老兄，其中一些比你可怕多了。无意冒犯。",
 "If you're looking to pay me later for fixin' your van well I'd like to know that you're coming back. Alive. With Vault money.":
    "你要是打算以后付我修车钱，那我希望知道你还会回来。活着。带着秘藏的钱。",
 "It ain't just gonna be another Vault with a giant monster in it?":
    "该不会又是那种里面有巨型怪物的秘藏吧？",
 "This Vault's special. And I've already got the lead on it.":
    "这座秘藏很特别。而且我已经有线索了。",
 "[I hope not] No.": "[I hope not] 不是。",
 "Huh. Well if that's true man then you're on the road to the best Vault of all, haaa.":
    "嗯。那要是真的，老兄，你就在通往最好的秘藏的路上，哈哈。",
 "It's dang inspiring, to say the least...": "起码说，这可真鼓舞人……",
 "You are confident as hell, huh man? It's dang inspiring, to say the least...":
    "你自信得要命，哈老兄？起码说，这可真鼓舞人……",
 "I've got this one in the bag.": "这一票我稳了。",
 "Maybe you do know what you're doin'.": "也许你确实知道自己在干什么。",
 "If you actually manage to survive gettin' to the Vault, gettin' IN the Vault, and then gettin' OUT of the Vault... You'd be one rich sumbitch.":
    "你要是真能活到秘藏、进去、再出来……你就是个有钱的狗东西了。",
 "Hey, I wouldn't do it if there weren't the promise of the big score.":
    "嘿，要不是有大买卖的指望，我也不干。",
 "That's a good point, man. That's a good point...":
    "说得好，老兄。说得好……",
 "Could buy yourself a whole mess of tiny hats.": "你可以给自己买一大堆小帽子。",
 "It's cool if you're not really \"Vault Hunting\" material. No shame in that. No profit, but no shame.":
    "你要不是当“秘藏猎人”的料也没关系。这没什么可耻。没利润，但不可耻。",
 "I'm just tellin' you the stats, man. I've seen a lot of Vault Hunters and a LOT of Vault Hunters go. And by go I mean \"meet grisly fates on every godsdamned inch of this hellhole of a planet,\" haaa.":
    "我只是跟你说数据，老兄。我见过很多秘藏猎人，也见过很——多秘藏猎人“走”。我说的走是指“在这个地狱星球的每一寸他妈的土地上迎来惨死”，哈哈。",
 "Why you think most folks is here on Pandora in the first place?":
    "你以为大多数人一开始为什么会在 潘多拉？",
 "Man, everyone on Pandora says the \"big one\" is right around the corner.":
    "老兄，潘多拉 上所有人都说“大买卖”就在转角。",
 "{ShockA}Whoa man, I never said that. {WorryC}We were just working things out, haha. {HappyA}We were just discussin' openin' you a line of {SlyA}credit right now this very minute {HappyA}is what we were doing. {WorryA}Lemme grab the {WorryC}paperwork, g'bye!":
    "{ShockA}哇老兄，我没那么说。{WorryC}我们只是在想办法，哈哈。{HappyA}我们只是在讨论现在就给你开一条{SlyA}信用额度{HappyA}，就是这样。{WorryA}我去拿{WorryC}文件，再见！",
 "[Flirty] {HappyC}Really? {SmugA}Scooter, you are just the greatest.":
    "[Flirty] {HappyC}真的？{SmugA}斯库特，你就是最棒的。",
 "{AngryA}Ugh. {SternB}I feel gross doing that.": "{AngryA}呃。{SternB}那么干我觉得恶心。",
 "[Sad, pouty] {SadA}Oh no!": "[Sad, pouty] {SadA}哦不！",
 "Hi, \"Scooter,\" right?": "嗨，“斯库特”，对吧？",
 "{HappyA}Thanks Sasha... {AngryA}I just couldn't get through to him.":
    "{HappyA}谢谢 萨莎……{AngryA}我就是跟他说不通。",
 "[Frustrated] {SternA}Yeah, {SadA}I guess I'm used to doing that by now.":
    "[Frustrated] {SternA}是啊，{SadA}我想我现在习惯干这个了。",
 "{FearA}Oh, I--": "{FearA}哦，我——",
 "[Dismissive] {NeutralA}It's fine. He's coming back.": "[Dismissive] {NeutralA}没事。他回来了。",
 "[Smirk] {SadA}Sure.": "[Smirk] {SadA}当然。",
 "{SternA}No? {InquireA}You didn't seem to be making any headway.":
    "{SternA}不是？{InquireA}你好像没什么进展。",
 "{SternA}I...{FearA} would've {SadA}had him soon enough.":
    "{SternA}我……{FearA}很快就会{SadA}拿下他的。",
 "Yeah... Well I'm glad it worked at least.": "是啊……至少成了，我很高兴。",
 "Let's just this over with.": "我们把这了结吧。",
 "{SadA}I'm sorry you had to do that. {AngryA}I just couldn't get through to the guy.":
    "{SadA}很抱歉你得那么做。{AngryA}我就是跟那家伙说不通。",
 "{HappyA}Alright man, alright, so I can give you the new standard repair for free- Cha-ching!- {SlyA} Call it the \"New Customer, {SmugA}No Charge Special,\" {WorryC}hah. {HappyA}I'll have that thing lookin' like new in no time.":
    "{HappyA}好老兄，好，那我可以免费给你做新的标准修理——叮当！——{SlyA}就叫“新客户{SmugA}免单特惠”吧，{WorryC}哈。{HappyA}我很快就能把那东西弄得像新的一样。",
 "{HappyA}So that all sound good to you man? I can throw in a new Torgue Stereo for free to if you want. I had, like, a hundred of em fall off the back of a truck. {WorryA}For actual serious though.":
    "{HappyA}这些听着都还行吧老兄？你要是想要，我还能免费送一套新版 Torgue 音响。我大概有一百套从卡车后面掉下来的。{WorryA}说真的。",
 "{SmugA}Not bad.": "{SmugA}不错。",
 "{InquireA}Just tryin' to figure {WorryA}out what we can afford to {ShockA}doooo--":
    "{InquireA}只是在算{WorryA}我们负担得起{ShockA}做哪些——",
 "--{HappyA}for you fine customers today and it's looking like we can do a lot, {WorryC}haaa. {WorryA}I figure we can give you the full repair for free{HappyA} today on credit - Call it the \"New Customer, No Charge Special\", haaa. {WorryA}Lemme just grab the paperwork.":
    "——{HappyA}今天能为你们这些好客人做些什么，看来我们能做很多，{WorryC}哈哈。{WorryA}我想我们今天可以赊账给你们做全套修理{HappyA}——就叫“新客户免单特惠”，哈哈。{WorryA}我去拿文件。",
 "{HappyA}Yeah so I can definitely work with you I think, it'll just be seein' if {InquireA}maybe we have to cut some corners or somethin'...":
    "{HappyA}是啊，我想我肯定能跟你配合，就是得看{InquireA}是不是得省点步骤什么的……",
 "[Sing-song] {HappyA}I got some gooood ones.": "[Sing-song] {HappyA}我有些很——好的。",
 "{HappyA}Anyway, I figure as long as I'm in there and, ha, {InquireA}doin' it for free, maybe {SlyA}you wanna splurge and get some of the special packages?":
    "{HappyA}总之，我想既然我都在那儿了，哈，{InquireA}还是免费做，也许{SlyA}你想大手笔一下，来几个特装套餐？",
 "{SternA}Yeah man I'm sure, I'm sure. {AngryA}You wanna back off before I stick my wrench in your mouth?":
    "{SternA}是啊老兄我确定，我确定。{AngryA}你想在我把扳手塞进你嘴里之前退后吗？",
 "{ShockA}Awww crap. {SternA}This doesn't look good.": "{ShockA}哦——操。{SternA}这看着不妙。",
 "{HappyA}Come on in, man. We'll get her all hooked up and get to work!":
    "{HappyA}进来吧，老兄。我们把她接好就开工！",
 "{WorryB}Oof. Ride.": "{WorryB}呃。座驾。",
})

# —— 第 7 批：Scooter 增补对白 + 选项短句 ——
T.update({
 "Lost your job at the Purple Skag?": "在紫异犬丢了工作？",
 "\"Old Haven 500?\" Haaaa. Good comedy joke man - There hasn't be anything in Old Haven for liiiike ten years.":
    "“老避风港 500？”哈哈。老兄这笑话真好——老避风港都大概十年没什么东西了。",
 "{SternA}Just doin' my duty to keep ruffians and crap out of my garage. {SlyA}I'm a real protector type.":
    "{SternA}只是尽我的职责，别让流氓之类的进我车库。{SlyA}我是那种保护者型。",
 "{InquireA}Just all part of the service when you{HappyA} Catch-A-Riiii-{AngryA}[starts coughing due to injury] 'Scuse me.":
    "{InquireA}当你在{HappyA} Catch-A-Riiii-的时候，这都是服务的一部分……{AngryA}[starts coughing due to injury] 抱歉。",
 "{InquireA}Man, just some wannabe tough guys tryin' to shake down a local business owner. {SmugA}You know how it is.":
    "{InquireA}老兄，就是几个想装狠的家伙来勒索本地商家。{SmugA}你知道的。",
 "{DoubtfulA}Yeah? They looked pretty {SternA}dangerous to me.":
    "{DoubtfulA}是吗？在我看来他们挺{SternA}危险的。",
 "{AngryA}Pffff. Yeah, they probably could've killed me, but {HappyA}I look death in the face a lot. {SlyA}Like, all the time. Like, \"Hey death, how you doin'?\" No big deal.":
    "{AngryA}嗤。是啊，他们大概本来能杀了我，但{HappyA}我经常直面死亡。{SlyA}就是，时时刻刻。就像，“嘿死亡，你好啊？”没什么大不了。",
 "{WorryA}I heard you cover for us out there.": "{WorryA}我听说你在外面替我们打了掩护。",
 "{SternA}Then it'd just be another day that ends in \"Y.\" {WorryA}Ha HA. 'Cause the days end in \"Y.\" {HappyA}But seriously, folks tryin' to kill me ain't that new. {SmugA}I'm used to it.":
    "{SternA}那不过是又一个以“Y”结尾的日子。{WorryA}哈哈。因为日子都以“Y”结尾。{HappyA}但说真的，有人想杀我可不是什么新鲜事。{SmugA}我习惯了。",
 "{HappyA}Hey man. You two are my customers and seem like nice folks. {SternA}If you got people after you, that ain't none of my business, but {HappyA}I ain't gonna be the one to turn you in.":
    "{HappyA}嘿老兄。你们俩是我的客人，看着也是好人。{SternA}要是有人追你们，那不关我的事，但{HappyA}我不会是那个去举报你们的人。",
 "{SmugA}What if they tried to kill you?": "{SmugA}要是他们想杀你呢？",
 "{NeutralA}Why'd you do that?": "{NeutralA}你干嘛那么做？",
 "{WorryA}But seriously please don't try to murder me.": "{WorryA}但说真的，求你别想着杀我。",
 "{InquireA}You might be murderers or some crap but you{SlyA} ain't tried to murder me yet, haaa.":
    "{InquireA}你们可能是杀人犯还是什么的，但你们{SlyA}还没试着杀我，哈哈。",
 "{HappyA}Thanks.": "{HappyA}谢了。",
 "{HappyA}Hey man it was no big deal. {SternA}Proper man ain't gonna turn in {HappyA}two nice-seemin' ladies.":
    "{HappyA}嘿老兄，没什么大不了。{SternA}正派男人不会去举报{HappyA}两位看着和善的女士。",
 "{SternA}Hey man, I ain't no hero. {HappyA}I trip over my own pant legs one at a time just like everybody else, {WorryA}haa.":
    "{SternA}嘿老兄，我不是英雄。{HappyA}我跟所有人一样，一次被自己一条裤腿绊一下，{WorryA}哈。",
 "{WorryA}Well, that was incredible, Scooter. {SadA}Thank you.":
    "{WorryA}好吧，刚才太厉害了，斯库特。{SadA}谢谢你。",
 "{InquireA}Seems like there's some bad men lookin' for you two though... {WorryB}You got a place to lay low while {NeutralA}I'm gettin' your ride all fixed up?":
    "{InquireA}不过看来有些坏人在找你们俩……{WorryB}在我修你们座驾的时候，你们有地方躲一躲吗？{NeutralA}",
 "[fondly remembering]I remember when Felix first showed us that place. Heh.  Filthy rat hole.":
    "[fondly remembering]我记得 菲利克斯 第一次带我们看那地方。嘿。恶心的老鼠洞。",
 "[Darkly] {SadA}And maybe we can get some answers.": "[Darkly] {SadA}也许我们还能得到些答案。",
 "{NeutralA}I say we hit the safehouse. {WorryA}It'll have everything we need... Money, gear, new IDs...":
    "{NeutralA}我说我们就去安全屋。{WorryA}那里面有我们需要的一切……钱、装备、新证件……",
 "{SadA}You saw those guys out there - {WorryB}This is getting dangerous!":
    "{SadA}你也看到外面那些家伙了——{WorryB}这越来越危险了！",
 "{WorryA}If there's even a chance... We should take it.": "{WorryA}哪怕只有一丝机会……我们就该抓住。",
 "And that's why we need that stuff!": "所以我们需要那些东西！",
 "Sasha. Your wanted poster is everywhere out there. August wants you dead. It's too dangerous--!":
    "萨莎。你的通缉海报外面到处都是。August 想要你死。太危险了——！",
 "{SternA}I just... I get {SadA}scared you're going to get hurt.":
    "{SternA}我只是……我{SadA}害怕你受伤。",
 "{SadA}I know, {DoubtfulA}but I like it better when we're a team.":
    "{SadA}我知道，{DoubtfulA}但我更喜欢我们是一队的时候。",
 "{SchemeA}Glad we're in agreement.": "{SchemeA}很高兴我们达成一致。",
 "{SternA}We gotta risk it. {SadA} What other choices do we have?":
    "{SternA}我们必须冒这个险。{SadA} 我们还有别的选择吗？",
 "{SternA}What if it's not even there anymore? {SternB}You don't know what Felix was up to.":
    "{SternA}要是东西已经不在那儿了呢？{SternB}你不知道 菲利克斯 在干什么。",
 "{SternB}We need to start fresh, and to do that {WorryA}we need to go to the safehouse.":
    "{SternB}我们需要重新开始，而要做到这点{WorryA}我们就得去安全屋。",
 "{SadA}Then {SmugA}let's do it.": "{SadA}那{SmugA}我们就去。",
 "{SternA}I don't think Felix's is too far away... {InquireB}If we're careful we can make it on foot.":
    "{SternA}我觉得 菲利克斯 那儿不算太远……{InquireB}小心点我们走路能到。",
 "[Sweetly] {WorryA}Yeah, I think we can figure something out. {SchemeA}Thanks, Scoot.":
    "[Sweetly] {WorryA}是啊，我想我们能想出办法。{SchemeA}谢了，Scoot。",
 "{HappyA}Anytime. And I really mean that. Imma go get started ok?":
    "{HappyA}随时。我是认真的。我去开工了，好吗？",
 "Man to be you right now: Facin' all them possibilities... Ripe for the takin'.":
    "真羡慕现在的你：面对那么多可能性……就等着被拿走。",
 "I remember one time I was standing around with my friend Smitty, and we were starin' at stuff  like this. And it was one of those times where you're like \"Man, sure is awesome to have such good friends you don't have to say a thing at all and it ain't awkward or nothing.\" But then I turned to him and- and he had... he had died. That was a... that was a tough birthday... for me.":
    "我记得有一次我跟我朋友 Smitty 站在这儿，盯着这种玩意儿看。那是那种你会想“天哪，有这么好的朋友真棒，什么都不用说也不尴尬”的时候。然后我转头看他——他……他死了。那是个……对我来说挺难熬的生日……",
 "Sometimes I just stand here and... and stare at 'em, y'know? I know how it is.":
    "有时候我就站在这儿……盯着它们看，你知道吗？我懂的。",
 "Lotta good choices, I know I know. Real classy ones too, ha.":
    "好选择不少，我知道我知道。还挺有格调的，哈。",
 "I know it's a big decision - You go ahead and take your time.":
    "我知道这是个大决定——你慢慢来。",
 "Can you taste the potential? It's, uh... it's kinda like cinnamon? Or that's just me licking spark plugs again, what day is it?":
    "你能尝到那潜力的味道吗？就是，呃……有点像肉桂？还是我又在舔火花塞了，今天几号？",
 "That one would look badass as hell, man. Take it from me! The badass from hell!":
    "那款会狠得要命，老兄。信我的！地狱来的狠角色！",
 "{HappyA}It's, uh, got good window tinting. Real nice.":
    "{HappyA}它，呃，车窗膜贴得好。真不错。",
 "{HappyA}Alright man, that's cool that's cool.": "{HappyA}好老兄，酷，酷。",
 "{HappyA}The Teed' is good for when you feel like {SmugA}spendin' money but your budget's a {SlyA}little tight, right? {WorryA}Haaa.":
    "{HappyA}“泰迪”适合那种{SmugA}想花钱但预算{SlyA}有点紧的时候，对吧？{WorryA}哈哈。",
 "{ShockA}Aw man the Anshin Deluxe! {HappyA}Badass!": "{ShockA}哦老兄，安心豪华版！{HappyA}狠！",
 "{SmugA}Real sensible but also with {SlyA}just enough flair because you're worth it, {HappyA}right? Yeah. You are.":
    "{SmugA}相当稳妥，同时{SlyA}又有那么点派头，因为你值得，{HappyA}对吧？对。你值得。",
 "I'll get started on it right away.": "我这就开始弄。",
 "{HappyA}That is some fine taste, man. Like a treat for yourself {ShockA}AND for me {HappyA}gettin' to do it. Can't wait!":
    "{HappyA}品味真好，老兄。既是对你自己的犒赏，{ShockA}也是{HappyA}对我的——能亲手做这个。等不及了！",
 "{ShockA}Well holy crap man - The Maliwan Platinum Package? {HappyA}If I were a car, that's what I'd wear on a date with {ShockA}ANOTHER car!":
    "{ShockA}我的天老兄——马利万铂金套餐？{HappyA}我要是辆车，跟{ShockA}*另一辆车*约会时穿的就是这个！",
 "{SmugA}I hear that package is a real popular graduation present in the Eden Sector. {HappyA}Y'know, like, to celebrate not dyin' or whatever. Lotta death in the Eden Sector.":
    "{SmugA}我听说那套餐在 Eden 星区是挺流行的毕业礼物。{HappyA}你知道，就是庆祝没死什么的。Eden 星区死的人可真多。",
 "I'll get it hooked up right away!": "我这就给你装上！",
 "{SternA}I'll take the{HappyA} \"Tediore Special.\"":
    "{SternA}我要那个{HappyA}“泰迪奥特别版”。",
 "{SternB}How about this one?": "{SternB}这个怎么样？",
 "{SchemeA}What the hell. {SchemeD}Let's go for the whole nine yards.":
    "{SchemeA}管他呢。{SchemeD}我们就来个全套。",
 "Actually I think we'll just take her back to factory settings. Save the extra cash.":
    "其实我想我们就把她恢复原厂设置吧。省下那笔钱。",
 "No problem, no problem.": "没问题，没问题。",
 "Let's take 'er back.": "把她恢复原样吧。",
 "Don't blame me when you're missing that flaa-ash though.":
    "不过等你怀念那闪——闪光的时候别怪我。",
 "Wrecked Car": "报废的车",
 "Pin-Up Calendar": "海报女郎日历",
 "Engine Block": "引擎缸体",
 "Scooter": "斯库特",
 "{SadA}Hope he's got time to help us.": "{SadA}希望他有时间帮我们。",
 "{FearA}Eeeeyikes. Suddenly the Caravan seems a lot less wrecked.":
    "{FearA}哇呀。突然觉得我们的房车没那么破了。",
 "{AngryA}Yowch. {SternA}That'll teach me to put my fingers where they don't belong.":
    "{AngryA}哎哟。{SternA}这会教会我别把手指放到不该放的地方。",
 "[Sing-song] {SchemeB}Looks like someone's over-compensating.":
    "[Sing-song] {SchemeB}看来有人在过度补偿。",
 "{FearA}On second thought... {AngryA}Who knows where that thing's been. Eesh.":
    "{FearA}再想想……{AngryA}谁知道那玩意儿待过哪儿。呃。",
 "{InquireA}I don't know much about engines... {SchemeB}but even I can tell that thing's got some serious oomph.":
    "{InquireA}我对引擎不太懂……{SchemeB}但连我都看得出那玩意儿马力很猛。",
 "{SchemeB}I wonder if Scooter can put something like this in the Caravan...":
    "{SchemeB}不知道 斯库特 能不能把这种东西装进房车……",
 "{HappyA}Well. {SmugA}Don't mind if I do.": "{HappyA}好吧。{SmugA}那我就不客气了。",
 "If I'd known that I'd be seeing this picture so much, I would've smiled...":
    "我要是早知道会这么常看到这张照片，我就笑一下了……",
 "One to add to the collection I guess.": "我想，又多一张收藏。",
 "[Stunned] Well that's new.": "[Stunned] 好吧，这可是新东西。",
})

# —— 第 8 批：选项短句 + Scooter 代言合同线 ——
T.update({
 "[Sing-song] {SchemeB}Looks like someone's over-compensating.\n[alt]":
    "[Sing-song] {SchemeB}看来有人在过度补偿。\n[alt]",
 "Nice place you have here.": "你这地方不错。",
 "I need repairs.": "我需要修车。",
 "\"New proprieter?\"": "“新老板？”",
 "I'm a wanted woman.": "我是个被通缉的女人。",
 "I'm a famous racer.": "我是个有名的车手。",
 "I'm a vault hunter.": "我是秘藏猎人。",
 "That's way too much!": "那也太多了！",
 "How about a down payment?": "付个定金怎么样？",
 "I'll pay you later.": "我以后再付你。",
 "Just know I'm the best there is.": "你只要知道我是最棒的就行。",
 "Candy from a baby.": "从婴儿手里抢糖。",
 "Too dangerous to talk about.": "太危险，不能说。",
 "Yeah, big race coming up.": "是啊，马上有场大赛。",
 "I only raced the one time.": "我只赛过那一场。",
 "Not the winnings, the endorsements.": "不是奖金，是代言。",
 "The Hollow Point Drags": "空心镇直线加速赛",
 "The name of the race isn't important.": "比赛叫什么名字不重要。",
 "I won!": "我赢了！",
 "I was the last woman standing.": "我是最后站着的女人。",
 "It was a massacre.": "那是一场屠杀。",
 "This Vault is different.": "这座秘藏不一样。",
 "I'm the best at what I do.": "我干这行是最棒的。",
 "No risk, no reward.": "没有风险，就没有回报。",
 "We can just stick with the basics.": "我们就用基础款就行。",
 "{NormalA}Might be needin' repairs.": "{NormalA}可能得修车。",
 "{NormalA}We're lookin' for these two women. {NormalB}They're traveling in an old caravan.":
    "{NormalA}我们在找这两个女人。{NormalB}她们开着一辆旧房车。",
 "{HappyA}Hey fellas. What can I do ya for?": "{HappyA}嘿几位。我能为你们做什么？",
 "What did you have to threaten him for?  He'll tun us in for sure!":
    "你干嘛非要威胁他？他肯定会举报我们的！",
 "[worried] {WorryA}Well, let's hope I made a great impression.":
    "[worried] {WorryA}好吧，希望我给他留了个好印象。",
 "{WorryA}I just hope whatever story you told Scooter is enough to get him to look the other way.":
    "{WorryA}我只希望你跟 斯库特 说的那套能让他睁一只眼闭一只眼。",
 "We are so screwed.": "我们彻底完了。",
 "{SadB}We are totally screwed.": "{SadB}我们彻底完了。",
 "{AngryA}Oh, that's great positive thinking, Fiona.":
    "{AngryA}哦，真是超棒的正向思维，Fiona。",
 "Scooter won't turn on us.": "斯库特 不会背叛我们。",
 "{SternA}Scooter won't turn us in.": "{SternA}斯库特 不会举报我们。",
 "{AngryA}You don't know that. {WorryA}We don't even know what the reward is this time!":
    "{AngryA}你不知道。{WorryA}我们连这次的赏金是多少都不知道！",
 "Get ready to run.": "准备跑。",
 "{WorryA}Only if it comes to it.": "{WorryA}真到那一步再说。",
 "{SternA}Okay, listen, if things go sour, {SternB}get ready to run.  {HappyA}I'll be right behind you.":
    "{SternA}好，听着，要是事情不对，{SternB}准备跑。{HappyA}我就在你后面。",
 "{SternA}I'll take the high ground, {WorryA}you cover the backend?":
    "{SternA}我占高位，{WorryA}你守后面？",
 "Have some faith.": "有点信心。",
 "My story was too good": "我那套说法太好了",
 "He likes you!": "他喜欢你！",
 "I hate when you say that.": "我讨厌你这么说。",
 "You've just got to have some faith, Sasha.": "你得有点信心，萨莎。",
 "[hesitant]...Ookay...": "[hesitant]……好——吧……",
 "{AngryA}{Body-A}Uh, no.  I mean I'm {InquireA}wanted.  {HappyB}As in, I'm an outlaw?  {SmugB}I'm pretty famous.":
    "{AngryA}{Body-A}呃，不是。我是说我是{InquireA}被通缉的。{HappyB}就是，我是亡命之徒？{SmugB}我挺有名的。",
 "{ShockA}You're on a poster? {HappyA}Aw crap man yeah that's it! I prolly seen you on one of my callendars!  {SlyA}Miss June, right? Hell yeah {HappyA}you're a wanted woman!":
    "{ShockA}你上通缉海报？{HappyA}哦操老兄对就是它！我大概在我某本挂历上见过你！{SlyA}六月小姐，对吧？他妈没错{HappyA}你是被通缉的女人！",
 "He's intrigued, means we've got him hooked.": "他感兴趣了，说明我们把他钩住了。",
 "He was totally into my \"Wanted Criminal\" story.": "他完全被我的“通缉犯”故事吸引住了。",
 "I hope you're right.": "我希望你说得对。",
 "Did you see how his eyes lit up when I started talking about cars?":
    "你看到他眼神在我开始聊车的时候亮起来了吗？",
 "He won't risk turning us in over what he could gain if we open a vault!":
    "他不会冒着失去我们开秘藏能给他的好处的风险去举报我们！",
 "Anyway, he's not gonna give up a chance with you by turning us in.":
    "总之，他不会为了举报我们而放弃跟你相处的机会。",
 "Something you could stand to learn.": "这点你该学学。",
 "You're really good at getting people to like you.": "你真的很擅长让人喜欢你。",
 "You know, it's creepy when you say it.": "你知道吗，你这么说挺瘆人的。",
 "[exasperated] {WorryA}Don't smile like that.  It's creepy.":
    "[exasperated] {WorryA}别那样笑。挺瘆人的。",
 "{InquireA}What, you {SternA}can't even tell me what they're wanted for?":
    "{InquireA}怎么，你{SternA}连她们因为什么被通缉都不能说？",
 "{NormalA}That's our business.": "{NormalA}那是我们的事。",
 "{SternA}Why do ya want 'em?": "{SternA}你要她们干嘛？",
 "{SternA}Is that right? {SlyA}Maybe I ain't got  such simple tastes.":
    "{SternA}是吗？{SlyA}也许我的口味没那么简单。",
 "{NormalA}There's a reward. {SarcasticA}Enough to make a simpleton like {NormalA}you happy.":
    "{NormalA}有赏金。{SarcasticA}多到能让{NormalA}你这种傻子满意。",
 "{AngryA}...Our. Business.": "{AngryA}……我们。的。事。",
 "{NormalA}So have you seen them or not?": "{NormalA}那你到底见过她们没有？",
 "[Making a decision NOT to sdell out the girls]{SternA}Nah. Naw I don't think I have. {InquireA}Now you two best be gettin on, {NeutralA}I've got business to attend to.":
    "[Making a decision NOT to sdell out the girls]{SternA}没有。不，我想我没见过。{InquireA}你们俩最好赶紧走，{NeutralA}我还有生意要照看。",
 "{SadA}Felix is... gone, {WorryB}but that stuff should still all be there.":
    "{SadA}菲利克斯 是……不在了，{WorryB}但那些东西应该还在那儿。",
 "I know, I'm sorry.": "我知道，抱歉。",
 "I didn't ask for your help.": "我没要你帮忙。",
 "It wasn't that bad.": "没那么糟。",
 "Who were those guys?": "那些家伙是谁？",
 "Why did you do that?": "你干嘛那么做？",
 "Thanks for covering for us.": "谢谢你替我们打掩护。",
 "Yeah, let's go.": "好，我们走。",
 "The Tediore Special [$]": "泰迪奥特别版 [$]",
 "The Anshin Deluxe [$$]": "安心豪华版 [$$]",
 "Platinum Package [$$$]": "铂金套餐 [$$$]",
 "No Upgrade": "不加升级",
 "Haven't seen this much paperwork since my aunt-cousin tried to marry my brother-uncle and sue him at the same time.":
    "我上次见这么多文件，还是我表姑想嫁给我表叔还同时起诉他的时候。",
 "{ShockA}I figure that's your ride...": "{ShockA}我想那是你们的座驾……",
 "Hi. \"Scooter,\" right?": "嗨。“斯库特”，对吧？",
 "but I let it blow up, along with my best friend.":
    "但我让它炸了，连同我最好的朋友一起。",
 "I uh, raced in the Bossanova Deathrace 3000.":
    "我，呃，跑过 Bossanova 死亡竞速 3000。",
 "{FearA}Look Scooter, I'm out of options here.  {SternA}I need those repairs.":
    "{FearA}听着 斯库特，我这儿没别的路了。{SternA}我需要那些修理。",
 "Look, this is a cash business.": "听着，这是现金生意。",
 "Maybe I could make an exception, if you know, you were kind of a big deal.":
    "也许我能破例，要是你，你知道，算个人物的话。",
 "{SternA}Look, {SchemeB}I AM kind of a big deal.":
    "{SternA}听着，{SchemeB}我*确实*算个人物。",
 "{SmugA}Remember when I said was a famous racer?":
    "{SmugA}记得我说过我是个有名的车手吗？",
 "{WorryC}Look, this is a cash business.": "{WorryC}听着，这是现金生意。",
 "{WorryA}Maybe I could make an exception, if you know, you were kind of a big deal.":
    "{WorryA}也许我能破例，要是你，你知道，算个人物的话。",
 "{HappyA}I heard that was a real nuclear kerfuffle.  Tell me more.":
    "{HappyA}我听说那是场真正的核级大乱斗。多说点。",
 "{InquireA}{Body-A}I'm a pretty famous {Body-B}racer.":
    "{InquireA}{Body-A}我是个挺有名的{Body-B}车手。",
 "{ShockA}Oh really.  {HappyA}I'm a big fan of the races.  {InquireA}I don't recognize you.":
    "{ShockA}哦真的。{HappyA}我是赛车的忠实粉丝。{InquireA}我不认识你。",
 "{SchemeA}I'm new.  {InquireA}New and famous.  {Body-A}{DoubtfulA}Maybe more new than famous.":
    "{SchemeA}我是新手。{InquireA}又新又有名。{Body-A}{DoubtfulA}也许“新”多过“有名”。",
 "{HappyA}Well good for you, you keep at it, and {SlyA}maybe I'll have heard of you someday.":
    "{HappyA}那恭喜你，你继续努力，{SlyA}也许哪天我就听说过你了。",
 "Well, not much of a story there.  You should work on your anecdotal proclivity.":
    "好吧，这故事没什么料。你该练练你讲轶事的本事。",
 "Alright, well call me crazy but I like your style.":
    "好，你可以说我疯，但我喜欢你的风格。",
 "I don't think I'm gonna be able to help you out here.":
    "我想我这儿帮不了你。",
 "I could see about fixing your ride.": "我可以想办法修你的座驾。",
 "Jesus, lady you are hard-CORE!": "天哪，女士你可真是狠——角色！",
 "Let's see what I can do for you.": "看看我能为你做什么。",
 "Vending Machine": "自动售货机",
 "Salty Snack": "咸味零食",
 "Candy": "糖果",
 "Scooter's Special": "斯库特 特制",
 "Jakobs Option": "雅各布斯选项",
 "Platinum Package": "铂金套餐",
 "Buy ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_7:-8><ui_cash_5:-8>":
    "购买 ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_7:-8><ui_cash_5:-8>",
 "Buy ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_1:-8><ui_cash_0:-8><ui_cash_0:-8>":
    "购买 ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_1:-8><ui_cash_0:-8><ui_cash_0:-8>",
 "Buy ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_2:-8><ui_cash_0:-8><ui_cash_0:-8>":
    "购买 ^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_2:-8><ui_cash_0:-8><ui_cash_0:-8>",
 "[to himself]C14, C14. Yes sir. Check.": "[to himself]C14，C14。是的先生。打勾。",
 "[to himself]One, two, three, four, five, check.":
    "[to himself]一、二、三、四、五，打勾。",
 "[to himself]B7. B7? That can't be right.": "[to himself]B7。B7？那不对吧。",
 "[to himself]Per month? Is this a checklist or a damn math test?":
    "[to himself]每月？这是清单还是该死的数学考试？",
 "[to himself]See addendum. Dear God.": "[to himself]见附录。我的天。",
 "[to herself about Scooter]Sure looks like an easy mark.":
    "[to herself about Scooter]看着确实像个好骗的肥羊。",
 "[To Herself]Hm. Smash up cars in the middle of the night, business stays good year round. Might be his angle.":
    "[To Herself]嗯。半夜砸车，生意全年都好。也许这就是他的门道。",
 "[to herself]If he can build this, he can't be a total idiot.":
    "[to herself]他能造出这个，就不可能是彻底的傻子。",
 "Leaving money out like this... I almost feel sorry for the poor sap. [beat] Almost.":
    "把钱就这么搁在外头……我都快替那可怜虫难过了。[beat] 快。",
 "I took out Bossanova": "我干掉了 Bossanova",
 "Almost got ten million dollars.": "差点拿到一千万美元。",
 "I kicked Bandit ass": "我把土匪揍了",
 "Fire Melon Air Freshener": "火焰瓜车载香氛",
 "My wanted poster.": "我的通缉海报。",
 "Was in a race.": "参加了一场比赛。",
 "I'd rather not say.": "我还是不说了。",
 "Oh yeah, sure.": "哦是啊，当然。",
 "No way, man.": "不行，老兄。",
 "If it's worth my while.": "要是值得的话。",
 "Some jerk robbed me.": "有个混蛋抢了我。",
 "I've already spent it.": "我已经花光了。",
 "I don't wanna talk about it.": "我不想谈这个。",
 "No thanks, I need to lay low.": "不了谢了，我得低调。",
 "Sounds good, Scooter.": "听着不错，斯库特。",
 "If you sweeten the deal.": "你要是加点甜头。",
 "I'm not signing that.": "我不签那个。",
 "Really not cool, Scooter.": "这可真不地道，斯库特。",
 "Anything for the fans.": "为了粉丝什么都行。",
 "Hey hey hey what are you doin' in there man? You can't just come into a man's garage and start pokin' around...":
    "嘿嘿嘿你在里面干什么，老兄？你不能就这么进别人车库乱翻……",
 "[Suspicious] Just what're you doing with that? Get out of there.":
    "[Suspicious] 你拿那个干什么？从那儿出来。",
 "[Warmer] Hey. Do I know you from somewhere, man? You look real familiar.":
    "[Warmer] 嘿。我是不是在哪儿见过你，老兄？你看着特别眼熟。",
 "[Bragging] You might recognize me from my Wanted poster.":
    "[Bragging] 你也许是从我的通缉海报上认出我的。",
 "You ever hang around Sanctuary?": "你在避风港待过吗？",
 "Or maybe": "或者也许",
 "Pffft oh YEAH that's it. You're totally right.":
    "嗤，哦*是*！就是它。你完全说对了。",
 "Well don't worry I ain't gonna drag you in or nothin'. I got lots of friends wanted for lots stuff.":
    "别担心，我不会把你交出去什么的。我有很多朋友因为各种事被通缉。",
 "[Stage whisper, trying to impress her] My really badass friends.":
    "[Stage whisper, trying to impress her] 我那些超狠的朋友。",
 "Oh well that's good.": "哦，那挺好。",
 "[Dismissive] Yeah man I don't give a rakk's ass what you done so long as your dough's good, y'know?":
    "[Dismissive] 是啊老兄，只要你的钱是真的，我才他妈不管你干过什么，懂吗？",
 "Whoa. I just need some repairs.": "哇。我只是需要修车。",
 "Let's take a look at whatcha rode in on, huh?": "我们看看你是开什么来的，哈？",
 "[Still can't place her face, letting it go] Alright man...":
    "[Still can't place her face, letting it go] 好吧老兄……",
 "[Dismissive] I have no idea. I know that I've never seen you before.":
    "[Dismissive] 我完全不知道。我确定我从没见过你。",
 "Alright, that's cool. Just making conversation, alright?":
    "好，酷。就是聊两句，行吗？",
 "Oh, it'll come to me soon, I swear, but in the meantime... just stay out of my stuff... and then we'll get down to business!":
    "哦，我很快就会想起来的，我发誓，但在此期间……别碰我的东西……然后我们就谈正事！",
 "So what're we working with?": "那我们手上是什么情况？",
 "[Low whistle] Aw crap man that girl is a MESS. What'd you do to her?":
    "[Low whistle] 哦操老兄，那姑娘简直就是一团糟。你把她怎么了？",
 "Aw crap man that girl is a MESS. What'd you do?":
    "哦操老兄，那姑娘简直就是一团糟。你干了什么？",
 "That crap is torn clean off, man. You piss off, like, a whole pack of threshers or somethin'?":
    "那玩意儿被整个撕下来了，老兄。你惹毛了一整群鞭尾兽还是怎么着？",
 "Almost looks like it should just explode and put itself out of its misery. No offense.":
    "看着几乎像是该直接炸掉、自我了结。无意冒犯。",
 "I mean I'm assuming that the whole, uh, hole, wasn't standard. Gonna have to patch that up. And you're gonna need new wheels that is for damn sure.":
    "我是说，我猜那个，呃，洞，不是标配。那个得补上。而且你他妈肯定需要新轮子。",
 "We were driving across the dust and Helios started taking potshots.":
    "我们正在沙地上开，太阳神就开始乱打炮。",
 "[Mimicking moonshot noise] Moonshot.": "[Mimicking moonshot noise] 月球投射。",
 "Frickin' Hyperion asshole sumbitches, man. That crap is nasty. Ugh. Hate those guys.":
    "他妈的 亥博龙混蛋狗东西，老兄。那玩意儿太毒了。呃。讨厌那帮家伙。",
 "I was in a race - Bossanova's Death Rally?": "我参加了一场比赛——Bossanova 的死亡拉力赛？",
 "Oh ho-ly CRAP that's it man! That's where I recognize you from!":
    "哦我——操，就是它老兄！我就是从那儿认出你的！",
 "[Excited] You were so freakin' awesome!": "[Excited] 你简直太他妈厉害了！",
 "[Humble] Oh, well, thank you thank you.": "[Humble] 哦，那个，谢谢，谢谢。",
 "How about we just figure out how to get it fixed, huh?":
    "我们不如想想怎么把它修好，哈？",
 "[Stung] Uhh, alright man. Little bit hostile, but that's cool. That's coool.":
    "[Stung] 呃，好吧老兄。有点敌意，但没事。没事。",
 "[Returning to caravan] Let's see...": "[Returning to caravan] 我们看看……",
 "The, uh, silent type, huh?": "那个，呃，沉默型的，哈？",
 "Alllllright. Well...": "好——吧。那么……",
 "[Hushed] Rough memories, huh? That's cool man I won't push it.":
    "[Hushed] 回忆不好受，哈？没事老兄，我不逼你。",
 "That's cool man I won't push it.": "没事老兄，我不逼你。",
 "[Excited] I knew I recognized this rig from somewhere - You were in the latest Bossanova Death Rally!":
    "[Excited] 我就知道我在哪儿见过这辆车——你参加了最近那场 Bossanova 死亡拉力赛！",
 "Hol. Ee. Crap.": "我。的。天。",
 "Oh, I was there, man! D'you see me? I was- I was waving, You were a BADASS!":
    "哦，我当时在场，老兄！你看到我了吗？我在——我在挥手，你太*狠*了！",
 "Now come on man, you should be able to afford twenty five hundo easy!":
    "得了吧老兄，两千五你肯定轻松拿得出来！",
 "Cuz my cousin, right?": "因为我表哥，对吧？",
 "'Course, those days they were mostly eatin', y- y'know, the... the money... but- but still, it was weeks!":
    "当然，那些日子里他们大多在吃——你——你知道，那……那钱……但——但还是撑了好几个星期！",
 "I saw how good you did - Where'd all your winnings go?":
    "我看到你跑得多好了——你的奖金都去哪儿了？",
 "[Humble] Oh. Yep. Caught me.": "[Humble] 哦。对。被你抓到了。",
 "Freakin' awesome, man.": "他妈的厉害，老兄。",
 "Yeah, someone stole it. Can you believe that?": "是啊，有人偷了它。你敢信吗？",
 "[Deadpan] Yes, actually. Yes I can.": "[Deadpan] 是啊，其实。我当然信。",
 "[Brag/lying] Sure it probably looked like a lot to SOME people, but when you live the sort of lifestyle that I do? That barely gets you home from the afterparty.":
    "[Brag/lying] 当然，在*某些*人看来那可能挺多，但当你的生活方式像我这样？那只够你从派对收场回家。",
 "Y'know there are some who would view that as boasting and downright wasteful, but I appreciate your gusto for life, man.":
    "你知道，有人会觉得那是吹牛、纯属浪费，但我欣赏你对生活的热情，老兄。",
 "Didn't anyone ever tell you it's inappropriate to ask somebody about their money?":
    "没人告诉过你问别人钱的事不礼貌吗？",
 "Alright man. That's your business.": "好老兄。那是你的事。",
 "Money problems, huh? I been there.": "钱的问题，哈？我也经历过。",
 "[Laying the groundwork for an offer] Well, tell me this: You think you could ever see yourself racing again?":
    "[Laying the groundwork for an offer] 那么，告诉我这个：你觉得你还能想象自己再赛车吗？",
 "Hittin' the track?": "上赛道？",
 "Knowing that any false move could be your last?": "知道任何一个失误都可能是最后一次？",
 "Feeling the dirt filling your lungs and just bein' grateful that your lungs are still moving at all?":
    "感受着尘土灌满你的肺，同时感激你的肺还在动？",
 "[Cocky] Depends on how much it'll pay out when I win.":
    "[Cocky] 得看我赢的时候能拿多少钱。",
 "Now that's the kind of attitude I can get behind, man! Power of positive thinkin' and, uh, other stuff.":
    "这才是我能支持的态度，老兄！正向思维的力量，还有，呃，别的什么的。",
 "Oh most definitely. They'd have to hire bodyguards to keep me away from the track.":
    "哦绝对的。他们得雇保镖才能拦住我上赛道。",
 "Hey that's just like my brother-uncle! Course, the track hired bodyguards so he would stop runnin' on it naked so maybe it's not exactly the same... What was I saying?":
    "嘿，这跟我表叔一模一样！当然，赛道雇保镖是为了让他别再光着身子在上面跑，所以也许不完全一样……我刚说什么来着？",
 "What was I saying?": "我刚说什么来着？",
 "We were talking about whether I'd race again?": "我们在聊我会不会再赛车？",
 "[Back on track] Right!": "[Back on track] 对！",
 "[Aside, nervous] I'm so aware of my lungs right now.":
    "[Aside, nervous] 我现在对自己的肺感受得特别清楚。",
 "No way, man. I'm done with that lifestyle.": "不行，老兄。那种生活我不干了。",
 "[Disappointed] Yeah? Well, before you give it up...":
    "[Disappointed] 是吗？那，在你放弃之前……",
 "Awkward cough, man.": "尴尬地咳嗽一下，老兄。",
 "Annnnyway.": "总——之。",
 "Lemme pitch ya somethin'. And it might be crazy.": "让我给你推销点什么。也许有点疯。",
 "But if you keep racin' I would love to endorse you as a SPONSOR. Whaddya say?":
    "但你要是继续赛车，我很乐意作为*赞助商*代言你。怎么样？",
 "It'll be GREAT. Maybe, like, a billboard...": "会很*棒*。也许，呃，一块广告牌……",
 "Be on, like, cereal boxes...": "上，呃，麦片盒……",
 "...lunch boxes... other stuff that's not on boxes...":
    "……午餐盒……其他不在盒子上的东西……",
 "...box boxes... (Think I'm fixating on boxes)": "……盒子盒子……（我觉得我盯上盒子了）",
 "And all you have to do is be asked stuff like--": "你只要被问这种问题——",
 "[Newscaster voice] \"Say, amazing racer, how do you keep your vehicle in such top-notch condition?\" And then you'll answer somethin' like [Fiona impression] \"Well, when my car's in trouble, I just Catch-A-Ride!\"":
    "[Newscaster voice]“我说，了不起的车手，你是如何让你的座驾保持这么顶尖状态的？”然后你就回答类似[Fiona impression]“这个嘛，我的车有麻烦时，我就 Catch-A-Ride！”",
 "And then YOU'LL answer somethin' like--": "然后*你*就回答类似——",
 "[Fiona impression] \"Well, when my car's in trouble I just... Catch A Ride.\"":
    "[Fiona impression]“这个嘛，我的车有麻烦时我就……Catch A Ride。”",
 "It'll be PERFECT.": "会完美无缺。",
 "...other stuff that's not on boxes...": "……其他不在盒子上的东西……",
 "Yeah, thanks but no thanks, Scooter. I think I'll pass.":
    "是啊，谢了但不必了，斯库特。我想还是算了。",
 "[Disappointed] Aw, well, I guess that's, like, your perogative or whatever man. But still, shoot...":
    "[Disappointed] 哦，好吧，我想那是，就，你的权利什么的吧，老兄。但还是，唉……",
 "[To himself, quiet] Would've been coo-ool.": "[To himself, quiet] 本来会很酷——的。",
 "Scooter, sir? You have yourself a deal.": "斯库特 先生？这交易成了。",
 "Yeah?! Aw man this is AWESOME. You will not regret this, no way no how, man. BadASS.":
    "是吗？！哦老兄这太*棒*了。你不会后悔的，绝对不会，老兄。*狠*。",
 "You will not regret this, no way no how, man. BadASS.":
    "你不会后悔的，绝对不会，老兄。*狠*。",
 "Tell you what: Throw in an extra thousand bucks and you've got yourself a deal.":
    "这样吧：再加一千块，这交易就成了。",
 "\"Thousand?\" Whoa man, that's kind of a hard bargain, don'tcha think?":
    "“一千？”哇老兄，这有点狠啊，你不觉得吗？",
 "[Thinking] Hnnnnnnnokay okay. Thousand bucks... it's yours, but you're gonna have to win, like, a crapload of races, alright? I ain't made of money, man.":
    "[Thinking] 嗯————好吧好吧。一千块……归你了，但你得赢他妈一大堆比赛，行吗？我可不是钱做的，老兄。",
 "But you're gonna have to win, like, a crapload of races, okay? I ain't made of money, man.":
    "但你得赢他妈一大堆比赛，行吗？我可不是钱做的，老兄。",
 "Orrrrr, y'know, nevermind. That's cool, that's cool.":
    "或——者，你知道，算了。没事，没事。",
 "I'm thinkin' that we put a big ol' ad on your van - Y'know, like maybe a picture of me with, like, \"Catch A Riiiiide\" up above it, y'know, all cool, right?":
    "我想我们在你们车身上贴个大广告——你知道，也许放张我的照片，上面写着“Catch A Riiiiide”，你知道，很酷，对吧？",
 "I'm looking all badass with you, and we'll put some... badass pictures of you with your car and your hat and all that...":
    "我跟你一起摆出狠样，然后我们再放些……你跟你的车、你的帽子的狠照……",
 "And, now, correct me if I'm wrong man... But did I see you with another girl back in that arena?":
    "还有，要是我说错了你纠正我，老兄……但我在那竞技场里是不是看到你跟另一个姑娘一起？",
 "Unrelated question: That girl with you back in the arena - Was that your sister or something because she was cuuuuuuuuuu--[trails off as he sees Sasha]":
    "无关的问题：竞技场里跟你一起的那个姑娘——那是你妹妹还是什么的？因为她可真是漂——[trails off as he sees Sasha]",
 "[Lovestruck, quiet] Ho-ly crap.": "[Lovestruck, quiet] 我——的天。",
 "[Stumbling] Anyway. That's why I'll be covering all the repairs for free today!":
    "[Stumbling] 总之。所以今天全部修理我包了！",
 "Just gotta grab the paperwork lemme go take care of that okay bye.":
    "只要去拿一下文件让我去处理一下好吗再见。",
 "Goin' great man! Just signed this badass racer here to an equally badass endorsement deal since I am, y'know, a legitimate man of legitimate business.":
    "进展顺利老兄！刚给这位狠角色车手签了一份同样狠的代言合同，毕竟我是，你知道，做正经生意的正经人。",
 "How's everything going?": "一切进展如何？",
 "[To both] Everything going okay?": "[To both] 一切都还好吗？",
 "[Quietly] Thank you...": "[Quietly] 谢谢……",
 "[Snippy] Well it was starting to get painful watching you dangle like that.":
    "[Snippy] 好吧，看你在那儿吊着越来越难受了。",
 "Hey. I don't seem to remember asking for your help.":
    "嘿。我好像不记得有请你帮忙。",
 "Easy for you to say. You weren't the one that he wanted to get his greasy hands all over.":
    "你说得轻松。他想用那双油手摸个遍的人不是你。",
 "Aw come on. It wasn't that bad.": "哎呀得了吧。没那么糟。",
 "Well it seems like we're at a, whatchacallit, crossroad.":
    "看来我们到了个，那个词怎么说，十字路口。",
 "Come on. What happened back there? Doing that flirty act always makes me feel gross.":
    "得了吧。刚才到底怎么回事？演那种调情的戏总让我觉得恶心。",
 "Sorry, but I'm not signing that.": "抱歉，但我不签那个。",
 "[Awkward throat clear] I was, uh, I was just gonna, y'know... go grab the paperwork. Lemme take care of that, okay bye.":
    "[Awkward throat clear] 我，呃，我正要去，你知道……去拿文件。让我处理一下，好吗再见。",
 "Alright man, here's my standard endorsement contract. Don't mind the sub-clauses about, uh, explosions and whatnot. I might'a copied it from Torgue...":
    "好老兄，这是我的标准代言合同。别在意那些关于，呃，爆炸之类的附加条款。我可能是从 Torgue 那儿抄的……",
 "Alright, go ahead and just sign right here on the dotted line and we can get you goin'!":
    "好，就在这儿的虚线上签个名，我们就能让你出发了！",
 "Say man, so long as you're here signing stuff, how about you sign somethin' to hang up here in the shop? Y'know? For your fans?":
    "我说老兄，既然你在这儿签东西，不如签点什么挂在店里？你知道？给你的粉丝？",
 "And a Wanted Poster? That's cool as hell, man. Outlaaaaw.":
    "签通缉海报？那可太他妈酷了，老兄。亡——命之徒。",
 "I mean when people hear about my badass new endorsed racer...":
    "我是说，等人们听说我新代言的狠角色车手……",
 "They are goin' to come flockin' like rakks around a fresh bullymong carcass, man.":
    "他们会像拉卡围着新鲜的恶霸兽尸体一样涌过来，老兄。",
 "Outlaaaaw.": "亡——命之徒。",
 "I mean, sure, I might not be ENDORSIN' you...": "我是说，当然，我也许没在*代言*你……",
 "But when people hear that a badass racer like you came here?":
    "但当人们听说像你这么狠的车手来过这儿？",
 "[Disappointed] No? Is it weird because it's a wanted poster? Damn social etiquette... Sorry. I'll just stick to fixing your ride.":
    "[Disappointed] 不行？是因为那是通缉海报所以怪吗？该死的社交礼仪……抱歉。我就专心修你的车吧。",
 "Sorry, though. I'll just stick to fixing your ride.": "不过抱歉。我就专心修你的车吧。",
 "Get that thing out of my face. I'm not signing my *wanted poster* for you.":
    "把那玩意儿从我眼前拿开。我不会给你签我的*通缉海报*。",
 "Okay, wow, I get it, man. Sorry. I just thought it would be kinda cool.":
    "好，哇，我懂了，老兄。抱歉。我只是觉得那会挺酷的。",
 "I'll just go... fix your ride I guess.": "那我就去……修你的车吧，我想。",
 "[Reluctant, but already signing] Anything for the fans, I guess?":
    "[Reluctant, but already signing] 为了粉丝什么都行，我想吧？",
 "Hellll yeah man. That's what I'm talking about. Haven't had somethin' I was this excited to hang since I caught that shoplifter.":
    "太——棒了老兄。这才对嘛。自从我抓到那个偷东西的之后，我还没这么兴奋地想挂点什么。",
 "[Awkward beat] Haaa... it's a joke! Hahahahaha...":
    "[Awkward beat] 哈……开玩笑的！哈哈哈哈哈……",
 "She's, uh, shy. Sorry Scooter.": "她，呃，害羞。抱歉 斯库特。",
 "Aw that's alright, I get that.": "哦没事，我懂。",
 "[Smirk] And don't tell me you're broke because I knowww you got that extra thousand I just gave you.":
    "[Smirk] 也别跟我说你破产了，因为我可知道——你刚拿了我那一千块。",
 "Name's Fiona.": "我叫 Fiona。",
 "I'm Fiona. I just really need some repairs.": "我是 Fiona。我真的需要修车。",
 "I ain't seen somethin' this torn up since we tied my pal Smitty up in a sack, put butter on him, and tossed him in a thresher field. [Snort of laughter] Aw Smitty. He had no sense of humor, man.":
    "我见过的破得最惨的，就是我们把哥们 Smitty 绑进麻袋、抹上黄油、扔进鞭尾兽田里那次。[Snort of laughter] 哦 Smitty。他一点幽默感都没有，老兄。",
 "Oh, I've seen some messes... like, some real bad messes, in my time, but this one takes the damn CAKE... and then it craps it back out again! You know what I'm saying?":
    "哦，我这辈子见过一些烂摊子……就是，一些真的烂透的摊子，但这个真是烂到*极点*……然后还又拉出来一次！你懂我意思吗？",
 "Uhhh, I mean, I guess. Except for usually when I'm doin' business with someone, I like to ask about how said business is gonna get paid for.":
    "呃，我是说，我想是吧。只不过通常我跟人做生意的时候，我喜欢问问这生意打算怎么付钱。",
 "[Nodding] Money problems is hard. My dentist had a, uh... [hushed] \"financial situation\" a few years back, y'know.":
    "[Nodding] 钱的问题很难。我牙医几年前有，呃……[hushed]“财务状况”问题，你知道。",
 "I'll tell you exactly what I told him: \"Don't be afraid to ask for help. And give back my bicuspid.\"":
    "我把跟他说的一字不差告诉你：“需要帮忙就别怕开口。还有把我的双尖牙还回来。”",
 "I'll tell you exactly what I told him: \"Don't be afraid to ask for help. And give me back my damn bicuspid.\"":
    "我把跟他说的一字不差告诉你：“需要帮忙就别怕开口。还有把我他妈的双尖牙还回来。”",
 "Anyway.": "总之。",
 "Say it just once: \"Catch A Ride!\"": "就说一次：“Catch A Ride！”",
 "Say it once for me, man: \"Catch A Ride!\"": "替我说一次，老兄：“Catch A Ride！”",
 "Say it once for me, man. Y'know. The catchphrase?": "替我说一次，老兄。你知道。那句招牌口号？",
 "Don't be shy. I'm your sponsor now! Gotta hear how you do the catchphrase!":
    "别害羞。我现在是你的赞助商了！我得听听你的招牌口号怎么说！",
 "[Eager] Go on. Do it.": "[Eager] 来啊。说啊。",
 "Yeah... no. Nuh-uh. No. Not now.": "是啊……不。不不。不。不是现在。",
 "No? Alright. Well, I guess there's no harm in saving it for the real deal.":
    "不行？好吧。那，我想留到正戏再喊也没什么损失。",
 "[Sound it out] \"Catch aaa--?\"": "[Sound it out]“Catch 啊——？”",
 "[Sad, pouty] There's... nothing you can do for us?": "[Sad, pouty] 就……没什么你能为我们做的？",
 "I'll just improvise.": "我就临场发挥。",
 "I can charm him.": "我能迷住他。",
 "He's an easy mark.": "他是个好骗的肥羊。",
 "I'm Fiona. Sorry I was poking around.": "我是 Fiona。抱歉我到处乱翻。",
 "Not to be impolite or nothin' but you must've won a buttload of money from that race, right?":
    "不是想无礼什么的，但你从那场比赛里肯定赢了天大一笔钱，对吧？",
 "Where'd it all go?": "那些钱都去哪儿了？",
 "You'd be huge!": "你会红得不行！",
 "You'd be on cereal boxes, lunch boxes, men's boxes... other stuff that's not boxes!":
    "你会出现在麦片盒、午餐盒、男士礼盒……其他不在盒子上的东西上！",
 "[Beat] \"Catch-A-Riiiide?\" You know it, come on!":
    "[Beat]“Catch-A-Riiiide？”你知道的，来吧！",
 "Unless you hate Hollowpoint, in which case, like, I hate it too, right? I mean, burn it to the ground, right?":
    "除非你讨厌空心镇，那样的话，就，我也讨厌它，对吧？我是说，烧成灰，对吧？",
 "Aw that's cool, that's cool, I mean I thought so.":
    "哦酷，酷，我是说我也这么觉得。",
 "[Backpedaling] I mean, not that I thought you, like, looked like a cave dweller, just like, that Hollowpoint seems pretty awesome and you seem pretty awesome...":
    "[Backpedaling] 我是说，不是我觉得你，就，看起来像洞穴居民，只是，那个空心镇看着挺棒，而你看着也挺棒……",
 "So uh, you hang around in caves like these much?": "那呃，你经常待在这种洞穴里吗？",
 "...suuure?": "……当——然？",
 "I'ma stop talking now, ok?": "我现在不说了，好吗？",
 "Heyyy Fiona. Don't we": "嘿——Fiona。我们是不是",
 "[Ahem] Right. Fiona?": "[Ahem] 对。Fiona？",
 "Aw I'm really sorry Scooter I'm loving having this conversation but we really have to go.":
    "哦我真的很抱歉 斯库特，我很喜欢这场对话，但我们真的得走了。",
 "[More sweaty] I'm just thinking that maybe we could like drink a lunch or eat a beverage, shi- maybe, like, go shootin...":
    "[More sweaty] 我只是在想，也许我们可以，就，喝个午饭或者吃点饮料，或——也许，就，去打打枪……",
 "Oh alright alright we'll have to take a raincheck I guess.":
    "哦好，好，那我想我们只能改天了。",
 "[Creepy wink] But I'll be thinkin' about you every minute I'm under that hood.":
    "[Creepy wink] 但我在那个引擎盖下每一分钟都会想着你。",
 "[Very forced] Ha ha. Great.": "[Very forced] 哈哈。真好。",
 "[pickup2] How're you going to get him to do it?": "[pickup2] 你打算怎么让他答应？",
 "[Trying to be 'hip' and 'with it'] I'll just play it by ear. Duck and weave. Go with the flow.":
    "[Trying to be 'hip' and 'with it'] 我见机行事。闪躲腾挪。顺其自然。",
 "[Doubtful] Uh-huh.": "[Doubtful] 嗯哼。",
 "Oh please. This is ME doing this. Nothing I can't handle.":
    "哦拜托。干这事的人是我。没什么我搞不定的。",
 "He's a mark, just like any other, and every mark has their angle.":
    "他是个目标，跟别的没什么两样，而每个目标都有自己的门道。",
 "Find the angle, and they'll do whatever you want.":
    "找到那门道，他们就会照你想的做。",
 "And we definitely can not get out of here if we don't get this fixed.":
    "而要是修不好这个，我们绝对离不开这儿。",
 "I mean, I'm assuming it's not exactly a charity.":
    "我是说，我猜这不算什么慈善机构。",
 "Okay, don't get too cocky.": "好，别太自负。",
 "I guess that's true.": "我想那是真的。",
 "You can't just come into a man's garage and start pokin' around...":
    "你不能就这么进别人车库乱翻……",
 "Not to be impolite or nothin'... but you must've won a buttload of money from that race, right? Where'd it all go?":
    "不是想无礼什么的……但你从那场比赛里肯定赢了天大一笔钱，对吧？那些钱都去哪儿了？",
})

# —— 第 9 批：收尾补漏 ——
T.update({
 "[Awkward cough]": "[尴尬地咳嗽]",
 "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_7:-8><ui_cash_5:-8>":
    "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_7:-8><ui_cash_5:-8>",
 "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_1:-8><ui_cash_0:-8><ui_cash_0:-8>":
    "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_1:-8><ui_cash_0:-8><ui_cash_0:-8>",
 "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_2:-8><ui_cash_0:-8><ui_cash_0:-8>":
    "^imageColor:red^^imageScale:1.4^<ui_cash_dollar:-8><ui_cash_2:-8><ui_cash_0:-8><ui_cash_0:-8>",
 "[pickup2]  That race was insane.": "[pickup2]  那场比赛真是疯狂。",
 "[pickup2] Scooter's a fan of the races.  Good to know.":
    "[pickup2] 斯库特 是赛车的粉丝。这倒是个有用的情报。",
 "[pickup2] Rest in peace, Bossanova.": "[pickup2] 安息吧，Bossanova。",
 "[pickup2] I just hope that little deal you two struck is enough to get him to look the other way.":
    "[pickup2] 我只希望你们俩谈成的那笔小交易够让他睁一只眼闭一只眼。",
 "[pickup2]  Though, maybe pressing him for that extra cash wasn't the greatest idea.":
    "[pickup2]  不过，也许逼他多掏那笔钱不是什么好主意。",
 "[pickup2] He won't risk messing things up for his new star client.":
    "[pickup2] 他不会为了自己的新明星客户冒险把事情搞砸。",
 "[pickup2] [alt] I can't believe we made it....": "[pickup2] [alt] 我不敢相信我们活下来了……",
 "[pickup2] They seem like smart guys.": "[pickup2] 他们看着挺聪明的。",
 "[pickup2] ...probably.": "[pickup2] ……大概吧。",
 "[pickup2] [alt] You think the [guys'll] guys will be okay?":
    "[pickup2] [alt] 你觉得那[几个人]——那几位会没事吗？",
 "Call it a signing bonus.": "就当是签约奖金。",
 "[alt if we film] Need it for any sorta commercial stuff we're doin'.":
    "[alt if we film] 我们要拍什么商业广告之类的，得用上。",
 "Bossanova Poster": "Bossanova 海报",
 "Speedway Poster": "赛道海报",
 "Ugh. Does every mechanic have to be gross?": "呃。每个修车工都非得这么猥琐吗？",
 "This calendar is contributing to nothing being scheduled on this calendar.\n[alt]":
    "这本挂历对这本挂历上的任何日程安排都毫无贡献。\n[alt]",
 "Is that a huge wrench or a tiny woman? \n[alt]": "那是一把巨大的扳手，还是一个小个子的女人？ \n[alt]",
 "That must have been an uncomfortable photo shoot.\n[alt]":
    "那照片拍的时候一定很别扭。\n[alt]",
 "Scooter must have connections at Dahl corp.": "斯库特 在达尔公司肯定有关系。",
 "This looks pretty high-tech.": "这看着挺高科技。",
 "Catch-A-Ride": "Catch-A-Ride",
 "Puttin' wheels to dirt as your very life hangs in the balance?":
    "在性命悬于一线的时候把轮子往土里蹚？",
 "He said that his sister's friend's neighbor's husband won one of them races one time and the cash kept them fed for WEEKS.":
    "他说他妹妹的朋友的邻居的丈夫有一回赢了一场那种比赛，那笔钱让他们吃了好几个星期。",
 "Coupl'a commercials... Product placement...": "几支广告……产品植入……",
 "Hi, I'm Fiona.": "嗨，我是 Fiona。",
 "I need my caravan fixed.": "我需要修我的房车。",
 "I didn't mean to snoop.": "我不是有意偷翻的。",
 "Yep, that was me.": "对，就是我。",
 "Let's focus on those repairs.": "我们专心谈修理吧。",
 "You like Death Races?": "你喜欢死亡竞速？",
 "I told you to stay put.": "我叫你待着别动。",
 "Thank you, sis.": "谢谢你，妹妹。",
 "Felix's place isn't far.": "菲利克斯 那儿不远。",
 "We should stay put.": "我们该待着别动。",
 "No, we don't.": "不，我们不需要。",
 "Sorry I was poking around.": "抱歉我刚才到处乱翻。",
 "It's just not good business and {ShockA}I... [he trails off]":
    "这不合生意规矩，而且{ShockA}我……[he trails off]",
 "New proprieter?": "新老板？",
 "Nice place, Scooter.": "地方不错，斯库特。",
 "Can you just fix my ride?": "你能不能就修我的车？",
 "{ShockA}Aw crap man that girl is not looking too good. {WorryB}Least I'm assuming it wasn't designed with that whole, uh, \"hole\" thing, hah.":
    "{ShockA}哦操老兄，那姑娘看着不太妙。{WorryB}至少我猜它设计的时候没有那个，呃，“洞”，哈。",
})
