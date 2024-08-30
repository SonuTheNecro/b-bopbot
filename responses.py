# Argument Winner Code was lost media found by JigglyJello and is under authorized permission.  All reproduced code is ILLEGAL and will be filed with a jokingly DMCA

from random import choice, randint
import re
#Checks if a string is in source
def analysis(ogStr: str) -> str:
    if 'among' in ogStr:
        return 'among'
    elif '<@&732688521831383081>' in ogStr:
        return 'briananime'
    elif '<@&1192175976663232582>' in ogStr:
        return 'brianlethalcompany'
    elif '<@&694717398678372394' in ogStr:
        return 'briansmash'
    elif 'work' in ogStr:
        return 'brianwork'
    elif 'jewel' in ogStr:
        return 'brianwork'
    elif '<@436655054196441128>' in ogStr:
        return 'matt'
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
        case 'among':
            return 'https://media1.tenor.com/m/jUMex_rdqPwAAAAd/among-us-twerk.gif'
        case 'briansmash':
            #Roll the Dice
           randno = randint(0,5)
           match randno:
               case 0:
                   return 'https://media.discordapp.net/attachments/766027094944645153/1196951444419514529/Brian_Smash_Time_Down.jpg?ex=65b97ee6&is=65a709e6&hm=f2226b6aa85b18c452b2b242310badafde77dc2a8837242c82546cef9920325b&=&format=webp&width=623&height=662'
               case 1:
                   return 'https://media.discordapp.net/attachments/766027094944645153/1196951444708925460/Brian_Smash_Time_Left.jpg?ex=65b97ee6&is=65a709e6&hm=e1badc56169ec024a544683309f490e0c0a24c5cc87855f987bd063859025e3c&=&format=webp&width=623&height=662'
               case 2:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1196951444985757716/Brian_Smash_Time_Right.jpg?ex=65b97ee6&is=65a709e6&hm=4b2648904145ac63f3394b40fa9822f640821133644d28ce7916a84c22636afb&'
               case 3:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1196951445275152434/Brian_Smash_Time_Up.jpg?ex=65b97ee6&is=65a709e6&hm=5b48b5dc28107234bb59938b1685460cb82758740e901a3cee9c7ac903622df7&'
               case 4:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1230736673072222328/Brian_Smash_Time_Kalos.jpg?ex=6623ed18&is=66229b98&hm=870f1e130f809157ee156543b85fcea59e68d3f36a2b29a9a84fabeca3cfb525&'
               case 5:
                   return 'https://cdn.discordapp.com/attachments/766027094944645153/1230739130980499466/Brian_PS2.jpg?ex=66346a22&is=6621f522&hm=1cf834a953b795eb384ce0223de98421fa8a0274e0c62dc9a079400ce5e730ff&'
        case 'brianlethalcompany':
            randno = randint (0,3)
            match randno:
                case 0:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1196946708052050072/Brian_Lethal_Time_2.jpg?ex=65b97a7d&is=65a7057d&hm=74e5870d014d1790f898df9704d3ec0fb5ba4cfbcac2ca89c59b974800bd50b0&'
                case 1:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1199235647643324528/Brian_Lethal_Time_3.jpg?ex=65c1ce3b&is=65af593b&hm=236a391f7551d2f041ab37951683f061c8e3f561ec4e77671151293684b4996b&'
                case 2:
                    return 'https://cdn.discordapp.com/attachments/766027094944645153/1199235678827978823/Brian_Lethal_Time_4.jpg?ex=65c1ce42&is=65af5942&hm=9acc8e2b7ecc84f4540f728fcfe3c8f012b6edeef43b97b612242ccd8cb2000f&'
                case 3:
                    return 'https://cdn.discordapp.com/attachments/1195931768247828511/1279204173593972828/image.png?ex=66d39739&is=66d245b9&hm=c65cb3c54255d1d287dd8f1fc4026ebbf911649a11cd591798096124afe7975a&'
        case 'briananime':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196962782235598900/Brian_Anime_Time2.jpg?ex=65b98975&is=65a71475&hm=f638ee432ba450fe46a1a25c0a721d724d1399d6943223af1243e1cdd99e3693&'
        case 'brianclash':
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1196943195674791936/Brian_Clash_Time2.jpg?ex=65b97737&is=65a70237&hm=bf439357d726620cfcd6d2d17fcbb06767149f0ebed8b2d5bb7496302ecd76be&'
        case 'brianwork':
            return file_read_rng('brian_work_quotes.txt')
        case 'matt':
            subject = choice(['Matt', 'Mathew', 'Soya', 'OchoOwner'])
            race = choice(['Korean','Japanese','Chinese','Taiwaneese','Indian','Vietnamease','African','Yapanese','British','Scotish','Polish','German','American','Canadian','Roman','Spanish','Italian','Ohioian','North Koreanease', 'Nebraskian'])
            sentence = subject + ", Aren't You are like " + race + ' right?'
            return sentence
        case 'lethal company phrase':
            word1 = choice(['dangerous', 'destructive', 'devasting', 'fatal', 'harmful', 'malignant', 'mortal', 'murderious', 'noxious', 'deadly', 'poisonous', 'terminal', 'deathly', 'risky'])
            word2 = choice(['association', 'club', 'company', 'organization', 'party', 'community', 'clan', 'clique', 'crew', 'ensemble', 'horde', 'league', 'gathering', 'order', 'troope'])
            lethalCompany = word1 + ' ' + word2
            return lethalCompany
        case 'p2025':
            return "that's like unrelated to trump!"
# Code that WE made me and TUX TAXU MADE
def nux_taxu_response(user_input: str) -> str:
    key_list = {
        r'\bI AM\b':  'WE ARE',
        r'\bi am\b':  'We are',
        r"\bI'm\b":  "WE\'RE",
        r"\bi'm\b":  "we\'re",
        r"\bI WAS\b":  "WE WERE",
        r"\bi was\b":  "we were",
        r"\bi\b":  "we",
        r"\bI\b":  "We",
        r"\bimma\b":  "we gonna",
        r"\bidk\b":  "wdk",
        r"\bidc\b":  "wdc",
        r"\bidfk\b":  "wdfk",
        r"\bidfc\b":  "wdfc",
        r"\bidgaf\b":  "wdgaf",
        r"\bme\b":  "us",
        r"\bMe\b":  "Us",
        r"\bME\b":  "US",
        r"\bMyself\b":  "Ourselves",
        r"\bMYSELF\b":  "OURSELVES",
        r"\bmyself\b":  "ourselves",
        r"\bMy\b":  "Our",
        r"\bMY\b":  "OUR",
        r"\bmy\b":  "our",
        r"\bMine\b":  "Ours",
        r"\bMINE\b":  "OURS",
        r"\bmine\b":  "ours",
    }
    response = user_input
    for key, key_list in key_list.items():
        response = re.sub(key,key_list, response, flags=re.IGNORECASE)

    return response
