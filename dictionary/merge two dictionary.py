# merge two dictionary
def merge(d1,d2):
    d1.update(d2)
    print(d1)
    return
d1 = {1: 10, 2: 20, 3: 30}
d2 = {4: 40, 5: 50, 6: 60}
merge(d1,d2)
