# convert list into n elements lists
# input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output: [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

def n_list(a,n):
    b = [] 

    # calculate no. of sub_list we need
    if len(a)%n == 0:
        count = len(a)//n    # for upper EX. => count = 3
    else:
        count = len(a)//n+1
    # main programm
    for i in range(count):
        x,high = [],0
        while high < n and len(a)>0:
            digit = a.pop(0)   # remove 0th order element and took it
            x.append(digit)    # make a sub_list of given counting
            high += 1
        b.append(tuple(x))           # append sub_list into main list
    print(n,'elements lists are',b)
    
# function call
n_list(list(map(eval,input('enter elements ').split())),int(input('enter sublist element counting ')))
n_list(list(map(eval,input('enter elements ').split())),int(input('enter sublist element counting ')))

