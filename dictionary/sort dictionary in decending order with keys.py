# sort assending a dictionary by keys
def decending(d):
    # take key and values in list and sort it
    x = sorted(d.items())
    # remake dictionary with sorted keys
    for key,value in x:
        d1[key] = value
    print('decending order dictionary by keys : ',d1)
    return
# function call
d = {1:23,4:32,-7:9,0:99}
d1 = {}
print('user input dic => ',d)
decending(d)
    
