# snail()


def snail(height, day, night):
    curr_loc = 0
    day_cnt = 0
    while curr_loc < height:
        curr_loc += day
        if curr_loc >= height:
            day_cnt += 1
            break
        curr_loc -= night
        day_cnt += 1
    
    return day_cnt

print(snail(100, 10, 3))


# 자리수 더하기

## 반복문 사용

def sum_of_digit(number):
    num_str = str(number)
    answer = 0
    for i in num_str:
        num_i = int(i)
        answer += num_i
    
    return answer

print(sum_of_digit(12345))

### 교수님 코드

# def sum_of_digit(number):
#     # 1. 변수 초기화
#     total = 0
#     # 2. 반복문
#     while number / 10:
#         # 3. 몫과 나머지를 분리
#         remainder = number % 10
#         number = number // 10
#         # 4. 나온 나머지 더하기
#         total += remainder

#     return total




## 재귀문 사용

def sum_of_digit_reculsive(number):
    num_str = str(number)
    if len(num_str) < 2:
        return int(num_str[0])
    else:
        return int(num_str[0]) + sum_of_digit_reculsive(num_str[1:])

### 김태삼님 코드

# def sum_of_digit_reculsive(number):
#     if number < 10:
#         return number
#     else:
#         return (number % 10) + sum_of_digit_reculsive(number // 10)