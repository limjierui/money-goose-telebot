import logging
from moneyGooseBot.master_mind import *
from moneyGooseBot.credentials import URL, reset_key, bot_token, bot_user_name
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

bot = telegram.Bot(token=bot_token)
# Step 1
# Start the local debugging session by entering  python3 local_debug.py 

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    """Start the bot. Entry point for the debugging session"""
    print("Start local debugging session")
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # a command is / + text
    # specify the command, then the function to handle comman
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    # on noncommand i.e message - echo the message on Telegram
    # any text/video/audio
    dp.add_handler(MessageHandler(Filters.text, message_parser))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def message_parser(update, context):
    return mainCommandHandler(incoming_message = update.message, telebot_instance=bot)


if __name__ == '__main__':
    main()
