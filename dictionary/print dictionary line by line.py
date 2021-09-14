# print a dictionary line by line
d = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in d:
    # display key
    print(i)
    # enter into value of that key which just before display
    for j in d[i]:
        # display nested key_value
        print(j,':',d[i][j])

 
