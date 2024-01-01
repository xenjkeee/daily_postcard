import scrapper
from bot import send_holiday
import os

CHAT_ID = os.environ.get("DP_TARGET_CHAT_ID")
BOT_TOKEN = os.environ.get("DP_BOT_ACCESS_TOKEN")


def post_holidays():
    for holiday in scrapper.get_holidays():
        send_holiday(holiday, BOT_TOKEN, CHAT_ID)


if __name__ == "__main__":
    print('job started')
    post_holidays()
    print('job finished')
