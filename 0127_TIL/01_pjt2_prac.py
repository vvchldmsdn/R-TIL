import requests
from bs4 import BeautifulSoup

# 주소
URL = 'https://finance.naver.com/sise/'


# 2. 요청
# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
response = requests.get(URL).text  # => str
# print(response, type(response))
# response가 200 이면 제대로 가져온 것임

# 2-1 BeautifulSoup (text -> 다른객체로)
# Kospi Now
# soup = BeautifulSoup(response, 'html,~~')
soup = BeautifulSoup(response, 'html.parser')
print(type(soup), type(response))
# print(soup, response) -> 결과동일, 타입다름 

# 2-2 내가 원하는 정보 가져오기
kospi = soup.select_one('#KOSPI_now')
print(kospi, kospi.text)