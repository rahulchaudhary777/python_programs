a = [10, 2, 2, 5, 6, 8, 2, 6]
b = []
l = []
# using loop
for i in a:
    if i not in b:
        b.append(i)
print(b)

# list comprehension
[l.append(i) for i in a if i not in l]
print('list using comprehension :- ', l)
