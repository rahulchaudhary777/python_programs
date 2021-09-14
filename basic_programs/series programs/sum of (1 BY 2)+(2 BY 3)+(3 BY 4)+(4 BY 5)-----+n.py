# sum of (1/2)+(2/3)+(3/4)+(4/5)+----+n
n = int(input('input length of series '))
#initilize variable
sum = 0
for i in range(1,n+1):
    sum += i/(i+1)
print('sum of commented series -> ',sum)
