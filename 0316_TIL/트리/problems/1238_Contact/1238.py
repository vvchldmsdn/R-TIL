import pprint
import sys

sys.stdin = open('input.txt')

def contact(info, start):
    global move
    move += 1
    for number in info[start]:
        if number not in ans.keys():
            ans[number] = move
            if number in info.keys():
                contact(info, number)
                move -= 1
        else:
            if ans[number] > move:
                ans[number] = move
                if number in info.keys():
                    contact(info, number)
                    move -= 1

T = 10  # 테스트케이스 개수

for tc in range(1, T + 1):
    N, start = list(map(int, input().split()))
    info_input = list(map(int, input().split()))

    info = {}
    for i in range(len(info_input) // 2):
        if info_input[2 * i] not in info.keys():
            info[info_input[2 * i]] = [info_input[2 * i + 1]]
        else:
            if info_input[2 * i + 1] not in info[info_input[2 * i]]:
                info[info_input[2 * i]].append(info_input[2 * i + 1])
    
    move = 0
    ans = {
        start: 0
    }
    contact(info, start)
    
    max_list = [start, ans[start]]
    for number in ans.keys():
        if ans[number] > max_list[1]:
            max_list = [number, ans[number]]
        elif ans[number] == max_list[1]:
            if number > max_list[0]:
                max_list = [number, ans[number]]

    print(f'#{tc} {max_list[0]}')