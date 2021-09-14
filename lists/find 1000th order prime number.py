# find nth order prime number
order = int(input('input order of element '))
lis = []
# make a list of prime numbers elements
for i in range(1,order*10):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        lis.append(i)
# find nth order element using pop method
print(order,'th order element is',lis.pop(order))
