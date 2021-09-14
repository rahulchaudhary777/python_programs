# Input : test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11], str, end = 3, 9
# Output : [6, 3, 1, 7, 12, 10, 2, 9, 8, 4, 11]

a = list(map(int,input('enter elements ').split()))

st, end = map(int,input('enter starting and ending point ').split())

# starting list
p = a[0:st]
# middile reversed list
q = a[st:end]
q.reverse()
# end list
r = a[end::]
print(f'reversed list at given range is {p+q+r}')
