import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.constants import ParseMode

# Get the bot token from Railway environment variables
TOKEN = os.getenv("ARCANE_BOT_TOKEN")

if not TOKEN:
    print("❌ Error: Bot token not found! Set ARCANE_BOT_TOKEN in Railway environment variables.")
    exit(1)

# Game list with your hosted game link and other WebGL games
GAMES = [
    ("🕹 Cube 3D", "https://dwip-biswas.github.io/G1/"),
    ("🕹 Fluid Simulator", "https://paveldogreat.github.io/WebGL-Fluid-Simulation/"),
    ("🕹 Mount Blanc Explorer", "https://therace.montblancexplorer.com"),
    ("🕹 Egg Hunt", "https://egghunt.merci-michel.com"),
    ("🕹 Interland", "https://beinternetawesome.withgoogle.com/en_us/interland/kind-kingdom"),
]

# Arcade-style welcome message
async def start(update: Update, context: CallbackContext):
    welcome_text = (
        "🕹️ *WELCOME TO ARCANE ARCADE* 🕹️\n"
        "══════════════════\n\n"
        "🔥 *THE ULTIMATE GAMING BOT* 🔥\n\n"
        "🎮 Play mini-games right inside Telegram!\n\n"
        "💀 Challenge your friends & beat high scores!\n\n"
        "⚡ Pick a game & start playing NOW!\n"
        "══════════════════\n\n"
        "🔻 *AVAILABLE GAMES:* 🔻"
    )

    # Create buttons for all games
    keyboard = [[InlineKeyboardButton(game[0], url=game[1])] for game in GAMES]
    
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
