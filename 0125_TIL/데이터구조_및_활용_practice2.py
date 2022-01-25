# 1.1
def my_find(text, alphabet):
    ans =[]

    for i in range(len(text)):
        if text[i] == alphabet:
            ans.append(i)
    
    if len(ans) > 0:
        return ans
    
    return -1

print(my_find('apple', 'p'))
print(my_find('a', 'p'))


# 1.2
def check(n, students):
    pres_stu = list(map(int, students.split(' ')))
    
    total_stu = list(range(1, n + 1))

    for i in pres_stu:
        if i in total_stu:
            total_stu.pop(total_stu.index(i))
    
    total_stu = list(map(str, total_stu))

    return ' '.join(total_stu)

print(check(7, '1 3 5'))

