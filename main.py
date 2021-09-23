import discord
import os
from discord.ext import commands
import youtube_dl

bot = commands.Bot(command_prefix=("$"))

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command(name="join")
async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

@bot.command()
async def leave(ctx):
        await ctx.voice_client.disconnect()

@bot.command()
async def msg(ctx, argx):
        await ctx.message.channel.send(argx)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))


bot.add_cog(Music(bot))

bot.run('ODkwNDIyODMyMjYwMDg3ODM4.YUvk4g.V05p3erMv-q79OBKCE-ZwSSlgp0')