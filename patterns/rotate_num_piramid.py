a = int(input('enter no of rows '))
# it is only for odd numbers apply
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
for i in range(1,(a//2+2)):
    print('$ '*i)
for j in range((a),(a//2+1),-1):
    print('$ '*(j-(a//2+1)))
