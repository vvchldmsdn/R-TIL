import json
from pprint import pprint



def movie_info(movie, genres):
    target_keys = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    ans = dict()
    
    for val in target_keys:
        ans[val] = movie[val]

    ans['genre_ids'] = []
    
    for genre in genres:
        if genre['id'] in movie.get('genre_ids'):
            ans['genre_ids'].append(genre['name'])

    ans['genre_name'] = ans['genre_ids']
    del ans['genre_ids']
 


    # id = movie.get('id')
    # title = movie.get('title')
    # poster_path = movie.get('poster_path')
    # vote_average = movie.get('vote_average')
    # overview = movie.get('overview')
    # genre_ids = movie.get('genre_ids')

    # # genre_name 이라는 새로운 리스트 만들기
    # # genres.json 은 딕셔너리가 담긴 리스트 파일
    # # 반복문으로 리스트 인덱싱
    # ## 장르네임 리스트를 for문안쪽에 만들어서 계속 초기화 됐었음ㅠㅠ
    # ## 장르네임에 append를 genre['name']으로 받아야하는데 genre['id']로 받아버림ㅠㅠ

    # genre_names = []

    # for genre in genres:
    #     if genre['id'] in genre_ids:
    #         genre_names.append(genre['name'])

    # # 반환할 딕셔너리 작성
    # a = {
    #     'genre_names': genre_names,
    #     'id': id,
    #     'overview': overview,
    #     'poster_path': poster_path,
    #     'title': title,
    #     'vote_average': vote_average
    # }
        

    return ans
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))