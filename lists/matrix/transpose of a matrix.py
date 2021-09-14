# transpose of a matrix

row = int(input('enter no. of rows in matrix '))
colum = int(input('enter no. of columns '))

print('inputs for matrix')
l = []
# for takes user input elements
for i in range(row):
    l1 = []
    for j in range(colum):
        user = int(input(f'enter elements at index {i+1}X{j+1} '))
        # user input store in a list
        l1.append(user)
        # then l1 store in another list means makes a nested list
    l.append(l1)

# for print matrix
print('first matrix is :-')
for i in range(row):
    for j in range(colum):
        print(l[i][j],end=' ')
    print()

# for print transpose matrix
print('transpose of matrix is :-')
# change range of loops BECAUSE  in transpose row become column and column become row
for i in range(colum):
    for j in range(row):
        print((l[j][i]), end=' ')
    print()