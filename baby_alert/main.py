import discord
import sys
import os
import asyncio
from pathlib import Path
from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).resolve().parents[1]))

print("環境変数一覧:", list(os.environ.keys()))
ALERT_CHANNEL_NAME="志輝"
USER_ID= "515881330253365263"

# インテントの設定
intents = discord.Intents.default()

bot = discord.Client(intents=intents)

#app = Flask(__name__)
app = FastAPI()

@app.post("/baby_cry")
async def baby_cry():
    print("赤ちゃんが泣いてる！")

    await sendAlert()
    
    return {"status": "ok"}


async def sendAlert():
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=ALERT_CHANNEL_NAME)
        if channel:
            await channel.send(f"<@{USER_ID}> 志輝が泣いてる！！！")

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

async def start_web():
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=int(os.environ["PORT"])
    )
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        bot.start(os.getenv("DISCORD_BOT_TOKEN")),
        start_web()
    )

asyncio.run(main())

