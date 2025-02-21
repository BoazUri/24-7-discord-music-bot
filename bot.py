import discord
from discord.ext import commands
import asyncio
import os
import random

bot = commands.Bot(command_prefix='!')

# Stel hier je map in met MP3-bestanden
MUSIC_FOLDER = "path/to/your/music/folder"  # Pas dit aan naar de juiste map
VOICE_CHANNEL_ID = YOUR_VOICE_CHANNEL_ID  # Vervang met je stemkanaal-ID
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Vervang met je bot-token

@bot.event
async def on_ready():
    print("Bot is ready.")
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if not channel:
        return print("Ongeldige stemkanaal-ID.")

    voice_client = await channel.connect()
    await play_music(voice_client)

async def play_music(voice_client):
    while True:
        mp3_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
        if not mp3_files:
            print("Geen MP3-bestanden gevonden in de map.")
            await asyncio.sleep(10)  # Wacht 10 seconden en probeer opnieuw
            continue
        
        file_path = os.path.join(MUSIC_FOLDER, random.choice(mp3_files))
        print(f"Speelt af: {file_path}")

        voice_client.play(discord.FFmpegPCMAudio(file_path))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        
        await asyncio.sleep(2)  # Korte pauze tussen nummers

bot.run(TOKEN)
