# 0. import
import requests
from pprint import pprint


# 1. URL 및 요청변수 설정
# https://developers.themoviedb.org/3/movies/get-now-playing
# https://api.themoviedb.org/3/movie/now_playing?api_key=d1a4feab78e87ac758f0b64d63f14214&region=KR&language=ko
# => ? 뒤에 요청 파라미터가 옴, &로 연결
Base_URL = 'https://api.themoviedb.org/3'

path = f'/movies/now_playing'
params = {
    'api_key': 'd1a4feab78e87ac758f0b64d63f14214',
    'region': 'KR',
    'language': 'ko'
}

# 2. 요청 보낸 결과 저장
response = requests.get(Base_URL+path, params = params)
print(response.status_code, response.url)
data = response.json()
# 3. 조작....
# print(response)

# print(type(data)) # dict
# print(data.keys()) # dict_keys(['dates', 'page', 'results', 'total_pages', 'total_results'])
# print(type(data.get('results'))) # list
# pprint(data.get('results')[0]) # list 첫번째 구조
# print(len(data.get('results'))) # 20



