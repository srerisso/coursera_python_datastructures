name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    line = line.lower()
    words = line.split()
   
    try:
        if words[0] == 'from':
            # print(line)
            words2 = line.split()
            words2 = words2[5].split(':')
            # print('WORDS2:',words2[0])
            hour = words2[0]
            if hour not in counts:
                counts[hour] = 1
            else:
                counts[hour] += 1
    except:
        # print('Blank line')
        continue

# print('COUNTS',sorted(counts.items()))

for k,v in sorted(counts.items()):
    print(k,v)