import json
from pprint import pprint


def movie_info(movies, genres):

    a = []

    for movie in movies:
        target = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
        ans = dict()
        
        for val in target:
            ans[val] = movie[val]

        ans['genre_ids'] = []

        for genre in genres:
            if genre['id'] in movie.get('genre_ids'):
                ans['genre_ids'].append(genre['name'])

        ans['genre_name'] = ans['genre_ids']
        del ans['genre_ids']

        a.append(ans)


    # 일단 movies는 리스트 형태
    # for문으로 movies에 있는 모든 딕셔너리를 problem_b처럼 출력하자!

    # a = []

    # for movie in movies:
    #     id = movie.get('id')
    #     title = movie.get('title')
    #     poster_path = movie.get('poster_path')
    #     vote_average = movie.get('vote_average')
    #     overview = movie.get('overview')
    #     genre_ids = movie.get('genre_ids')

    #     genre_names = []

    #     for genre in genres:
    #         if genre['id'] in genre_ids:
    #             genre_names.append(genre['name'])

    #     b = {
    #         'genre_names': genre_names,
    #         'id': id,
    #         'overview': overview,
    #         'poster_path': poster_path,
    #         'title': title,
    #         'vote_average': vote_average
    #     }
        
    #     a.append(b)

    return a
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))