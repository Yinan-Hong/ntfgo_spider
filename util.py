from config import *
from datetime import datetime
import csv
from selenium import webdriver
import json


def set_up():
    chrome_options = webdriver.ChromeOptions()
    # 开启无头模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    global DRIVER
    DRIVER = webdriver.Chrome()

    field_names = ['name', 'time(utc)', 'avgPrice',
                   'floorPrice', 'salesScatter', 'marketCap', 'volume']
    with open('res.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writerow({
            'name': 'name',
            'time(utc)': 'time(utc)',
            'avgPrice': 'avgPrice(ETH)',
            'floorPrice': 'floorPrice(ETH)',
            'salesScatter': 'salesScatter(ETH)',
            'marketCap': 'marketCap($)',
            'volume': 'volume($)'
        })


def get_top_10_collections():
    print('Retrieving top 10 collections')
    url = BASE_URL + TOP_COLLECTION_PATH
    DRIVER.get(url)
    text = DRIVER.find_element_by_tag_name('pre')
    data = json.loads(text.text)

    users = []
    for user in data['data']['list']:
        info = {}
        info['id'] = user['id']
        info['name'] = user['name']
        users.append(info)

    return users


def time_formatter(timestamp):
    # change timestamp to utc format
    timestamp //= 1000
    return datetime.fromtimestamp(timestamp)


def get_asset_info(id):
    # get marketcap and volume
    url1 = BASE_URL + USER_DATA_PATH + id + \
        MARKETCAP_VOLUME_REQUEST_PATH + id + RANGE
    DRIVER.get(url1)
    text1 = DRIVER.find_element_by_tag_name('pre')
    cap_vol_data = json.loads(text1.text)

    # get price
    url2 = BASE_URL + USER_DATA_PATH + id + PRICE_REQUEST_PATH + id + RANGE
    DRIVER.get(url2)
    text2 = DRIVER.find_element_by_tag_name('pre')
    price_data = json.loads(text2.text)

    return cap_vol_data['data']['marketCap']['values'], cap_vol_data['data']['volume']['values'], price_data['data']


def csv_handler(user):
    with open('res.csv', 'a') as file:
        field_names = ['name', 'time(utc)', 'avgPrice',
                       'floorPrice', 'salesScatter', 'marketCap', 'volume']
        writer = csv.DictWriter(file, fieldnames=field_names)
        name = user['name']

        # write in current user's info
        for i in range(30):
            data = {
                'name': name,
                'time(utc)': time_formatter(user['market_cap']['x'][i]),
                'avgPrice': user['price']['avgPrice']['values']['y'][i],
                'floorPrice': user['price']['floorPrice']['values']['y'][i],
                'salesScatter': user['price']['salesScatter']['values']['y'][i],
                'marketCap': user['market_cap']['y'][i],
                'volume': user['volume']['y'][i]
            }
            writer.writerow(data)


def get_data():
    print('-----------START-------------')
    # retrieve users info
    users = get_top_10_collections()

    # retrieve trading-info of each user
    for user in users:
        print(
            'Retrieving information from collection owner \'{}\''.format(user['name']))
        user['market_cap'], user['volume'], user['price'] = get_asset_info(
            user['id'])
        csv_handler(user)

    print('-----------DONE-------------')
