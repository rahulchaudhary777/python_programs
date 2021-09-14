# find list is empty or not

'''a = list(map(eval,input('enter elements ').split()))
print(type(a))
for i in a:
    if len(i) == 0:
        print('list is empty')
    else:
        print('list is not empty')'''
a = list(map(eval,input('enter elements ').split()))
plus,z = 0,0

for i in a:
    if i.isdigit():
        i = int(i)
        x = i%10
        plus += x
        i //= 10
        z += plus
    else:
        continue
print(z)



