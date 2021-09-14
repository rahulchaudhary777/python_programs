a = input('enter string ')
b = len(a)

'''
p
py
pyt
pytho
python'''
for i in range(b):
    for j in range(i+1):
        print(a[j],end ='')
    print()
print()

'''
     r
    ra
   rah
  rahu
 rahul'''
for i in range(b):
    for j in range(b-i):
        print(' ',end ='')
    for j in range(i+1):
        print(a[j],end='')
    print()