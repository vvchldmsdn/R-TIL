import sys
sys.stdin = open('input.txt')

decode = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    infos = [list(map(int, input())) for _ in range(N)]

    tmp_target = []
    for info in infos:
        if sum(info) > 0:
            tmp_target = info
            break
    
    target = []
    for i in range(len(tmp_target) -1, -1, -1):
        if tmp_target[i] == 1:
            target = tmp_target[i - 55: i + 1]
            break
    
    decoded = []
    for i in range(8):
        code_str = ''.join(str(_) for _ in target[7 * i: 7 * i + 7])
        decoded.append(decode[code_str])

    check = 0
    for i in range(8):
        if i == 7:
            check += decoded[i]
        elif not i % 2:
            check += 3 * decoded[i]
        else:
            check += decoded[i]
    
    if not check % 10:
        print(f'#{tc} {sum(decoded)}')
    else:
        print(f'#{tc} {0}')
