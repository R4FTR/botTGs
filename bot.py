from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "7932007378:AAFPSTg7QvGmrizjRrvbATqZ26FoSWaPGd0"   # <-- замени на свой!

async def start(update: Update, context):
    await update.message.reply_text(f"Привет, {update.effective_user.full_name}! Я эхо-бот.")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()



#7932007378:AAFPSTg7QvGmrizjRrvbATqZ26FoSWaPGd0
