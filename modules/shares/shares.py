import argparse
import sys
import os
from datetime import datetime

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests


load_dotenv()

# def dt_to_unixtime(dt):
#     return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ').timestamp()

def clean_up(row):
    curr_price = float(row['values'][0]['close'])
    currency = row['meta']['currency']
    ts = row['values'][0]['datetime']
    symbol = row['meta']['symbol']
    exchange_tz = row['meta']['exchange_timezone']
    return {
        'symbol': symbol,
        'currency': currency,
        'price': curr_price,
        'exchange_tz': exchange_tz,
        'ts': ts
    }

def get_stock_data(symbol=None, url=None):

    if not url: 
        base_url = os.getenv('SHARES_BASE_URL')
        key = os.getenv('SHARES_TWELVEDATA_KEY')
        payload = {
            'apikey': key, 
            'interval': '1min',
            'symbol': symbol
        }
        url = base_url
    
    try:
        resp = requests.get(url, params=payload)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'Failed response from {url}')
        print(e.request)
        print(e.response)
        sys.exit(1)

    data = resp.json()
    clean_data = clean_up(data)
    return clean_data

# def transmit(data):
#     hub_url = os.getenv('ELECTRICITY_API_URL')
    
#     try:
#         r = requests.post(hub_url, json=data)
#         r.raise_for_status()
#         print(r.json())
#     except requests.exceptions.ConnectionError as e:
#         print(f'Failed to connect to {hub_url}')
#         print(f'With payload: {data}')
#         print(e.request)
#         sys.exit(1)
#     except requests.exceptions.HTTPError as e:
#         print(f'Invalid request sent to {hub_url}')
#         print(f'With payload: {data}')
#         print(e.request)
#         sys.exit(1)

def get_watch_list():
    watch_list = os.getenv('SHARES_WATCH_LIST').split(',')
    return watch_list

def main():
    watch_list = get_watch_list()
    symbol_data = [get_stock_data(s) for s in watch_list]
    # d = get_stock_data(wl[0])
    print(symbol_data)
    print(f'{datetime.now()} --- done')

if __name__ == '__main__':
    # argParser = argparse.ArgumentParser()
    # argParser.add_argument("-r", "--rows", type=int, default=10, help="Number of rows to request")
    # args = argParser.parse_args()

    main()
