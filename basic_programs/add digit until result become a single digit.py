# add digit until result become a single digit

# take a number from user
a = int(input('input an element '))
# assign two variable
sum,sum1 = 0,0
while a > 0:
    mod = a%10
    sum = sum*10+mod
    a //= 10
print(sum)
'''# add digit second time
while sum > 0:
    mod1 = sum%10
    sum1 += mod1
    sum //= 10
print(sum1)
'''
