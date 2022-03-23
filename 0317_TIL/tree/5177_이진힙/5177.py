import sys
sys.stdin = open('input.txt')


def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p >= 1 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = list(map(int, input().split()))

    tree = [0] * (N + 1)
    last = 0  # 마지막 정점 번호

    for number in info:
        enq(number)

    ans = 0
    while N > 1:
        ans += tree[N // 2]
        N //= 2
    print(f'#{tc} {ans}')