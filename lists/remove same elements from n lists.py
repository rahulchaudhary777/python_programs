# remove same number from lists
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2, 3, 4, 55, 66, 77]
s1 = set(l1)
s2 = set(l2)
# 1. METHOD with set
print('without position unique elemnts list :- ',list(s1^s2))

# 2. METHOD with list
common = list(s1&s2)
for i in common:
    l1.remove(i)
    l2.remove(i)
print('with correct position unique element list :- ',l1+l2)