# make a largest number by using list

l2 = []
def num(l):
    x = ''
    for i in range(len(l)):
        l2.append(str(max(l)))
        l.remove(max(l))
        x += l2[i]
    print(x)
    return
num([2,7,4,9,8])
num([8,1,9])
