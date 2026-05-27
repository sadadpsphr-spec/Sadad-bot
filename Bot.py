import telebot
from datetime import datetime

TOKEN = 916908668:FF8og8rbsWjGt7s3j-CAQcTS29n3NuHgVec

bot = telebot.TeleBot(TOKEN)

appointments = {}

WORK_HOURS = [8,9,10,11,12,13,14,15]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "✂️ به ربات نوبت‌دهی سداد خوش آمدید\n\n1️⃣ رزرو نوبت\n2️⃣ نوبت‌های من")

@bot.message_handler(func=lambda m: True)
def handle(message):
    text = message.text
    cid = message.chat.id

    if text == "1" or text == "رزرو نوبت":
        bot.send_message(cid, "📅 تاریخ را وارد کنید (مثلاً 2026-05-27)")
    
    elif text == "2":
        user_apps = appointments.get(cid, [])
        if not user_apps:
            bot.send_message(cid, "نوبتی ندارید")
        else:
            bot.send_message(cid, str(user_apps))
    
    elif "-" in text:
        bot.send_message(cid, "⏰ ساعت را وارد کنید (8 تا 15)")
    
    elif text.isdigit():
        hour = int(text)
        if hour in WORK_HOURS:
            appointments.setdefault(cid, []).append(text)
            bot.send_message(cid, "✅ نوبت ثبت شد")
        else:
            bot.send_message(cid, "⛔ خارج از ساعت کاری")

bot.infinity_polling()
