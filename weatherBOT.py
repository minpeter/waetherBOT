import discord
import time
import requests
import json

client = discord.Client()
discordbottoken="here"
openweatherapitoken="and here"

def weatherrequests(lat, lon):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweatherapitoken}&units=metric')
    rt = response.text
    json_data = json.loads(rt)

    mainweather = json_data["weather"][0]["main"]
    temp = json_data["main"]["temp"]
    feels_like = json_data["main"]["feels_like"]
    humidity = json_data["main"]["humidity"]
    windspeed = json_data["wind"]["speed"]

    return mainweather,temp,feels_like,humidity,windspeed

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity = discord.Game("!help or !한세날씨"))


@client.event
async def on_message(message):
    if message.content.startswith("!status"):
        f = open("status.txt", "r", encoding="utf8")
        data = f.read()
        f.close()
        await message.channel.send(data)

    if message.content.startswith("!help"):
        f = open("help.txt", "r",  encoding="utf8")
        data = f.read()
        f.close()
        await message.channel.send(data)

    if message.content.startswith("!김포날씨") or message.content.startswith("!ㄱㅍㄴㅅ"):
        weather = weatherrequests(37.64524,126.67132)
        await message.channel.send(f"```오늘의 날씨 : {weather[0]}\n온도 : {weather[1]}\n체감온도 : {weather[2]}\n습도 : {weather[3]}\n풍속 : {weather[4]}\n```")

    if message.content.startswith("!한세날씨") or  message.content.startswith("!ㅎㅅㄴㅅ"):
        weather = weatherrequests(37.55157,126.95194)
        await message.channel.send(f"```오늘의 날씨 : {weather[0]}\n온도 : {weather[1]}\n체감온도 : {weather[2]}\n습도 : {weather[3]}\n풍속 : {weather[4]}\n```")

client.run(discordbottoken)
