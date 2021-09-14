# Write a program to find sum of all even numbers upto 30 except 10 and 20.
a = int(input('enter endpoint number '))
b = 0
for i in range(2,a+1):
    if i%2==0:
        if i == 10 or i == 20:
            continue
        b +=i
        print(i)
print(f'sum of all even numbers except 10 & 20 is {b}')