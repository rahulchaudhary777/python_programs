# Generate 6 digit random secure OTP
def otp():
    import random
    password = ''
    # run while we get digit
    for i in range(6):
        # add random number in string form in password
        password += str(random.randint(0, 9))
    return password
# function call
for j in range(int(input('how many OTP you want '))):
    print(otp())
