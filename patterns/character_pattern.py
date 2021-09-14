a = input('enter a string ')
b = len(a)

# 1.
for i in range(b):
    for j in range(b-i):
        print(a[j],end='')
    print()

# 2.
for i in range(b):
    for j in range(i):
        print(' ',end='')
    for j in range(b-i):
        print(a[j],end='')
    print()

# 3.
for i in range(b):
    for j in range(i+1):
        print(a[j],end='')
    print()

# 4.
for i in range(b):
    for j in range(b-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(a[j],end='')
    print()
