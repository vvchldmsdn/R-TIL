import sys
sys.stdin = open('input.txt')


def post_order(v):
    global ans
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        ans.append(v)


T = int(input())

for tc in range(1, T + 1):
    E, N = list(map(int, input().split()))
    info = list(map(int, input().split()))

    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(len(info) // 2):
        if ch1[info[2 * i]] == 0:
            ch1[info[2 * i]] = info[2 * i + 1]
        else:
            ch2[info[2 * i]] = info[2 * i + 1]
    
    ans = []
    post_order(N)
    
    print(f'#{tc} {len(ans)}')