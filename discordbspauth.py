import discord
from discord.ext import commands
import requests
client = commands.Bot(command_prefix="?")
client.remove_command("help")
@client.event
async def on_ready():
    print('The bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name="BlockStarPlanet"))
@client.command()
async def Activation(ctx):
    args = ctx.message.content.split(" ")
    if(len(args) == 2):
        requests.get(f"http://suerte.ct8.pl/AuthService.php?hwid={hwid}&dcid={ctx.author.id}&method=addnew")
client.run("MTAxNDgyNjg1ODQ2ODA4OTg3Ng.GrgYCX.b4xmMPQOHB9KuwOg0MWJZcn8XXJOqvr1uzEfEk")
