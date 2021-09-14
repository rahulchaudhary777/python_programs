# find a key is present or not
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a = eval(input('enter key '))

# 1.
if a in d:
    print('present')
else:
    print('absent')

# 2.
if d.get(a,'none') == 'none':
    print('absent')
else:
    print('present')
for d_keys(),d_values() in d.items():
    print(d_keys,' :- ',d_values)
