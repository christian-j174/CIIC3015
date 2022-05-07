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


#
# def beach_dist(fname):
#   cCity=''
#   cDistance=0
#   fh=open(fname)
#   for line in fh:
#     line=line.rstrip()
#     comma=line.find(',')
#     city=line[:comma]       #encuentra el town
#     space = city.find( ' ' )
#     print(space)
#     dist=line[comma+1:space]
#     n_or_nb=line[space+1:]
#     if n_or_nb=='b':
#       d=int(dist)
#       if cDistance==0 or cDistance>d:
#         cDistance=d
#         cCity=city
#   fh.close()
#   return str(cCity)
#
#
# beach_dist('test5.txt')