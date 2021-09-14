a = int(input('enter a number '))
b = []
# if num = even => a/2 if num = odd => 3*a+1 
while a>1:
    if a%2 == 0:
        a //= 2
        b.append(a)
    else:
        a = 3*a+1
        b.append(a)
print('answer in given format',b)
