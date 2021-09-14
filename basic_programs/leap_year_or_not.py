a = int(input('enter year '))

if a%4==0 and a%100 != 0 or a%400 == 0:
    print("given year is leap year ")
else:
    print("given year is not leap year ")