a = [1, 2, 4, 9, 78, 45]
p = a[0]
a[0] = a[-1]
a[-1] = p
print(a)

# find length
# 1.
print(f'length of list is :-  {len(a)}')
# 2.
count = 0
for i in a:
    count +=1
print(f'length of list is :-  {count}')