# 0121 Project

* **open(file, mode='r', encoding=None)**: file: 파일명 ...

```python
with open('workfile') as f:
	read_data = f.read()

f.closed
```

```python
f = open('workfile', 'm')
```



## **JSON 파일 활용**

* 객체(리스트, 딕)을 JSON으로 변환
* vice versa

* **Pprint**: 임의의 파이썬 데이터 구조를 예쁘게 인쇄 할 수 있는 기능 제공

* 리스트 안 딕셔너리들 여러개 있을때 -> 이름만 출력하고 싶다면

  * ```python
    for stock in stocks:
    	print(~~~)
    ```

​		-> 가격만 출력하고 싶다면 (가격 key가 없는 dict가 있는 경우)

```python
for stock in stocks:
	print(stock.get('price', '비상장주식'))
```

 -> price key가 없는 dict의 경우 '비상장주식' print





* 프로젝트 등록

  *  gitlab 저장소 생성 및 담당교수 maintainer등록
  * 로컬 정장소 생성 및 README.md 추가 후 루트 커밋
  * GitLab 원격저장소 등록 및 push 테스트

* 과제 수행 및 제출

  * 수행 수 단께별 커밋

  * 과제제출

    * 과제 제출시 반드시 README.md 파일에 수행 내용 작성 필수

      * README.md -> 프로젝트를 하면서 막힌 부분, 어떻게 해결 했는지, 해결과정에서 새로 학습한 개념은 무엇인지...

        프로젝트 총평

        ex) project1, project2, .... 코드블럭활용, 느낀 점 등

        ​		프로젝트 리뷰

        



* 제목만 뽑는다 -> title = movie.get('title') -> return title

* 필요 데이터를 추리는데 dict으로 {'제목': '쇼생크탈출'} 식으로 return을 하려면

​	-> dict을 만든다: result = {'제목': title} 

​	-> return result



* problem b -> movie랑 genre밖에 못씀 
  * -> genre는 리스트로 되있음 / movies는 dict
  * 반복문 사용하기
* movies에 있는 json에 있는 파일에 접근해서 정보 가져오기 필요 (?)





# Get 쓰기!



### README.md 항목 정리

* 놓친 부분
* 해결 한 방법
* 해결 방법에서 새로 학습한 것



  id = movie.get('id')

  title = movie.get('title')

  poster_path = movie.get('poster_path')

  vote_average = movie.get('vote_average')

  overview = movie.get('overview')

  genre_ids = movie.get('genre_ids')