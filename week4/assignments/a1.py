fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for t in line.split():
        if t not in lst: lst.append(t)

lst.sort()
print(lst)
