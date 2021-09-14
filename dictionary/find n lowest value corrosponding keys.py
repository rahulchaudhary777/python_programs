# find n lowest value of corresponding keys in a dictionary
d = {1:12,4:34,7:56,'a':9,'u':-46,'t':55,5:40}
l = []
def n_lowest(n):
    print(n,'lowest values are :')
    for i in range(n):
        key = list(d.keys())   # list of keys
        value = list(d.values())   # list of values
        
        index = value.index(min(value))   # find minimum value index
        l.append(key[index])    # add that minimum value corrosponding key
        d.pop(key[index])       # remove that key from main dictionary    
    print(l)
    return
n = int(input('input no. of lowest values '))
n_lowest(n)
