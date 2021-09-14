a = int(input('enter no. of row '))

for i in range(1, a + 1):
    b = 1
    for j in range(1, i + 1):
        print(b, end=' ')
        b += 1
    print()
print()

'''
1
2,3
4,5,6 '''
b = 1
for i in range(1, a + 1):
    for i in range(1, i + 1):
        print(b, end=' ')
        b += 1
    print()
print()

'''
1,2,3
1,2
1    '''
b = 1
for i in range(a, 0, -1):
    b = 1
    for j in range(1, i + 1):
        print(b, end=' ')
        b += 1
    print()
print()

'''
1,2,3
4,5
6    '''
b = 1
for i in range(a, 0, -1):
    for j in range(1, i + 1):
        print(b, end=' ')
        b += 1
    print()
print()
