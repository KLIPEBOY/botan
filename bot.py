import discord
from discord.ext import commands

TOKEN = "ODIyODk3NDIwNDY3NDM3NTk5.YFY88Q.nFaKZ1PqglVwL22eICCqFAqZQSs"

bot = commands.Bot(command_prefix=('+'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")

@bot.command()
async def Hi(ctx):
    await ctx.send('Hi')

@bot.command()
async def test1(ctx):
    embed = discord.Embed(
        title="Привет всем!",
    )
    await ctx.send(embed=embed)

@bot.command()
async def lolzsait(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на lolz",
        url='https://lolz.guru',
    )
    await ctx.send(embed=embed)

bot.run(TOKEN)
