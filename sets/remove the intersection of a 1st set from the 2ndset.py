# remove intersection of 1st set from 2nd set
a = {1,2,3,4,6,5}
b = {9,4,7,8,5,6}

x = a&b
print('intersection of a and b is -> ',a&b)

for i in x:
    a.discard(i)
print('updated set -> ',a)
