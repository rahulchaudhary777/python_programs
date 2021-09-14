# write all even_odd in different files
fp = open('even.txt', 'w')
fb1 = open('odd.txt','w')
for i in range(1,100):
    if i%2 == 0:
        fp.write(str(i)+' ')
    else:
        fb1.write(str(i)+' ')
