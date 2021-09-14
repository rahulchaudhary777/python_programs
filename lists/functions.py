a = [1, 2, 4, 9, 78, 'hello', 'jaat', 45]

# find an object
b = 'jaat'
print('index of', b, 'is ',a.index(b))
print()

# 2.
print("index of all elements ")
for i in a:
    print(i, ' = ', a.index(i))
