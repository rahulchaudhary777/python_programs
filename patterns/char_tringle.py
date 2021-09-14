a = int(input('enter no. of rows '))

b = 65
for i in range(1,a+1):
    for j in range(1,i+1):
        print(chr(b),end='')
        b +=1
    print()
print()

# 2.
for i in range(1,a+1):
    b = 96
    b +=i
    for j in range(1,i+1):
        print(chr(b),end='')
        b +=1
    print()
