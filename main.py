import scrapper
from bot import send_holiday

for holiday in scrapper.get_holidays():
    send_holiday(holiday)
