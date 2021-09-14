a = int(input('enter the amount '))
b = int(a/2000)
a = a-b*2000
c = int(a/500)
a = a-c*500
d = int(a/100)
a = a-d*100
print('notes of 2000 & 500 & 100 & reminder amount are ', b,c,d,a)
