# check all values are same in dictionary
# INPUT :- {'Cierra': 12, 'Alden': 12, 'Kierra': 12, 'Cox': 12}
# user_input 'n' for check
# OUTPUT :- True

# 1.METHOD
def with_input(n):
    result = all(j == n for i,j in d.items())
    return result
# function call
d = {'Cierra': 12, 'Alden': 12, 'Kierra': 12, 'Cox': 12}
print(with_input(int(input('enter a value to check other '))))
print(with_input(int(input('enter a value to check other '))))

# 2. METHOD
# check this without take user_input 'n'
print('2nd METHOD :-')
def without_input(d):
    c = 0 # for counting
    for i in d.values():
        # check first element of values list is equal to every value_list element 
        if list(d.values())[0] == i:
            c += 1
        else:
            continue
    # return true if same value counting is equal to length of dictionary
    if c == len(d):
        return True
    else:
        return False
print(without_input({'Cierra': 15, 'Alden': 15, 'Kierra': 15, 'Cox': 15}))
print(without_input({'Cierra': 20, 'Alden': 22, 'Kierra': 35, 'Cox': 20}))
