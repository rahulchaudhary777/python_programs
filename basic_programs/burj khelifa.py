# print a pattern like burj_khelifa shape in binary number
n = int(input('enter highest range number '))    # like :- 10, 15, 9

for i in range(n + 1):
    bi = bin(i)[2:]        # convert integer into binary
    # difference between length of binary input value and loop iteration value
    space = int(len(bin(n)[2:])) - int(len(bin(i)[2:]))
    print(' ' * space + bi)     # print iteration after a specific space
