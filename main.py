import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

TOKEN_DEFAULT = os.getenv('TOKEN')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()
    user_link = args.link.strip()

    link_data = get_link_counter(user_link)
    if link_data:
        answer = ["Короткая ссылка: {}".format(user_link), 'Количество переходов:']
        for day_stat in link_data['link_clicks']:
            answer.append('{} переходов: {}'.format(day_stat['date'][:10], day_stat['clicks']))      
        print('\n'.join(answer))
    else:
        response = make_short_link(user_link)
        if response:
            print(response)
        else:
            print('Неправильный формат ссылки')


def make_short_link(long_link, token=TOKEN_DEFAULT):
    """
    Функция делает короткую ссылку вида bit.ly/2GyKlVv из стандартного url
    """
    authorization = 'Bearer {}'.format(token)
    headers = {
        'Authorization': authorization,
    }
    params = {
        'long_url': long_link
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, json=params, headers=headers)
    if response.ok:
        link_tag = response.json()
        return link_tag['link']
    else:
        return None


def get_link_counter(bitlink, token=TOKEN_DEFAULT):
    """
    Функция возвращает статистику кликов по короткой ссылки за последний месяц (по дням)
    """
    authorization = 'Bearer {}'.format(token)
    headers = {
        'Authorization': authorization,
    }

    if bitlink.startswith('http://bit.ly'):
        bitlink = bitlink[7:]
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks'.format(bitlink=bitlink)
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    main()
