from collections import deque

def check(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        next_x, next_y = queue.popleft()
        for i in range(4):
            new_x = next_x + dx[i]
            new_y = next_y + dy[i]
            if check(new_x, new_y):
                tmp = 1
                if info[new_x][new_y] > info[next_x][next_y]:
                    tmp += info[new_x][new_y] - info[next_x][next_y]
                if cost[new_x][new_y] > cost[next_x][next_y] + tmp:
                    cost[new_x][new_y] = cost[next_x][next_y] + tmp
                    queue.append((new_x, new_y))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    cost = [[1000 * N ** 2] * N for _ in range(N)]
    cost[0][0] = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    bfs(0, 0)
    print(f'#{tc} {cost[N - 1][N - 1]}')