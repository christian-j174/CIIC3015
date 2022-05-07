nfile = input('Enter file name: ')

fh = open(nfile)
total = 0
nTimes = 0

for line in fh:
    line = line.strip('\n')
    if 'X-DSPAM-Confidence:' in line:
        nTimes += 1
        total += float(line[line.find(' '):])

print(f"Average spam confidence: {(total/nTimes)}")
