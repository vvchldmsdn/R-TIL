# a 막대에 n개가 꼽혀있고 최종적으로 c막대기에 꼽아야 함


def tower_of_hanoi(number, a='', b='', c=''):
    if number == 1:
        return 1
    else:
        
