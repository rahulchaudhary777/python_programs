# Python – Remove empty List from List

a = [1, 34, [], 34, 5, 3, [36, -4, 9], -24, [], -3, 5, -9]

for i in a:
    if i == []:
        a.remove(i)
    else:
        continue
print(a)

# Cloning or Copying a list
a = [1, 34, [], 34, 5, 3, [36, -4, 9], -24, [], -3, 5, -9]
b = []
for i in a:
    b.append(i)
print(f'original list is {a}\n\ncopies list is {b}')

# count an element
a = [1, 34, [], 34, 5, 34, [36, -4, 5], -24, [], -3, 5, -9]
p = int(input('enter an element '))
x = a.count(p)
print(f'occuerence of {p} is {x}')

