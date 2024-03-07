import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode

from handlers import dp
from conf.config import settings

# Bot token is obtained via BotFather (t.me/botfather)
TOKEN = settings.BOT_TOKEN


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
