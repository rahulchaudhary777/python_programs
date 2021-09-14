# add two list
a = list(map(eval,input('enter first elements ').split()))
b = list(map(eval,input('enter second elements ').split()))
l = len(a)-len(b)-1

for i in range(0,len(b)):
    if l-i >= len(a):
        break
    else:
        a[i] = a[i]+b[i]
print(a)
