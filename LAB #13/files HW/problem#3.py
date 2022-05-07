fname = input("Enter file name: ")

fh = open(fname)
line_count = 0
head_tag = [0,0]
LINES = []

for line in fh:
    line = line.strip('\t')
    line = line.strip('\n')
    line_count +=1
    LINES.append(line)
    if line.startswith('<head>'):
        head_tag[0] = line_count
    if line.startswith('</head>'):
        head_tag[1] = line_count

for line in range(head_tag[0]-1, head_tag[1]):
    print(LINES[line])
