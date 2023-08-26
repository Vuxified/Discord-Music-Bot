import discord
from discord.ext import commands
intents = discord.Intents.all() 
intents.members = True
client = commands.Bot(command_prefix= '$', intents=intents)

@client.event
async def on_ready():
    print("Bot is now ready")
    print("*****************")


@client.command()
async def basiccommands(ctx):
    await ctx.send("$python")

@client.command()
async def python(ctx):
    await ctx.send('''Python is an interpreted, 
object-oriented, high-level programming language with dynamic semantics. 
Its high-level built-in data structures, combined with dynamic typing and dynamic binding make it very attractive for Rapid Application Development, 
as well as for use as a scripting or glue language to connect existing components together. 
Python's simple, easy-to-learn syntax emphasizes readability and therefore reduces the cost of program maintenance. 
Python supports modules and packages, which encourages program modularity and code reuse.''')
    


client.run('MTExOTEwNjAxODcxNTExOTY5Ng.GVS34v.WI1srqM9iia7fb4mXpa6is_RLW31rio1A4hc8E')