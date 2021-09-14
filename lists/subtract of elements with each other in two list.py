a = [1,2,3,4,5]
b = [5,4,3,2,1,3,4,5]
c = []
# difference of length between given list
diff = len(a)-len(b)
# for make difference value positive if it return negative
diff = int((diff**2)**0.5)

# make both list length equal by adding ZERO
for i in range(diff):
    if len(a) < len(b):
        a.append(0)
    else:
        b.append(0)    # a = [1,2,3,4,5,0,0,0]
        
# find difference of elements between given list
for i in range(len(a)):
    sum = a[i]-b[i]
    c.append(sum)
print(c)
