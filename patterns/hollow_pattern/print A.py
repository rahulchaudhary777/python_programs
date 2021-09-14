
a = int(input('enter no. of rows '))
'''
$$$$$
$   $
$$$$$
$   $
$   $'''

for i in range(1,a+1):
    for j in range(1,a+1):
        if i==1 or j==1 or j==a or i==a//2+1:
            print('$',end='')
        else:
            print(' ',end='')
    print()
