# 회문 판별

# 1. 반목문 사용

def is_pal_while(word):
    list_word = list(word)
    list_new_word = []

    while len(list_new_word) != len(word):
        list_new_word.append(list_word[-1])
        list_word.pop()
    
    new_word = ''.join(list_new_word)

    if new_word == word:
        return True
    else:
        return False


def is_pal_while(word):
    cnt = 0
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        cnt += 1
    if cnt < len(word) // 2:
        return False
    else:
        return True

## 교수님 풀이

# def is_pal_while(word):
#     while len(word) > 1:
#         if word[0] == word[-1]:
#             word = word[1:-1]
#         else:
#             return False
#     return True

# ---> 조건문 하나하나 항상 리턴 해주지 않아도 된다고 생각하고 해야 할 듯 



# 2. 재귀문 사용

# def is_pal_recursive(word):
#     list_word = list(word)
#     list_new_word = []
    
#     if len(word) < 1:
#         return True
#     else:
#         list_new_word.append(list_word[-1])
#         list_word.pop()
#         new_word = ''.join(list_word)
#         return is_pal_recursive(list_new_word) == list(word)



def is_pal_recursive(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    else:
        return word[0] == word[-1] and is_pal_recursive(word[1:-1])

print(is_pal_while('racecar'))
print(is_pal_recursive('tomato'))
print(is_pal_recursive('racecar'))