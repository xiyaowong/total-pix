import json
import time

import requests

session = requests.Session()
repos = [
    'pix',
    'pix-2'
]

data = {
    'count': 0,
    'last_update': 0,
    'pics': []
}

try:
    for repo in repos:
        url = 'https://cdn.jsdelivr.net/gh/XiyaoWong/' + repo + '/data.json'
        rep = session.get(url)
        pics = [f'https://cdn.jsdelivr.net/gh/XiyaoWong/{repo}/pics/{pic}' for pic in rep.json()['pics']]
        data['pics'].extend(pics)

    data['count'] = len(data['pics'])
    data['last_update'] = int(time.time())

    with open('data.json', 'w') as f:
        json.dump(data, f)
except Exception as e:
    print(e)
