def collatz(num):
    cnt = 0
    while num > 1:
        if num % 2 == 0:
            cnt += 1
            num = num // 2
            if cnt >= 500:
                cnt = -1
                break
        else:
            cnt += 1
            num = num * 3 + 1
            if cnt >= 500:
                cnt = -1
                break
    return cnt