from random import shuffle

a = list(map(eval,input('enter elements ').split()))
shuffle(a)
print(f'random list is {a}')
