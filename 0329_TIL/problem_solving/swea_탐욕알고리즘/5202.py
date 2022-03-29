T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    infos.sort()
    
    ans = []
    for i in range(len(infos)):
        cnt = 1
        last = infos[i][1]
        for j in range(i + 1, len(infos)):
            if infos[j][0] >= last:
                last = infos[j][1]
                cnt += 1
        first = infos[i][0]
        for j in range(i - 1, -1, -1):
            if infos[j][1] <= first:
                first = infos[j][0]
                cnt += 1
        ans.append(cnt)

    print(f'#{tc} {max(ans)}')