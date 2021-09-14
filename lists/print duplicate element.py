a = list(map(int,input('enter elements with space sepration ').split()))
print(f'your list is {a}')

b = []
count = 0

for i in a:
    for j in a:
        if i ==j:
            count += 1
    if count > 1:
        if i not in b:
            b.append(i)
    count = 0

print(f'duplicates elements are {b}')
b.sort()
print(f'sorted list are {b}')

# take int and character from user
n = list(map(eval,input('enter elements with space sapretion ').split()))
print(n)
