fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

# print("There were", count, "lines in the file with From as the first word")
for line in fh:
    # print('Line:',line.strip())
    line2 = line.strip().split()
    try:
        if line2[0]=='From':
            print(line2[1])
            count = count+1
    except:
        # print('Linea en blanco')
        continue

print('There were',count,'lines in the file with From as the first word')
