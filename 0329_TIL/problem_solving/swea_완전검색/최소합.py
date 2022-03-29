def check(a, b):
    return 0 <= a < N and 0 <= b < N


def bfs(a, b):  
    ans = []
    dx = [0, 1]  # 오른쪽, 아래
    dy = [1, 0]
    stack = [[a, b, info[a][b]]]
    while stack:
        next_x, next_y, sum_path = stack.pop()
        if next_x == N - 1 and next_y == N - 1:
            ans.append(sum_path)
        for i in range(2):
            new_x = next_x + dx[i]
            new_y = next_y + dy[i]
            if check(new_x, new_y):
                stack.append([new_x, new_y, sum_path + info[new_x][new_y]])
    return ans


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(0, 0)
    print(f'#{tc} {min(result)}')
