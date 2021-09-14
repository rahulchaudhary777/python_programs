a = int(input('enter total remaining days in year '))

count = 0
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # days in every month's

print(f'convert {a} days into months ')
for i in range(11,-1,-1):
    if a>27:
        a -=m[i]
        count +=1
        print(m[i])

print('remaning months are ',count)
print('remaining days are ',a)