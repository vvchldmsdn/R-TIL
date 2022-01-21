import json

# 파일을 어떻게 열고 파일명은 어떤 형태로 출력되는지 몰라서 고생중ㅠㅠ
# 반복문으로 불러와야 되는데..
# movies안에 있는 것들 불러와야되는데
# open으로 열어서 하라는거같은데
# 안에 있는 json파일들에서 정보를 가져와야되는데 (dictionary가 저장되있음 각각) -> 여기서 'revenue' key 의 value를 갖고
# os 써도 되는지 모르겠는데 일단 이걸로 해야겠다



def max_revenue(movies):

    a = []

    for movie in movies:
        files = open('data/movies/' + str(movie['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        open_files = json.load(files)
        revenue = open_files.get('revenue')
        a.append(revenue)

    max_revenue = max(a)

    # max_revenue값을 가지는 json파일을 찾아 title 출력해야 함

    for movie in movies:
        files = open('data/movies/' + str(movie['id']) + '.json', encoding = 'UTF8')#영화의 ID를 참조하여 경로 설정
        open_files = json.load(files) # 파일에 접속한 것임
        revenue = open_files.get('revenue') # 파일에서 revenue 값 부른 것
        if revenue == max_revenue:
            title = open_files.get('title')
            break
    
    return title
        


    # movie = open('data/movies.json', 'r')
    # print(movie)
    # for file in f:
    #     dd = file['revenue']
    #     print(dd)
    # for a in movies:
    #     b = open('a.josn', 'r')
    #     print(b['budget'])

    # 여기에 코드를 작성합니다.  
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))