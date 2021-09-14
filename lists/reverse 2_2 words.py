li = list(input('enter a string :- '))
for i in range(0, len(li), 2):
    temp = li[i]
    li[i] = li[i + 1]
    li[i + 1] = temp
print(li)
print(''.join(li))
