# find which type of triangle
# 1.scalene triangle 2. isosceles 3. equilateral triangle
a, b, c = map(int,input('enter three sides of triangle ').split())

if a == b == c:
    print('equilateral triangle')
elif a != b and b != c and a != c:
    print('scalene triangle')
else:
    print('isosceles triangle')
