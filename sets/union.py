# unoin of set

a = set(map(eval,input('enter space sapreted item ').split()))
b = set(map(eval,input('enter space sapreted item ').split()))

print('user input set -> ',a)
print('user input second set -> ',b)

# 1.
print('union of a and b -> ',a|b)
# 2.
print('second method -> ',a.union(b))
