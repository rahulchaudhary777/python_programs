#1. using predefined function
a = map(int,input('enter a number ').split())
print(max(a))


# 2.using if anf logical opreator
a, b, c = map(int,input('input three variables ').split())
if a>b and a>c:
    print(f'largest number is {a}')
elif b>c and b>a:
    print(f'largest number is {b}')
else:
    print(f'largest number is {c}')
    
# 3. using nested if-else
if a>b:
    if a>c:
        x = a
    else:
        x = c
elif b>a:
    if b>c:
        x = b
    else:
        x = c
else:
    x = c
print('largest number is ',x)
