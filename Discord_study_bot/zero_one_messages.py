import discord

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print("Bot is now online and ready to roll")


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    #await message.channel.send("bot speaking")
    if message.content=="start_session":
        await message.channel.send("study bot started study session")

token = "MTEwMjExNTI3NTc3Nzc4MTc5MQ.GOZbOg.mTARC1Fa0w4LxWH5AtEFmrR2XyxcvL24ZG8Wqk"
client.run(token)
