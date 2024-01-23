from random import choice, randint, random

#Checks if a string is in source
def analysis(ogStr: str) -> str:
    if '<@&732688521831383081>' in ogStr:
        return 'briananime'
    elif '<@&1192175976663232582>' in ogStr:
        return 'brianlethalcompany'
    elif '<@&694717398678372394' in ogStr:
        return 'briansmash'
    elif 'work' in ogStr:
        return 'work'
    elif 'jewel' in ogStr:
        return 'work'
    elif '<@436655054196441128>' in ogStr:
        return 'matt'
    elif 'test ' in ogStr:
        return 'test'
    elif '<@&908554913024466996>' in ogStr:
        return 'brianclash'
    else:
        return ogStr

#Returns based on the input of the message it reads in Sans Mains
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    lowered = analysis(lowered)
    
    
    match lowered:
        case 'skibidi':
            return 'Toilet'
        case 'what is the best state?':
            return 'Ohio'
        case 'gyatt':
            return 'Stick your gyatt out for the rizzler'
        case 'digitalcircus':
            randno = randint(0,2)
            match randno:
                case 0:
                    return 'Alright today, we are doing the digital circus challenge so lets see if we can do watch it in French!'
                case 1:
                    return 'WHAT IS UP YOUTUBE! Today we are seeing if we can watch all of the new SMG4 before Bbop gets on Lethal Company!'
                case 2:
                    return 'Digital Circus MID.  SMG4 & Hazbin Hotel PEAK'
        case 'garten of banban':
            return 'garten of peakpeak'
        case 'briansmash':
            #Roll the Dice
           randno = randint(0,3)
           match randno:
               case 0:
                   return 'https://media.discordapp.net/attachments/766027094944645153/1196951444419514529/Brian_Smash_Time_Down.jpg?ex=65b97ee6&is=65a709e6&hm=f2226b6aa85b18c452b2b242310badafde77dc2a8837242c82546cef9920325b&=&format=webp&width=623&height=662'
               case 1:
                   return 'https://media.discordapp.net/attachments/766027094944645153/1196951444708925460/Brian_Smash_Time_Left.jpg?ex=65b97ee6&is=65a709e6&hm=e1badc56169ec024a544683309f490e0c0a24c5cc87855f987bd063859025e3c&=&format=webp&width=623&height=662'
               case 2:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1196951444985757716/Brian_Smash_Time_Right.jpg?ex=65b97ee6&is=65a709e6&hm=4b2648904145ac63f3394b40fa9822f640821133644d28ce7916a84c22636afb&'
               case 3:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1196951445275152434/Brian_Smash_Time_Up.jpg?ex=65b97ee6&is=65a709e6&hm=5b48b5dc28107234bb59938b1685460cb82758740e901a3cee9c7ac903622df7&'
        case 'brianlethalcompany':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196946708052050072/Brian_Lethal_Time_2.jpg?ex=65b97a7d&is=65a7057d&hm=74e5870d014d1790f898df9704d3ec0fb5ba4cfbcac2ca89c59b974800bd50b0&'
        case 'briananime':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196962782235598900/Brian_Anime_Time2.jpg?ex=65b98975&is=65a71475&hm=f638ee432ba450fe46a1a25c0a721d724d1399d6943223af1243e1cdd99e3693&'
        case 'brianclash':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196943195674791936/Brian_Clash_Time2.jpg?ex=65b97737&is=65a70237&hm=bf439357d726620cfcd6d2d17fcbb06767149f0ebed8b2d5bb7496302ecd76be&'
        case 'work':
            randno = randint(0,30)
            match randno:
                case 0:
                    return 'I am currently working til unix.MaxValue so call me until then'
                case 1:
                    return 'I will get on at around 11:00 and by 11:00.  I actually mean 12:32 the next day. :D'
                case 2:
                    return 'I am working the night shift as Charles Entertainment Cheeses Restaurant'
                case 3:
                    return 'The Jewel Osco Manager is asking me for 29 hours of overtime. BRB'
                case 4:
                    return 'A fat vietnamese teenager just arrived at the Jewels so I have to make sure he is not stealing stuff'
                case 5:
                    return 'I am currently traveling to Indiana for that extra overtime bonus.'
                case 6: 
                    return 'Jewel Osco Just gave me a promotion.  I am now the Manager for every department.  My payment is now 15.50 per hour'
                case 7:
                    return 'I used my employee discount to buy a google play gift card for 5 percent off for clash royale'
                case 8:
                    return 'Thang keeps calling me at my workplace.  I have been working for the past 128 hours and this kid wants to hangout like wtf'
                case 9:
                    return 'I can not wait to get off of the clock to play a videogame where we go on the clock.'
                case 10: 
                    return 'My life goal is to become the next Little Z.  Hopefully I can'
                case 11:
                    return 'I just bought the steve dlc for smash 5.  I deserve to win every game now : D'
                case 12: 
                    return 'My Jewels is now hiring guys.  Please go to our website for more information!'
                case 13:
                    return 'I just caught someone pissing in the brocolii in the vegetable section. WTF'
                case 14: 
                    return 'I really hope I can get a promotion to be a senior manager for the deli department.  I really like the meats'
                case 15:
                    return 'These jewel osco employees do not realize I am actually an accounting major'
                case 16:
                    return 'Honestly, Target is just a better store not gonna lie. #NotSponsered #TotallySponsered'
                case 17:
                    return 'I am really excited to try Honkai Star Rail.  Oh wait my phone from 2001 keeps crashing wtf'
                case 18:
                    return 'Jewel Osco actually is a great place for medicine! Highly recommend 10/10'
                case 19:
                    return 'I cannot wait to get off of the clock to play a video game where I am on the clock :D'
                case 20:
                    return 'This message has been censored and removed by Albertsons, American Stores, and Jewel Companies Inc due to the harassment and false statements provided by the individual.'
                case 21:
                    return 'I can not wait to afford my own smash content house with my $1.39 per week'
                case 22:
                    return 'I am at work for the next 72 hours so contact me then if you want to voice chat :D'
                case 23:
                    return 'I have used 95 percent of my life savings on Clash Royale and Apex Legends'
                case 24:
                    return 'Gas Prices are just so high right now thanks to the terrible economy we are in...'
                case 25:
                    return 'My last 3 paychecks were spent on Pokemon Go incubators...'
                case 26:
                    return 'I have invested heavily into the DogeCoin. Hopefully I can become a billionaire like Elon Musk Soon!'
                case 27:
                    return 'I have invested a lot of my personal savings into the housing market.  Surely it would not burst like a bubble'
                case 28:
                    return 'I have now received my raise of $15 per hour.  Hopefully I can contribute a lot to Zaiyldes House'
                case 29:
                    return 'I have now purchased another Switch Oled Pro Hypermax 1080p 60FPS mode!  It goes Crazy!!'
                case 30:
                    return 'I am excited to purchase Orange Juice when it gets a 20 cent discount :D'
        case 'matt':
            randno = randint(0,10)
            match randno:
                case 0:
                    return 'Soya... Shut the Fuck Up'
                case 1:
                    return 'Matt, no one asked you!'
                case 2:
                    return 'Matt... you are like korean right?'
                case 3:
                    return 'Matt... you are like japanese right?'
                case 4:
                    return 'Matt... you are like chinese right?'
                case 5:
                    return 'Matt... you are like taiwaneese right?'
                case 6:
                    return 'Matt... you are like vietnamease right?'
                case 7:
                    return 'Matt... you are like indian right?'
                case 8:
                    return 'Matt... you are like african right?'
                case 9:
                    return 'Soya, who are you even talking to?'
                case 10:
                    return 'Mathew... You are like british? correcto?'
        case 'test':
            return 'Test?  I do not study for those...'
        case 'lethal company phrase':
            word1 = choice(['dangerous', 'destructive', 'devasting', 'fatal', 'harmful', 'malignant', 'mortal', 'murderious', 'noxious', 'deadly', 'poisonous', 'terminal', 'deathly', 'risky'])
            word2 = choice(['association', 'club', 'company', 'organization', 'party', 'community', 'clan', 'clique', 'crew', 'ensemble', 'horde', 'league', 'gathering', 'order', 'troope'])
            lethalCompany = word1 + ' ' + word2
            return lethalCompany
        case 'brianjewelfacts':
            return 'このコメントは削除されました。このバグが発生した場合は、開発者に報告してください。'
                
