
a = list(map(eval,input('enter elements ').split()))
n1, n2, n3 = map(int,input('enter three indexes ').split())

b = []
for i in a :
    if a.index(i) == n1 or a.index(i) == n2 or a.index(i) == n3:
        continue
    else:
        b.append(i)
print(f'updated list is {b}')


