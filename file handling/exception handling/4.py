s = 'rahul'
try:       # name error
    if a in s:
        print(s)
except NameError:
    print('An error is occurred')

try:
    if 'a' in s:
    print(s)
except IndentationError:
    print('An error is occurred')