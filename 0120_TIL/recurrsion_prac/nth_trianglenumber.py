# n번째 삼각수 구하기
# 자연수 1 부터 n까지의 합

def triangle_number(number):
    # 종료시점 설정
    if number < 2:
        return number
    else:
        return number + triangle_number(number - 1)

print(triangle_number(10))
        
