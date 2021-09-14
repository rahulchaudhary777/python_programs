l = [1,2,3,434,3,73,62,450,38,15,1524,35346,1235346,23545]
x = list(filter(lambda s : s%2==0,l))
print('list of even numbers :- ', x)
print('list of odd numbers ')
print(list(filter(lambda s:s%2!=0,l)))