a = eval(input('enter the amount '))
i = eval(input('enter rate of monthly interest '))
t = eval(input('enter the time in months '))
si = (a*i*t)/100
amount = si+a
print('interest & total amount are ',si, amount)
