
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to HMP AI Cartoon Studio!\n\n"
        "မင်္ဂလာပါ။ Cartoon Video ဖန်တီးဖို့ ကြိုဆိုပါတယ်။\n\n"
        "ကိုယ်ပိုင် သို့မဟုတ် အသုံးပြုခွင့်ရှိတဲ့ "
        "ဗီဒီယိုကို ပေးပို့နိုင်ပါတယ်။"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "အသုံးပြုပုံ\n"
        "1. Video ပေးပို့ပါ။\n"
        "2. Cartoon Style ရွေးပါ။\n"
        "3. AI Processing ကို စတင်ပါ။"
    )

async def receive_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Video လက်ခံရရှိပါပြီ။\n"
        "နောက်အဆင့်မှာ AI နဲ့ Cartoon ပြောင်းလဲမှု "
        "စနစ်ကို ချိတ်ဆက်ပါမယ်။"
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.VIDEO | filters.Document.VIDEO, receive_video)
    )

    print("HMP Cartoon Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
