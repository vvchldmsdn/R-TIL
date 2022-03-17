'''
input values
ex - 1)
4
1 2 1 3 3 4 3 5
ex - 2)
12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(v):  # 전위순회 함수
    global ans
    if v:  # v == 0인 경우는 없으므로
        ans.append(v)
        pre_order(ch1[v])
        pre_order(ch2[v])


E = int(input())
arr = list(map(int, input().split()))
V = E + 1  # 정점 수

# 부모번호를 인덱스로 자식번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:  # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c

'''
=>
ch1 = [0, 2, 0, 4, 0, 0]
ch2 = [0, 3, 0, 5, 0, 0]
'''

ans = []
pre_order(1)
print(*ans)