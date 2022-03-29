import itertools

def check(p):
    global ans
    flag = 0
    tmp = info[0][p[0] - 1]
    for i in range(len(p) - 1):
        tmp += info[p[i] - 1][p[i + 1] - 1]
        if tmp > min(ans):
            flag += 1
            break
    if flag != 1:
        tmp += info[p[-1] - 1][0]
        ans.append(tmp)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    
    permut_target = list(range(2, N + 1))
    permuts = itertools.permutations(permut_target, N - 1)

    ans = [100 * N]
    for permut in list(permuts):
        check(permut)

    print(f'#{tc} {min(ans)}')