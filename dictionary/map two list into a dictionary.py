# map two list into a dictionary
# keys are :-
k = [1,2,3,4,5]
# values are :-
v = [12,23,34,45,56]
# 1.
# zip convert two itreable into tuple __ it didn't work for single key-value
d = dict(zip(k,v))
print(d)

# 2.
d = {}
for i in range(len(k)):
    for j in range(i,len(v)):
        d.update({k[i]:v[j]})
        break
    # new dictionary
print(d)
