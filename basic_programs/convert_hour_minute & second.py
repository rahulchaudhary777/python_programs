a = int(input('enter seconds '))
hour = int(a/3600)
a = a%3600
minute = int(a/60)
a = a%60
second = a
print('hour,minute,second ',hour,minute,second)
