# read any file and return longest line
fp = open('file.txt')
length = len(fp.readlines())
l = []
for i in range(length):
    l.append(len(fp.readlines()[i]))
print(max(l))

# incomplete code