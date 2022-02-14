import sys

sys.stdin = open('input.txt')

N = int(input())  # 3

input_list = []

for tc in range(1, N+1):
    my_sum = 0
    my_len = 0
    nums = list(map(int, input().split()))

    for num in nums:
        my_sum += num
        my_len += 1

    result = round(my_sum / my_len)

    print(f'#{tc} {result}')




