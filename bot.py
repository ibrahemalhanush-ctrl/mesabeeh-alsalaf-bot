import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("يرجى ضبط BOT_TOKEN في إعدادات التشغيل")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        InlineKeyboardButton("📚 المشايخ", callback_data="sheikhs"),
        InlineKeyboardButton("📖 الدورات والسلاسل", callback_data="courses"),
        InlineKeyboardButton("📝 الاختبارات", callback_data="quizzes"),
        InlineKeyboardButton("📊 تقدمي في التعلم", callback_data="progress"),
        InlineKeyboardButton("🔖 دروسي المحفوظة", callback_data="saved")
    )

    bot.send_message(
        message.chat.id,
        "💡 أهلاً بك في مصابيح السلف\n\n"
        "منصتك لتنظيم الدروس العلمية ومتابعة رحلتك في طلب العلم.\n\n"
        "اختر من القائمة:",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    messages = {
        "sheikhs": "📚 قسم المشايخ: سنضيف أسماء المشايخ ودروسهم قريباً.",
        "courses": "📖 قسم الدورات: سنضيف الدورات والسلاسل العلمية قريباً.",
        "quizzes": "📝 قسم الاختبارات: سنضيف الاختبارات بعد تجهيز الدروس.",
        "progress": "📊 سيظهر تقدمك هنا بعد إضافة نظام متابعة الدروس.",
        "saved": "🔖 لم تحفظ أي دروس بعد."
    }

    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        messages.get(call.data, "اختر أحد الخيارات من القائمة الرئيسية.")
    )

if __name__ == "__main__":
    print("مصابيح السلف يعمل...")
    bot.infinity_polling()
