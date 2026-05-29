import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

print("🚀 BOT STARTED")

async def start(update, context):
    await update.message.reply_text("🔥 BorykNews Bot працює!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
