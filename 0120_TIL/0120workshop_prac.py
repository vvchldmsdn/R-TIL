# 0120 workshop no.1

def get_secret_word(lists):
    answer_list = []
    for i in lists:
        answer_list.append(chr(i))
    answer_string = ''.join(map(str, answer_list))

    return answer_string

print(get_secret_word([83, 115, 65, 102, 89]))



# 0120 workshop no.2

def get_secret_number(strings):
    tmp_list = []
    for i in strings:
        tmp_list.append(ord(i))
    answer_list = map(int, tmp_list)

    return sum(answer_list)

print(get_secret_number('tom'))


# 0120 workshop no.3

def get_strong_word(a, b):
    tmp_list_a = []
    tmp_list_b = []

    for i in a:
        tmp_list_a.append(ord(i))

    answer_list_a = map(int, tmp_list_a)

    for i in b:
        tmp_list_b.append(ord(i))

    answer_list_b = map(int, tmp_list_b)

    if sum(answer_list_a) >= sum(answer_list_b):
        return a
    else:
        return b

print(get_strong_word('tom', 'john'))

