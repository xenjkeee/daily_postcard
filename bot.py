from telegram import Bot
import asyncio


async def __send_holiday(holiday: object, bot_token: str, chat_id: str) -> None:
    from mappers import to_pretty_text_message
    bot = Bot(token=bot_token)
    await bot.send_photo(chat_id=chat_id,
                         photo=holiday['image'],
                         caption=to_pretty_text_message(holiday), parse_mode='HTML')
    await asyncio.sleep(5)


def send_holiday(holiday: dict, bot_token: str, chat_id: str) -> None:
    """
    Post holiday info to the Telegram channel.

    :param holiday: dict representing holiday
    :param bot_token: bot access token
    :param chat_id: target telegram chat id
    """
    print(holiday)
    try:
        asyncio.run(__send_holiday(holiday, bot_token, chat_id))
    except Exception as err:
        print(f'Failed! {str(err)}')
    print('--------------------------------------------------------')
