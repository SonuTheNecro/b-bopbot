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
        case 'briansmash':
            #Roll the Dice
            if(randint(0,1) == 0):
                return 'https://cdn.discordapp.com/attachments/766027094944645153/1195944151896830052/Brian_Smash_Time.png?ex=65b5d4c9&is=65a35fc9&hm=36ca33befe87ecd65a83ace0926917cc38cdb2142f990d142548d53d60a28751&'
            else:
                return 'https://cdn.discordapp.com/attachments/766027094944645153/1195945072211013702/Brian_Smash_Time.png?ex=65b5d5a4&is=65a360a4&hm=f812e261d313bcdae1679f0fe008199300777fb477124ed376f1e8e3a3763b25&'
        case 'brianlethalcompany':
            return 'https://cdn.discordapp.com/attachments/1195931768247828511/1195947867471351928/brian_Lethal_Time.jpg?ex=65b5d83f&is=65a3633f&hm=2ae52d393f607c3e103ac4edd8c8cb9e8eab72ff64468247622265f1b2e60f12&'
        case 'briananime':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1195931619102564512/Brian_Anime_Time.jpg?ex=65b5c91d&is=65a3541d&hm=1b7f0978c58ced0e4af816d4423cb0a6240e75dbf6615180e585c1e01a943441&'
        case 'brianfnaf':
            return 'https://cdn.discordapp.com/attachments/760905671133757442/1196247891405193276/Brian_Game_Time.gif?ex=65b6efaa&is=65a47aaa&hm=f7d892a4418995df310b3fa057c30d9a8f24547ef07e861895f9b5c9c4dfb847&'
        case 'work':
            randno = randint(0,4)
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
        case 'matt':
            randno2 = randint(0,8)
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
        case 'test':
            return 'Test?  I do not study for those...'
        case 'brianclash':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196879066565967923/Brian_Clash_Time2.jpg?ex=65b93b7e&is=65a6c67e&hm=f71b87743b249addd6c3c1945c3fb52528cf50f26cef915b2f785a4026ffd0ac&'
        
        
