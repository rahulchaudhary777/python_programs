# filter the height and width of students, which are stored in a dictionary
# EXP :- Height > 6ft and Weight> 70kg:
# output :- {'Cierra Vega': (6.2, 70)}

# user input dictionary  
d = {'Cierra': (6.2, 71), 'Alden': (5.9, 65), 'Kierra': (6.0, 68), 'Cox': (5.8, 66)}

def filter(h,w):
    d1 = {}
    for i,j in d.items():
        if j[0] > h and j[1] > w:
            d1.update({i:(j[0],j[1])})
    print('filtered string :-',d1)
# function call
# take height(h) and weidth(w) from user
filter(float(input('enter height for filter dic ')),int(input('enter weidth for filter dic ')))
