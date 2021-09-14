# print subtraction of two matrix

# for first matrix
row = int(input('enter no. of rows in matrix '))
colum = int(input('enter no. of columns '))

print('inputs for FIRST matrix')
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

# take user input for SECOND matrix
print('inputs for SECOND matrix')

l_new = []
# for takes user input elements
for i in range(row):
    l2 = []
    for j in range(colum):
        user = int(input(f'enter elements at index {i+1}X{j+1} '))
        # user input store in a list
        l2.append(user)
        # then l1 store in another list means makes a nested list
    l_new.append(l2)

# for print first matrix
print('first matrix is :-')
for i in range(row):
    for j in range(colum):
        print(l[i][j],end=' ')
    print()

# for print second matrix
print('second matrix is :-')
for i in range(row):
    for j in range(colum):
        print(l_new[i][j],end=' ')
    print()

# for print subtraction of two matrix
print('subtraction of two matrix is :-')
for i in range(row):
    for j in range(colum):
        print((l[i][j])-(l_new[i][j]), end=' ')
    print()