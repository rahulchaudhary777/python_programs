
a = int(input('enter no. of rows '))

# 1.
for i in range(1, a+1):
    for j in range(1, 2*a):
        if i == a or i+j == a+1 or j-i == a-1:
            print('$', end='')
        else:
            print(' ', end='')
    print()
print()

# 2.
k = 2
for i in range(1, a+1):
    for j in range(1, 2*a):
        if i+j == a+1 or j-i == a-1:
            print('$', end='')
        elif i == a and j != k:
            print('$', end='')
            k += 2
        else:
            print(' ', end='')
    print()
