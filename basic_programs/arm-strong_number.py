a = int(input())

temp = a
arm = 0
while a>0:
    b = a%10
    arm += b**3
    a //=10
print(temp)
print(arm)
if temp == arm:
    print('armstrong number')
else:
    print('none')