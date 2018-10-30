#  Importar statistics para calcular la media
# import statistics

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
scpos = 0
j = 0
confidence = []
value = 0.0
value2 = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    scpos = line.find(':')
    value = float(line[scpos+1:])
    # print(j)
    # print(value)
    confidence.append(value)
    value2 = value2 + value
    j=j+1
    
# print("Done")
# print('Average spam confidence: ',statistics.mean(confidence))
print('Average spam confidence:', value2/j) 
print(value)
print(value2)
