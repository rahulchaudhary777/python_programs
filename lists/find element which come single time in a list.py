# find a number which come in single time in list
# input : [5, 3, 4, 3, 5, 5, 3]
# Output : 4

# take list from user
a = list(map(int,input('enter elements ').split()))
for i in a:
    if a.count(i) == 1:
        print('single time coming element => ',i)
    else:
        continue
