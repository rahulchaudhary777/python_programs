# clear the list of values in dictionary
# output :- {'C1': [], 'C2': [], 'C3': []}
d = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

for i in d:
    d[i].clear()
print(d)
