import json
import os
import time

import requests

session = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
repos = os.listdir('repos')
print(repos)
print()
data = {
    'count': 0,
    'last_update': 0,
    'pics': []
}

for repo in repos:
    try:
        try:
            url = f'https://raw.githubusercontent.com/XiyaoWong/{repo}/master/data.json'
            rep = session.get(url, headers=headers)
            print(url, rep.status_code, repo, rep.json()['count'])
            rep.raise_for_status()
            pics = [f'https://cdn.jsdelivr.net/gh/XiyaoWong/{repo}/pics/{pic}' for pic in rep.json()['pics']]
            data['pics'].extend(pics)
        except Exception:
            url = 'https://cdn.jsdelivr.net/gh/XiyaoWong/' + repo + '/data.json'
            rep = session.get(url, headers=headers)
            print(url, rep.status_code, repo, rep.json()['count'])
            rep.raise_for_status()
            pics = [f'https://cdn.jsdelivr.net/gh/XiyaoWong/{repo}/pics/{pic}' for pic in rep.json()['pics']]
            data['pics'].extend(pics)
    except Exception as e:
        print(e)

data['count'] = len(data['pics'])
data['last_update'] = int(time.time())

with open('data.json', 'w') as f:
    json.dump(data, f)
