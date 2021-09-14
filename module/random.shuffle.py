# use of shuffle function
'''
# 1. it can be rearrange the list elements or change the order of list element
# 2. it is work only on list
'''
a = [1, 2, 3, 4, 5, 6]
import random
random.shuffle(a)
print('after use first shuffle :- ',a)
random.shuffle(a)
print('after use second shuffle :- ',a)