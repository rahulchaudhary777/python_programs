# sort list of tuples by list element
def sort_list(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j][-1] > l[j+1][-1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    print(l)
# function call


sort_list([(1, 2), (4, 3), (5, 1), (3, 0)])
sort_list([(9, 4), (4, -3), (2, 6), (5, -1)])
