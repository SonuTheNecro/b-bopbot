from random import choice, randint, random


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    animeCheck = "<@&732688521831383081>" in lowered
    lcCheck = "<@&1192175976663232582>" in lowered
    smashCheck = "<@&694717398678372394" in lowered
    workCheck = "work" in lowered 
    mattCheck = "<@436655054196441128>" in lowered 
    
    # image based ones
    if(animeCheck):
        return 'https://cdn.discordapp.com/attachments/766027094944645153/1195931619102564512/Brian_Anime_Time.jpg?ex=65b5c91d&is=65a3541d&hm=1b7f0978c58ced0e4af816d4423cb0a6240e75dbf6615180e585c1e01a943441&'
    if(lcCheck):
        return 'https://cdn.discordapp.com/attachments/1195931768247828511/1195947867471351928/brian_Lethal_Time.jpg?ex=65b5d83f&is=65a3633f&hm=2ae52d393f607c3e103ac4edd8c8cb9e8eab72ff64468247622265f1b2e60f12&'
    if(mattCheck or lowered is "matt"):
        return 'KYS NOW NI-'
    if(workCheck):
        return "I can't wait to earn $4.59 per week!"
    if(smashCheck):
        if(random() <= 0.5):
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1195944151896830052/Brian_Smash_Time.png?ex=65b5d4c9&is=65a35fc9&hm=36ca33befe87ecd65a83ace0926917cc38cdb2142f990d142548d53d60a28751&'
        else:
            return 'https://cdn.discordapp.com/attachments/766027094944645153/1195945072211013702/Brian_Smash_Time.png?ex=65b5d5a4&is=65a360a4&hm=f812e261d313bcdae1679f0fe008199300777fb477124ed376f1e8e3a3763b25&'
    match lowered:
        case 'skibidi':
            return 'Toilet'
        case 'what is the best state?':
            return 'Ohio'
        case 'gyatt':
            return 'Stick your gyatt out for the rizzler'

