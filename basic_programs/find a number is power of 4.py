# find a given number is power of 4
# take a value from user
a = int(input('enter a number '))

while (a%4 == 0):
    a //= 4
if a == 1:
    print(a,'is power of 4')
else:
    print(a,'is not power of 4')
