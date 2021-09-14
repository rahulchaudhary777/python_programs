# find occurance of every number
a = [1,2,3,4,1,2,3,4,2,4,4]
# convert list into set, b = [1,2,3,4]
b = set(a)

for i in b:
    x = a.count(i)     # count no. of occurance of a element
    print(f'occurance of {i} => {x}')
