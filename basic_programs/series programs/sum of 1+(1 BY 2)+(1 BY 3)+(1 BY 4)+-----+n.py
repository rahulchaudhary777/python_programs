# sum of 1+(1/2)+(1/3)+(1/4)+----+n
n = int(input('enter length '))
s = 0
for i in range(1,n+1):
    s += 1/i
print('sum of series',s)
