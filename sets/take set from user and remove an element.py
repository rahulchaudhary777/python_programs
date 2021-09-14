# enter a set by user
a = set(map(eval,input('enter elements ').split()))
b = eval(input('enter item for remove '))
print('user input set -> ',a)
# remove an element
a.discard(b)
print('updated set -> ',a)

