import requests
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
movie_id = 13
path = f'/movie/{movie_id}/release_dates'
params = {
    'api_key': 'd1a4feab78e87ac758f0b64d63f14214'
}

response = requests.get(Base_URL+path, params = params)
print(response.status_code, response.url)
data = response.json()

print(type(data)) # dict
print(data.keys()) # dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results'])
print(type(data.get('results'))) # list
pprint(data.get('results')[0]['release_dates']) # list 첫번째 구조
print(len(data.get('results'))) # 20
