#sort values_list of dictionary
d = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3,-6,0,-4]}
d1 = {}
print('sorted value dictionary : ')
def sort_value():
    for key,value in d.items():
        d1.update({key:sorted(value)})
    return d1
print(sort_value())
