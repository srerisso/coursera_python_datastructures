name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict() # dictionary to save email address and number-of-times-it-appears

for line in handle:
    line = line.rstrip()
    line = line.lower()
    words = line.split()
    # print(words)
    for word in words:
        if '@' in word:
            # print('*** EMAIL FOUND ***',word)
            email = word
            if word not in counts:
                counts[email] = 1
            else:
                counts[email] += 1
        else:
            continue

print(counts)

BigEmail = 0
BigAppearences = 0

# for k,v in counts.items():
#     if BigAppearences > v:
#         BigAppearences
