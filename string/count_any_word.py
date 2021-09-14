# by string functionds
a = input('enter a string\n')
b = input('enter a word that you wants to find\n')

st = a.count(b)
print('frequancy of given word ',st)
print()

# by using loop

count = 0
for i in range(len(a)):
    if a[i]==b:
        count +=1
    else:
        continue
print('frequancy of given word ',count)
