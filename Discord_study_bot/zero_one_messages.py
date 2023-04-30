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
    else:
        if message.content=="start_session":
            await message.channel.send("study bot started study session")



token = "MTEwMjIwMzU2Mjg1NzA3NDgwOA.GLrlZl.jpv44tgdpac8XzbzIWp3aCkBQoqql1lOjxn47Q"
client.run(token)
