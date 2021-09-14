# convert a list into nested dictionary
# take list from user
l = list(map(eval,input('input elements ').split()))
d = current = {}
for i in l:
    # add a key(i) in current_dic.
    current[i] = {} 
    current = current[i]
print('nested dictionary is : ',d)
