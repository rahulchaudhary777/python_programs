st = input()
pos = int(input())
turn = int(input())

s = (st[pos:]+st[:pos]).replace(' ', '')*turn
print(*s)
#  *string :- it (*) returns string all elements in space_separated manner
