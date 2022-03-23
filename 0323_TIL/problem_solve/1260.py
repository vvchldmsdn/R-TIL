import pprint

N, M, V = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(M)]

graph = {}

for info in infos:
    if info[0] not in graph.keys():
        graph[info[0]] = [info[1]]
    else:
        if info[1] not in graph[info[0]]:
            graph[info[0]].append(info[1])
    if info[1] not in graph.keys():
        graph[info[1]] = [info[0]]
    else:
        if info[0] not in graph[info[1]]:
            graph[info[1]].append(info[0])

for node in graph.keys():
    graph[node].sort()

pprint.pprint(graph)

def bfs(n):
    queue = []
    queue.append(n)
    visited = []
    while queue:
        next = queue.pop(0)
        if next not in visited:
            visited.append(next)
            for node in graph[next]:
                queue.append(node)
    return visited

def dfs(n):
    queue = []
    queue.append(n)
    visited = []
    while queue:
        next = queue.pop()
        if next not in visited:
            visited.append(next)
            for i in range(len(graph[next]) - 1, -1, -1):
                queue.append(graph[next][i])
    return visited

print(*dfs(V))
print(*bfs(V))