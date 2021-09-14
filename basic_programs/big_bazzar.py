'''Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the
shopping amount is greater than 25000, the category is GOLD. If the shopping amount is
between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The
discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is
10% of the shopping amount and 5% otherwise. Design a program in python that asks the user
to input the total shopping amount, outputs the category and amount to be paid.'''

a = int(input('enter amount '))
if a>25000:
    print('you are in gold catogery\nyou got 20% discount \ndiscount amount is ',a*20/100 )
    print('payable amount is ',a-(a*0.2))
elif a>10000 and a<=25000:
    print('you are in silver catogery\nyou got 10% discount \ndiscount amount is ', a * 10 / 100)
    print('payable amount is ', a - (a * 0.1))
elif a<=10000:
    print('you are in bronze catogery\nyou got 5% discount \ndiscount amount is ', a * 5 / 100)
    print('payable amount is ', a - (a * 0.05))