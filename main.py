# Imports

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Game
import discord
from discord.ext import commands, tasks
from responses import get_response, argument_winner, file_read_rng
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
        if(randno == 95):
            response = argument_winner(user_message)
        else:    
            response = get_response(user_message)
        
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# startup for bot
        
@client.event
async def on_ready() -> None:
    print(f'{client.user} has joined the company')
    


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
    if(username == 'bbop82' and ('cant' in user_message.lower() or 'can\'t' in user_message.lower())):
        temp1 = file_read_rng('ocho_reaction.txt')
        #await message.author.send(temp1)
        message.channel.send(temp1)
        return
    if(username == ADMIN and '!update_status' in user_message):
        await update_status(user_message)
        return
    if("ocho" in user_message.lower()):
        await ocho_check(message)
    if(username == ADMIN and '!pick_status' in user_message):
        await pick_status()
        return
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)
    
    
#Picks a random game as the status
async def pick_status() -> None:
    random_game = choice(['Apex Legends', 'Clash Royale', 'Lethal Company', 'Super Smash Bros Ultimate', 'Dokapon Kingdom! Connect', 'Epstein Island: The Video Game', 'Uno!', 'Dead by Daylight', 'ඞ Among Us: Nintendo Switch Imposter Edition ඞ', 'Brawl Stars', 'Rocket League', 'League of Legends', 'Unknown Error! DM B-Bop82 for information!'])
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

if __name__ == '__main__':
    main()