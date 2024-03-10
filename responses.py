# Argument Winner Code was lost media found by JigglyJello and is under authorized permission.  All reproduced code is ILLEGAL and will be filed with a jokingly DMCA

from random import choice, randint

#Checks if a string is in source
def analysis(ogStr: str) -> str:
    if '!update_status' in ogStr:
        return '!update_status'
    elif '!change_status' in ogStr:
        return '!change_status'
    elif 'among' in ogStr:
        return 'among'
    elif '<@&732688521831383081>' in ogStr:
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
    
def file_read_rng(fileName: str) -> str:
    fileStream = open(fileName, "r")
    lines = fileStream.readlines()
    line_chosen = choice(lines)
    fileStream.close()
    return line_chosen
    
#Author JigglyJello No DMCA PLEASE!
def argument_winner(inputStr: str) -> str:
    response: str = ""
    for char in inputStr:
        if randint(0,1) == 1:
            response += char.upper()
        else:
            response += char.lower()
    return response


#Returns based on the input of the message it reads in Sans Mains
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    lowered = analysis(lowered)
    
    
    match lowered:
        case '!update_status':
            return 'You do not have the correct permissions/ missing paramaters'
        case '!change_status':
            return 'This command does not exist! Did you mean !update_status?'
        case 'among':
            return 'https://media1.tenor.com/m/jUMex_rdqPwAAAAd/among-us-twerk.gif'
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
            randno = randint (0,2)
            match randno:
                case 0:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1196946708052050072/Brian_Lethal_Time_2.jpg?ex=65b97a7d&is=65a7057d&hm=74e5870d014d1790f898df9704d3ec0fb5ba4cfbcac2ca89c59b974800bd50b0&'
                case 1:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1199235647643324528/Brian_Lethal_Time_3.jpg?ex=65c1ce3b&is=65af593b&hm=236a391f7551d2f041ab37951683f061c8e3f561ec4e77671151293684b4996b&'
                case 2:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1199235678827978823/Brian_Lethal_Time_4.jpg?ex=65c1ce42&is=65af5942&hm=9acc8e2b7ecc84f4540f728fcfe3c8f012b6edeef43b97b612242ccd8cb2000f&'
        
        case 'briananime':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196962782235598900/Brian_Anime_Time2.jpg?ex=65b98975&is=65a71475&hm=f638ee432ba450fe46a1a25c0a721d724d1399d6943223af1243e1cdd99e3693&'
        case 'brianclash':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196943195674791936/Brian_Clash_Time2.jpg?ex=65b97737&is=65a70237&hm=bf439357d726620cfcd6d2d17fcbb06767149f0ebed8b2d5bb7496302ecd76be&'
        case 'work':
            return file_read_rng('brian_work_quotes.txt')
        case 'matt':
            subject = choice(['Matt', 'Mathew', 'Soya', 'OchoOwner'])
            race = choice(['Korean','Japanese','Chinese','Taiwaneese','Indian','Vietnamease','African','Yapanese','British','Scotish','Polish','German','American','Canadian','Roman','Spanish','Italian','Ohioian','North Koreanease'])
            sentence = subject + ', You are like ' + race + ' right?'
            return sentence
        case 'test':
            return 'Test?  I do not study for those...'
        case 'lethal company phrase':
            word1 = choice(['dangerous', 'destructive', 'devasting', 'fatal', 'harmful', 'malignant', 'mortal', 'murderious', 'noxious', 'deadly', 'poisonous', 'terminal', 'deathly', 'risky'])
            word2 = choice(['association', 'club', 'company', 'organization', 'party', 'community', 'clan', 'clique', 'crew', 'ensemble', 'horde', 'league', 'gathering', 'order', 'troope'])
            lethalCompany = word1 + ' ' + word2
            return lethalCompany
        case 'brianjewelfacts':
            return 'このコメントは削除されました。このバグが発生した場合は、開発者に報告してください。'
                

