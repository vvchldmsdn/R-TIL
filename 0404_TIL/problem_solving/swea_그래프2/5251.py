def dfs(n, ssum):
    global ans
    if ssum >= ans:
        return
    if n == N:
        if ssum < ans:
            ans = min(ans, ssum)
            return
    for info in graph[n]:
        dfs(info[0], ssum + info[1])


T = int(input())

for tc in range(1, T + 1):
    N, E = list(map(int, input().split()))
    infos = [list(map(int, input().split())) for _ in range(E)]

    graph = {}
    for i in range(len(infos)):
        if infos[i][0] not in graph.keys():
            graph[infos[i][0]] = [[infos[i][1], infos[i][2]]]
        else:
            graph[infos[i][0]].append([infos[i][1], infos[i][2]])

    ans = 10 * E
    dfs(0, 0)
    print(f'#{tc} {ans}')