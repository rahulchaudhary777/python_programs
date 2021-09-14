# print 0 1 1 2 3 5 8 -----
# how many numbers want you in this series
n = int(input('enter length of series '))
first = 0
second = 1
# print only first element
print('fabonacci series => ',first,end=' ')
for i in range(1,n+1):
    sum = first + second
    # assine value in fist from second and in second from sum
    first,second = second,sum
    print(second,end=' ')
