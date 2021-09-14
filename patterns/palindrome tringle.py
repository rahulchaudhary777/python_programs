'''
1
121
12321
1234321'''
# 1.
n = int(input('enter no. of rows '))
for i in range(1,n+1):
    print(int('1'*i)**2)

# 2.
def palin(n):
    for i in range(1,n+1):
        print(int('1'*i)**2)

palin(int(input('enter no. of rows -> ')))
