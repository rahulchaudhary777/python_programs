a = [1, 2, 4, 9, 78, 'hello', 'jaat', 45]

# clear a string
# 1.
print('first method is ')
print(a.clear())

# 2.
print('second method is ')
for i in a:
    print(a.remove(i))
print(a)

# 3.
print('third method is ')
for i in a:
    a = a.pop(i)
print(a)
