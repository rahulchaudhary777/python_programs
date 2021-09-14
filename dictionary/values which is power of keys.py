# create dictionary which values is power of keys
n = int(input('enter length of dictionary '))

def power_of_keys(n):
    for i in range(1,n+1):
        d[i] = i**2
    print('updated dictionary is : ',d)
    return
d = {}
power_of_keys(n)
