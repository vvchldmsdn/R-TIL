import json


def dec_movies(movies):

    December_movie = []

    for movie in movies:
        files = open('data/movies/' + str(movie['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        open_files = json.load(files)
        release_date = open_files.get('release_date')
        
        if release_date[5:7] == '12':  # 12월이라는 정보만 찾기위해 슬라이싱
            December_movie.append(open_files.get('title'))

    return December_movie 
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))