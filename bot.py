import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json', model_name="neforgpt")
chatbot.train_model()
chatbot.save_model()

client = discord.Client(intents=discord.Intents.all())

load_dotenv()
bot_token = os.getenv('bot_token')

@client.event
async def on_message(message):
    print("message-->", message)
    print("message content-->", message.content)
    print("message attachments-->", message.attachments)
    print("message id", message.author.id)
    if message.author == client.user:
        return

    if message.content.startswith('ало хуй'):
        await message.channel.send('нахуй иди')

    if message.content.startswith('-'):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)
        await message.channel.send(file=discord.File('emote1.png'))

client.run(bot_token)