import requests
from bs4 import BeautifulSoup
from datetime import datetime


def __soup_html(url: str) -> BeautifulSoup:
    print(f'Request:{url}')
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def __parse_shares(text: str) -> int:
    parts = text.split()
    shares = parts[0] if parts else '0'
    return int(shares.lower().replace('k', '000'))


def __to_holiday(self: BeautifulSoup) -> dict:
    title_tag = self.find(class_='holiday-title')
    description_tag = self.find(class_='excerpt')
    image_url = self.find('a').get('style')[22:][:-2] if self.find('a') is not None else None
    shares_tag = self.find(class_='trending-share-count')

    return {
        'title': title_tag.text if title_tag is not None else None,
        'description': description_tag.text if description_tag is not None else None,
        'link': self.find('a').get('href') if self.find('a') is not None else None,
        'image': requests.utils.requote_uri(image_url) if image_url is not None else None,
        'shares': __parse_shares(shares_tag.text) if shares_tag is not None else 0
    }


def __scrap_holidays(soup: BeautifulSoup) -> [dict]:
    return list(map(lambda tag: __to_holiday(tag), soup.find_all(class_='day-card')))


def __get_current_link() -> str:
    link_format = 'https://nationaltoday.com/{date}-holidays/'
    current_time = datetime.now()
    formatted_date = current_time.strftime("%B-%-d").lower()
    return link_format.format(date=formatted_date)


def get_holidays() -> [dict]:
    """
    Load today url, parse and sort holidays

    :return: array of parsed holidays sorted by popularity
    """
    url = __get_current_link()
    unfiltered = __scrap_holidays(soup=__soup_html(url))
    filtered = list(filter(lambda x: x['title'] is not None, unfiltered))
    return sorted(filtered, key=lambda x: x['shares'], reverse=True)
