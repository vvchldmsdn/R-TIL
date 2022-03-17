import sys
sys.stdin = open('input.txt')

def in_order(v):
    global ans
    if v:
        in_order(ch1[v])
        ans.append(v)
        in_order(ch2[v])

T = 10  # 테스트케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 노드의 개수
    info = [list(input().split()) for _ in range(N)]

    # 부모 자식 관계 저장해야 함
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in range(N):
        if len(info[i]) == 4:
            ch1[int(info[i][0])] = int(info[i][2])
            ch2[int(info[i][0])] = int(info[i][3])
        elif len(info[i]) == 3:
            ch1[int(info[i][0])] = int(info[i][2])

    ans = []
    in_order(1)
    print(f'#{tc}', end=' ')
    for i in range(N):
        if i < N - 1:
            print(info[ans[i] - 1][1], end='')
        else:
            print(info[ans[i] - 1][1])