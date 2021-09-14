# find a key when we know value
a = {1: 1, 2: 4, 3: 9, 4: 96, 5: 25, 6: 36, 7: 49}
n = int(input('enter value in dictionary '))

x = list(a.keys()) # list of keys
y = list(a.values())  # list of all values
position = y.index(n)  # it return index of given value
print('key is -> ',x[position])  # that index is also related with that key
