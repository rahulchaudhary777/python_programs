a = input('enter sentence ')
a = a.split()
high,low = 0,100

for i in a :
    if len(i) > high:
        high = len(i)
        b = i
    elif len(i) < low :
        low = len(i)
        x = i
print(f'largest {high} char. word is {b}\nsmallest {low} char. word is {x}')

