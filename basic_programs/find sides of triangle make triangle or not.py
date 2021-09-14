# find sides of triangle make a triangle or not and also calculate area

# took values from user
a, b, c = map(int,input('enter three sides of triangle ').split())

# using math formula (two sides addition is greater than remaning side)
if (a+b)>c and (b+c)>a and (a+c)>b:
    print('given sides forms triangle')
    # calculate area using heron\'s formula
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print('area of given triangle is -> ',area)
else:
    print('given sides didn\'t forms triangle')
