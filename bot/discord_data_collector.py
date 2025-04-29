import discord
import json
import config

TOKEN = config.DISCORD_BOT_TOKEN

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=100):
                    save_message(message)
            except Exception as e:
                print(f"Error accessing {channel.name}: {e}")

def save_message(message):
    """Save Discord messages to a JSON file"""
    with open("data/discord_messages.json", "a") as file:
        json.dump({"author": str(message.author), "content": message.content}, file)
        file.write("\n")

client.run(TOKEN)