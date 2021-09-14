# push all zeros in the end of list
# take a list from user
a = list(map(int,input('enter elements ').split()))
i = 0
while i < len(a) :
    if a[i] == 0:
        a.remove(0)    # remove zero from list
        a.append(0)    # add zero in end of list
        i += 1         # increase index of list 
    else:
        i += 1
print('updated list => ',a)

