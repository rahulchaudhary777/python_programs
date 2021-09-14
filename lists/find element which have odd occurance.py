# find a element which have odd occurance
a = [1,2,3,4,1,2,3,4,2,4,4]
# convert list into set, b = [1,2,3,4]
b = set(a)
print('number which have odd occurance => ',end = '')
for i in b:
    x = a.count(i)     # count no. of occurance of a element
    if x%2 != 0:
        print(i,end=' ')
    else:
        continue
    
