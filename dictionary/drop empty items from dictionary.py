# drop empty items from dictionary
d1 = {}

def drop_empty(d):
    for i,j in d.items():
        if j is not None:
           d1.update({i:j})
    return d1
print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}))
