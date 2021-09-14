# get total length of all values
x,a = [],[]

def total_length(d1):
    for value in d1.values():
        # make list of string values length 
        x.append(len(value))
    # sum of list all elements
    print('length of all values : ',sum(x))
    return
# function call
total_length(d1 = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'})
total_length(d1 = {1:'12',2:'23',3:'34',4:'45'})

# for integer

def int_total_length(d2):
    for values in d2.values():
        # make lisst of all int values
        a.append(values)
    print('length of all integer values ',sum(a))
    return
int_total_length(d2 = {1:12,2:23,3:34,4:45,5:56})
