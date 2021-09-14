a = int(input('enter no. of rows '))
'''
$$$$$
 $  $
  $ $
   $$
    $'''
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==1 or j==a or i==j:
            print('$',end='')
        else:
            print(' ',end='')
    print()
'''
$
$$
$ $
$$$$'''
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==a or i==j or j==1:
            print('$',end='')
        else:
            print(' ',end='')
    print()
'''
   $
  $$
 $ $
$$$$'''
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==a or j==a or j==a-i+1 :
            print('$',end='')
        else:
            print(' ',end='')
    print()
print()
'''
$$$$
$ $
$$
$  '''
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==1 or j==1 or j==a-i+1:
            print('$',end='')
        else:
            print(' ',end='')
    print()
