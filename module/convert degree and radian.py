# convert degree to radian
d = float(input('enter a angle in degree '))
import math
r = d*(math.pi/180)
print('converted angle in radian :- ',r)

# convert radian to degree
rad = float(input('enter a angle in radian '))
degree = rad*(180/math.pi)
print('converted angle in degree :- ',degree)