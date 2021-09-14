# remove item if it is present
a = set(map(eval,input('enter space sapreted item ').split()))

print('user input set -> ',a)
x = eval(input('enter an item '))
a.discard(x)
print('updated set -> ',a)
