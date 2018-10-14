import discord
client = discord.Client()



@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="too busy SCROLLing"))
#await client.send_message(message.channel, "I live!")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "scroll":
        await client.send_message(message.channel, "MOJE!")
    if message.content == "Michal je debil":
        await client.send_message(message.channel, "Ano, souhlasím")



client.run("NDk5Mjk5ODc1MzU2Mjc4Nzk2.Dp6Sbw._mu4AkJJnC1C2DAMmXt1ZP7-w_E")
