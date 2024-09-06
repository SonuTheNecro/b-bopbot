# Imports

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Game
import discord
from discord.ext import commands, tasks
from responses import get_response, argument_winner, file_read_rng, nux_taxu_response
from random import randint, choice
import asyncio
# Load Token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ADMIN = 'sonuthenecro'

# Bot Setup (Setup Intents) 

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

#send message
async def send_message(message, user_message) -> None:
    #If its empty
    if not user_message: 
        return
    #If its private
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    # try to stop errors
        

    randno = randint(0,99)

    try:
        match randno:
            case 95:
                response = argument_winner(user_message)
            case 94:
                response = "idgaf"
            case 93:
                response = "AND BUMBLEBEE!"
            case 51:
                response = nux_taxu_response(user_message)
            case 52:
                response = nux_taxu_response(user_message)
            case 53:
                response = nux_taxu_response(user_message)
            case 54:
                response = nux_taxu_response(user_message)
            case 55:
                response = nux_taxu_response(user_message)
            case 56:
                response = nux_taxu_response(user_message)
            case 57:
                response = nux_taxu_response(user_message)
            case 58:
                response = nux_taxu_response(user_message)
            case 59:
                response = nux_taxu_response(user_message)
            case _:    
                response = get_response(user_message)
        
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# startup for bot
        
@client.event
async def on_ready() -> None:
    print(f'{client.user} has joined the Arena')
    


@client.event
async def on_message(message) -> None:
    # Bot doesn't reply to itself
    if message.author == client.user:
        return
    #Log
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    fileStream = open("log.txt", "a")
    fileStream.write(f'[{channel}] {username}: "{user_message}"\n')
    fileStream.close()
    if username == 'thaze.':
        await maan_check(message)
        return
    if("ocho" in user_message.lower()):
        await ocho_check(message)
    if len(user_message) > 300:
        await puking_horse(message)
        return
    if(username == 'bbop82' and ('cant' in user_message.lower() or 'can\'t' in user_message.lower())):
        temp1 = file_read_rng('ocho_reaction.txt')
        #await message.author.send(temp1)
        await message.channel.send(temp1)
        return
    if(username == ADMIN and '!update_status' in user_message):
        await update_status(user_message)
        return
    #if(username == ADMIN and '!pick_status' in user_message):
        #await pick_status()
        #return
    # If Thang tries to use the Lord's weapon against us
    if 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXlpbWtlMDF5emwwdjAyZ3lobzhod2ZpczBoOHRmdXZ4c2hrZmlpMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Hb4Ns3rwPXmkdYhKnv/giphy.gif' in user_message or "https://tenor.com/view/memes-gif-9980668056796018353" in user_message:
        if username == 'thangamangalang':
            await great_leader_response(message, False)
            return
        elif username == ADMIN:
            await great_leader_response(message, True)
            return
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)
    
    
#Picks a random game as the status
async def pick_status() -> None:
    random_game = choice(['Apex Legends', 'Unknown Error! DM B-Bop82 for information!', "Thanga-GameH"])
    await client.change_presence(activity=Game(random_game))
#Picks the status based on User_Input
async def update_status(input_str: str) -> None:
    input_str = input_str[14:]
    await client.change_presence(activity=Game(input_str))
    return


#Reacts with dog emojis
async def ocho_check(message):
    await message.add_reaction("🐕")
    await message.add_reaction("🐶")
    await message.add_reaction("🦴")
    await message.add_reaction("🍖")
    await message.add_reaction("🐕‍🦺")
    await message.add_reaction("🦮")
    await message.add_reaction("🐩")
    await message.add_reaction("🅾️")
    await message.add_reaction("🇨")
    await message.add_reaction("🇭")
    await message.add_reaction("0️⃣")
#Responds with the opposite gif
async def great_leader_response(message,value: bool) -> None:
    if value:
        await message.channel.send("https://tenor.com/view/memes-gif-9980668056796018353") #TRUTH
    else:
        await message.channel.send("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXlpbWtlMDF5emwwdjAyZ3lobzhod2ZpczBoOHRmdXZ4c2hrZmlpMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Hb4Ns3rwPXmkdYhKnv/giphy.gif") #FALSE
# Sends a random message of a horse
async def puking_horse(message) -> None:
    string = ""
    match randint(0,8):
        case 0:
            string = "https://cdn.discordapp.com/attachments/694710307909533760/1278895612355674222/GWMVToiXkAALMpL.png?ex=66d3209a&is=66d1cf1a&hm=501c9b8cbb304f3e2d9fac47b0ef1238b09e55479704c5728bc878e3c959374d&"
        case 1:
            string = "https://pbs.twimg.com/media/GWLCxqwXIAADaA6?format=jpg&name=small"
        case 2:
            string = "https://pbs.twimg.com/media/GWKYtXcW4AAxK7H?format=jpg&name=240x240"
        case 3:
            string = "https://cdn.discordapp.com/attachments/1148460410719182909/1278850641183375380/GWFWHVUW8AAT62c.png?ex=66d2f6b8&is=66d1a538&hm=1e83d54a16fd3e1a7d620748790b6d350288e3b7804c5713a42360641c0bca13&"
        case 4:
            string = "https://pbs.twimg.com/media/GWLeiX_WUAAlFrN?format=jpg&name=small"
        case 5:
            string = "https://pbs.twimg.com/media/GWLCY2hWEAAdYlC?format=jpg&name=medium"
        case 6:
            string = "https://pbs.twimg.com/media/GWLCY2aWIAA43eE?format=jpg&name=medium"
        case 7:
            string = "https://pbs.twimg.com/media/GWLCY2jWgAEybE8?format=jpg&name=medium"
        case 8:
            string = "https://pbs.twimg.com/media/GWKGr7IWgAEDaGd?format=jpg&name=900x900"
    await message.channel.send(string)
# Replies whenever maan checks with the full combo
async def maan_check(message) -> None:
    await message.channel.send("Nah I'm Good")
    await message.channel.send(":skull:")
    await message.channel.send("idgaf")
    await message.add_reaction("🤮")
    await message.add_reaction("🥸")
    await message.add_reaction("💀")
    await message.add_reaction("🤡")
    await message.add_reaction("🙉")
if __name__ == '__main__':
    main()