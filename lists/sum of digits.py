# sum of number digits
# input : [12, 67, 98, 34]
# output : [3, 13, 17, 7]

a = list(map(int,input('enter elements ').split()))
b = []
sum = 0

for i in a:
    while i > 0:
        x = i%10
        sum += x
        i //= 10
    b.append(sum)
    sum = 0
print(b)
