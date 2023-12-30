from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

__chat_id = os.environ.get("DP_TARGET_CHAT_ID")
__bot_token = os.environ.get("DP_BOT_ACCESS_TOKEN")


async def __send_holiday(holiday):
    from mappers import to_pretty_text_message
    bot = Bot(token=__bot_token)
    await bot.send_photo(chat_id=__chat_id,
                         photo=holiday['image'],
                         caption=to_pretty_text_message(holiday), parse_mode='HTML')
    await asyncio.sleep(5)


def send_holiday(holiday):
    print(holiday)
    print('Sending...')
    try:
        asyncio.run(__send_holiday(holiday))
    except:
        print('Failed!')
    print('--------------------------------------------------------')
