#  Generate  random String of length 5

# a function with 2 non_default variables
def random_string(l=[],st=''):
    import string
    import random
    # take all alphabet in list
    l += list(string.ascii_letters)
    # pick any 5 element from l and convert into string format
    for i in random.choices(l,k=5):
        st += i
    return st
# function call
print('string is :- ')
print(random_string())