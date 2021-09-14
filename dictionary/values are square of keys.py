# create a dictionary in which values : key^2

a = int(input('input numbers '))
b = dict()

for i in range(1,a+1):
    b[i] = i*i
print(b)
