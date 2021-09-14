# take dictionary from user
n = int(input('enter length of dictionary '))
b = {}

for i in range(n):
    x = input('enter keys : ')
    y = input('enter values : ')
    b.update({x:y})
print(b)
# remove duplicate elements
a = {}
for key,value in b.items():
    if value not in a.values():
        a[key] = value
print(a)
