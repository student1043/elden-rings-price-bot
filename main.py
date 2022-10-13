import os

import discord
from discord.ext import tasks
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import asyncio
from discord.ext import commands
import time
from requests_html import HTMLSession



load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
list_prices = []
dict_names = {"Dreugh Wax": "", "Style Page: Pirate Skeletons Mask": "", "Style Page: Opal Engine Guardian Staff": "",
"Tempering Alloy": "", "Chromium Plating": "", "Zircon Plating": "", "Perfect Roe": "", "Style Page: Opal Engine Guardian Dagger": "",
"Kuta": "", "Heartwood": "", "Mundane Rune": "", "Style Page: Opal Engine Guardian Greatsword": "",
"Hakeijo": "", "Style Page: Opal Ilambris Sword": "", "Potent Nirncrux": "", "Aetherial Dust": "",
"Sealed Woodworking Writ": "", "Columbine": "", "Platinum Ounce": "", "Rosin": ""}


"""async def newdata():
    await bot.wait_until_ready()
    counter = 0
    second_counter = 0
    channel = bot.get_channel(1024849506258407454)
    URL = "https://eu.tamrieltradecentre.com/pc/Trade"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    for item in soup.find_all(class_="gold-amount"):
        list_prices.append(item.get_text(strip=True))
    dict_names["Dreugh Wax"] = list_prices[0]
    dict_names["Style Page: Pirate Skeletons Mask"] = list_prices[1]
    dict_names["Style Page: Opal Engine Guardian Staff"] = list_prices[2]
    dict_names["Tempering Alloy"] = list_prices[3]
    dict_names["Chromium Plating"] = list_prices[4]
    dict_names["Zircon Plating"] = list_prices[5]
    dict_names["Perfect Roe"] = list_prices[6]
    dict_names["Style Page: Opal Engine Guardian Dagger"] = list_prices[7]
    dict_names["Kuta"] = list_prices[8]
    dict_names["Heartwood"] = list_prices[9]
    dict_names["Mundane Rune"] = list_prices[10]
    dict_names["Style Page: Opal Engine Guardian Greatsword"] = list_prices[11]
    dict_names["Hakeijo"] = list_prices[12]
    dict_names["Style Page: Opal Ilambris Sword"] = list_prices[13]
    dict_names["Potent Nirncrux"] = list_prices[14]
    dict_names["Aetherial Dust"] = list_prices[15]
    dict_names["Sealed Woodworking Writ"] = list_prices[16]
    dict_names["Columbine"] = list_prices[17]
    dict_names["Platinum Ounce"] = list_prices[18]
    dict_names["Rosin"] = list_prices[19]
    while not bot.is_closed():
        counter += 1
        print(counter)
        await channel.send(dict_names)
        await asyncio.sleep(60)"""

@bot.command()
async def get_price(ctx, *args):
    counter = 0
    second_counter = 0
    channel = bot.get_channel(1024849506258407454)
    URL = "https://eu.tamrieltradecentre.com/pc/Trade"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    for item in soup.find_all(class_="gold-amount"):
        list_prices.append(item.get_text(strip=True))
    dict_names["Dreugh Wax"] = list_prices[0]
    dict_names["Style Page: Pirate Skeletons Mask"] = list_prices[1]
    dict_names["Style Page: Opal Engine Guardian Staff"] = list_prices[2]
    dict_names["Tempering Alloy"] = list_prices[3]
    dict_names["Chromium Plating"] = list_prices[4]
    dict_names["Zircon Plating"] = list_prices[5]
    dict_names["Perfect Roe"] = list_prices[6]
    dict_names["Style Page: Opal Engine Guardian Dagger"] = list_prices[7]
    dict_names["Kuta"] = list_prices[8]
    dict_names["Heartwood"] = list_prices[9]
    dict_names["Mundane Rune"] = list_prices[10]
    dict_names["Style Page: Opal Engine Guardian Greatsword"] = list_prices[11]
    dict_names["Hakeijo"] = list_prices[12]
    dict_names["Style Page: Opal Ilambris Sword"] = list_prices[13]
    dict_names["Potent Nirncrux"] = list_prices[14]
    dict_names["Aetherial Dust"] = list_prices[15]
    dict_names["Sealed Woodworking Writ"] = list_prices[16]
    dict_names["Columbine"] = list_prices[17]
    dict_names["Platinum Ounce"] = list_prices[18]
    dict_names["Rosin"] = list_prices[19]
    await ctx.send(dict_names)
    

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

"""channel = client.get_channel(1024849506258407454)
channel.send(old_data)"""
bot.run(TOKEN)
