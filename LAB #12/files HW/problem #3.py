def read_numbers(file_name):
    result = 0
    fh = open(file_name)
    #numbers = fh.read()
    for line in fh:
        line = int(line.strip())
        result += line
    return result


print(read_numbers('x.txt'))