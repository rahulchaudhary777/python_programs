# find max. winner name from them
# if winner more than one then decide name fron alphabetical order
l = ['ram', 'ram', 'ramesh', 'joy', 'roy', 'joy', 'ram', 'joy']  # output = joy
d, l1 = {}, []

for i in l:
    if i not in d.keys():
        d[i] = l.count(i)
max_ = max(d.values())

for i, j in d.items():
    if j == max_:
        l1.append(i)
sort = sorted(l1)
print('winner is :- ', sort[0])
