import discord
import sys
import os
from pathlib import Path
from flask import Flask, request

sys.path.append(str(Path(__file__).resolve().parents[1]))

print("環境変数一覧:", list(os.environ.keys()))
ALERT_CHANNEL_NAME="志輝"

# インテントの設定
intents = discord.Intents.default()

bot = discord.Client(intents=intents)
bot.run(os.getenv("DISCORD_BOT_TOKEN"))


app = Flask(__name__)

@app.route("/baby_cry", methods=["POST"])
def baby_cry():
    print("赤ちゃんが泣いてる！")

    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=ALERT_CHANNEL_NAME)
            if channel:
                await channel.send("@ukauka 志輝が泣いてる！！！")

    return "ok"

app.run(host="0.0.0.0", port=5000)

