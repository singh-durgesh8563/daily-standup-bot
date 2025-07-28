import discord
import os

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message reading permissions

# Get Discord token and thread ID from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
THREAD_ID = os.getenv("THREAD_ID")

# Set up the bot client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Get the thread to send the reminder
    channel = client.get_channel(int(THREAD_ID))
    await channel.send("Reminder: Please submit your standup updates!")

# Run the bot
client.run(DISCORD_TOKEN)
