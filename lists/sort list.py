# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
l1 = []
for i in l:
    if type(i) == int:
        l1.append(i)
        l.remove(i)
a = sorted(l)
b = sorted(l1)
print(b+a)