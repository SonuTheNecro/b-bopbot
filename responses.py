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
            randno = randint(0,8)
            match randno:
                case 0:
                    return 'I can not wait to afford my own smash content house with my $1.39 per week'
                case 1:
                    return 'I am at work for the next 72 hours so contact me then if you want to voice chat :D'
                case 2:
                    return 'I have used 95 percent of my life savings on Clash Royale and Apex Legends'
                case 3:
                    return 'Gas Prices are just so high right now thanks to the terrible economy we are in...'
                case 4:
                    return 'My last 3 paychecks were spent on Pokemon Go incubators...'
                case 5:
                    return 'I have invested heavily into the DogeCoin. Hopefully I can become a billionaire like Elon Musk Soon!'
                case 6:
                    return 'I have invested a lot of my personal savings into the housing market.  Surely it would not burst like a bubble'
                case 7:
                    return 'I have now received my raise of $15 per hour.  Hopefully I can contribute a lot to Zaiyldes House'
                case 8:
                    return 'I have now purchased another Switch Oled Pro Hypermax 1080p 60FPS mode!  It goes Crazy!!'
        case 'matt':
            randno2 = randint(0,10)
            match randno2:
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
        
        
        
