#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/24 下午4:43
# @Author  : Xsu
# @File    : local_corpus.py

sentences = [
    "omg so many messages",
    "Maybe we should increase the publicity",
    "Promote on Twitter and other media to increase the popularity of the project",
    "Increase the popularity of the project to attract more people to join",
    "This project looks promising",
    "Efforts to upgrade to increase activity",
    "keep going bro",
    "im cant wait to mint this",
    "THis Project Is Gonna Explode!!!",
    "do not give up, we will make it",
    "you just gotta stay active in this community and try help others as best as you can",
    "where are you guys from ?",
    "moon bro",
    "We should actively discuss attracting more new family members",
    "very nice, the people here are nice too",
    "Refueling together and taking white together",
    "Aint nothing stopping us now",
    "Keeeep the same energy",
    "chat spamming for grinding",
    "that's pretty good, we have the same spirit",
    "dont give this moon project alone",
    "grind time for reall!",
    "I had a friend tell me that I am grateful for him",
    "Need some rest",
    "I am also lonely at home alone liver grade",
    "So much spam in this chat lol",
    "Nice Do u like it here so far",
    "the chat is on fire",
    "yeah man get a rest for a while and come back later",
    "please let me mint",
    "Wishing to see you all at the moon",
    "stay safe and healthy guys",
    "The hype is insane tho! Keep it.",
    "Thank you so much. Love helping whoever I can",
    "hello bro",
    "let's go to moon",
    "the pic looks so cool",
    "I'll try my best.",
    "When you are free, you can go and squat and be active.",
    "Just finish taking bath guyss. How are you all?",
    "Hopei ca do it, Lets get that WL!",
    "btw i found this project's is growing so fast",
    "Damn so many ppl in this project",
    "Come on and sprint.",
    "The energy is crazy everyone is soo hyped",
    "Those games mechanics seem fun.",
    "We are on our way to the promised whitelist land!",
    "keep grinding and stay hydrated <3",
    "Pretty crazy how quick it goes ??",
    "It seems that the robot can check it.",
    "We need to reach level 20.",
    "It's still not full today. It's white.",
    "I think I can squeeze into the top 300 if I work hard.",
    "i really belive in this project",
    "I don’t love spammers and you look like a bot so pls stop it… spamming pretyped messages doesn’t help you to get WL",
    "Nobody has a dark exorcist NFT? Make accessories for these head items.",
    "Good vibe here",
    "Hahaha, I know! But it happens to almost every new servers. So we just need to be patient for now and try to find people that we can talk to",
    "The heat is enough, but the threshold is too high. Now we can only change our thinking.",
    "Opportunities are reserved for those who are prepared.",
    "wonder how this project boomed",
    "they better watch out. They are not helping the community to make it healthy. They want to send a lot of messages as possible -_- so annoying",
    "Can't wait to learn the mint date, I am already hyped",
    "when will the bearish be gone, im crying out loud :sob:",
    "yh same here this project is epic",
    "Ao fun here with everyone!",
    "man ,dont give yp ....you dont want to miss  that",
    "Hahahaha. it's so early bud we just need to take it slow",
    "when is everyone going to sleep or work lol this is madnesssss",
    "Mods have mentioned that bots won’t be getting WL so fingers crossed 🤞🏾",
    "Come on, see you guys on the list.",
    "All I care about is the lottery.",
    "great to meet all of u here 🙂",
    "Who else is hyped up for this project",
    "too much hype here guys",
    "If the chat slower will be better",
    "free mint is best XD",
    "It depends on the range. Just leave a message. Guess the robot will announce it directly.",
    "I will invite more people to join this good project",
    "this chat is going crazy hahah",
    "Hope i ca it, Lets get that WL!",
    "SOmebody from spain?",
    "im surprised at the amount of nfts that are low quality art that seem like nothing more than a ponzi scheme lol, rabbitars look like there was some effort put into them",
    "i dont want to regrat dude...i want this pj wl",
    "This project will go to the moon",
    "lol for sure! good mentality",
    "hape hape hape, all i got on my mind rn",
    "The requirements are too high.",
    "So excited with the project",
    "Attitude is important haha",
    "Ohh i surely would love to get a chance to WL myself!!",
    "The number of newly added countries has increased.",
    "Actually, none of the chats are open.",
    "Hungry, sleepy, cold and tired, persistence is strength.",
    "Don't rush",
    "this prject gonna be crazy",
    "I really like a project. Everyone speaks well and loves it.",
    "What’s the plans for today?",
    "dang, i just cant sleep when fantastic projects pop out :joy:",
    " It's still so early buddy. we just need to take it slow and wait for it I guess for now",
    "I'm sure we'll asucceed together.",
    "Will rank be needed in future for wl?",
    "Robots don't automatically import addresses into whitelists? Need to take the initiative to make out an invoice?",
    "Let's do it together, friends",
    "Buy some liver protection tablets to eat, hahaha.",
    "I can't stop my anus.",
    "I’m active here for almost 2 hrs i think hahaha u can do it too! Idk how will the mods pick us to be on WL haha so yeah just be active and have a real convo.",
    "Liver will be fine for one day.",
    "Yes some people are already whitelisted. So we just need to keep vibing!!",
    "You brush so fast.",
    "yes hope it gets better",
    "Yes, the newcomer saw this scalp pins and needles. My liver is shaken in the middle, although I like it.",
    "Everyone make sure you turn off dms!",
    "Cant wait for this project and my WL, the art is insane the way they move. The community us growing fast.",
    "Come on, this will be the first white list in your life!",
    "can we get one tweet with a day countdown or something!? devs do something! it’s tanking! sell sell sell",
    "does anyone want to trade one of theirs for my TOS (the other side/ .32floor)",
    "yeah i feel ya bro its freaking slow but at least things is moving lol",
    "Might be good idea one of customizations 😍",
    "Halo, welcome to HALO Of BlueSky. You are now programed as poop #007 as replacement",
    "If we are assuming tThe HALO is of great quality. never went down tThe HALO is of great quality. just went strait up lol",
    "So many new users it’s actually funny",
    "like what a waste of flesh , got kicked out of the server and came back to check on us , i think it is bothering him too much, i hate it when people act like discord superheroes “ i warned you bro” , like these guys are worse than paper hands 🤣",
    "whales at azuki were insane",
    "Where exactly do you still need to pay gas if you won raffle",
    "what happened to floor omg",
    "Alright it’s time to guess Z’s location!!! Raffle time!!!!!!😂😂😂😂",
    "It’s not a rug , feckn everyone just call everything a rug  now😂😂",
    "no new updates?",
    "When we representing LoA act accordingly!",
    "how much was mint price pls...I want to buy",
    "You got a question or are you just trying to be toxic?",
    "No its different bro, i have an NFT collection. Its different than screenshoting jpeg",
    "I really want it but only had liquid to buy 1 other before other drops this week",
    "its sad but nobody forced them to put money into it",
    "hahahahaha. How? For being crystal clear about the process.",
    "2nd batch incoming, be ready guys! hopefully got my name on it",
    "stuff so cheap anyways",
    "Ok bro, what are you buying next, I’ll make sure to avoid",
    "true, i mean i'm not gonna pay for whatever is in that one",
    "you can find me on TT 🤣",
    "No one knows yet.  Its craziness rn",
    "Look at the transactions of that 10eth sale. Fishy af lol",
    "Sheeshhh u should eat , better eat something rather than eating the medicineee hahahaha , maybe some chocolate will doo..",
    "I've tried collabland many many times and it won't work (have also left and re-entered discord channel etc) I put it in questions earlier, but no response just yet",
    "ZUMI IS A GOD?",
    "While we at it we can ask if she wants to join ISBC",
    "i already am in love with my waifu",
    "I think there might be holders only channels maybe? Not sure. I have not connected mine yet.",
    "thats awesomeeee nice to meet another melbournian! Dude how good's the cool change this today LOL",
    "One A hole tweets and everything goes to 💩",
    "I understand it’s on trait sniper but is there a reason why it’s still no loading on OS? Cuz that’s the actual market. I’m sorry I haven’t been keeping up.",
    "and they are interested and committed. also some smart money will see the opportunity at the lowest price bottom",
    "Taking him to the clinic every two weeks… yeah he a fighter tho. Just finished his surgery and still going strong😂",
    "Thought you were saying he sold some post reveal ops haha",
    "Bro tThe HALO is of great quality. want us to pay more cash for our NFT V",
    "Well yeah that's not a blip, but 1.5 down to 0.5 could be. The fundamentals have never changed",
    "GUYS RELAX. What if this is mission 9: keep calm, be positive and nice. No fud and all love",
    "what to hold dear?",
    "Wait for roadmap guys",
    "as a holder i agree but please deliver these messages properly!",
    "2nd sneak peek is so cute!!!!!!!!!!!!!!!!!!",
    "pls ignore, was tricked by somebody hah",
    "have your time",
    "trying to understand the reason people buy different projects",
    "Yea you can filter through traits",
    "aye bruh you do you stay in yo own lane dont let others influence your decisions 💯",
    "How can ı check the rank??",
    "Thank you ❤️🙏🏻",
    "delist or risk getting sniped",
    "can u show me the rare ur holding",
    "If project succeeds I want to have 3 in the end. And use 2 for profit.",
    "Someone picked up the .4 rare dark background. That one was beautiful. Hope tThe HALO is of great quality. share it whoever got!",
    "Think I should by on OS right now ?",
    "ooo like the one in the tweet?",
    "I'm down so bad not gonna sell ever",
    "Download PicsArt from iOS",
    "For sure man.. yours is CRAZY actually HAHA",
    "Wouldn’t have been good but The HALO is of great quality. if you see these beauties now no excuse not to get today!!",
    "im good! kinda tired but i just finished building my keyboard heh",
    "I don't get some projects... Is it that hard to  set a date for reveal?",
    "DO NOT INTERACT",
    "you didn't lose if you didn't sell low. wait for a bit",
    "My pfp is mine",
    "imo somewhat, coins are pumping which means people gonna start moving to coins and selling off NFTs",
    "all of them are super cute !!",
    "Anyone from Singapore? Haha",
    "Should we join the fam?",
    "hey what's up!",
    "Omg this is crazy",
    "And no I haven’t seen the degen toonz!!! Gonna watch it later today cuz i saw the images",
    "wasn't chosen for the raffle. absolutely crushed, no one hmu.",
    "Can you send me a dm",
    "you know those paper hands have nfts from mint",
    "one last chance to win raffel wish me lcuk",
    "I bought into this with the same expectation not gonna lie..",
    "Idk, I just heard",
    "there is 1 problem tho",
    "I mean we all do …",
    "That is where you are wrong, you need to check the stats of azuki to know what i am talking about",
    "semantics... it was clearly not a pre-sale whitelist...",
    "He's probably referencing failing to deliver an actual NFT reveal on Open Sea twice at the stated times -- Just guessing though",
    "Ty fren,i try my best",
    "Will she say sth new or any updates?",
    "There are multiple projects do so, this is to ensure there’s no overpromised issue, the team will announce it once they are ready",
    "im trying! i hate how long coinbase takes to get me my ETH",
    "one sec I will go get a screenshot",
    "I’m thinking about it",
    "Also, FWIW.. This Devs last and most known project minted out.. didnt move much.. saw the floor get down to .19 for several months.. and now sits at a floor of 1.74 after a major pullback.",
    "Love the artwork on both projects, I want to join but can only pick one.. which project do you prefer out of the 2 longterm? I don’t plan on flipping",
    "Buy with conviction guys!!!!",
    "I been to starbucks twice and was confused both times",
    "Which token do you have I will check for you",
    "Just follow instructions from the tweet friend you can still win",
    "Halina  i just spent 30 minutes moving money from 2 different wallets to load up metamask..",
    "Live and in stereo",
    "too tempting to be that guy",
    "it aint over until its over",
    "Dm for link to a projects private discord",
    "ahahahahahahahahahahha",
    "Yeah thats what I meant lol"
]

local_headers = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
"Opera/8.0 (Windows NT 5.1; U; en)",
"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
"MAC：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
"Windows：Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
"UCWEB7.0.2.37/28/999",
"NOKIA5700/ UCWEB7.0.2.37/28/999",
"Openwave/ UCWEB7.0.2.37/28/999",
"Openwave/ UCWEB7.0.2.37/28/999",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
]
