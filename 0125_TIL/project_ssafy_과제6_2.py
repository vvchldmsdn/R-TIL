def mass_percent(infos=[]):
    c = 0
    infos = []
    while c == 0:
        try:
            a, b = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: '). split()
            num_a = int(a[:-1])
            num_b = int(b[:-1])
            infos.append([num_a, num_b])
        except:
            c = 1
            print('Done')

    salt_list = []
    total_water = 0
    
    for info in infos:
        salt = (info[0] / 100) * info[1]
        salt_list.append(salt)
        total_water += info[1]

    total_salt = sum(salt_list)

    ans_percent = (total_salt / total_water) * 100
    return f'{ans_percent}% {total_water}g'

print(mass_percent())
