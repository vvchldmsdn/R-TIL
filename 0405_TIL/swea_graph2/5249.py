def uni(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y]


def find_set(n):
    if n != p[n]:
        p[n] = find_set(p[n])
    return p[n]


def kruskal(g):
    result = 0
    for info in g:
        if find_set(info[0]) != find_set(info[1]):
            result += info[2]
            uni(info[0], info[1])
    return result


T = int(input())

for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    infos = [list(map(int, input().split())) for _ in range(E)]
    infos.sort(key=lambda x:x[2])

    # p 리스트 세팅
    p = [0] * (V + 1)
    for i in range(1, V + 1):
        p[i] = i

    # rank 리스트 세팅
    rank = [0] * (V + 1)

    ans = kruskal(infos)
    print(f'#{tc} {ans}')