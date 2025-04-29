import discord
import json

TOKEN = "YOUR_DISCORD_BOT_TOKEN"

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    with open("chat_history.json", "a") as file:
        json.dump({"author": str(message.author), "content": message.content}, file)
        file.write("\n")

client.run(TOKEN)
import json
import nltk
from transformers import GPT2Tokenizer

nltk.download("punkt")

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def preprocess_text(text):
    return tokenizer.encode(text, return_tensors="pt")

chat_data = []
with open("chat_history.json", "r") as file:
    for line in file:
        msg = json.loads(line)
        chat_data.append(preprocess_text(msg["content"]))