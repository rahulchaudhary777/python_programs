# print second largest number

a = list(map(eval,input('enter elements ').split()))
a.remove(max(a))
print('second largest number : ',max(a))

# print second lowest number

a.remove(min(a))
print('second lowest number : ',min(a))
