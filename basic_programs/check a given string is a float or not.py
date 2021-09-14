# check a given string is a float or not

def check_float(s):
    x = s.replace('.','')
    if x.isdigit() == True:
        print('Given string is float')
    else:
        print('given string isn\'t float')
    return
# function call
check_float(input('enter a string : '))
check_float(input('enter a string : '))
# incomplete
