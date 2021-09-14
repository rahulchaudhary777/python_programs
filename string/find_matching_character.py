a = input('enter first string ')
b = input('enter second string ')

print("same characters are :- ")
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            print(a[i],end=' ')
        else:
            continue
# little incomplete
