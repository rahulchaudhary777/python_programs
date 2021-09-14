# Generate 100 random lottery tickets and pick two lucky tickets from it as a winner
# all lottery number must be 10 digit
# lottery ticket should not be repeat

# make a function with non_default argument
def lottery(s=set()):
    import random
    # add 100 unique 10 digit lottery numbers by using set
    while len(s) < 100:
        s.add(random.randint(1000000000,9999999999))
    l = list(s)
    # take any 2 number from 100 numbers randomly
    result = random.choices(l,k=2)
    return result
# function call
for i in range(int(input('how many times you want to get lucky numbers '))):
    print(f'# {i+1}. lucky winners are :- ')
    print(lottery())
