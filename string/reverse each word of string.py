# reverse each word in string
"""INPUT  :- My Name is Jessa
   OUTPUT  :- yM emaN si asseJ """
st = list(map(str, input('enter a string ').split()))
_ = []

for i in st:
    _.append(i[::-1])
s = ' '.join(_)
print(s)
