# exception handling
user = 'Y'
while user.upper() != 'N':
    def fun(*a):
        try:
            x = a[0] / a[1]
            print(x)
        except ZeroDivisionError:
            print('your input is invalid')


    fun(int(input('first ')), int(input('second ')))
    user = input('Do you want re_enter :- ')
