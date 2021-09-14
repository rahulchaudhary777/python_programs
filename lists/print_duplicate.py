a = list(map(eval,input('enter elements with space sapretes ').split()))
b = []
count = 0

for i in a:
    for j in a:
        if i == j:
            count += 1
    if count > 1:
        if i not in b:
            b.append(i)
    count = 0
print(f'duplicate elements list is {b}')
b.sort()
print(f'sorted list are {b}')
