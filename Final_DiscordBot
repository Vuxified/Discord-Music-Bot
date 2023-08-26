import yt_dlp
import nacl
import os
import uuid
import asyncio
import discord
from discord.ext import commands
from discord.utils import get
#These are all the libraries we used to build the bot. Each have their own purpose and our sources for each of them is listed at the bottom of our essay.

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)

queue = []

@client.event
async def on_ready():
    print("The bot is now ready, commands are: $basic_commands, $play, $show_queue, $skip")

#The previous and following are commands for the bot that we set up to happen asynchronously, the bot responds to the users commands and does what 
@client.command()
async def basic_commands(ctx):
    await ctx.send("These are the commands for the bot: $play, $show_queue, $skip. Wait 5 seconds in between each command.")

@client.command()
async def play(ctx, *, song):
    voice_channel = ctx.author.voice.channel
    voice_client = get(client.voice_clients, guild=ctx.guild)

    if not voice_channel:
        await ctx.send("You have to be in a voice channel to use this command, join one accessible to the bot.")
        return

    if voice_client and voice_client.is_connected():
        if voice_client.channel != voice_channel:
            await voice_client.move_to(voice_channel)
    else:
        voice_client = await voice_channel.connect()

    song_info = await search_song(song)

    if not song_info:
        await ctx.send("Couldn't find the requested song, make sure the format for the <$play> command is <$play <song name> by <artist>.")
        return

    queue.append(song_info)

    if not voice_client.is_playing():
        await play_song(ctx, voice_client)
#Again these are just commands that the bot executes aynschronously at the users request. We explain it more in the video and essay.

@client.command()
async def show_queue(ctx):
    if not queue:
        await ctx.send("The queue is empty, add some songs!")
        return

    queue_list = "\n".join([item['title'] for item in queue])
    await ctx.send(f"Queue:\n{queue_list}")

@client.command()
async def skip(ctx):
    voice_client = get(client.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await play_song(ctx, voice_client)

async def search_song(song):
    unique_id = uuid.uuid4()  # This generates a unique ID for each song to be used later.
    file_name = f'song_{unique_id}.webm'
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        'extractor_args': {'youtube': ' --no-playlist'},
        'outtmpl': file_name 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{song}", download=True)  
            song_info = {'url': file_name, 'title': info['entries'][0]['title']}  # After this, the url is now the unique file name/path
            return song_info
        except Exception:
            return None

async def play_song(ctx, voice_client):
    if not queue:
        await ctx.send("The queue is empty.")
        await voice_client.disconnect()
        return

    song = queue.pop(0)
    voice_client.play(discord.FFmpegPCMAudio(song['url'], options="-vn"), after=lambda e: client.loop.create_task(play_song(ctx, voice_client)) if queue else client.loop.create_task(delete_file(song['url'])))
    await ctx.send(f"Now playing: {song['title']}")

async def delete_file(path):
    #The following is that the bot deletes the files of the songs downloaded after use.
    while True:
        try:
            os.remove(path)
            return
        except PermissionError:
            await asyncio.sleep(1) 

client.run('MTExOTEwNjAxODcxNTExOTY5Ng.GVS34v.WI1srqM9iia7fb4mXpa6is_RLW31rio1A4hc8E')
