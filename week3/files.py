xfile = open('mbox-short.txt')
count = 0
for line in xfile:
    line = line.rstrip()
    if line.startswith('From:'):
        count = count+1
    
print('File has ',count, ' emails.')