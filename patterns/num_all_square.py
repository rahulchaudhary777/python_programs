a = int(input('enter no. of row '))

#for 1,1,1
for i in range(1,a+1):
    for j in range(1,a+1):
        print('1',end=' ')
    print()
print()

#for 1,2,3 continuously
for i in range(1,a+1):
    b = 1
    for j in range(1,a+1):
        print(b,end=' ')
        b +=1
    print()
print()

''' 1,2,3
    4,5,6 '''
b = 1
for i in range(1,a+1):
    for j in range(1,a+1):
        print(b,end=' ')
        b +=1
    print()
print()
