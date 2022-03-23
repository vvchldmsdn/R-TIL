import sys
sys.stdin = open('input.txt')


def in_order(v):
    global order
    if v:
        in_order(ch1[v])
        order.append(v)
        in_order(ch2[v])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in range(1, N + 1):
        if 2 * i + 1 <= N:
            ch1[i] = 2 * i
            ch2[i] = 2 * i + 1
        elif 2 * i <= N and 2 * i + 1 > N:
            ch1[i] = 2 * i
    
    order = []
    in_order(1)

    ans1 = order.index(1) + 1
    ans2 = order.index(N // 2) + 1
    print(f'#{tc} {ans1} {ans2}')

