# check a dictionary is empty or not
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d1 = {}
def empty(d):
    if len(d.keys()) == 0 :
        print('dictionary is empty')
    else:
        print('dictionary is not empty')
    return
empty({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
empty({})
