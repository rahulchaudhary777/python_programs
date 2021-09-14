# convert binary number into decimal number
a = list(input('enter a binary number '))
binary = 0
for i in range(len(a)):
    digit = a.pop()    # get last element from binary number and remove it
    if digit == '1':   
        binary += 2**i
    
print(binary)
