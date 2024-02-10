# Imports

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Game
from responses import get_response, argument_winner
from random import randint
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
    await pick_status()
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

    if(username == ADMIN and '!update_status' in user_message):
        await update_status(user_message)
        return
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

async def pick_status() -> None:
    randno = randint(0,8)
    match randno:
        case 0:
            await client.change_presence(activity=Game('Apex Legends'))
        case 1:
            await client.change_presence(activity=Game('Clash Royale'))
        case 2:
            await client.change_presence(activity=Game('Lethal Company'))
        case 3:
            await client.change_presence(activity=Game('Super Smash Bros Ultimate'))
        case 4:
            await client.change_presence(activity=Game('Dokapon Kingdom! Connect'))
        case 5:
            await client.change_presence(activity=Game('Epstein Island: The Video Game'))
        case 6:
            await client.change_presence(activity=Game('Uno!'))
        case 7:
            await client.change_presence(activity=Game('Dead By Daylight'))
        case 8:
            await client.change_presence(activity=Game('ඞ Among Us: Nintendo Switch Imposter Edition ඞ'))

async def update_status(input_str: str) -> None:
    input_str = input_str[14:]
    await client.change_presence(activity=Game(input_str))
    return




if __name__ == '__main__':
    main()