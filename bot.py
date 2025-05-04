import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# Список инструкций
instructions = [
    "STRANGER HANDSHAKE\n\nShake hands with someone you’ve never met. Then sip.",
    "EYE CONTACT\n\nLook someone in the eye for five seconds. Then drink.",
    "INVISIBLE CHEERS\n\nToast without clinking glasses.\nJust imagine the sound. Drink.",
    "UNEXPECTED GIFT\n\nApproach someone and silently offer them something small that you have in your pocket or bag. Watch their reaction. Then sip.",
    "FORWARD STEP\n\nTake a step toward someone, but stop just before you touch them. Then sip.",
    "INVISIBLE OBJECT\n\nPretend to hold an object and pass it to someone. Drink.",
    "COLOR CONNECTION\n\nFind a color that both you and another person are wearing. Briefly describe a scene or place you associate with that color, then share it with each other. Then sip.",
    "COMPLIMENT CIRCLE\n\nGive a genuine compliment to someone. Then sip.",
    "SHARED SILENCE\n\nSit next to someone in silence for one minute. Then drink.",
    "TOAST TO THE FUTURE\n\nToast to something that hasn’t happened yet. Then sip.",
    "SIMPLE DRAWING\n\nDraw something with your eyes closed for 30 seconds and then show it to someone. Let them guess what it is. Then sip.",
    "SHARE A MEMORY\n\nShare a short happy memory from your childhood with someone. Then drink.",
    "PAUSE AND LISTEN\n\nFind a spot where there’s background noise (like a conversation, music, or nature sounds). Stand still for 1 minute and listen. Try to identify every sound you can. Drink.",
    "THE SPONTANEOUS SHOT\n\nAsk someone to take a photo of you with the person closest to you right now. Afterward, share what you think about the moment captured. Then drink.",
    "MYSTERY OBJECT\n\nPick an object from your bag or pocket (without showing it to anyone) and describe it to someone. Let them guess what it is. Then sip."
]

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🍸 get a score", callback_data="get_instruction")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "<b>Hey there! Welcome to Gin Scores Bot.</b>\n\n"
        "Maybe you’re here because you’re holding a bottle of A Gin to Gather.\n\n"
        "If so — that’s no coincidence.\n\n"
        "This gin is a handcrafted drink born from a collaboration between Bauhaus students and Wiegand Manufactur Weimar.\n\n"
        "It’s created to bring people together: students and professors, friends and strangers. Each sip is like an individual element that becomes part of something bigger when shared with others.\n\n"
        "Inspired by Fluxus “event scores,” this bot gives you playful, poetic prompts to break the ice, to spark a moment, to gather.\n\n"
        "Tap below to get your first instruction — and let the gathering begin."
    )

    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")

# Обработка нажатия кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    instruction = random.choice(instructions)
    keyboard = [[InlineKeyboardButton("🍸 get another score", callback_data="get_instruction")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=instruction, reply_markup=reply_markup)

# Запуск бота
if __name__ == '__main__':


    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()

