# print only even numbers

a = [1, 6, 3, 45, 2, 9, 7, -5, 46, 10, -21]
b = []
c = []
p = []
q = []

for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(f'even element list is {b}\nodd element list is {c}')

for i in a:
    if i >= 0:
        p.append(i)
    else:
        q.append(i)
print(f'positive element list is {p}\nnegative element list is {q}')
