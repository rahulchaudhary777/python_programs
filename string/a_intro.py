a = input('enter a name ')
b = input('please enter a date ')
c = input('please enter job name ')

st = '''dear 'rahul'
         you are selected in 'job'
         date 21/05/2003
          please come and join your job on time
           '''
st = st.replace('rahul',a)
st = st.replace("'job'",c)
st = st.replace('21/05/2003',b)
print(st)
