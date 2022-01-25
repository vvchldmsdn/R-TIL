# 1
def fn_d(n):
    new_n = n
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10
    return a + new_n



# 2
def is_selfnumber(n):
    for i in list(range(1, n + 1)):
        if n == fn_d(i):
            return False

    return True

print(is_selfnumber(32))
