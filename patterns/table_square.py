a = int(input('enter no. of rows '))

'''
1 2 3 4 5                                                                                                                                     
2 4 6 8 10                                                                                                                                    
3 6 9 12 15 
4 8 12 16 20                                                                                                                                  
5 10 15 20 25 '''
for i in range(1, a + 1):

    for j in range(1, a + 1):
        b = i * j
        print(b, end=' ')
    print()
