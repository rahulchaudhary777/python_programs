# count the occurence of each word in string
a = input('enter string ')
l = a.split(' ')
d = {}

for item in l:
    c = 0
    for i in range(len(l)):
        if item == l[i]:
            c += 1
    d.update({item: c})
print('occurence of each character -> \n', d)
