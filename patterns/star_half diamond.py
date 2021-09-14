# print half diamond
a = int(input('enter no. of rows '))
'''
    $
   $ $ 
  $   $
 $     $
$       $
 $     $
  $   $
   $ $
    $ '''
for i in range(1, a//2+2):
    for j in range(1, a+1):
        if i+j == a//2+2 or j-i == a//2:
            print('$', end='')
        else:
            print(' ', end='')
    print()

for i in range(1, a//2+1):
    for j in range(1, a+1):
        if j-i == (a-2)//2:
            print('$', end='')
        else:
            print(' ', end='')
    print()
# incomplete code