#take element in list without using eval
# input : 1
#       : 2
#       : rahul
# output : [1,2,'rahul']

l = []
for i in range(int(input('enter list length : '))):
    # take element from user
    x = input('enter elements ')
    if x.isdigit() == True:
        l.append(int(x))
    elif (x.replace('.','')).isdigit() == True:
        l.append(float(x))
    else:
        l.append(x)
print(l)
