# first method
a = input('enter a string ')
de = input("enter deleting character ")
for i in range(len(a)):
    if a[i] == de:
        continue
    print(a[i], end='')
print()

# second method
a = input('enter a string ')
de = input("enter deleting character ")
a = a.replace(de, '')
print(a)