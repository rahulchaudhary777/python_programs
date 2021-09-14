# sum of (1/2)-(2/3)+(3/4)-(4/5)+----+n
n = int(input('input length of series '))
# initilize variable
x = 0
for i in range(0,n):
    x += ((-1)**(i)) * ((i+1)/(i+2))
print('sum of commented series ->',x)
