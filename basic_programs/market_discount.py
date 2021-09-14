a = int(input('enter purchasing amount '))
b = a*10/100
if a>1000:
    print('you got 10% discount ')
    print("payable amount is ",a-b)
else:
    print("you did not got any discount ")