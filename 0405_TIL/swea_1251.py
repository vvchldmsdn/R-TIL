from itertools import combinations

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
    N = int(input())  # 섬의 개수
    X_coords = list(map(int, input().split()))
    Y_coords = list(map(int, input().split()))
    E = float(input())

    infos = []
    for comb in list(combinations(list(range(N)), 2)):
        dist = (X_coords[comb[0]] - X_coords[comb[1]]) ** 2 + (Y_coords[comb[0]] - Y_coords[comb[1]]) ** 2
        cost = E * dist
        infos.append([comb[0], comb[1], cost])
    
    infos.sort(key=lambda x:x[2])
    # pprint.pprint(infos)

    p = [0] * N
    for i in range(1, N):
        p[i] = i

    rank = [0] * N

    ans = kruskal(infos)
    print(f'#{tc} {round(ans)}')