
import os
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

    url_section = "https://archiveofourown.org/works/"
    if url_section in message.content:
        id = utils.work_id_from_url(message.content)
        api = AO3()
        print("ID: "+id)
        work = api.work(id=id)
        print("work: " + str(work))
        output_list = [" | ".join(work.fandoms), " | ".join(work.warnings), " | ".join(work.rating), " | ".join(work.author), " | ".join(work.words)]
        response = " |-| ".join(output_list)
        await message.channel.send(str(response))

client.run(TOKEN)