import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="`")

@bot.event
async def on_ready():
  print("Logged in")
  
@bot.command()
async def 안녕(ctx):
    embed = discord.Embed(
        title="ㅎㅇㅎㅇ",
        description="ㅎㅇ"
    )
    await ctx.send(embed=embed)
