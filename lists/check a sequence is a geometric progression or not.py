# check a sequence is a geometric progression or not
def geometric(n):
    # calculate common ratio of sequance
    diff = n[1]/n[0]
    for i in range(len(n)-1):
        if n[i]*diff != n[i+1]:
            return False
    else:
        return True
# function call
print(geometric([54,18,6,2]))
print(geometric([3,12,48,192]))
print(geometric([1,5,20,60,240]))
