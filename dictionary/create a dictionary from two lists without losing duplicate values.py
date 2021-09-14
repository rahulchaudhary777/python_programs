# create a dictionary from two lists without losing duplicate values
# output :- {'1': {21}, '2': {22}, '3': {23}, '4': {22}}
def list_dic():
    d = {}
    for i in range(len(l1)):
        d.update({l1[i]:{l2[i]}})
    return d

# list INPUT :-
l1 = ['1','2','3','4']
l2 = [21,22,23,22]

# function call
print(list_dic())
    
