# know about list comprihension

# 1. METHOD
# SIMPLE  method
# without list comprihension
l = []
for i in range(10):
    l.append(i)
print(l)
# with list comprihension
# don't need to declare a empty lit variable
l1 = [i for i in range(10)]
print('new list :- ', l1)

# 2.
# CONDITIONAL method
l_new = []
for i in range(20):
    if i % 2 == 0:
        if i % 3 == 0:
            l_new.append(i)
print(l_new)
# with list comprehension
# don't need to declare a empty lit variable
l_new1 = [i for i in range(20) if i % 2 == 0 if i % 3 == 0]
print('conditional statement list :- ', l_new1)

# 3.
# use if-else
l_1 = []
for i in range(10):
    if i % 2 == 0:
        l_1.append(i)
    else:
        l_1.append('none')
print(l_1)
# with list comprihension
l_2 = [i if i % 2 == 0 else 'none' for i in range(10)]
print('New List :- ', l_2)
