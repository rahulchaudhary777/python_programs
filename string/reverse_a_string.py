# reverse string with loop

a = input('enter string ')

print('first method is ')
for i in range(len(a),0,-1):
    print(a[i-1],end='')
print()

# for
print('second method is ')
for i in range(len(a)-1,-1,-1):
    print(a[i],end='')
print()

print('third method is ')
a = a[::-1]
print(a)