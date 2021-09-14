a = input('enter string ')

if len(a) < 3:
    print(a)
elif a[-1] == 'g' and len(a) > 3:
    print(a+'ly')
else :
        print(a+'ing')
