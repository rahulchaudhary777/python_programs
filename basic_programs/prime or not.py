# check a number is prime or not
def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('not prime number')
                break
        else:
            print('prime number')


prime(int(input('input a number => ')))
