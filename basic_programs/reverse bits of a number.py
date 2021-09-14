# reverse bits of a number
# take input from user
a = int(input('enter a number '))
res = 0
for i in range(32):
    res <<= 1
    res |= a&1
    a >>= 1
print(res)
