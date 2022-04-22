def beach_dist(file):
    fh = open(file)
    db = dict()
    Maxxx = 99999999999
    d1 = 0
    town = ''
    status = None
    rr = 0
    for line in fh:
        line = line.strip('\n')
        town = line[:line.find(',')]        #desde 0 hasta la primera comma
        distance = line[line.find(',')+1:line.find(' ', line.find(','))]
        status = line[line.find(distance)+ len(distance):]
        status = status.strip()
        db[town] = (int(distance), status)

    for key,value in db.items():
        if value[1] == 'b':
            if (value[0]) < Maxxx:
                rr = key
                Maxxx = value[0]
    return rr

