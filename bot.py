# test_bot.py
import os, random
import utils
from ao3 import AO3
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    url_section = "https://archiveofourown.org/works/"
    if url_section in message.content:
        print("here " , message.content)
        id = utils.work_id_from_url(message.content)
        print("ID = ", id)
        api = AO3()
        work = api.work(id=id)
        print(work.warnings)
        output_list = [work.fandoms[0], work.warnings[0], work.rating[0]]
        # response = "\n".join(output_list)
        await message.channel.send(str(output_list))

client.run(TOKEN)