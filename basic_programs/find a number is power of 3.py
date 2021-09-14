# find a given number is power of 3
# take a value from user
a = int(input('enter a number '))

while (a%3 == 0):
    a //= 3
if a == 1:
    print('yes')
else:
    print('no')
