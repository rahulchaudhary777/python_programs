# reverse two number and also reverse its sum
def reverse(a,b):
    return int(str(int(str(a)[::-1]) + int(str(b)[::-1]))[::-1])
print(reverse(130,1))
