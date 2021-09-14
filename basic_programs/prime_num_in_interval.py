# Print all Prime Numbers in an Interval
a = int(input("enter lowercase "))
b = int(input('enter upper number '))

print(f'prime numbers between {a} and {b} are')
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)