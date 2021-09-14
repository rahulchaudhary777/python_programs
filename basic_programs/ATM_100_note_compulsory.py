a = int(input('enter the amount '))
a = a-100
b = int(a/2000)
a = a % 2000
c = int(a/500)
a = a % 500
d = int(a/100)
a = a % 100
print('notes of 2000 & 500 & 100 & reminder amount are ', b, c, d+1, a)
