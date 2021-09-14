# Roll dice in such a way that every time you get the same number
def dice():
    import random
    for i in range(int(input('how many times you want same number '))):
        # random.seed(12) => it is used for get same output value
        # its parameter doesn't matter we can fill any number but can't remain blank
        random.seed(10)
        same_num = random.randint(1,6)
        print(same_num)
    return
# function call
dice()