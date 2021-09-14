# filter a dictionary based on values
# input :- {'Cierra': 155, 'Alden': 180, 'Kierra': 165, 'Pierre': 190}
# EXP. :- n = 170
# output :- {'Alden': 180, 'Pierre': 190}

def filter_dic(d):
    n = int(input('enter a value for filter dic. '))
    d1 = {}
    for i in d:
        # check greater than user_value
        if d[i] > n:
            # here i MEANS :- key and  d[i] MEANS :- value of dictionary
            d1.update({i:d[i]})
        # return value of d1 Dic.
    return d1
# function call
print(filter_dic({'Cierra': 155, 'Alden': 180, 'Kierra': 165, 'Pierre': 190}))
print(filter_dic({'ram': 12,'saurabh':21,'gaurav':22,'rahul':18,'sellu':19}))
