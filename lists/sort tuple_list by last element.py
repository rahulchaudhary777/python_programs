# input = [(1,3),(3,2),(2,1)]
# output = [(2,1),(3,2),(1,3)]


a = list(map(eval,input('enter elements of list ').split()))
b = []
x = int(input('enter length of tuple '))

for i in a:
    if len(i) >= x:
        b.append(i)
print(b)
