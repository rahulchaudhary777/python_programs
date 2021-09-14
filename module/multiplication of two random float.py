#  Calculate multiplication of two random float numbers
# conditions :-
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5

def float():
    import random
    # random.random() => it returns float b/w 0.1,1
    # random.uniform() => it returns float b/w given range
    cross = random.random() * random.uniform(9.5,99.5)
    return cross
print(float())