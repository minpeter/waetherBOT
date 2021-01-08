
import discord
import time
import requests
import json

client = discord.Client()
discordbottoken="Nzk1NTc1MTA5ODU4ODg1NjUy.X_LXDw.waMtfMWQaiT9EhS654xaGUXYNsQ"

def weatherrequests(lat, lon):

	openweatherapitoken="f274a5616d927108ae79c369991175e5"
	response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweatherapitoken}&units=metric')
	rt = response.text
	json_data = json.loads(rt)

	print(json.dumps(json_data,indent='\t'))
	
#main = json_data["weather"]["main"]
	temp = json_data["main"]["temp"]
	feels_like = json_data["main"]["feels_like"]
	humidity = json_data["main"]["humidity"]
	windspeed = json_data["wind"]["speed"]
	return temp,feels_like,humidity,windspeed

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
	
	if message.content.startswith("!김포날씨"):
		weather = weatherrequests(37,126)
		await message.channel.send(f"```온도 : {weather[0]}\n체감온도 : {weather[1]}\n습도 : {weather[2]}\n풍속 : {weather[3]}\n```")


client.run(discordbottoken)
