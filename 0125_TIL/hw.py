## 1
# sorted -> 원본 안 바뀜, 정렬된 리스트 출력
a = [1, 4, 2, 5, 7]
b = sorted(a)
print(a, b)

# sort -> 원본 바뀜, None 출력
c = [1, 4, 2, 5, 7]
d = c.sort()
print(c, d)



## 2
# extend
test = ['I', 'my', 'me', 'mine']
test.extend('you')
test.extend(['yours'])
print(test)

# append
test2 = ['I', 'my', 'me', 'mine']
test2.append('you')
test2.append(['yours'])
print(test2)



## 3
aa = [1, 2, 3, 4, 5]
bb = aa

a[2] = 5

print(aa)
print(bb)