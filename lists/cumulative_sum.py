# print cumulative sum of given elements

'''a = list(map(eval,input('enter elements ').split()))
b = []
sum = 0
for i in range(len(a)):
    for j in range(i+1):
        sum += a[j]
    b.append(sum)
    sum = 0
print(f'cumulative list is {b}')'''
    
# Input : [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
x = int(map(int,input().split(',')))
print(x)
