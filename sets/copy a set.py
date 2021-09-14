# create a shallow copy set
a = set(map(eval,input('input space saprated item ').split()))
print('original set a is -> ',a)

x = a.copy()
print('copied set x is -> ',x)
