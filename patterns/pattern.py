# make a pattern of number
# input :- 1234
"""'output :-
   1
  12
 123
1234
234
34
4    """


def pattern(n):
    # length of given number
    length = len(n)
    # 1.PART
    for i in range(length + 1):
        print(n[0:i].rjust(length, ' '))
    # 2.PART
    for i in range(1, length):
        print(n[i:])
    return


pattern(input('enter a number '))
pattern(input('enter a number '))
