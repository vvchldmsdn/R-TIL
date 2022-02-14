import requests


# 1. URL
# URL = 'https://api.agify.io?name=michael'
for name in ['tom', 'john', 'jane']:
    URL = 'https://api.agify.io'
    params = {
        'name': name
    }
    response = requests.get(URL, params=params).json()
    print(response.get('age'))
# 2. 요청
# response = requests.get(URL)
# => 얘는 json 파일이여서 beautifulsoup4 할 필요 없음
# json 파일은 .json() 으로 정리 가능
# => 
# response = requests.get(URL, params=params).json()
# print(response.get('age'))