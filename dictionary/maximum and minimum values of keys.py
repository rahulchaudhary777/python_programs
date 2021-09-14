# find maximum and minimum keys by values

a = {'rahul' : 21, 'ramesh' : 67, 'jay' : 10, 'zoy ' : 76}
# 1.
x = max(a.keys(),key=a.get)
print('maximum value of keys ',x)
z = min(a.keys(),key=a.get)
print('minimum values of key ',z)

# 2.
x = list(a.keys()) # list of keys
y = list(a.values())  # list of all values
position = y.index(max(a.values()))  # it return index of maximum value
print('key is -> ',x[position])  # that index is also related with that key


