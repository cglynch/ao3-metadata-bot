
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
        work = api.work(id=id)
        output_list = [work.fandoms[5], work.warnings[0], work.rating[0]]
        response = " | ".join(output_list)
        await message.channel.send(response)
print("token:"+TOKEN)
client.run(TOKEN)