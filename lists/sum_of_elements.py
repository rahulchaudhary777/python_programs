# find sum of elements

a = [1, 6, 3, 45, 2, 9, 7, -5]
b = sum(a)
print(f'sum of given elements is {b}')

mul = 1
# multiply all numbers
for i in a:
    mul *= i
print(f'multiply of given elements is {mul}')

# smallest number

print('smallest elements of given list is ',min(a))

# greatest element

print('greatest element of given list ',max(a))

# second greatest & smallest element

a.sort()
print(f'second largest element is {a[-2]}\nsecond smallest element is {a[1]}')
print('sorted list is ',a)

# Nth greatest element
n = int(input('enter order of greater element '))
print(f'{n}th greatest element is {a[-n]}')
