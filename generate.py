import os
from datetime import datetime
from pprint import pprint

import requests

url_base = os.environ.get('URL_BASE') or 'https://smart.caveon.com'
access_token = os.environ.get('ACCESS_TOKEN') or input('Access token: ')
item_id = os.environ.get('ITEM_ID') or input('Item ID: ')
n_str = os.environ.get('NUM_INSTANCES') or input('How many instances would you like to generate? ')
n = int(n_str)

headers = {
    'Authorization': 'Bearer {0}'.format(access_token)
}

item_url = '{0}/api/v1/items/{1}'.format(url_base, item_id)
item_request = requests.get(item_url, headers=headers)
item_json = item_request.json()
template_ids = item_json['templateIds']

# TODO: let them pick a template if the item has more than one templateId

gen_url = '{0}/api/v1/items/{1}/generate'.format(url_base, item_id)
gen_payload = {
    'n': n
}
gen_request = requests.post(gen_url, json=gen_payload, headers=headers)
gen_json = gen_request.json()

dirname = 'gen/{0}'.format(datetime.now().isoformat())

os.makedirs(dirname)

for result in gen_json['results']:
    filename = '{0}/{1}.txt'.format(dirname, result['id'])
    with open(filename, 'w') as f:
        f.write(result['value'])
