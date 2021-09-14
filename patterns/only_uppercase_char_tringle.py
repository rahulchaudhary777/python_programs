a = int(input('enter no. of rows '))
b = 65
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(chr(b),end='')
        b +=1
    print()
    if b > 87:
        break
