# 1
def duplicated_letters(word):
    a = set()
    for letter in word:
        if word.count(letter) > 1:
            a.add(letter)

    return list(a)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))


# 2.1(반복문)
# def low_and_up(word):
#     new_word = ''
#     for i in range(len(word)):
#         if i % 2 == 0:
#             new_word = new_word + word[i]
#         else:
#             new_word = new_word + word[i].capitalize()

#     return new_word

   
# 재귀로 해보고 싶었음.. -> 홀수 인덱스 짝수 인덱스 구분하는 법 고민중
# 2.2 (재귀)
def low_and_up(word):
    if len(word) == 0:
        return ''
    else:
        if len(word) % 2 == 0:
            return word[0].capitalize() + low_and_up(word[1:])
        else:
            return word[0] + low_and_up(word[1:])
    # 이게 아닌데 ㅅㅂ..

print(low_and_up('applee'))



# 3
# def lonely(numbers):
#     for i in numbers:
#         cnt = 0
#         for j in numbers:
#             while j == i:
#                 cnt += 1
#         info.append((i,cnt))

def lonely(numbers):
    tmp = []
    
    while len(numbers) > 0:
        tmp.append(numbers.pop(0))
        if len(tmp) > 1:
            if tmp[-2] == tmp[-1]:
                tmp.pop()

    return tmp

print(lonely([1,1,3,3,0,1,1]))


        