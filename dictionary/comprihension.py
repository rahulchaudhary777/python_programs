d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']

dic = {i: j for i, j in d1.items() if i in l1}
print(dic)
