N, M = list(map(int, input().split()))
info = [list(map(int, input())) for _ in range(N)]
K = int(input())

max_cnt = 0

for col in range(N):
    zero_cnt = 0
    for num in info[col]:
        if num == 0:
            zero_cnt += 1
    
    col_light_cnt = 0
    if zero_cnt <= K and zero_cnt % 2 == K % 2:  # 한 행을 다 킬 수 있다면
        for col2 in range(N):
            if info[col] == info[col2]:  # 처음 기준 행과 똑같은 행의 개수 세기
                col_light_cnt += 1
    
    max_cnt = max(max_cnt, col_light_cnt)

print(max_cnt)
