import json
from pprint import pprint

def movie_info(movie):
    target = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    ans = dict()

    for val in target:
        ans[val] = movie[val]
        
    return ans

    # id = movie.get('id')
    # title = movie.get('title')
    # poster_path = movie.get('poster_path')
    # vote_average = movie.get('vote_average')
    # overview = movie.get('overview')
    # genre_ids = movie.get('genre_ids')

    # # 원래 딕셔너리에 있는 키 순서대로 호출 원함

    
    # # 만들 dictionary에 들어갈 value값 만들기
    # a = {
    #     'genre_ids': genre_ids,
    #     'id': id,
    #     'overview': overview,
    #     'poster_path': poster_path,
    #     'title': title,
    #     'vote_average': vote_average      
    # }
    # print(a)
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


# 처음엔 하드코딩으로 했다가 나중에 고민해서 바꿈ㅎㅎ