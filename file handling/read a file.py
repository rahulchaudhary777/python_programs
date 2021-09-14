# read a file
'''it has 4 method :-
1. read()   2. read(n)   3. readline()   4. readlines()'''
fp = open('file.txt')
x = fp.read()
print(x)
fp.close()

fp = open('file1.txt')
x = fp.read(11)
# read(n) is read n numbers characters in file
print(x)
fp.close()

fp = open('file.txt')
r = fp.readline()
# it read only first line
print(r)
fp.close()

fp = open('file1.txt')
print(fp.readlines())
# it reads all lines from file
fp.close()

# we can also use slicing in read.lines() method
fp = open('file.txt')
print(fp.readlines()[1:4:2])
fp.close()