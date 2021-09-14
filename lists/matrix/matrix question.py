# take matrix from user and solve problem
''' matrix :-
1 2 3
5 12 6
9 7 3
IN this question -> find sum of [5*12*6 + 2*12*7]
THAT is 528 after this it reverse is -> 825
SO ANSWER is -> 825'''

row = int(input('enter no. of rows in matrix '))

print('inputs for matrix')
l = []
# for takes user input elements

for j in range(row):
    l1 = list(map(int, input(f'enter {row} space separated element for {j} row ').split()))
    # user input store in a list
    l.append(l1)

# for print first matrix
print('first matrix is :-')
for i in range(row):
    for j in range(row):
        print(l[i][j], end=' ')
    print()
value = (row//2)
sum1, sum2 = 1, 1
for i in range(row):

    sum1 *= l[value][i]
    sum2 *= l[i][value]

new_sum = sum1+sum2
# reverse of new_sum
reverse_sum = str(new_sum)[::-1]
print('sum is ', new_sum)
print('reverse of sum ', reverse_sum)
