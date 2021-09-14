#for integer
a = int(input('enter a number '))

p = a
temp = 0
while a>0:
    b = a%10
    temp = temp*10+b
    a = a//10
print('reverse value is ',temp)
if p == temp:
    print(f'{p} is palindrome')
else:
    print(f'{p} is not palindrome')
print()

# for string
st = input('enter a word ')

x = st
st = st[::-1]
print(f'reverse string is {st}')
if st==x:
    print(f'{x} is palindrome')
else:
    print(f'{x} is not palindrome')