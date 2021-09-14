# check a sequance is an arithmetic progression or not
def arithmetic(n):
    diff = n[1]-n[0]
    for i in range(len(n)-1):
        if n[i]+diff != n[i+1]:
            return False
    else:
        return True
# function call
print(arithmetic([1,3,5,7,9]))
print(arithmetic([9,7,5,3]))
print(arithmetic([1,4,6,9]))
