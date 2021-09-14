# get a dictionary from user
a = int(input('enter length of dictionary '))
b = {}

for i in range(a):
    x = input('enter keys ')
    y = input('enter values ')
    b.update({x:y})
print(b)
