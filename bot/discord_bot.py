import discord
import config
import helpers
from chatbot_model import ChatBot
from transformers import GPT2Tokenizer

client = discord.Client(intents=discord.Intents.default())
chatbot = ChatBot("models/trained_chatbot")
tokenizer = GPT2Tokenizer.from_pretrained("models/trained_chatbot")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    helpers.save_chat_history(message)  # Store messages for training
    response = chatbot.generate_response(message.content, tokenizer)

    await message.channel.send(response)

client.run(config.DISCORD_BOT_TOKEN)