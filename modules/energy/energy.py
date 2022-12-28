import argparse
import sys
import os
from datetime import datetime

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests


load_dotenv()

def dt_to_unixtime(dt):
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ').timestamp()

def clean_up(row):
    return {
        "product": "Electricity",
        'interval_start': dt_to_unixtime(row['interval_start']),
        'interval_end': dt_to_unixtime(row['interval_end']),
        'consumption': row['consumption']
    }

def get_electricity_usage(max_rows, url=None):
    basic_auth = HTTPBasicAuth(os.getenv('ELECTRICITY_API_KEY'), '')
    
    if not url:
        e_mpan = os.getenv('ELECTRICITY_MPAN')
        e_serial = os.getenv('ELECTRICITY_SERIAL')
        base_url = os.getenv('ELECTRICITY_BASE_URL')
        url = f'{base_url}electricity-meter-points/{e_mpan}/meters/{e_serial}/consumption/?page_size={max_rows}'
    
    try:
        resp = requests.get(url, auth=basic_auth)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'Failed response from {url}')
        print(e.request)
        print(e.response)
        sys.exit(1)

    data = resp.json()['results']

    clean_data = [clean_up(r) for r in data]
    return clean_data

def transmit(data):
    hub_url = os.getenv('ELECTRICITY_API_URL')
    
    try:
        r = requests.post(hub_url, json=data)
        r.raise_for_status()
        print(r.json())
    except requests.exceptions.ConnectionError as e:
        print(f'Failed to connect to {hub_url}')
        print(f'With payload: {data}')
        print(e.request)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f'Invalid request sent to {hub_url}')
        print(f'With payload: {data}')
        print(e.request)
        sys.exit(1)

def main(max_rows):
    data = get_electricity_usage(max_rows)
    transmit(data)
    print(f'{datetime.now()} --- done')

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-r", "--rows", type=int, default=10, help="Number of rows to request")
    args = argParser.parse_args()

    main(max_rows=args.rows)
