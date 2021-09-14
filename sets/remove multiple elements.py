# remove multiple elements at once time
a = set(map(int,input('enter elements ').split()))
print('original set is -> ',a)

x = set(map(int,input('enter removing elements ').split()))
a.difference_update(x)
print('updated set -> ',a)
