filename = input("file name")
fh = open(filename)

for line in fh:
    fh = fh.strip('\n')
