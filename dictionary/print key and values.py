# show key, value and item_number from dictionary
d =  {'item1': 45, 'item2':35, 'item3': 41, 'item4':55, 'item5': 24}
c = 0
print('key : value =>  item_number')
for i in d:
    print(i,':',d[i],'=>   ',c)
    c += 1
