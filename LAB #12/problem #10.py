def Passwords(file):
    fh = open( file )
    db = dict()
    username = ''
    password = ''
    for line in fh:
        line = line.strip('\n')
        username = line[:line.find(':')]
        password = line[line.find(':') + 1:]
        db[username] = password
    return db

Passwords('test10.txt')