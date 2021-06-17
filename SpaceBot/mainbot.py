import discord
from discord.ext import commands
import json
import requests
from api import(covidf)
from astroapi import(
    #apod,
    #caption,
    astrof
    )
from nextlunch import (next1f, next5f )
import mysql.connector

mydb = mysql.connector.connect(
  host="redacted",
  user="redacted",
  password="redacted",
  database="redacted"
)

TOKEN = 'redacted'

description = '''Space and general info bot'''
bot = commands.Bot(command_prefix='??', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def covid(ctx):
    """Gives API data on coronavirus"""

    await ctx.send(covidf())

@bot.command()
async def fact(ctx):
    """Gives a random fact"""
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    json_data = response.json()

    randfact=(json_data["text"])
    FactMsg=(randfact)
    await ctx.send(FactMsg.replace("`", "'"))

@bot.command()
async def nasapod(ctx):
    """gives NASA's image of the day"""

    await ctx.send(astrof())

@bot.command()
async def nextlaunch(ctx):
    """gives info on the next rocket launch"""
    await ctx.send(next1f())

@bot.command()
async def launches(ctx):
    """Gives info on the next 5 launches"""
    await ctx.send(next5f())

@bot.command()
async def spacex(ctx, message : str):
    """Returns data on spacex launches only. put mission name in qoutes"""
    mycursor = mydb.cursor()

    sql = "SELECT * FROM test.spacex WHERE name LIKE %s"
    adr =  ("%" + message + "%", )
    print(adr)
    print(sql + "\n")
    print("\n\n")
    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    await ctx.send(myresult[0][1])

@bot.command()
async def missions(ctx, message : str):
    """Returns data on all space launches. put mission name in qoutes"""
    mycursor = mydb.cursor()

    sql = "SELECT * FROM test.launches WHERE name LIKE %s"
    adr =  ("%" + message + "%", )
    print(adr)
    print(sql + "\n")
    print("\n\n")
    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()
    await ctx.send(myresult[0][1])

@bot.command()
async def github(ctx):
    """sends the github link to my source code, for those who are interested and for transparency. :)"""
    await ctx.send("https://github.com/SimonTheCommunist/SpaceBot")

@bot.command(pass_context=True)
async def psu(ctx):
    """sends a msg about psu"""
    await ctx.send(">>> it sounds like you are having an issue with power supplies. The optimal voltage and amps for the **Pi 3 is 5.1v, 2.5 amps**. \n**Pi4 is 5.1v, 3.5 amps.** You may also want to try disconnecting peripherals. Never use a phone charger.")


@bot.command(pass_context=True)
async def act(ctx):
    """sends a msg about act light codes"""
    acttext = "The green led next to red power one can indicate early boot problems \n" + ">>> ** 1 flash: ** Incompatible SD card\n **2 flashes:** SD card can not be read\n **3 flashes:** loader.bin not found\n **4 flashes** loader.bin not launched\n **5 flashes:** start.elf not found\n **6 flashes:** start.elf not launched\n **7 flashes** kernel.img not found\n"
    await ctx.send(acttext)

@bot.command()
async def hdmi(ctx):
    """sends a message to assist thoses who assist"""
    hdmimsg = ("**First:** check if the sd card is working, refer to ??act.\n**Second: ** Verify the hdmi cable is working. either try a different cable, or try the current one on another device.\n**Third:** Check if the power supply is sufficent. Refer to ??psu.\n**Fourth:** SSH into your pi and type ```sudo nano /boot/conifg.txt``` Find where it may say: ```#hdmi_force_hotplug=1\n#hdmi_drive=2``` and either remove the, # or type it in w/o the #. Restart the pi\n**Fifth:** if that didnt work, add `hdmi_safe=1` and restart.")
    await ctx.send(hdmimsg)

@bot.command()
async def channels(ctx):
    """directs people to the correct channel"""

    cgeneral = "<#204621105720328193>"
    techtalk = "<#413076326430539806>"
    memechat = "<#730101197079445555>"
    bcommands = "<#323186380379389952>"
    help1 = "<#204648659248218113>"
    help2 = "<#706717626822426705>"
    programming = "<#394965670523043840>"
    curchan = ("<#" + (str(ctx.channel.id) + ">"))

    if(curchan in [help1, help2, programming]):
        await ctx.send("It sounds like you have mistakenly asked a question in the wrong help channel for your problem.\n>>> If you have a programming problem, to get the best help, please go over too: " + programming + "\n If you need help with your pi, linux, hardware or software, " + help1 + " and" + help2 + " are the best place")
    elif(curchan in [cgeneral, techtalk]):
        await ctx.send(curchan + " is for discussion. \n>>> if you need help with your pi, linux, hardware or software, "
                       + help1 + " and" + help2 + " are the best place. We would appreciate it if you please used it instead.\nIf you are using bot commands or posting memes, please keep " + curchan + " free of clutter and use " + bcommands + " and " + memechat)
    else:
        await ctx.send("it seems you are in the wrong channel \n>>> " + cgeneral + " and " + techtalk + " is for discussion.\n" + help1 + " and " + help2 + "are for if you need help with your pi, linux, hardware or software" + programming + " is for getting help with programming. " )
@bot.command()
async def link(ctx, message : str):
    """creates a tinyurl of the one you sent"""
    longurl = message

    turl = 'http://tinyurl.com/api-create.php?url='+ longurl
    response = requests.get(turl)
    newurl = response.text
    await ctx.send(newurl)

@bot.command()
async def pinAmps(ctx):
    """relays how much current the pis 5 volt pin can output"""
    pinAmpsmsg = '>>> **How much current can the 5V pins supply?**\nThere is no simple answer to this. You can roughly calculate;\n min of polyfuse rating (2.5A for PI3) and power supply rating,\nminus the current required by the Pi itself (~750mA for Pi3, although this will increase for heavy use),\nminus USB peripheral current,\nminus Camera Module (~250mA if fitted),\nminus HDMI port (~50mA),\nminus Display (if fitted),\nminus 3.3V current supplied to external devices (including GPIO).'
    await ctx.send(pinAmpsmsg)

@bot.command()
async def mc(ctx):
    """sends a message explaining minecraft on the PI"""
    mcmsg = "The PI comes with its own, extremly limited native version of Minecraft. There is currently no offical native supported version of bedrock Minecraft and Java edition. There is an open source version for the Java edition, but it is difficult to get working, its slow and an older version.\n\nIt is not reccomended to use the Pi to host a MC server. Even if its only for a few people, even if its a bedrock server, even if you get the 8gb version of the pi. Performance will be incredibly slow, and render distance will be terrible. There are better cheap alternatives to make a Minecraft server."
    await ctx.send(mcmsg)
    
@bot.command()
async def ram(ctx):
    """sends a message explaining the 8gb model of raspberry pi, along with best use cases"""
    rammsg = "We do not reccomend you buy the 8gb model raspberry pi, for the majority of use cases. The increased memory gives minimal perforamnce gains per dollar. This is because any benifets more ram can give you, is limited by the speed of the proccessor.\n > so, what reason would there be to buy this model of Pi?\nYoud want to buy this model if you were to need the increased RAM. If you were using your Pi in some server applications, yes youd need it. Id you were to be doing some engineering simulations, yes. MATLAB, yes. Hosting a minecraft server? No. Daily Driver? No. Doing home automation? No. Programming code? No. "
    await ctx.send(rammsg)
    
@bot.command()
async def code(ctx):
    codemsg = "When sending code, or terminal readouts, please use **code blocks** or a code sharing website like https://pastebin.com or https://hastebin.com\nThis makes your code more readable, and easier for you to get help.\nCode blocks can be used by putting three backticks at the start and end of the code you copy and paste. They look like this \`\`\`\nThey can be found by the tilda key, and if you are using discord on IOS, you can hold down the ' key to bring up a menu to place them.\n> example:\n\`\`\`print(var)\`\`\`\n\n> They looks like:\n```print(var)```"
    await ctx.send(codemsg)
bot.run(TOKEN)
