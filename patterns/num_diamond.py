a = int(input('enter no. of row '))

''' 1
  2,2,2
3,3,3,3,3
  2,2,2
    1
'''
b = 0
for i in range(1,a+1):
    b +=1
    for j in range(a-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print(b,end=' ')
    print()

b = a
for i in range(a-1,0,-1):
    b -=1
    for j in range(a-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print(b,end=' ')
    print()
print()

'''
1 2 3 4 5
  1 2 3
    1
  1 2 3
1 2 3 4 5 '''
b = 1
for i in range(a,0,-1):
    b = 1
    for j in range(a-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print(b,end=' ')
        b += 1
    print()

b = 1
for i in range(2,a+1):
    b = 1
    for j in range(a-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print(b,end=' ')
        b +=1
    print()
print()