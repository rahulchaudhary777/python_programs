a = int(input('ente no. of rows '))

'''
* * *
*   *
* * *  '''
for i in range(1,a+1):
    for j in range(1,a+1):
        if i == 1 or i == a or j == 1 or j == a:
            print('$',end=' ')
        else:
            print(' ',end=' ')
    print()