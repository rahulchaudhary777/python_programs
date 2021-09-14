# find a missing number from list
# input like this : [1,2,3,4,5,6]
a = list(map(int,input('enter number orderly ').split()))
# assign any variable
x = 1
for i in a:
    if i != x:
        print('missing number is => ',x)
        break
    else:
        x += 1
        
        
