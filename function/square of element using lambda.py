l = [1,2,3,4,5,6]
# make square of every element using lambda
print('square of every number ')
x = list(map(lambda sq : sq*sq, l))
print(x)
# cube of every number
print('cube of every number ')
c = list(map(lambda cu : cu**3,l))
print(c)