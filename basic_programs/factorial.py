a = int(input('enter a number '))
b = 1
for i in range(a, 0, -1):
    b *= i
print(f'factorial of given number is ', b)