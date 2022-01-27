# 1.1
def change_rotten_fruit(fruit_bag):
    for i in range(len(fruit_bag)):
        if fruit_bag[i].startswith('rotten'):
            fruit_bag[i] = fruit_bag[i].lstrip('rotten').lower()

    if fruit_bag == None or []:
        return []
    return fruit_bag

    print(change_rotten_fruit(['apple', 'rottenBanana', 'apple']))
print(change_rotten_fruit([]))



# 1.2.1
# '잘못된 풀이' -> 입력 값에 중복 되는 숫자는 최대 2번 나오는 줄 알고 푼 풀이 -> 그래서 .pop() 을 쓰려 함
def sum_of_repeat_number(numbers):
    tmp =[]
    org_numbers = numbers[:]
    for number in numbers:
        if numbers.count(number) == 2:
            tmp.append(numbers.pop(numbers.index(number)))
    return sum(org_numbers) - (sum(tmp) * 2)

# 1.2.2
# 교수님 풀이
def sum_of_repeat_number(numbers):
    multiple = []
    once = []
    for number in numbers:
        if number in once:
            multiple.append(number)
            once.remove(number)
        elif number not in multiple:
            once.append(number)
    return sum(once)

# 1.2.3 
# 홍제민님 풀이: 한 번 나오는 것만 세서 더하기
def sum_of_repeat_number(numbers):
    sum1 = 0
    for i in numbers:
        if numbers.count(i) == 1:
            sum1 += i
    return sum1

print(sum_of_repeat_number([4,4,7,8,10,4]))