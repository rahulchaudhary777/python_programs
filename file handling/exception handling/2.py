a, b = map(int, input('enter values ').split())
# without exception handling
# sum = a+c
# print(sum)

# exception handling
try:
    sum = a + c
    print(sum)
except NameError:
    print('An error is occurred')
else:  # It is optional
    print('No error occurred in program')  # It runs when except block didn't run
