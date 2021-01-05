import discord
import time

client = discord.Client()
token="your token"

@client.event
async def on_ready():
	print(client.user.id)
	print(client.user.name)
	print("ready")
	await client.change_presence(status=discord.Status.online, activity = discord.Game("!status"))

@client.event
async def on_message(message):
	if message.content.startswith("!status"):
		f = open('status.txt','r')
		data = f.read()
		f.close()
		await message.channel.send(data)
		
	if message.content.startswith("!help"):
		f = open('help.txt', 'r')
		data = f.read()
		f.close()
		await message.channel.send(data)



client.run(token)