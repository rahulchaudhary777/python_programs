a = int(input('enter no. of rows '))

b = 0
for i in range(1,a+1):
    b = -1
    b +=i
    for j in range(1,a+1):
        b +=1
        print(b,end=' ')
    print()
