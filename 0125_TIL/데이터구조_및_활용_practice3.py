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

# 1.2
def sum_of_repeat_number(numbers):
    tmp =[]
    org_numbers = numbers[:]

    for number in numbers:
        if numbers.count(number) == 2:
            tmp.append(numbers.pop(numbers.index(number)))

    return sum(org_numbers) - (sum(tmp) * 2)


print(sum_of_repeat_number([4, 5, 7, 5, 4, 8]))