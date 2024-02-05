import discord, asyncio, pytz
from datetime import datetime, time
from discord.ext import commands

bot = commands.Bot(command_prefix="e!", intents=discord.Intents.all())

user_id = 22 #id de la personne à DM, sans "

@bot.event
async def on_ready():
    print("CLAIM_BOT en ligne !")
    message_envoye = False

    while True:
        now = datetime.now(tz=pytz.timezone("Europe/Paris"))
        heure_actuelle = now.time()

        print(heure_actuelle) #ça envoye dans la console tout les heures juste à l'heure prévue
        print()

        if heure_actuelle >= time(20, 11) and not message_envoye: #time(20, 11), c'est l'heure, là c'est tout les jours à 20h11
            print("Message envoyé avec succès !")
            user = await bot.fetch_user(user_id)
            await user.send("<:elexyr22:1067501213085597806> || <@902859548740698144> || - Il faut faire les [Reward](https://rewards.bing.com/) ! <a:alerterouge:1147554988596412495> ")
            message_envoye = True

        await asyncio.sleep(1)

        if now.hour == 0 and now.minute == 0 and now.second == 0:
            message_envoye = False

bot.run("TOKEN")