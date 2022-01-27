# # 1.1
# def tax(won):
#     if won <= 1200:
#         return won * 0.06
#     elif 1200 < won <= 4600:
#         return 72 + (won - 1200) * 0.15
#     else:
#         return 582 + (won - 4600) * 0.24


# # 1.2
# def fee(minute, distance):
#     lent = (minute // 10) * 1200
#     insur = ((minute - 1) // 30 + 1) * 525
#     dist = 170 * min(distance, 100) + 85 * max(distance - 100, 0)
#     return lent + insur + dist


# # 1.3
# def start_end(words):
#     cnt = 0
#     for word in words:
#         if len(word) > 1:
#             if word[0] == word[-1]:
#                 cnt += 1
#     return cnt


# # 1.4.1 (재귀)
# def collatz(num):
#     if num == 1:
#         return 0
#     else:
#         if num % 2 == 0:
#             return 1 + collatz(num // 2)
#         else:
#             return 1 + collatz(num * 3 + 1)
# # 1.4.2 (반복문)
# def collatz(num):
#     cnt = 0
#     while num > 1:
#         if num % 2 == 0:
#             cnt += 1
#             num = num // 2
#             if cnt >= 500:
#                 cnt = -1
#                 break
#         else:
#             cnt += 1
#             num = num * 3 + 1
#             if cnt >= 500:
#                 cnt = -1
#                 break
#     return cnt
# # 1.4.3 (반복문 깔끔하게)
# def collatz(num):
#     cnt = 0
#     while num > 1 and cnt <= 500:
#         if num % 2 == 0:
#             cnt += 1
#             num = num // 2
#         else: 
#             cnt += 1
#             num = num * 3 + 1
#     if cnt == 501:
#         return -1
#     else:
#         return cnt


# # 1.5.1
# def dict_invert(my_dict):
#     new_dict = {}
#     md_key = list(my_dict.keys())
#     md_value = list(my_dict.values())
#     for i in range(len(md_key)):
#         new_dict[md_value[i]] = md_key[i]
#     return new_dict
# 1.5.2
# def dict_invert(my_dict):
#     new_dict = {}
#     for key, value in my_dict.items():
#         if value not in new_dict.keys():
#             new_dict[value] = [key]
#         else:
#             new_dict[value].append(key)
#     return new_dict
# 1.5.3
def dict_invert(my_dict):
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[value] = new_dict.get(value, []) + [key]  ###
    return new_dict


a = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
print(dict_invert(a))

