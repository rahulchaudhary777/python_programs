# find LCM of two numbers
# take two variable
a = int(input('enter first number '))
b = int(input('enter second number '))
# find greater value
if a > b:
    higher = a
else:
    higher = b
# assign greater value in other variable
value = higher
# loop run whenever condition become true
while True:
    if higher % a == 0 and higher % b == 0:
        print(f'LCM of {a} and {b} is => ', higher)
        break
    else:
        higher += value
