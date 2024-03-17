import asyncio
import logging
import sys

import aiocron
from aiogram import Bot
from aiogram.enums import ParseMode

from handlers import dp
from conf.config import settings

from services.scrapper import scheduled_crypto, scheduled_stock, scheduled_covid, scheduled_country_economy

TOKEN = settings.BOT_TOKEN


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
