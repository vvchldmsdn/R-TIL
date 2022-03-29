def check(a):  # 입력변수 = 리스트
    for i in range(len(a) - 2):
        if 0 not in a[i:i + 3]:
            return True
    for i in range(len(a)):
        if a[i] == 3:
            return True
    return False


T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))

    p1_visit = [0] * 10
    p1_visit[info[0]] += 1

    p2_visit = [0] * 10
    p2_visit[info[1]] += 1

    i = 2
    winner = 0
    while i <= len(info) - 1:
        if not i % 2:
            p1_visit[info[i]] += 1
            if check(p1_visit):
                winner = 1
                break
            else:
                i += 1
        else:
            p2_visit[info[i]] += 1
            if check(p2_visit):
                winner = 2
                break
            else:
                i += 1

    print(f'#{tc} {winner}')