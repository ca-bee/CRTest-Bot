import discord
import random

client = discord.Client()

TOKEN = "NzYwMTYzMDMxMTUyODUzMDIy.X3IC_Q.Cw5NOjfpD3EOrOszq2cbLCbvB48"

client = discord.Client()

responses = [
    "NO",
    "YES",
    "meh maybe",
    "why",
    "It is extremely likely",
    "Probable chance of not"

]

greetingMessage = [
    "Don't straggle too long~",
    "Have a cup of joe"
]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Hello") or message.content.startswith("Hi"):
        await message.channel.send("Welcome to the server! \n")
        # await message.channel.send(random.choice(responses))

    if message.content.startswith(".say"):
        mes = message.content.split()
        output = ""
        try:
            i = 0
            for x in mes:
                if i != 0:
                    for word in x:
                        output += word
                output += " "
                i = i + 1
            await message.channel.send(output)
            await message.delete()
        except:
            await message.channel.send("Try sending something else.")

    if message.content.startswith(".8ball"):
        await message.channel.send(random.choice(responses))


@client.event
async def on_ready():
    print("RUNNING")


client.run(TOKEN)
client.close()
