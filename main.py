import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_anime_quote():
  response_anime = requests.get('https://animechan.vercel.app/api/random')
  json_data1 = json.loads(response_anime.text)
  quote = json_data1["quote"] + " - " + json_data1["character"] + "  ." + json_data1["anime"]
  return (quote)

@client.event
async def on_ready(): 
  print('We have logged in as {0.user}'.format(client))
  print (get_anime_quote())


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if message.content.startswith('$anime'):
    quote1 = get_anime_quote()
    await message.channel.send(quote1)
   

my_secret = os.environ['TOKEN']
client.run(my_secret)
