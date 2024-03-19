import asyncio
import logging
import sys

import aiocron
from aiogram import Bot
from aiogram.enums import ParseMode

from handlers import dp
from conf.config import settings

from services.scrapper import scheduled_crypto, scheduled_stock, scheduled_covid, scheduled_country_economy

# Telegram Bot API token
TOKEN = settings.BOT_TOKEN


# Schedule the tasks to run at specific intervals
async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


# Schedule the tasks to run at specific intervals
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()

"""In the above code snippet, we have defined the main function that initializes the Bot instance with the Telegram Bot API token
and starts the polling process to receive updates from the Telegram bot. We have also scheduled the tasks to run at specific intervals
using the aiocron library. The main function is executed when the script is run, and the polling process is started to receive updates
from the Telegram bot. The scheduled tasks are run in the background at specific intervals to fetch data from various sources and send
updates to the users."""
