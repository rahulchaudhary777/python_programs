# Generate 3 random integers between 100 and 999 which is divisible by 5
# make a function
def rand(a,b,r = 0):
    # use random module
    import random
    # loop for print 3 int.
    while r < 3:
        # module function for get random integer with range
        x = random.randint(a, b)
        if x%5 == 0:
            print(x)
            r += 1
    return
# function call
print('# 1')
rand(a = int(input('starting range ')),b = int(input('last range ')))
print('# 2')
rand(a = int(input('starting range ')),b = int(input('last range ')))