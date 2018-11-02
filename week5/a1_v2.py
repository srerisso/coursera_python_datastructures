name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict() # dictionary to save email address and number-of-times-it-appears

for line in handle:
    if len(line) < 1:
        continue
    else:
        if 'From:' in line:
            line = line.rstrip()
            line = line.lower()
            print(line)
            words = line.split()
            email = words[1]
            if email in counts:
                counts[email] += 1
            else:
                counts[email] = 1

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