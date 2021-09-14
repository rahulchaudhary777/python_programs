a = list(map(eval,input('enter elements in single quote ').split()))
count,x = 0,0

for i in a:
    if i.isalpha():
        if i == i[::-1]:
            count += 1
    elif i.isdigit():
        if i == i[::-1]:
            x += 1
print(count+x)
