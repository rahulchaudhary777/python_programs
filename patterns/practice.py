# cook your dish here
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
c = 0

for i in range(len(l)):
    if l[i] == i:
        print(l[i])
        c += 1
if c < 1:
    print("-1")
