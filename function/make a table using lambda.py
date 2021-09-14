print('table is :- ')
a = int(input('enter a number which you want make a table '))
for i in range(1,int(input('enter range of table '))+1):
    result = lambda a,i : a*i
    print(result(a, i))
