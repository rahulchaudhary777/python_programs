# concanate two list index wise
a = [1,2,3,4,5]
b = [6,7,8,9,0]
x = []
for i in range(len(a)):
    p = str(a[i])
    q = str(b[i])
    n = p+q
    x.append(int(n))
print('concanate two lists index wise -> \n',x)
