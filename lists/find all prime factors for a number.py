# find all prime factors o=for given number
a = int(input('enter a number '))
lis,x = [],[]
# make list of all prime numbers for that number
for i in range(1,a+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        lis.append(i)
# make list of all prime factors
for i in lis:
    if a%i == 0:
        a //= i
        x.append(i)
    else:
        continue
print('prime factors of given number => ',x)
print('maximum prime factor of given number => ',max(x))
