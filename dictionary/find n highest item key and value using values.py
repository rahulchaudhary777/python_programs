# pick top three items from shop by it's value

# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#Expected Output:
'''
item4 55
item1 45.5
item3 41.3'''

def top_items(d):
    # run loop for find n highest number
    for i in range(n):
        # list of keys from dictionary
        key = list(d.keys())
        # list of values from dictionary
        value = list(d.values())
        # find maximum value from  value_list
        high = max(value)
        # find index of that max value in value_list
        index = value.index(high)
        # display that index key_value
        print(key[index],high)
        # remove that index key from dictionary
        d.pop(key[index])
    return
# user input_to know how many highest number we want
n= int(input('no. of highest value for find '))
# function call
top_items({'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':-55, 'item5': 24})
