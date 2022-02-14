# 배운 점
* 자꾸 새로운 변수에 할당하려 하는 버릇 고치기
* 입력된 변수 자체를 변화시키면서 반복문 돌리는 연습 필요
* while문 안에서 객체 고치면 while문 조건에 고쳐진걸로 반영
* for문은 안됨 -> deep copy, shallow copy 구분 잘 해야함
* dictionary method **.items()** : (key, value)인 튜플들을 반환
* dictionary method **.get()**: value가 없을 때의 default값을 바꿔서 유용하게 쓸 수 있음
  * ex) OOP_practice3 -> 1.5 


# 주의할 점

* remote directory에서 파일 변경 **금지**!!
* VS Code 닫기전에 **terminal 지우고** 닫기!!



# 알고리즘

## 리스트

**문제 풀 때 항상 이 목록들 중 뭘 쓸 수 있을까 생각하기**

* BubbleSort

* CountingSort

  * 0~9까지 나타나는 숫자 횟수 저장하는 리스트 이용 꼭 생각!!
    * ex) a = [1,3,5,3,6,7] -> [0,1,0,2,0,1,1,1,0,0]

* 2차원 리스트

  * 행 탐색, 열 탐색, transpose만드는 법, 점대칭, 오른쪽회전, 왼쪽회전

  * 블럭요소 탐색 ex) 2*3행렬로 쪼개기

    ```python
    ans = []
    for i in range(3):
        for j in range(3):
            a = [row[3*j:3*j+3] for row in sudoku[3*i:3*i+3]]
            ans.append(a)
    ```

    

