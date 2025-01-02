import discord
import os
import random
import requests
from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Modal, TextInput, View, Button

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Event triggered when a member joins the server
@bot.event
async def on_member_join(member):
    print(f"user joined: {member}")
    try:
        welcome_channel = discord.utils.get(member.guild.text_channels, name='lounge')
        if welcome_channel:
            eevee_nap = "<:EeveeNap:1046348052849496134>"
            message = f"Welcome to the server, {member.mention}! Celly is the goat streamer!! {eevee_nap}"
            print(f"Sending message: {message}")
            await welcome_channel.send(message)
        else:
            print(f"Lounge channel not found in {member.guild.name}!")
    except Exception as e:
        print(f"Error in on_member_join: {e}")

# Event triggered when a member leaves the server
@bot.event
async def on_member_remove(member):
    print(f"user left: {member}")
    try:
        leave_channel = discord.utils.get(member.guild.text_channels, name='lounge')
        if leave_channel:
            eevee_pout = "<:EeveePout:1046348055328337940>"
            message = f"{member.mention} has left the server! fking noob!! {eevee_pout}"
            print(f"Sending message: {message}")
            await leave_channel.send(message)
        else:
            print(f"Lounge channel not found in {member.guild.name}!")
    except Exception as e:
        print(f"Error in on_member_join: {e}")

bot.run(TOKEN)