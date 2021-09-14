# input : ['abc', 'xyz', 'aba', '1221']
# output : 2

'''a = list(map(eval,input('enter elements ').split()))

count = 0
for i in a :
    if len(i) > 1 and i[0] == i[-1]:
        count += 1
print(f'palindrome elements are in given list {count}')'''

# find list is empty or not
a = list(map(eval,input('enter elements ').split()))
print(type(a))
for i in a:
    if len(i) == 0:
        print('list is empty')
    else:
        print('list is not empty')
