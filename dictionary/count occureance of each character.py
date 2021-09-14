# create a dictionary from string
# MEANS count occurance of each character from string
l = list(input('input a string '))
# 1.
def st_dic(l):
    # convert list into set for remove duplicate
    s = set(l)
    d = {}
    print('occurence of each character :')
    print('FIRST METHOD :')
    for i in s:
        # append key,value into dic.
        d[i] = l.count(i)
    return d
print(st_dic(l))

# 2.second method
dic = {}
print('SECOND METHOD :')
for i in l:
    count = 0
    for j in range(len(l)):
        if i == l[j]:
            count += 1
        else:
            continue
    # append key,value into dic.
    dic.update({i:count})
print(dic)
