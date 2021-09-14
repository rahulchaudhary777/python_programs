a = int(input('enter no. of rows '))

'''
12345
23456
34567
45678
'''
for i in range(1,a+1):
    b = 0
    b +=i
    for j in range(1,a+1):
        print(b,end='')
        b +=1
    print()

'''
13579
1113151719
2123252729
3133353739
4143454749
'''
b = 1
for i in range(1,a+1):


    for j in range(1,a+1):
        print(b,end='')
        b +=2
    print()