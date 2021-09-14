a = [1, 2, 4, 9, 78, 45, 17, 5, 45, 2, 17, 17, 34, 21]


# del a[11]          # del a[] is invalid syntax
print(a)
del a[1::2]          # this method also allows for slicing
print(a)

print(a.pop(4))    # a.pop() is remove last index element
print(a)

print(a.clear())     # this condition gives none
print(a)             # this method has only blank argument

a = [1, 2, 4, 9, 78, 45, 17, 5, 45, 2, 17, 17, 34, 21]

print(a.remove(2))     # this condition gives none
print(a)              # it removes only first finding element
a.remove()           # this method wants only one argument otherwise it gives type error
print(a)