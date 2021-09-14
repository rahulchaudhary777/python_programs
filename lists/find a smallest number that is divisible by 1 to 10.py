# find a smallest number that is devisible by 1 to 10
a = int(input('enter last range '))
found = False
temp = a
while found == False:
    count = 0
    for i in range(1,a+1):
        if temp%i == 0:
            count += 1
    if count == a:
        print(temp)
        found = True
    temp += 1
# run for only last range 12
# BECAUSE above this it takevery much for run
