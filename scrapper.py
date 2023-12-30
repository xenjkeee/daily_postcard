import requests
from bs4 import BeautifulSoup


def __soup_html(url='https://nationaltoday.com/today/'):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def __to_holiday(self, title_class='holiday-title', excerpt_class='excerpt'):
    title_tag = self.find(class_=title_class)
    description_tag = self.find(class_=excerpt_class)
    image_url = self.find('a').get('style')[22:][:-2] if self.find('a') is not None else None
    return {
        'title': title_tag.text if title_tag is not None else None,
        'description': description_tag.text if description_tag is not None else None,
        'link': self.find('a').get('href') if self.find('a') is not None else None,
        'image': requests.utils.requote_uri(image_url) if image_url is not None else None,
    }


def __scrap_holidays(soup, card_class='day-card'):
    return list(map(lambda tag: __to_holiday(tag), soup.find_all(class_=card_class)))


def get_holidays():
    unfiltered = __scrap_holidays(soup=__soup_html())
    return list(filter(lambda x: x['title'] is not None, unfiltered))
