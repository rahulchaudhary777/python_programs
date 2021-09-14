a = list(map(eval,input('enter elements ').split()))
b = list(map(eval,input('enter elements ').split()))

count = 0
for i in a :
    for j in b:
        if i == j:
            count += 1
if count >= 1:
    print('same number found ')
print(f'same elements are {count}')
