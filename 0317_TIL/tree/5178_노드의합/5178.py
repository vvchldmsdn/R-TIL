import sys
sys.stdin = open('input.txt')


def child_sum(t):
    for i in range(N, 1, -1):
        t[i // 2] += t[i]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)

    # 리프 노드 정보들 tree리스트에 저장하기
    for i in range(M):
        tree[info[i][0]] = info[i][1]

    child_sum(tree)
    print(f'#{tc} {tree[L]}')