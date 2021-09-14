# write armstrong numbers
fp = open('armstrong.txt','w')
fp.write('armstrong numbers are :- ')
fp.close()

fp = open('armstrong.txt', 'a')
for i in range(100,1000):
    l = list(str(i))
    if int(l[0])**3 + int(l[1])**3 + int(l[2])**3 == i:
        fp.write(str(i)+' ')
fp.close()