import discord
import os

# Get Discord token and thread ID from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
THREAD_ID = os.getenv("THREAD_ID")

# Set up the bot client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Get the channel (thread) to send the reminder
    channel = client.get_channel(int(THREAD_ID))
    await channel.send("Reminder: Please submit your standup updates!")

# Run the bot
client.run(DISCORD_TOKEN)
