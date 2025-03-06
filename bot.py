import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.constants import ParseMode

# Get the bot token from Railway environment variables
TOKEN = os.getenv("ARCANE_BOT_TOKEN")

if not TOKEN:
    print("❌ Error: Bot token not found! Set ARCANE_BOT_TOKEN in Railway environment variables.")
    exit(1)

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
async def start(update: Update, context: CallbackContext):
    welcome_text = (
        "🕹️👽 *WELCOME TO ARCANE ARCADE* 👽🕹️\n"
        "══════════════════\n\n\n"
        "🔥 *THE ULTIMATE GAMING BOT* 🔥\n\n"
        "🎮 Play mini-games right inside Telegram!\n\n"
        "💀 Challenge your friends & beat high scores!\n\n"
        "⚡ Pick a game & start playing NOW!\n"
        "══════════════════\n\n\n"
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

    await update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Arcane Arcade Bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
