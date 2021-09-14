a = list(map(eval,input('enter elements ').split()))
large = 1
for i in a:
    if len(i)>large:
        large = len(i)
        b = i
print(f'largest word is :- {b}\nlargeest word length :- {large}')

