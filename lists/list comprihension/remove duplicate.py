# remove duplicate elements
l = list(map(eval, input('enter elements ').split()))
l_new = []
[l_new.append(i) for i in l if i not in l_new]
print(l_new)
