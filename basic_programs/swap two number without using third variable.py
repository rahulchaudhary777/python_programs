# swap two number without using third variable
# a = 12, b = 6

a, b = map(int,input('enter two space saprated numbers -> ').split())

a = a+b            # a = 12+6 = 18
b = a-b            # b = 12-6 = 6
a = a-b            # a = 18-6 = 12
print(f'swap number a is :- {a}\nb is -> {b}')
