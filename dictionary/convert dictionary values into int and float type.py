# convert dictionary values into int and float type

# 1. for INTEGER
def type_conversion(d):
    l1,l2 = [],[]
    for i in range(len(d)):
        d1,d2 ={},{}
        for k,v in d[i].items():
        # convert value in INTEGER
            d1.update({k:int(v)})
        # convert value in FLOAT
            d2.update({k:float(v)})
        l1.append(d1)
        l2.append(d2)
    print('convert string into integer',l1)
    print('convert string into float',l2)
    return
print('# 1.')
type_conversion([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}])
print('# 2.')
type_conversion([{'p': '40'},{'a':'12','b':'23','c':'34'}])
