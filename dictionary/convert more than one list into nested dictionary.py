# convert more than one list into nested dictionary

#output :- [{'S001': {'Adina': 85}}, {'S002': {'Leyton': 98}}, {'S003': {'Duncan': 89}}

def nested_dic():
    d = {}
    for i in range(len(l1)):
        d.update({l1[i]:{l2[i]:l3[i]}})
    return d

# nested list INPUTS:-
l1 = ['S001', 'S002', 'S003']
l2 = ['Adina', 'Leyton', 'Duncan']
l3 = [85, 98, 89]

# function call
print('nested dictionary :- ',nested_dic())
