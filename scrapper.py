import requests
from bs4 import BeautifulSoup
from datetime import datetime


def __soup_html(url):
    print(f'Request:{url}')
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def __parse_shares(text):
    parts = text.split()
    shares = parts[0] if parts else '0'
    return shares.lower().replace('k', '000')


def __to_holiday(self, title_class='holiday-title', excerpt_class='excerpt'):
    title_tag = self.find(class_=title_class)
    description_tag = self.find(class_=excerpt_class)
    image_url = self.find('a').get('style')[22:][:-2] if self.find('a') is not None else None
    shares_tag = self.find(class_='trending-share-count')

    return {
        'title': title_tag.text if title_tag is not None else None,
        'description': description_tag.text if description_tag is not None else None,
        'link': self.find('a').get('href') if self.find('a') is not None else None,
        'image': requests.utils.requote_uri(image_url) if image_url is not None else None,
        'shares': int(__parse_shares(shares_tag.text) if shares_tag is not None else '0')
    }


def __scrap_holidays(soup, card_class='day-card'):
    return list(map(lambda tag: __to_holiday(tag), soup.find_all(class_=card_class)))


def __get_current_link():
    link_format = 'https://nationaltoday.com/{date}-holidays/'
    current_time = datetime.now()
    formatted_date = current_time.strftime("%B-%-d").lower()
    return link_format.format(date=formatted_date)


def get_holidays():
    url = __get_current_link()
    unfiltered = __scrap_holidays(soup=__soup_html(url))
    filtered = list(filter(lambda x: x['title'] is not None, unfiltered))
    return sorted(filtered, key=lambda x: x['shares'], reverse=True)
