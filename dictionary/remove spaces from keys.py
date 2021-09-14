# remove spaces from keys

def remove_keys(d):
    d1 = {}
    print('dictionary of without space keys : ')
    for i,j in d.items():
        # take a key in string format and remove spaces
        a = i.replace(' ','')
        # add key_value in new empty dictionary
        d1.update({a:j})
    return d1
# function call
print(remove_keys({'1 2':23,'4 3':56,'9 7':76}))
print(remove_keys({'se a ': 8,"ra hu l":18,'za ra':45,'3 0 4':'number'}))
