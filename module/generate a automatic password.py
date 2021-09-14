# generate a 8 digit random automatic password

# function to take all necessary elements for make password in one list
def password(l = []):
    import string
    # string.ascii_letters => it return all upper and lowercase character
    # string.digits => it returns all digits
    # string.punctuation => it returns all punctuation marks
    l = l+list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    return l

# function for generate a password with random word from l
def generate(digit=''):
    # function call of first function
    password()
    import random
    x = random.choices(password(), k=8)     # it returns list
    # convert list in a string format
    for i in x:
        digit += i
    return digit
print('your password is :- ')
# call second function
print(generate())