# convert a number into OCTAL, HEXADECIMAL, BINARY
def print_formatted(number):
    # your code goes here
    l1 = len(bin(n)[2:])
    for i in range(1,n+1):
        
        print(oct(i)[2:].rjust(l1,' '),end = ' ')
        print(hex(i)[2:].rjust(l1,' ').upper(),end = '  ')
        print(bin(i)[2:].rjust(l1,' '),end = ' ')
        print()
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

'''input = 12
output = 
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100'''
