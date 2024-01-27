from discord.ext import commands

@commands.slash_command()
async def ping(ctx):
    await ctx.respond('pong')
