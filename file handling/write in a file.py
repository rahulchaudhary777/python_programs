# write in a file
''' in this write method if we rewrite in a file then old content will autometic remove'''

# 1. write a single line
fp = open('file.txt','w')
# 'w' for tell to use writing
fp.write('rahul chaudhary')
fp.close()
# it is must

# 2. write multiple lines in file
fp = open('file1.txt','w')
fp.write('Name : rahul chaudhary\ncollage : gla university\nyear : 1st')
fp.close()