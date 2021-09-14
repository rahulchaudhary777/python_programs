# mulyiply of all elements

a = {1: 1, 2: 4, 3: 9, 4: 16}

x,t = 1,1
for i in a.keys():
    x *= i

for i in a.values():
    t *= i
print('multiply of all elements in dictionary -> ',x*t)
