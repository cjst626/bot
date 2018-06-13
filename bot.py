import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
        print("Verification for me")
        print (bot.user.id)

@bot.command(pass_context=True)
async def commands(cxt):
    await bot.say("!commands, !Get_Help, !Sherpa, !Lore, !Random_Lore, !Bungie, !Bnet, !Forsaken, !Warmind, !Forsaken_reveal, !rat_king, !legend_of_acrius, !sturm_and_drang, !mida_multi_tool, !borealis, !INFO, !NEWS, !DLC, !exotics, !WorldLine_zero, !Sleeper, !Wormgod_caress, !Wormhusk_crown, !Veritys_brow, !Fragments_Nodes.")

@bot.command(pass_context=True)
async def Bungie(cxt):
    await bot.say("https://www.bungie.net/")

@bot.command(pass_context=True)
async def Bnet(cxt):
    await bot.say("https://www.blizzard.com/en-us/")

@bot.command(pass_context=True)
async def rat_king(cxt):
    await bot.say(" https://www.youtube.com/watch?v=9qwsLxb2IlY ")

@bot.command(pass_context=True)
async def legend_of_acrius(cxt):
    await bot.say(" https://www.youtube.com/watch?v=K_jBXm1zXJY ")

@bot.command(pass_context=True)
async def mida_multi_tool(cxt):
    await bot.say(" https://www.youtube.com/watch?v=XT0Fs-9Owcg ")

@bot.command(pass_context=True)
async def borealis(cxt):
    await bot.say("the Borealis is not avalable to PC and Xbox one but on Playstation 4 the boreialis can be obtained through vendor packages from Banshee-44.")

@bot.command(pass_context=True)
async def INFO(cxt):
    await bot.say("coming to you from Unknown player :  https://www.youtube.com/watch?v=PZZaWEGhxi8  .")

@bot.command(pass_context=True)
async def DLC(cxt):
    await bot.say("The new DLC, Forsaken, is comeing in September and will be the second year of Destiny 2 use command 'Forsaken' for more information. ")

@bot.command(pass_context=True)
async def Warmind(cxt):
    await bot.say("The DLC can be found at https://www.destinythegame.com/buy ")

@bot.command(pass_context=True)
async def NEWS(cxt):
    await bot.say("News updates from Unknown player : https://www.youtube.com/watch?v=YT24D1Um3dk  ")

@bot.command(pass_context=True)
async def exotics(cxt):
    await bot.say("There are going to be more exotics uncovered but this is a headstart for those who want to collect 'em all, *warning* there may be story spoilers ahead. https://www.youtube.com/watch?v=IjINAi-S_uQ")

@bot.command(pass_context=True)
async def Daddy(cxt):
    await bot.say("Why does Xur have to go to different planets each weekend?   It's for his own Xurvival.")

@bot.command(pass_context=True)
async def  Sleeper(cxt):
    await bot.say ("Sleeper simulant Quest break down by Datto https://www.youtube.com/watch?v=wiMG8bBTfDY " )

@bot.command(pass_context=True)
async def WorldLine_zero(cxt):
    await bot.say ("Worldline zero quest with the 45 data fragments by Datto https://www.youtube.com/watch?v=RI5KQ_yQLoU ")


text = "the Wormgod caress, the Wormhusk crown, and Verity's Brow are all unlocked from completing the Warmind campaign on said character."

@bot.command(pass_context=True)
async def Wormgod_caress(cxt):
    await bot.say (text)

@bot.command(pass_context=True)
async def Wormhusk_crown(cxt):
    await bot.say (text)

@bot.command(pass_context=True)
async def Veritys_brow(cxt):
    await bot.say (text)

@bot.command(pass_context=True)
async def Dad_jokes(cxt):
    await bot.say(random.choice(jokes))

@bot.command(pass_context=True)
async def Fragments_Nodes(cxt):
    await bot.say ("All data fragments and nodes can be found here by Unknow player https://www.youtube.com/watch?v=-fQbCOIk6pE&t=87s")

@bot.command(pass_context=True)
async def Forsaken(cxt):
    await bot.say ("The new DLC info and purchase location on Battle.net https://us.shop.battle.net/en-us/product/destiny2-forsaken")

@bot.command(pass_context=True)
async def Forsaken_reveal(cxt):
    await bot.say ("The announcement video/Vidoc https://www.youtube.com/watch?v=vQDH-3Hu4PI&feature=youtu.be ")

@bot.command(pass_context=True)
async def Lore(cxt):
    await bot.say(random.choice(lore))

@bot.command(pass_context=True)
async def Random_Lore(cxt):
    await bot.say("you can pick out a lore entry for your self: https://www.ishtar-collective.net/  ")

@bot.command(pass_context=True)
async def Sherpa(cxt):
    await bot.say("If you are looking to become a sherpa you should talk with AGreeNer#2539 so that you can apply for the sherpa 'position' *please dont put me out of a job* -CJST626")

@bot.command(pass_context=True)
async def Get_Help(cxt):
    await bot.say("You should contact one of our Sherpas or Admins located on the right side of your discord app, look for the Gold, Blue, and Pink profile names.")




jokes = [    
    "How does Kabr fix his cerial? Vex milk first.\nOuch.",
    "What is a Goblins favorite instrument? a Harpy.",
    "Why couldn't Osiris find his glasses?  Because he lost his lenses.",
    "Why is the crucible like a christmas tree?  Because Uriel gave every one gifts.",
    "Whats a Hobgoblins favorite song? Vex gon' give it to ya'.",
    "What did one Hobgoblin say to the other when it killed a gaurdian? That was a Vexcellent shot!",
    "Whats a fallens favourite holiday? Shanksgiving.",
    "what do gaurdians mix their eggs with?  Wisk-runner.",
    "Where on earth can you buy exotics?!?! in the Xur-opean Dead zone.",
    "What do the doctors in the tower give kids when they have low vitamin D?   A Sunshot.",
    "What do gaurdians eat for breakfast?  nothing special, usually something light.",
    "Why did Ghaul have so much confidence in his plan? because he took the gaurdians light-ly.",
    "What do you get when you cross a Cabal with a subatomic particle? a Valus electron.",
]

lore = [
    "Cayde-06:  https://www.ishtar-collective.net/categories/cayde-6",
    "Ana Bray:  https://www.ishtar-collective.net/categories/ana-bray",
    "Alpha Lupi:  https://www.ishtar-collective.net/categories/alpha-lupi",
    "Exo Stranger:  https://www.ishtar-collective.net/categories/the-exo-stranger",
    "Crota:  https://www.ishtar-collective.net/categories/the-first-crota-fireteam",
    "Kabr:  https://www.ishtar-collective.net/categories/kabr",
    "The Nine: https://www.ishtar-collective.net/categories/the-nine",
    ]


bot.run("NDM5MTI5MjEzNjkwNDQ1ODI0.DgBPIw.HCUJAXUIN45Lt2iALs9sKS_Vnbg")