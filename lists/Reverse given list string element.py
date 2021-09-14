# l = ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

l = ['Red', 'Green', 'Blue', 'White', 'Black']
for i in range(len(l)):
    l[i] = l[i][::-1]
print(l)