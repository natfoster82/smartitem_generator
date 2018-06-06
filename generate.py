import requests
import os


url_base = os.environ.get('URL_BASE') or 'https://smart.caveon.com'
access_token = os.environ.get('ACCESS_TOKEN') or input('Access token: ')
item_id = os.environ.get('ITEM_ID') or input('Item ID: ')

headers = {
    'Authorization': 'Bearer {0}'.format(access_token)
}

item_url = '{0}/items/{1}'

item_request = requests.get(item_url, headers=headers)

pprint(item_request.json())
