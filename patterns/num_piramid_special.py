a = int(input('enter no. of rows '))

'''    1
      212
     32123
    4321234'''
b = 1
for i in range(1,a+1):
    for j in range(a-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end ='')
    for j in range(2,i+1):
        print(j,end='')
    print()
