"""
make a array of 3 * 3 and find max value number and resize it.
[[1 2 3]           [[1 3 2]
 [6 5 4]     =>     [5 6 4]       (INPUT AND OUTPUT)
 [8 9 7]]           [8 9 7]]
"""
import numpy

l1 = []
row = int(input('enter row of array '))

for i in range(row):  # append all matrix element in list format
    for j in range(row):
        n = int(input(f'enter a number of {i} row :- '))
        l1.append(n)

a = numpy.array(l1)  # convert list into array
b = a.reshape(row, -1)  # convert array into 3X3 array
print(b)
r_index = row // 2  # for find replacing index

for i in range(row):
    result = numpy.where(b[i] == max(b[i]))  # find index of max. value element in each row
    index = result[0]  # extract only index value from where function

    for j in range(3):  # exchange max value with replacing index
        if max(b[i]) > b[i, r_index]:
            temp = max(b[i])
            b[i, index] = b[i, r_index]
            b[i, r_index] = temp
print(b)  # final result
