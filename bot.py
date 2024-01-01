from telegram import Bot
import asyncio


async def __send_holiday(holiday, bot_token, chat_id):
    from mappers import to_pretty_text_message
    bot = Bot(token=bot_token)
    await bot.send_photo(chat_id=chat_id,
                         photo=holiday['image'],
                         caption=to_pretty_text_message(holiday), parse_mode='HTML')
    await asyncio.sleep(5)


def send_holiday(holiday, bot_token, chat_id):
    print(holiday)
    print('Sending...')
    try:
        asyncio.run(__send_holiday(holiday, bot_token, chat_id))
    except Exception as err:
        print(F'Failed! {str(err)}')
    print('--------------------------------------------------------')
