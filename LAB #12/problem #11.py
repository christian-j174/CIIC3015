def Inventory(file):
    fh = open(file)
    result = dict()
    for line in fh:
        line = line.strip('\n')
        if line not in result:
            result[line] = 1
        else:
            result[line] += 1
    fh.close()
    return result



