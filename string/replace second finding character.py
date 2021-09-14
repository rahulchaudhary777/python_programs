a = input('enter elements ')
# replace character without changing first characcter
b = a[0]
string = a[1:].replace(b,'$')
print(b+string)

