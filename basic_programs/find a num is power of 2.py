# 1.
# find a given number is power of 3
# take a value from user
a = int(input('enter a number : '))

while (a%3 == 0):
    a //= 3
if a == 1:
    print(a'is power of 2')
else:
    print(a,'is power of 2')
# 2.

x,res = 0,0
while res<a:
    res = 1<<x    # bitwise left_shift opreator
    if a == res:
        print(a,'is power of 2')
        break
    x = x+1
else:
    print(a,'is not power of 2')
    
# 3.
if (a**2)&(a**2-1) == 0: # bitwise AND opreator
    print('yes')
    
else:
    print('no')

