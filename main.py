# Imports

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load Token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
    try:
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
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()