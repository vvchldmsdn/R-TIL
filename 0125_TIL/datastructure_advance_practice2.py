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


# 1.2.1 
# in을 이용한 풀이 -> 굳이 전체 학생 리스트를 만들어 출석한 학생 빼려하지 않아도 됨 -> 1.2.2로
def check(n, students):
    pres_stu = list(map(int, students.split(' ')))
    total_stu = list(range(1, n + 1))
    for i in pres_stu:
        if i in total_stu:
            total_stu.pop(total_stu.index(i))
    total_stu = list(map(str, total_stu))
    return ' '.join(total_stu)

# 1.2.2
# not in 을 이용한 풀이 -> 1.2.1 처럼 전체에서 출석한 사람 빼지 않고 결석한 사람 찾는 방법
def check(n, students):
    pres_stu = list(map(int, students.split(' ')))
    ans = []
    for i in range(1,n + 1):
        if i not in pres_stu:
            ans.append(str(i))
    return ' '.join(ans)


print(check(7, '1 3 5'))

