print("🔥 BOT FILE STARTED")

from telegram.ext import Updater

def main():
    print("🚀 MAIN START")

    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()