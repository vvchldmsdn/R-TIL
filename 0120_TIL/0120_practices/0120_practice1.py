# abs() 직접 구현하기

def my_abs(x):
    if type(x) == complex:
        return ((x.real) ** 2 + (x.imag) ** 2) ** 0.5
    else:
        if x == 0:
            return x ** 2
        elif x < 0:
            return -1 * x
        else:
            return x

print(my_abs(-8))


# all() 직접 구현하기

def my_all(elements):
    if len(elements) > 0:
        for element in elements:
            if bool(element) == False:
                return False
            else:
                return True
    else:
        return True

print(my_all([[], 2, 5, '6']))

## all() 교수님 코드

# def my_all(elements):
#     for element in elements:
#         if bool(element) == False:
#             return False
#     return True


# any() 직접 구현하기

def my_any(elements):
    if len(elements) > 0:
        answer = False
        for element in elements:
            if bool(element) != False:
                answer = True
    else:
        answer = False

    return answer

print(my_any([]))


# def my_any(elements):
#     answer = False

#     for element in elements:
#         if bool(element) != False:
#             answer = True

#     return answer