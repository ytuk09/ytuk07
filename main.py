from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "extract-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "👋 Hello!\nSend me any message or link.\nBot is running successfully 🚀"
    )

@app.on_message(filters.text)
async def echo(client, message):
    await message.reply_text(f"Received:\n{message.text}")

print("Bot Started Successfully 🚀")

app.run()
