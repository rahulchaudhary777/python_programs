# create a dictionary grouping a sequance of key value pairs
''' input :- [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    output :- {'yellow':[1,3],'blue':[2,4],'red':[1]}'''
# 1. METHOD
def grouping(l):
    result = {}
    for i,j in l:
        result.setdefault(i,[]).append(j)
    print('updated dictionary :- ',result)
    return
# function call
grouping([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])
grouping([('ram',32),('mohan',29),('rahul',18),('ram',12),('roy',43),('rahul',15),('ram',41)])
