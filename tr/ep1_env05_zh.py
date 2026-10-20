# 批次3-12：第1章 env_05_prosperityjunction_rhys_atshades（Rhys 线：战后复盘 + 名人之厅 + ECHO 扫描资料）
import importlib.util as _ilu, os as _os
def _load(fn, name):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fn)
    s = _ilu.spec_from_file_location(name, p); m = _ilu.module_from_spec(s); s.loader.exec_module(m)
    return m.T
T = {}
for _f, _n in (('ep1_env18b_zh.py', '_a'), ('ep1_env19_zh.py', '_b'), ('ep1_env15_zh.py', '_c'),
               ('ep1_env18_zh.py', '_d'), ('ep1_env04_zh.py', '_e'), ('ep1_env11_zh.py', '_f'),
               ('ep1_env13_zh.py', '_g'), ('ep1_env12_zh.py', '_h'), ('ep1_env01_zh.py', '_i'),
               ('ep1_env09_zh.py', '_j'), ('ep1_env06_zh.py', '_k')):
    T.update(_load(_f, _n))

# —— 说话人 / 技术条目（保留原文）——
T.update({
 "SHADE": "SHADE",
 "RHYS": "RHYS",
 "VAUGHN": "VAUGHN",
 "AUGUST": "AUGUST",
 "SASHA": "SASHA",
 "FIONA": "FIONA",
 "STRANGER": "STRANGER",
 "ECHOCOMM": "ECHOCOMM",
 "LOADER": "LOADER",
 "<<ID": "<<ID",
 "{B9964747-9B21-4DEE-A9DE-B89D5FBDB517}>>": "{B9964747-9B21-4DEE-A9DE-B89D5FBDB517}>>",
 "{591E92FD-FA58-4BB4-B927-FBC24A59F099}>>": "{591E92FD-FA58-4BB4-B927-FBC24A59F099}>>",
 "Seated Man": "Seated Man",
})

# —— 战后复盘 + 抵达 Shade 处 ——
T.update({
 "{WorryA}[relieved sigh]": "{WorryA}[relieved sigh]",
 "[relieved sigh]": "[relieved sigh]",
 "{smugA}[relieved sigh]": "{smugA}[relieved sigh]",
 "[as his grandfather, Prof. Penumbra]": "[as his grandfather, Prof. Penumbra]",
 "[to himself]": "[to himself]",
 "[surprised shriek]": "[surprised shriek]",
 "[short shock sound]": "[short shock sound]",
 "[starts background of a song... Mike has an idea]": "[starts background of a song... Mike has an idea]",
 "[bitter; big breath] {ShockA} Okay.[beat] That. Sucked.":
    "[bitter; big breath] {ShockA} 好。[beat] 那。太。糟。了。",
 "{SternC}Nothing's worth getting killed over.": "{SternC}没什么值得拿命去换。",
 "{SternA}The key's not worth getting killed over.": "{SternA}那把钥匙不值得拿命去换。",
 "It was kinda fun.": "还挺好玩的。",
 "{SternB}\tWow, okay, uh, no. It didn't. At all.": "{SternB}\t哇，好吧，呃，不。一点都不好玩。",
 "{SmugA}\tAw c'mon. It was a little fun. Right?": "{SmugA}\t哎呀拜托。还算是有点好玩吧。对吧？",
 "{HappyA}\tYou cannot honestly stand there and tell me that it didn't feel kind of great to kick all those guys' asses.":
    "{HappyA}\t你不能站在那儿老实告诉我，把那些家伙全部揍趴下一点都不过瘾。",
 "They got what they deserved.": "他们罪有应得。",
 "{NeutralB} But let's just get this over with so we can go home.":
    "{NeutralB} 但我们把这了结吧，好回家。",
 "It's over now, we made it!": "现在结束了，我们成功了！",
 "[tired]{NeutralA} No, just... it happened, and it's done, and we're fine, okay? Cope faster.":
    "[tired]{NeutralA} 不，就……它发生了，已经结束了，我们没事，行吗？快点适应。",
 "{ShockA}Oh, I'm sorry, is my trying to cope with watching you turn a bunch of bandits inside out disturbing you?":
    "{ShockA}哦，抱歉，我尝试消化看着你把一群土匪翻个里朝外这件事，是不是打扰到你了？",
 "[annoyed]{AngryA} Yeah, no kidding, it sucked. I'm so glad I have you here to narrate.":
    "[annoyed]{AngryA} 是啊，没开玩笑，糟透了。真高兴有你在旁边解说。",
 "{NeutralB}Alright, let's just find this guy, August, buy the key and get the Hell out of here.":
    "{NeutralB}好，我们去找那个叫 August 的家伙，买下钥匙，然后赶紧滚出这儿。",
 "[out of breath] {FearA}If you had told me... I mean, if you had told me any of that... was even possible down here...":
    "[out of breath] {FearA}要是你告诉过我……我是说，要是你告诉过我这些……在这下面居然可能发生……",
 "{SternB}Man.": "{SternB}天哪。",
 "[chuckling]": "[chuckling]",
 "[light laughter]": "[light laughter]",
 "{SternB}Listen, we're here to make a deal, alright? We're buying a... thing. Something valuable.":
    "{SternB}听着，我们是来做交易的，行吗？我们要买一件……东西。很值钱的东西。",
 "{SternA}We're looking for a man named August.[beat] We're supposed to meet him here.":
    "{SternA}我们在找一个叫 August 的人。[beat] 我们该在这儿跟他碰头。",
 "{NeutralA}Uh, we're here to meet August.  You know him?":
    "{NeutralA}呃，我们是来见 August 的。你认识他？",
 "{AngryA}Oh, it's locked.": "{AngryA}哦，锁着。",
 "[annoyed] {AngryA}Oh come on, are you serious?": "[annoyed] {AngryA}哦拜托，你认真的？",
 "{ThinkA}This feels like we came in the back, so maybe there's a front door somewhere?":
    "{ThinkA}这感觉像是我们从后面进来的，也许哪儿有扇前门？",
 "{WorryA}\tYeah, I don't know if we can get out there with the murderers all over the place.":
    "{WorryA}\t是啊，我不知道能不能出去，到处都是杀人犯。",
 "{ThinkB}Maybe one of those bodies has a key or something and we just missed it.":
    "{ThinkB}也许哪具尸体上有把钥匙什么的，我们只是没看到。",
 "[muttering to himself]{AngryB} Wow, I mean if we just randomly found the key, I mean that would be amazing.":
    "[muttering to himself]{AngryB} 哇，我是说，要是我们随便就找到了钥匙，那岂不是太棒了。",
 "{ShockB}I mean, I--I never wanna see somebody's brains come out of their nose, not ever again.":
    "{ShockB}我是说，我——我再也不想看到谁的脑浆从鼻子里流出来，再也不想。",
 "{HappyA}Hi!": "{HappyA}嗨！",
 "{ShockB}[being startled] Ahh!": "{ShockB}[being startled] 啊！",
 "{ShockB}\t[being startled] Augh!": "{ShockB}\t[being startled] 啊呃！",
 "{NeutralA}Hey. Wait. wasn't there a-[gets cut off]":
    "{NeutralA}嘿。等等。不是有——[gets cut off]",
 "{HappyB}\tAre you two not just the handsomest devils I've seen in ages. [Laughs]":
    "{HappyB}\t你们俩真是我这么久以来见过最俊的小伙子。[Laughs]",
 "{AngryB}[pissed] Not great!": "{AngryB}[pissed] 不太好！",
 "[flustered]{AngryA} Asshole!": "[flustered]{AngryA} 混蛋！",
 "[angry]{AngryB} Yes, you! Asshole![beat] What do you think you're doing?":
    "[angry]{AngryB} 对，就是你！混蛋！[beat] 你以为你在干什么？",
 "[sighs] {NeutralB}Uh okay, so awes- so what are you, and who is going on?":
    "[sighs] {NeutralB}呃，好吧，那么——那么你是什么，还有这是怎么回事？",
 "{HappyA}\tThanks!": "{HappyA}\t谢谢！",
 "{HappyCX}\tI'm Shade, and this... is my World of Curiosities!":
    "{HappyCX}\t我是 Shade，这里……就是我的奇珍世界！",
 "[flustered]{AngryA} What--what is this, is this part of the-- like some kind of ride or something?":
    "[flustered]{AngryA} 什——这是什么，这是那个——是某种游乐项目之类的吗？",
 "{HappyB}\tTime can take a toll, you know. And on more things than one![light, sad laughter]":
    "{HappyB}\t时间会留下痕迹，你知道。而且不止体现在一件事物上！[light, sad laughter]",
 "{NeutralA}\tBut unfortunately we are closed for renovations.":
    "{NeutralA}\t但很遗憾我们在装修歇业。",
 "[laughs]{HappyB} Dead? No! No, no, no, no, asleep, maybe, dead, that's, you're-- you're getting ahead of yourself.":
    "[laughs]{HappyB} 死了？不！不不不不，是睡着了，也许，死了，那——你想太多了。",
 "[exasperated] {ShockA}Why are you pretending to be dead? Why?":
    "[exasperated] {ShockA}你干嘛要装死？为什么？",
 "{HappyC}\tLet me tell you right off the very bat, I am deeply sorry that you strapping young threshers of gentlemen here have to witness it in such sad disrepair.":
    "{HappyC}\t我一开始就得说，我非常抱歉让你们这两位健壮的年轻绅士看到它如此破败的样子。",
 "{HappyC}You're already here. We... we can just hang out.":
    "{HappyC}你们既然来了。我们……我们就一起玩玩嘛。",
 "{HappyB}I mean we can do other things.": "{HappyB}我是说，我们也可以干点别的。",
 "{HappyA}\tBut that doesn't mean you have to leave, of course, no.":
    "{HappyA}\t但那当然不代表你们得走，不。",
 "{AngryA}Don't do that!": "{AngryA}别那样！",
 "[being hit]{HappyC}Ah! Oh, okay, okay, I'm sorry, I didn't mean to scare you guys!":
    "[being hit]{HappyC}啊！哦，好，好，对不起，我不是故意吓你们的！",
 "{NeutralA}\t[Laughs] It just... it just happened, you know, things happen, they happen!":
    "{NeutralA}\t[Laughs] 它就……它就是发生了，你知道，事情会发生，它们就是会发生！",
 "{AngryB}Since the moment we walked in, it's been just been one big freaky puppet show, so I--[gets cut off]":
    "{AngryB}从我们进门那一刻起，就一直是场大怪诞木偶戏，所以我——[gets cut off]",
 "{SternA}Look, Shade, or whatever, just, stop wasting our time, alright. We're not here to see your weird zoo of death.":
    "{SternA}听着，Shade，或者随便你叫什么，别浪费时间了，行吗。我们不是来看你这怪异死亡动物园的。",
 "{NeutralA}\"Wasting time.\"[beat] \"No time to waste,\" \"Act now,\" \"Buy fast,\" \"We're digi-structing your future.\"":
    "{NeutralA}“浪费时间。”[beat] “别浪费时间”、“立即行动”、“快点买”、“我们正在数码构造你的未来”。",
 "{NeutralA}You're [stressing each syllable]Hyperion.[beat] Right? Here for August?":
    "{NeutralA}你们是[stressing each syllable]亥博龙。[beat] 对吧？来找 August 的？",
 "{HappyA}Yeah? If you wanna buy something strange and illegal, this is the certainly the place to do it!":
    "{HappyA}是啊？你要买奇怪又非法的东西，这儿绝对是对的地方！",
 "{NeutralA}I know a lot of things about a lot of things, and this thing in particular.":
    "{NeutralA}我对很多事情都懂很多，尤其是这件事。",
 "{NeutralA}You know anything about that?": "{NeutralA}你知道那是什么吗？",
 "{HappyB}\tOh, sure! Sure! Why didn't you say so, huh? You're late, actually.":
    "{HappyB}\t哦，当然！当然！你怎么不早说，啊？其实你们迟到了。",
 "{NeutralA}Yeah, we know.": "{NeutralA}是啊，我们知道。",
 "{NeutralA}How are you?": "{NeutralA}你好吗？",
 "[coughing fit]": "[coughing fit]",
 "{AngryA}Oh, c'mon!": "{AngryA}哦，拜托！",
 "{ThinkA}Looks like a, uh, looks kinda like a technical with legs. Right? The armored plates?":
    "{ThinkA}看起来像个，呃，像个长了腿的武装车。对吧？那些装甲板？",
 "{NeutralA}[uncaring] Ugh, does every animal on this planet have to look like a giant monster?":
    "{NeutralA}[uncaring] 呃，这星球上每种动物都非得长得像巨型怪物吗？",
 "[reading]{NeutralA} \"A common rakk. An active, strident and social creature. Particularly territorial during breeding season.\"":
    "[reading]{NeutralA} “常见的拉卡。一种活跃、聒噪且群居的生物。繁殖季尤其具有领地意识。”",
 "{NeutralB}What's not to like?": "{NeutralB}有什么理由不喜欢呢？",
 "{WorryB}[pickup1][hiding his anxiety] Or is he just happy to see us. [nervous, awkward laugh]":
    "{WorryB}[pickup1][hiding his anxiety] 还是他只是见到我们很高兴。[nervous, awkward laugh]",
 "{NeutralB}I think he has something in his pocket.": "{NeutralB}我觉得他口袋里有什么东西。",
 "{FearA}Ugh, there's gotta be some kind of... rule, about stealing from a dead guy.":
    "{FearA}呃，偷死人的东西总该有……什么规矩吧。",
 "{SmugA}There is, but I don't think his estate will complain.":
    "{SmugA}有，但我认为他的遗产继承人不会抱怨。",
 "[nervous]{WorryB} Nice fellow, huh.": "[nervous]{WorryB} 真是个好人，哈。",
 "{NeutralB}I was wondering why he didn't come to the company picnic...":
    "{NeutralB}我还在纳闷他怎么没来公司野餐……",
 "{NeutralB}Oh, I remember this guy, he was an asshole.":
    "{NeutralB}哦，我记得这家伙，他是个混蛋。",
 "[getting nervous]{WorryC} I am really not into this at all.":
    "[getting nervous]{WorryC} 我真的一点都不喜欢这个。",
 "{NeutralA}Can we just get on with this?": "{NeutralA}我们能快点办完吗？",
 "[not wanting to]{NeutralA} There's no where else to go. Come on, let's just get through it.":
    "[not wanting to]{NeutralA} 没别的地方可去了。来吧，我们就走过去吧。",
 "{WorryA}Alright, you know, the stuffed animals was one thing, but this is taking a turn I really don't want it to.":
    "{WorryA}好吧，你知道，那些填充动物就算了，但这正朝着我很不想去的方向转。",
 "{SadA}\t[big sigh]": "{SadA}\t[big sigh]",
 "[unnerved]{ShockA} Huh.": "[unnerved]{ShockA} 嗯。",
 "Not a great place for a first date, is it?": "首次约会来这儿可不太妙，对吧？",
 "Bullymong": "恶霸兽",
 "Rakk": "拉卡",
 "Bewm": "比姆",
 "Steele": "斯蒂尔",
 "Shade": "Shade",
 "Nakayama": "Nakayama",
 "No Shade?": "没有 Shade？",
 "{HappyB}<<id:361825687>>\tAre you two not just the handsomest devils I've seen in ages.":
    "{HappyB}<<id:361825687>>\t你们俩真是我这么久以来见过最俊的小伙子。",
 "{HappyC}<<id:361825703>>\tAnd let me tell you right off the very bat that I am deeply sorry that you strapping young threshers of gentlemen here have to witness it in such sad disrepair.":
    "{HappyC}<<id:361825703>>\t我一开始就得说，我非常抱歉让你们这两位健壮的年轻绅士看到它如此破败的样子。",
 "{HappyA}<<id:361825706>>\tBut that doesn't mean you have to leave, of course, oh no.":
    "{HappyA}<<id:361825706>>\t但那当然不代表你们得走，哦不。",
 "You're not dead?": "你没死？",
 "Stop wasting our time.": "别浪费我们时间了。",
 "We're here to make a deal.": "我们是来做交易的。",
 "We're looking for August.": "我们在找 August。",
 "Pick Up": "拾取",
 "Alright, let's just find this guy, August, buy the key...":
    "好，我们去找那个叫 August 的家伙，买下钥匙……",
 "{ShockB}...and get the {ThinkA}Hell out of here.":
    "{ShockB}……然后{ThinkA}赶紧滚出这儿。",
 "[tired sighs]": "[tired sighs]",
})

# —— ECHO 对话 + 扫尸取物 ——
T.update({
 "[pickup1] {SmugA} We'll never have to deal with crap like this [shows Vaughn the projection] ever again.":
    "[pickup1] {SmugA} 我们再也不用应付这种破事了[shows Vaughn the projection] 永远不会。",
 "[pickup1] {NeutralA} Vaughn, {SternA} I need your help [beat] {SternB} so I need you to handle this.":
    "[pickup1] {NeutralA} 沃恩，{SternA}我需要你帮忙[beat] {SternB}所以我需要你来处理这个。",
 "[pickup1] I'm serious, Rhys.  That was pretty heavy. I don't know if -- [gets cut off] I can handle this.":
    "[pickup1] 我是认真的，瑞斯。那事挺沉重的。我不知道——[gets cut off]我能不能应付得了。",
 "[pickup1] {HappyA}Good. {SlyA}Look we pull this off and we-- [gets cut off by the chime]":
    "[pickup1] {HappyA}好。{SlyA}听着，我们只要办成这事，我们就——[gets cut off by the chime]",
 "[pickup1] {ShockA} We...?": "[pickup1] {ShockA} 我们……？",
 "[pickup1] *We*.": "[pickup1] *我们*。",
 "[pickup1] {SlyB}Exactly.": "[pickup1] {SlyB}没错。",
 "[pickup1] {SlyC} We'll be the ones doing the billing and the indenturing and the terminating.":
    "[pickup1] {SlyC} 开账单、签契约、炒鱿鱼的人都将是我们。",
 "[pickup1][putting on a brave face] Let's go get rich.":
    "[pickup1][putting on a brave face] 我们去发财吧。",
 "[pickup1][putting on a brave face] Hyperion will kneel before us.":
    "[pickup1][putting on a brave face] 亥博龙会跪在我们面前。",
 "[pickup1][putting on a brave face] Fame and glory, meet your new masters.":
    "[pickup1][putting on a brave face] 名声与荣耀，来见见你们的新主人。",
 "[pickup1][putting on a brave face]Let's... try not to die.":
    "[pickup1][putting on a brave face]我们……尽量别死。",
 "[pickup1]": "[pickup1]",
 "[pickup1] {SmugC} Kinda like college all over again, huh? {SternB}Just... deathier.":
    "[pickup1] {SmugC} 有点像又回到大学了，哈？{SternB}只是……更容易死。",
 "[pickup1] {ThinkA} Can you do that... for me?": "[pickup1] {ThinkA} 你能为我……做那个吗？",
 "[pickup1] Now let's find this guy August, buy the key, and get the hell out of here.":
    "[pickup1] 现在我们去找那个叫 August 的家伙，买下钥匙，然后赶紧滚出这儿。",
 "[pickup1] I can try.": "[pickup1] 我可以试试。",
 "[pickup1] {SmugC}You and me, buddy.": "[pickup1] {SmugC}你和我，哥们。",
 "[pickup1][ALT] Out of the frying pan and into the preserves.":
    "[pickup1][ALT] 出了煎锅，进了果酱罐。",
 "[pickup1] Maybe we were better off outside.": "[pickup1] 也许我们待在外面还更好。",
 "[pickup1] Same as every other rule: don't get caught.":
    "[pickup1] 跟其他规矩一样：别被抓到。",
 "[pickup1][nervous] Who around here doesn't?": "[pickup1][nervous] 这附近谁不是呢？",
 "[pickup1][ALT] It's totally disrespectful do do something like this... [beat] to a fine, upstanding Hyperion employee.":
    "[pickup1][ALT] 对一位正直优秀的 亥博龙员工做这种事……[beat] 简直是大不敬。",
 "[pickup1] This planet just breeds insanity, doesn't it?":
    "[pickup1] 这星球就是专门繁殖疯子的，对吧？",
 "[pickup1]{AngryA}What... wha... {ThinkA}Who are you?":
    "[pickup1]{AngryA}什么……什……{ThinkA}你是谁？",
 "[pickup1] I just don't know if I can do this.": "[pickup1] 我只是不知道自己能不能做到。",
 "[pickup1] {SadA} I know this is a little... outside your comfort zone. [beat] {NeutralA}":
    "[pickup1] {SadA} 我知道这有点……超出你的舒适区。[beat] {NeutralA}",
 "[pickup1] {WorryA} Can we just skip right to the \u201cgo home\u201d part?":
    "[pickup1] {WorryA} 我们能直接跳到“回家”那一段吗？",
 "[pickup1][sympathetic] {ShockA} I know. It totally sucked. [beat] {SadA} I never wanna see anything like that again, either.":
    "[pickup1][sympathetic] {ShockA} 我知道。那糟透了。[beat] {SadA} 我也不想再看到那种东西了。",
 "[pickup1] {NeutralB} But we've come this far...": "[pickup1] {NeutralB} 但我们都走到这一步了……",
 "[pickup1] {SlyA} Which earns us an A... {WorryA} For \u201calmost killed\u201d.\nearB} You must be more traumatized than I am.":
    "[pickup1] {SlyA} 这能给我们打个 A……{WorryA} 因为“差点被杀”。\nearB} 你受的创伤肯定比我重。",
 "[pickup1] {AngryB} No witty rejoinder? You must be more traumatized than I am.":
    "[pickup1] {AngryB} 没有俏皮回嘴？你受的创伤肯定比我重。",
 "[pickup1] {SlyA}You and me and Yvette, of course.":
    "[pickup1] {SlyA}当然，还有你、我和 Yvette。",
 "[pickup1] [not joking] {AngryA}You need to work on your {SternB}motivational speaking.":
    "[pickup1] [not joking] {AngryA}你该练练你的{SternB}激励演讲。",
 "[pickup1] {SlyC}I meant the Royal We.": "[pickup1] {SlyC}我说的是皇家“我们”。",
 "[pickup1] {NeutralA}We... [beat]{SmugA} I like{SlyC} the sound of that.":
    "[pickup1] {NeutralA}我们……[beat]{SmugA} 我喜欢{SlyC}这个说法。",
 "{ShockA}...what do you mean by we?": "{ShockA}……你说“我们”是什么意思？",
 "{AngryA}I hope you mean...": "{AngryA}我希望你指的是……",
 "[dismissive of himself]{WorryB}Wait...what do you mean?":
    "[dismissive of himself]{WorryB}等等……你什么意思？",
 "We?": "我们？",
 "[pickup 3] [processed: speaker]Her leader-ness came to an end when she was skewered by a monstrous tentacle.":
    "[pickup 3] [processed: speaker]她那位“领袖”的人生，在一根巨型触手把她串起来时结束了。",
 "[pickup 3] [processed: speaker]The once ruthless leader of the Crimson Lance, Commandant Steele.":
    "[pickup 3] [processed: speaker]曾经冷酷无情的猩红长枪领袖，斯蒂尔指挥官。",
 "[pickup 3] [processed: speaker]She later died a second time after having been resurrected as some kind of cyborg zombie thing.":
    "[pickup 3] [processed: speaker]后来她被以某种赛博格僵尸的形态复活，然后又死了第二次。",
 "[pickup 3][processed: speaker]Even after all that she retains her porcelain like alabaster skin.":
    "[pickup 3][processed: speaker]即便如此，她仍保有那身瓷器般的雪花石膏肌肤。",
 "Open": "打开",
 "You and me, buddy.": "你和我，哥们。",
 "You, me and Yvette.": "你、我和 Yvette。",
 "I meant the Royal We.": "我说的是皇家“我们”。",
})

# —— ECHO 扫描：标本资料卡（保留 ^color: 标记）——
T.update({
 "color:#ffea7f^Alpha Skag Skull\nHeight: 1.75m\nLength: 3.9m\nWeight: 4,000lbs\nCause of death: Choked on a midget femur":
    "color:#ffea7f^首领异犬头骨\n身高: 1.75m\n体长: 3.9m\n体重: 4,000 磅\n死因: 被侏儒的股骨噎死",
 "^color:white^Spiderant Worker\n^color:#ffea7f^Likes: ^color:white^Its territory\n^color:#ffea7f^Dislikes: ^color:white^Things on its territory\n\nSpiderants are burrowing insects commonly found in areas of open ground which will attack anything that treads on their territory. Also many of them are racist and hate that restaurant you love.":
    "^color:white^蛛蚁工蚁\n^color:#ffea7f^喜欢: ^color:white^它的领地\n^color:#ffea7f^讨厌: ^color:white^它领地里的东西\n\n蛛蚁是穴居昆虫，常见于开阔地带，会攻击任何踩进它领地的东西。此外它们很多都种族歧视，还讨厌你最爱的那家餐厅。",
 "^color:#ffea7f^A Common Rakk\n^color:white^\n\"My neighbor gave me advice about Rakks one time. He said 'If you don't bother them, they won't bother you.' Know where that neighbor is now? He's F*CKING DEAD because a F*CKING RAKK TORE HIS HEAD OFF. BUY TORGUE AND MURDER THOSE MOTHERF*CKERS. PREEMPTIVE KILLING! WOO!.\" -Mister Torgue, CEO of Torgue":
    "^color:#ffea7f^常见拉卡\n^color:white^\n“我邻居有次给我讲拉卡的建议。他说‘你不招惹它们，它们就不招惹你。’知道那邻居现在在哪儿吗？他他妈的死了，因为一只他妈的拉卡把他的头撕了下来。买 TORGUE，干掉那群狗娘养的。先发制人！呜！。”——Torgue 先生，Torgue 公司 CEO",
 "^color:#ffea7f^Beer Bottles\n^color:#ffea7f^Brand: ^color:white^\"Stout At The Devil\"\n^color:#ffea7f^Ingredients:\n^color:white^-Alcohol\n-Yeast\n-Hops or something\n-[Classified]":
    "^color:#ffea7f^啤酒瓶\n^color:#ffea7f^品牌: ^color:white^“恶魔黑啤”\n^color:#ffea7f^配料:\n^color:white^-酒精\n-酵母\n-啤酒花之类的\n-[机密]",
 "Alpha Skag Skull\nHeight: 1.75m\nLength: 3.9m\nWeight: 4,000lbs\nCause of death: Choked on a midget femur":
    "首领异犬头骨\n身高: 1.75m\n体长: 3.9m\n体重: 4,000 磅\n死因: 被侏儒的股骨噎死",
 "^color:#ffea7f^Alpha Skag Head\n^color:#ffea7f^Height: ^color:white^1.75m\n^color:#ffea7f^Length: ^color:white^3.9m\n^color:#ffea7f^Weight: ^color:white^4,000lbs\n^color:#ffea7f^Cause of death: ^color:white^Choked on a midget femur":
    "^color:#ffea7f^首领异犬头\n^color:#ffea7f^身高: ^color:white^1.75m\n^color:#ffea7f^体长: ^color:white^3.9m\n^color:#ffea7f^体重: ^color:white^4,000 磅\n^color:#ffea7f^死因: ^color:white^被侏儒的股骨噎死",
 "^color:#ffea7f^Velvet Rope\n^color:#ffea7f^Material: ^color:white^Poly-cotton blend, synthetic linen core\n^color:#ffea7f^Weak against: ^color:white^Fire\n^color:#ffea7f^Effective against: ^color:white^Clumsy people":
    "^color:#ffea7f^天鹅绒隔离绳\n^color:#ffea7f^材质: ^color:white^涤棉混纺，合成亚麻芯\n^color:#ffea7f^弱于: ^color:white^火焰\n^color:#ffea7f^有效克制: ^color:white^笨手笨脚的人",
 "^color:#ffea7f^Arrow sign\n^color:#ffea7f^Materials: ^color:white^Plywood and white greasepaint\n^color:#ffea7f^Purpose: ^color:white^To point user in a pre-set direction\n^color:#ffea7f^Effectiveness: ^color:white^[Testing in progress]":
    "^color:#ffea7f^箭头指示牌\n^color:#ffea7f^材质: ^color:white^胶合板与白色油彩\n^color:#ffea7f^用途: ^color:white^把使用者指向预设方向\n^color:#ffea7f^有效性: ^color:white^[测试中]",
 "^color:#ffea7f^Vaughn\n^color:#ffea7f^Occupation: ^color:white^Accountant\n^color:#ffea7f^Underwear status: ^color:white^86% cotton, 7% soiled\n^color:#ffea7f^Favorite Color: ^color:white^Goldenrod\n^color:#ffea7f^Last book read: ^color:white^\"Mind the GAAP: Generally Accepted Accounting Principles and You\"":
    "^color:#ffea7f^沃恩\n^color:#ffea7f^职业: ^color:white^会计\n^color:#ffea7f^内裤状态: ^color:white^86% 棉，7% 已弄脏\n^color:#ffea7f^最喜欢的颜色: ^color:white^金菊黄\n^color:#ffea7f^最近读的书: ^color:white^“谨守 GAAP：公认会计原则与你”",
 "^color:#ffea7f^Badass Borok\n^color:#ffea7f^Continent of origin: ^color:white^Aegrus\n^color:#ffea7f^Weak point(s): ^color:white^Throat\n^color:#ffea7f^Strong point(s): ^color:white^Bloodthirsty Disposition, Positive Attitude":
    "^color:#ffea7f^狠角色博洛克\n^color:#ffea7f^原产大陆: ^color:white^埃格鲁斯\n^color:#ffea7f^弱点: ^color:white^喉咙\n^color:#ffea7f^强项: ^color:white^嗜血性格、积极心态",
 "^color:#ffea7f^Professor Penumbra\n^color:#ffea7f^Height: ^color:white^5'10\"\n^color:#ffea7f^Weight: ^color:white^143lbs\n^color:#ffea7f^Dead: ^color:white^Yes\n^color:#ffea7f^Professor: ^color:white^[Under Review]\n^color:#ffea7f^Famous Quotes: ^color:white^\"OH GOD WHY ARE YOU STABBING ME?!\"":
    "^color:#ffea7f^Penumbra 教授\n^color:#ffea7f^身高: ^color:white^5'10\"\n^color:#ffea7f^体重: ^color:white^143 磅\n^color:#ffea7f^已死亡: ^color:white^是\n^color:#ffea7f^教授资格: ^color:white^[审核中]\n^color:#ffea7f^名言: ^color:white^“我的天你为什么要捅我？！”",
 "^color:#ffea7f^Splorghuld the Flesh-Slayer\n^color:#ffea7f^Length: ^color:white^15m\n^color:#ffea7f^Width: ^color:white^4m\n^color:#ffea7f^Breath: ^color:white^Awful\n\nIt is said that certain rituals involving colored barrels can raise Splorghuld from its aquatic slumber to perform elaborate dance routines.":
    "^color:#ffea7f^屠肉者斯普洛古尔德\n^color:#ffea7f^体长: ^color:white^15m\n^color:#ffea7f^体宽: ^color:white^4m\n^color:#ffea7f^口气: ^color:white^极臭\n\n据说某些涉及彩色油桶的仪式能把斯普洛古尔德从水中沉睡中唤醒，表演精心编排的舞蹈。",
 "^color:#ffea7f^Loot crate\nContents:\n^color:white^-Endless potential\n-Disappointment\n-An utter lack of fulfillment\n-Old paperclip":
    "^color:#ffea7f^战利品箱\n内容物:\n^color:white^-无限可能\n-失望\n-彻底的空虚\n-一枚旧回形针",
 "RE: COMPANY PROPERTY DAMAGE\nTO: EMPLOYEE #8675309,\nYou are accountable for DAMAGE TO ONE LOADERBOT, for which you may BE FINED, \nINDENTURED, AND/OR TERMINATED.\nHave a great day!":
    "关于：公司财产损坏\n收件人：员工 #8675309，\n你须对损坏一台装载机器人负责，为此你可能被罚款、\n签订契约，和/或被解雇。\n祝你今天愉快！",
 "[postpax]No keys on this guy.": "[postpax]这家伙身上没钥匙。",
 "[poxtpax]So, I guess it's not gonna be that easy.": "[poxtpax]所以，我想这不会那么容易。",
 "[postpax]Couple of bucks.  Nothing else.": "[postpax]几块钱。没别的了。",
 "[poxtpax]Anything?": "[poxtpax]有什么吗？",
 "[postpax]Nada.": "[postpax]什么都没有。",
 "[postpax]Did you find the key?": "[postpax]你找到钥匙了吗？",
 "[postpax] [admiring the hi tech stuff he's just found] Nice.":
    "[postpax] [admiring the hi tech stuff he's just found] 不错。",
 "[postpax]No, but Nakayama was holding onto some nice bits of tech.  It's worth taking back to Hyperion.":
    "[postpax]没有，但 Nakayama 身上留了些不错的科技零件。值得带回 亥博龙。",
 "[embarased]Oops.": "[embarased]哎呀。",
 "Hey, he's still got his Hyperion ID chip.": "嘿，他还留着 亥博龙身份芯片。",
 "Really? Keep it!": "真的？留着它！",
 "[postpax]Well... that I don't need.": "[postpax]这个……我不需要。",
 "Ugh, His skin is, like, rotting with Eridium.": "呃，他的皮肤像是被镒矿腐蚀烂了。",
 "Skag Skull": "异犬头骨",
 "Spiderant": "蛛蚁",
 "Splorghuld": "斯普洛古尔德",
 "{worryA}Anything yet?": "{worryA}有什么发现吗？",
 "[while searching a body]{sterna} Look. No key.":
    "[while searching a body]{sterna} 看。没钥匙。",
 "{angryA}Of course I'm looking, I'm--": "{angryA}我当然在找，我——",
 "{sternA}No.  What about you, huh?  {thinkA}Are you even looking?":
    "{sternA}没有。那你呢，啊？{thinkA}你到底在找吗？",
 "{SlyB}Hyperion pays out a nice bonus for recovering those things.":
    "{SlyB}亥博龙回收这些东西给不错的奖金。",
 "{happyA}Oh, Nakayama still has his Hyperion ID drive with him though.":
    "{happyA}哦，不过 Nakayama 还随身带着他的 亥博龙身份芯片。",
 "[postpax] [alt] I'm starting to think I wanna skip straight to the going home part.":
    "[postpax] [alt] 我开始想直接跳到回家那一段了。",
 "[postpax] Let's just get this over with...": "[postpax] 我们把这了结吧……",
 "[postpax] Yes, okay. That was awful. I agree, but we got through it, you know, and that probably shouldn't have happened.":
    "[postpax] 是啊，好吧。那太糟了。我同意，但我们熬过来了，你知道，而那本来大概不该发生。",
 "[postpax] Yeah, that's what's upsetting me.": "[postpax] 是啊，就是这点让我不安。",
 "Okay... yeah... it was a little... awesome.": "好吧……是啊……确实有点……爽。",
 "We're probably gonna need some therapy in the future, you know that, right?":
    "我们以后大概得看点心理医生，你知道的吧？",
 "But I'm sure it was as traumatic as it was fun.": "但我敢说它有多好玩就有多创伤。",
 "[a little traumatize] I... I can't believe we're alive.":
    "[a little traumatize] 我……我不敢相信我们还活着。",
 "That... that was the single scariest experience... of my entire life!":
    "那……那是我这辈子……最吓人的一次经历！",
 "[postpax] We'll be able to afford it.": "[postpax] 我们付得起。",
 "[postpax] but it's not... for some reason... but for those guys... a lot of those guys...":
    "[postpax] 但不是……不知为什么……但对那些家伙……他们很多人……",
 "[postpax] it is...": "[postpax] 是……",
 "[postpax] Which... should probably be over by now...": "[postpax] 那……现在大概该结束了……",
 "[postpax] Well... I guess that's just a little more nightmare fuel to keep me going.":
    "[postpax] 这个……我想这又给我添了点做噩梦的燃料，好让我继续撑下去。",
 "[postpax] It's over now. We made it.": "[postpax] 现在结束了。我们成功了。",
 "If what, if brains ooze out of people's noses?": "什么，脑浆从别人鼻子里流出来那种？",
 "[postpax] At least now we know we can handle ourselves if--":
    "[postpax] 至少现在我们知道，要是——我们能应付得了。",
 "[postpax] I guess you... sort of have a point... somewhere in there.":
    "[postpax] 我想你……大概有点道理……藏在那堆话里。",
 "[postpax] [beat] W--Yeah, basically.": "[postpax] [beat] 什——对，基本上。",
 "[traumatic] I mean his... brains... just... just like, like snot...":
    "[traumatic] 我是说他……脑浆……就……就像，像鼻涕一样……",
 "[postpax] Maybe next time they'll think twice before--":
    "[postpax] 也许下次他们动手前会多想一下——",
 "[postpax] They're not thinking anything. I told you, I saw their brains.":
    "[postpax] 他们什么都没想了。我跟你说过，我看到了他们的脑浆。",
 "[postpax] Look, they got what they deserved. They attacked us.":
    "[postpax] 听着，他们罪有应得。是他们袭击我们的。",
 "[postpax] Yeah, I heard you.": "[postpax] 是啊，我听见了。",
 "Weapon": "武器",
 "Dead Guy's Arm": "死人的手臂",
 "Dead Guy's Pocket Bulge": "死人口袋里的鼓包",
 "^color:#ffea7f^Rotting Arm contains Eridium:\n^color:white^- Alien mineral\n- Used frequently in weapons processing":
    "^color:#ffea7f^腐烂的手臂上含有镒矿：\n^color:white^- 外星矿物\n- 常用于武器加工",
 "^color:#ffea7f^Pocket Bulge contains Scientific vials:\n^color:white^- Unknown origin.\n- Unknown taste.\n- Unpleasant aroma.":
    "^color:#ffea7f^口袋鼓包里是科学试剂瓶：\n^color:white^- 来源不明。\n- 味道不明。\n- 气味难闻。",
 "^color:red^PORTABLE ID DRIVE DETECTED\n^color:white^Neuron-Linked Cannon\n^color:#ffea7f^Weapon Type: ^color:white^Slag\n^color:#ffea7f^GenID: ^color:white^ Prof. Nakayama\n^color:#ffea7f^Modifications: ^color:white^Self-Inflicted\n\n\"Crazy, am I? Tell it to the robot gun arm on my spine!\"\n-Professor Nakayama, Crazy Person":
    "^color:red^检测到便携身份芯片\n^color:white^神经链接炮\n^color:#ffea7f^武器类型: ^color:white^残渣\n^color:#ffea7f^持有者ID: ^color:white^ Nakayama 教授\n^color:#ffea7f^改装: ^color:white^自行实施\n\n“我疯了？那你跟我脊背上这条机器人枪臂说去！”\n——Nakayama 教授，疯子",
 "^color:#ffea7f^'Big Ole Head Limerick' by Edwin Gabshite\n^color:white^In Crossroads there once was a man\n^color:white^ And if I add the rest, Tulley will yell at me\n^color:white^Temporary text! DELETE ME ASAP, YO!\n\n<<id:361826282>>^color:#ffea7f^Badass Borok\n^color:#ffea7f^Continent of origin: ^color:white^Aegrus\n^color:#ffea7f^Weak point(s): ^color:white^Throat\n^color:#ffea7f^Strong point(s): ^color:white^Bloodthirsty Disposition, Positive Attitude":
    "^color:#ffea7f^“大脑袋打油诗”——Edwin Gabshite 作\n^color:white^十字路口曾有一个男人\n^color:white^ 要是我把剩下的补上，Tulley 会骂我\n^color:white^临时文本！尽快删掉我，喂！\n\n<<id:361826282>>^color:#ffea7f^狠角色博洛克\n^color:#ffea7f^原产大陆: ^color:white^埃格鲁斯\n^color:#ffea7f^弱点: ^color:white^喉咙\n^color:#ffea7f^强项: ^color:white^嗜血性格、积极心态",
 "^color:#ffea7f^Grenade\n^color:#ffea7f^Status: ^color:white^Deactivated*\n^color:#ffea7f^Grenade Damage: ^color:white^2050\n^color:#ffea7f^Blast Radius: ^color:white^312\n^color:#ffea7f^Fuse Time: ^color:white^3.2\n\n*Unconfirmed":
    "^color:#ffea7f^手雷\n^color:#ffea7f^状态: ^color:white^已解除*\n^color:#ffea7f^手雷伤害: ^color:white^2050\n^color:#ffea7f^爆炸半径: ^color:white^312\n^color:#ffea7f^引信时间: ^color:white^3.2\n\n*未证实",
 "^color:#ffea7f^\"Cigarette Holder\"\n^color:white^A DIY fancy accessory\n^color:#ffea7f^Owner: ^color:white^Shade\n^color:#ffea7f^Manufacturer: ^color:white^Shade\n^color:#ffea7f^Materials: ^color:white^Firecracker, stick, fear":
    "^color:#ffea7f^“烟嘴”\n^color:white^一件自制的花哨配件\n^color:#ffea7f^所有者: ^color:white^Shade\n^color:#ffea7f^制造商: ^color:white^Shade\n^color:#ffea7f^材质: ^color:white^鞭炮、木棍、恐惧",
 "^color:#ffea7f^Brain Case\n^color:white^Probably used to contain organs.\n^color:#ffea7f^Contents: ^color:white^Nothing. It's a hole.":
    "^color:#ffea7f^脑容器\n^color:white^大概原本是用来装器官的。\n^color:#ffea7f^内容物: ^color:white^什么都没有。就是个洞。",
 "^color:#ffea7f^Rakk\n^color:white^-Carnivorous (Exclusively)\n-Hunts living prey (Obsessively)\n-Clings to cave walls and cliff faces (Tenderly)":
    "^color:#ffea7f^拉卡\n^color:white^-肉食（只吃肉）\n-捕猎活物（痴迷地）\n-紧贴洞穴与崖壁（温柔地）",
 "^color:#ffea7f^Professor Penumbra\n^color:#ffea7f^Height: ^color:white^5'10\"\n^color:#ffea7f^Weight: ^color:white^143lbs\n^color:#ffea7f^Dead: ^color:white^Yes\n^color:#ffea7f^Professor: ^color:white^No\n^color:#ffea7f^Famous Quotes: ^color:white^\"OH GOD WHY ARE YOU STABBING ME?!\"":
    "^color:#ffea7f^Penumbra 教授\n^color:#ffea7f^身高: ^color:white^5'10\"\n^color:#ffea7f^体重: ^color:white^143 磅\n^color:#ffea7f^已死亡: ^color:white^是\n^color:#ffea7f^教授资格: ^color:white^没有\n^color:#ffea7f^名言: ^color:white^“我的天你为什么要捅我？！”",
 "^color:#ffea7f^Spiderant\n^color:white^-Highly territorial\n-Thick armor on head and forelimbs\n-Doesn't \"do\" hugs":
    "^color:#ffea7f^蛛蚁\n^color:white^-领地意识极强\n-头部与前肢有厚甲\n-不“来”拥抱这套",
 "^color:#ffea7f^Bullymong\n^color:white^\"Twice the arms for twice the fun,\nBullymongs are the pet for everyone!\"\n-Lyrics to \"The Bullymong Jingle\" by Horace Blitsmith, Head of Marketing (Exotic Pets Division) [DECEASED]":
    "^color:#ffea7f^恶霸兽\n^color:white^“两条手臂双倍乐趣，\n恶霸兽是人人适合的宠物！”\n——“恶霸兽小调”歌词，Horace Blitsmith 作，市场部主管（异宠事业部）[已故]",
 "^color:#ffea7f^Splorghuld the Flesh-Slayer\n^color:#ffea7f^Length: ^color:white^15m\n^color:#ffea7f^Width: ^color:white^4m\n^color:#ffea7f^Breath: ^color:white^Awful":
    "^color:#ffea7f^屠肉者斯普洛古尔德\n^color:#ffea7f^体长: ^color:white^15m\n^color:#ffea7f^体宽: ^color:white^4m\n^color:#ffea7f^口气: ^color:white^极臭",
 "^color:#ffea7f^'Big Ole Head Limerick' by Edwin Gabshite\n^color:white^In Crossroads there once was a man\n^color:white^ And if I add the rest, Tulley will yell at me\n^color:white^Temporary text! DELETE ME ASAP, YO!":
    "^color:#ffea7f^“大脑袋打油诗”——Edwin Gabshite 作\n^color:white^十字路口曾有一个男人\n^color:white^ 要是我把剩下的补上，Tulley 会骂我\n^color:white^临时文本！尽快删掉我，喂！",
 "[Smack Him]": "[扇他一巴掌]",
 "^color:white^A Common Rakk\n^color:#ffea7f^Diet: ^color:white^Meat (Any, all)\n^color:#ffea7f^Social Structure: ^color:white^Hive-based\n^color:#ffea7f^Natural defenses:\n^color:white^-Curved talons*\n-Hooked barbs*\n-Mean thoughts**\n\n*Deadly\n**Less deadly, but still pretty mean":
    "^color:white^常见拉卡\n^color:#ffea7f^食性: ^color:white^肉（什么都吃，全部吃）\n^color:#ffea7f^社会结构: ^color:white^蜂巢式\n^color:#ffea7f^天然防御:\n^color:white^-弯曲利爪*\n-带钩倒刺*\n-恶毒念头**\n\n*致命\n**没那么致命，但还是很恶毒",
 "^color:white^Bullymong (Killed in Frozen Wastes)\n^color:#ffea7f^Intelligence: ^color:white^Low\n^color:#ffea7f^Speed: ^color:white^Fast enough\n^color:#ffea7f^Strength: ^color:white^F*%#ing high\n\n\"Twice the arms for twice the fun,\nThey're the pet for everyone!\"\n-\"The Bullymong Jingle\" by Horace Blitsmith (Marketing, Exotic Pets)":
    "^color:white^恶霸兽（死于冰封荒原）\n^color:#ffea7f^智力: ^color:white^低\n^color:#ffea7f^速度: ^color:white^够快\n^color:#ffea7f^力量: ^color:white^他*%# 的高\n\n“两条手臂双倍乐趣，\n它们是人人适合的宠物！”\n——“恶霸兽小调”，Horace Blitsmith 作（市场部，异宠）",
 "^color:#ffea7f^Name: ^color:white^Professor Penumbra\n^color:#ffea7f^Hometown: ^color:white^Oasis\n^color:#ffea7f^Height: ^color:white^5'10\"\n^color:#ffea7f^Weight: ^color:white^143lbs\n^color:#ffea7f^Current Status: ^color:white^Stuffed and mounted\n^color:#ffea7f^Cause of death: ^color:white^Stabbing\n^color:#ffea7f^Last words: ^color:white^\"What're you gonna do? Stab me?\"":
    "^color:#ffea7f^姓名: ^color:white^Penumbra 教授\n^color:#ffea7f^家乡: ^color:white^绿洲镇\n^color:#ffea7f^身高: ^color:white^5'10\"\n^color:#ffea7f^体重: ^color:white^143 磅\n^color:#ffea7f^当前状态: ^color:white^已制成标本并挂起\n^color:#ffea7f^死因: ^color:white^被捅死\n^color:#ffea7f^遗言: ^color:white^“你能把我怎么样？捅我？”",
 "^color:white^Incendiary Grenade\n^color:#ffea7f^Status: ^color:white^Deactivated*\n^color:#ffea7f^Grenade Damage: ^color:white^2050\n^color:#ffea7f^Blast Radius: ^color:white^312\n^color:#ffea7f^Fuse Time: ^color:white^3.2\n\n*Unconfirmed":
    "^color:white^燃烧手雷\n^color:#ffea7f^状态: ^color:white^已解除*\n^color:#ffea7f^手雷伤害: ^color:white^2050\n^color:#ffea7f^爆炸半径: ^color:white^312\n^color:#ffea7f^引信时间: ^color:white^3.2\n\n*未证实",
 "^color:white^A DIY fancy accessory\n^color:#ffea7f^Owner: ^color:white^Shade\n^color:#ffea7f^Manufacturer: ^color:white^Shade\n\nFor the man who wants to feel fancy without sacrificing that certain \"Je ne suis pas sain d'esprit\" quality.":
    "^color:white^一件自制的花哨配件\n^color:#ffea7f^所有者: ^color:white^Shade\n^color:#ffea7f^制造商: ^color:white^Shade\n\n献给那种想显得讲究、又不愿舍弃那份“我神志不清”气质的男人。",
 "^color:white^The Brain of Commandant Steele\n^color:#ffea7f^Composition: ^color:white^Military grade carbon nanotube polymer.\n^color:#ffea7f^Contents: ^color:white^A brain (Still includes \"augmentation\" by I.N.A.C.)":
    "^color:white^斯蒂尔指挥官的脑\n^color:#ffea7f^成分: ^color:white^军规级碳纳米管聚合物。\n^color:#ffea7f^内容物: ^color:white^一颗脑（仍包含 I.N.A.C. 的“强化”）",
 "^color:white^Alpha Skag\n^color:#ffea7f^Diet: ^color:white^Literally anything\n^color:#ffea7f^Habitat: ^color:white^Wherever it wants\n^color:#ffea7f^Weak Points: ^color:white^Good luck\n\nExistence of Alpha Skags indicates that there is a certain hierarchy in skag social structure; one in which the biggest jerks apparently boss everyone else around.":
    "^color:white^首领异犬\n^color:#ffea7f^食性: ^color:white^字面意义上的任何东西\n^color:#ffea7f^栖息地: ^color:white^它想待的任何地方\n^color:#ffea7f^弱点: ^color:white^祝你好运\n\n首领异犬的存在说明异犬社会有一定等级结构；在这个结构里，显然是最混蛋的那个在指挥所有人。",
 "Giant Bug Head": "巨型虫头",
 "Incendiary Grenade": "燃烧手雷",
 "Firecracker": "鞭炮",
 "Steele's Brain Tube": "斯蒂尔的脑管",
 "^color:white^Badass Borok\n^color:#ffea7f^Continent of origin: ^color:white^Aegrus\n^color:#ffea7f^Weak point(s): ^color:white^Throat\n^color:#ffea7f^Strong point(s): ^color:white^Bloodthirsty Disposition, Positive Attitude\n\nHunting Boroks is best avoided by small children, the elderly, and anyone with a heartbeat. Seriously. Just run. They are not even tasty.":
    "^color:white^狠角色博洛克\n^color:#ffea7f^原产大陆: ^color:white^埃格鲁斯\n^color:#ffea7f^弱点: ^color:white^喉咙\n^color:#ffea7f^强项: ^color:white^嗜血性格、积极心态\n\n猎杀博洛克这件事，小孩、老人，以及任何还有心跳的人都最好别尝试。说真的，跑就对了。它们连好吃都算不上。",
 "^color:white^Pocket Bulge\n^color:#ffea7f^Contents: ^color:white^Scientific Vials\n^color:#ffea7f^Composition: ^color:white^Science-y\n^color:#ffea7f^Alignment: ^color:white^Chaotic Neutral\n^color:#ffea7f^Taste: ^color:white^Nasty":
    "^color:white^口袋鼓包\n^color:#ffea7f^内容物: ^color:white^科学试剂瓶\n^color:#ffea7f^成分: ^color:white^很科学\n^color:#ffea7f^阵营: ^color:white^混乱中立\n^color:#ffea7f^味道: ^color:white^恶心",
 "^color:#CC1919^Foreign Contaminant Detected\n^color:#ffea7f^Analysis: ^color:#CC1919^Eridium\n^color:white^-Alien mineral\n-Used frequently in weapons processing\n-Do not eat or use in coffee":
    "^color:#CC1919^检测到外来污染物\n^color:#ffea7f^分析: ^color:#CC1919^镒矿\n^color:white^-外星矿物\n-常用于武器加工\n-请勿食用或加入咖啡",
 "^color:white^Vaughn\n^color:#ffea7f^Age: ^color:white^27\n^color:#ffea7f^Hyperion Employee ID: ^color:white^RM-9452\n^color:#ffea7f^Occupation: ^color:white^Accountant\n^color:#ffea7f^Favorite Color: ^color:white^Goldenrod\n^color:#ffea7f^Favorite Book: ^color:white^\"Mind the GAAP: Generally-Accepted Accounting Principles and You!\"\n\n^color:#ffea7f^Underwear Status: ^color:white^Mildly Soiled":
    "^color:white^沃恩\n^color:#ffea7f^年龄: ^color:white^27\n^color:#ffea7f^亥博龙员工编号: ^color:white^RM-9452\n^color:#ffea7f^职业: ^color:white^会计\n^color:#ffea7f^最喜欢的颜色: ^color:white^金菊黄\n^color:#ffea7f^最喜欢的书: ^color:white^“谨守 GAAP：公认会计原则与你！”\n\n^color:#ffea7f^内裤状态: ^color:white^轻微弄脏",
 "^color:white^Rotting Arm\n^color:#ffea7f^Foreign Contaminant Detected\n^color:#ffea7f^Analysis: ^color:white^Eridium\n^color:white^-Alien mineral\n-Used frequently in weapons processing\n-Despite best attempts, does not work as male enhancement":
    "^color:white^腐烂的手臂\n^color:#ffea7f^检测到外来污染物\n^color:#ffea7f^分析: ^color:white^镒矿\n^color:white^-外星矿物\n-常用于武器加工\n-尽管多方尝试，并不具备男性功能增强效果",
 "^color:white^Neuron-Linked Cannon\n^color:#ffea7f^Weapon Type: ^color:white^Slag\n^color:#ffea7f^GenID: ^color:white^ Prof. Nakayama\n^color:#ffea7f^Modifications: ^color:white^Self-Inflicted\n\n\"Oh yeah? Well would a crazy person attach a robot gun arm to their spine?!\"\n-Professor Nakayama, Crazy Person":
    "^color:white^神经链接炮\n^color:#ffea7f^武器类型: ^color:white^残渣\n^color:#ffea7f^持有者ID: ^color:white^ Nakayama 教授\n^color:#ffea7f^改装: ^color:white^自行实施\n\n“哦是吗？那疯子会往自己脊背上装一条机器人枪臂吗？！”\n——Nakayama 教授，疯子",
 "Professor Penumbra": "Penumbra 教授",
})

# —— 补漏：键里含 ASCII 双引号的两条 ——
T.update({
 "[pickup1] {WorryA} Can we just skip right to the \"go home\" part?":
    "[pickup1] {WorryA} 我们能直接跳到“回家”那一段吗？",
 "[pickup1] {SlyA} Which earns us an A... {WorryA} For \"almost killed\".\nearB} You must be more traumatized than I am.":
    "[pickup1] {SlyA} 这能给我们打个 A……{WorryA} 因为“差点被杀”。\nearB} 你受的创伤肯定比我重。",
})
