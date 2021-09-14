# create and display all combinations of letters, selecting each letter from a different key in a dictionary
d = {1:['a','b'],2:['c','d']}
l = []

# calculate total no. of keys in dictionary
length = len(d.keys())
# add all values from dictionary in empty list
for x in list(d.keys()):
    l.append(d.pop(x))
    
print('combinations are :')
# print all combinations
for i in l[0]:
    for j in l[1]:
        print(i+j)
# it is aplicable for 2 keys dictionary
