# find a given integer is a perfect square

# take a value from user
a = int(input('input number '))
# assign a variable
c1 = 0
for item in range(1,a+1):
    
    if a // item == item: # 9//3 = 3 => it is perfect square
        c1 += 1
    else:
        continue
if c1 == 1:
    print('true')
else:
    print('false')
       
        
