from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    # Main menu options
    main_menu_text = (
        "Welcome to Business Analyst Assistant!\n"
        "Choose an option:\n"
        "/stock_tracker - Stock Information\n"
        "/crypto_tracker - Cryptocurrency Price Tracker"
    )
    update.message.reply_text(main_menu_text)

def stock_tracker(update: Update, context: CallbackContext) -> None:
    # Sub-menu for stock information
    stock_menu_text = (
        "Ok, which stocks would you like to track?\n"
        "Options are:\n"
        "💻MSFT: 403.35\n"
        "📈Day Range: 403.44 - 408.29\n"
        "📊PE Ratio: 36.54\n"
        "📉52 Week Range: 245.61 - 420.82\n"
        # Add other stock options...
    )
    update.message.reply_text(stock_menu_text)

def crypto_tracker(update: Update, context: CallbackContext) -> None:
    # Sub-menu for cryptocurrency price tracker
    crypto_menu_text = (
        "Choose a cryptocurrency:\n"
        "💰BTC: $50,000\n"
        "📈24h Change: +5%\n"
        "🚀All-Time High: $60,000\n"
        # Add other crypto options...
    )
    update.message.reply_text(crypto_menu_text)

def main() -> None:
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stock_tracker", stock_tracker))
    dispatcher.add_handler(CommandHandler("crypto_tracker", crypto_tracker))

    # Start the bot
    updater.start_polling()
    updater.idle()

if name == "main":
    main()