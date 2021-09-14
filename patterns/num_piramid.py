a = int(input('enter no. of row '))

'''  1
   1,2,3
 1,2,3,4,5  '''
b = 1
for i in range(1,a+1):

    for j in range(a-i):
        print(' ',end=' ')
    for j in range((2*i-1)):
        print(b,end=' ')
        b += 1
    print()
print()

''' 
3,3,3,3,3
  2,2,2  
    1'''
b = a+1
for i in range(a,0,-1):
    b -=1
    for j in range(a-i):
        print(' ',end=' ')
    for j in range((2*i-1)):
        print(b,end=' ')
    print()
