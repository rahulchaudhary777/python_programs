# Python Check if a Substring is Present in a Given String
a = input('enter a string\n')
b = input("enter sub_string that you wants to find\n")
st = a.find(b)
if st==-1:
    print('given sub_string not existing in given string')
else:
    print('index of given sub_string in main string ',st)