T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    cargos = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    cargos.sort()
    trucks.sort()

    ans = 0
    while True:
        if not cargos or not trucks:
            break
        elif trucks[-1] >= cargos[-1]:
            ans += cargos.pop()
            trucks.pop()
        else:
            cargos.pop()

    print(f'#{tc} {ans}')