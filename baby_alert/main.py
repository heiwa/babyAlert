import discord
import sys
import os
import asyncio
from pathlib import Path
from flask import Flask, request

sys.path.append(str(Path(__file__).resolve().parents[1]))

print("環境変数一覧:", list(os.environ.keys()))
ALERT_CHANNEL_NAME="志輝"

# インテントの設定
intents = discord.Intents.default()

bot = discord.Client(intents=intents)

app = Flask(__name__)

@app.route("/baby_cry", methods=["POST"])
def baby_cry():
    print("赤ちゃんが泣いてる！")

    asyncio.run(sendAlert())


async def sendAlert():
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=ALERT_CHANNEL_NAME)
        if channel:
            await channel.send("@ukauka 志輝が泣いてる！！！")

async def main():
    await asyncio.gather(
        app.run(host="0.0.0.0", port=5000),
        bot.run(os.getenv("DISCORD_BOT_TOKEN"))
    )

asyncio.run(main())

