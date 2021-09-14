a = int(input('enter date '))
b = int(input('enter month '))
year = int(input('year '))

if year%4==0 and year%100!=0 or year%400==0:
    print('leap year')
    day = 366
else:
    print('not leap year')
    day = 365

m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0,b-1):
    a +=m[i]
print('passing days are ',a)
f = 365-a
print('remaining days are ',365-a)
