name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict() # dictionary to save email address and number-of-times-it-appears

for line in handle:
    line = line.rstrip()
    line = line.lower()
    words = line.split()
   
    try:
        if words[0] == 'from':
            # print(words)
            # print('*** EMAIL FOUND ***',word)
            email = words[1]
            if email not in counts:
                counts[email] = 1
            else:
                counts[email] += 1
    except:
        # print('Blank line')
        continue

# print(counts)

BigEmail = 0
BigCount = 0

for k,v in counts.items():
    # print(k,v)
    if BigCount < v:
        BigCount = v
        BigEmail = k
    else:
        continue

print(BigEmail,BigCount)