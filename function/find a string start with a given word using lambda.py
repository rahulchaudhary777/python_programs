# find a string starts with a given word or not
s = input('enter finding word for starting in sentence ')
x = lambda st:True if st.startswith(s) else False
print(x(input('enter a word ')))

# find a string ends with a given word or not
s = input('enter finding word for ending in sentence ')
x = lambda st:True if st.endswith(s) else False
print(x(input('enter a word ')))