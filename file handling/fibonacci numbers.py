# write all fibonacci number upto n terms
fp = open('fibonacci.txt', 'w')
n = int(input('enter range of series '))

first, second = 0, 1
for i in range(n):
    sum = first+second
    first, second = second, sum
    fp.write(str(sum)+' ')
fp.close()