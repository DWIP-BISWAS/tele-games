import os
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# Get the bot token from Railway environment variables
TOKEN = os.getenv("ARCANE_BOT_TOKEN")

# Game list (You can add more games here)
GAMES = [
    ("🕹 Cube 3D", "cube3d"),
    ("⚽ Ultimate Football", "football"),
    ("🚀 Space Blaster", "spaceshooter"),
    ("🧩 Brain Puzzle", "puzzle"),
    ("🏎️ Neon Racer", "racing"),
    ("🎵 Beat Battle", "musicbattle"),
]

# Arcade-style welcome message
def start(update: Update, context: CallbackContext):
    welcome_text = (
        "🕹️👽 *WELCOME TO ARCANE ARCADE* 👽🕹️\n"
        "════════════════════════\n"
        "🔥 *THE ULTIMATE GAMING BOT* 🔥\n"
        "🎮 Play mini-games right inside Telegram!\n"
        "💀 Challenge your friends & beat high scores!\n"
        "⚡ Pick a game & start playing NOW!\n"
        "════════════════════════\n\n"
        "🔻 *AVAILABLE GAMES:* 🔻"
    )

    # Create arcade-style game buttons in a 2x2 layout
    keyboard = []
    for i in range(0, len(GAMES), 2):
        row = [
            InlineKeyboardButton(GAMES[i][0], url=f"https://t.me/{context.bot.username}?game={GAMES[i][1]}")
        ]
        if i + 1 < len(GAMES):
            row.append(InlineKeyboardButton(GAMES[i + 1][0], url=f"https://t.me/{context.bot.username}?game={GAMES[i + 1][1]}"))
        keyboard.append(row)

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

# Main function to run the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
