"""
Your task is to write a function that receives the name of the file,
read the file and returns the nearest city to San Juan that has a beach.
"""

def shortest_beach(file):
    fh = open(file)
    town = ''
    shortest_town = ''
    distance = 0
    d1 = 0
    town = ''
    status = None
    starting_run = 1
    for line in fh:
        line = line.strip()
        town = line[:line.find(',')]        #desde 0 hasta la primera comma
        distance = int(line[line.find(',')+1:line.find(' ')])
        status = line[line.find(' '):]
        #print(status, town)
        # --------------------------------------------
        if status == 'b':
            if starting_run == 1:  # ESTE ES UN CASO ESPECIAL PARA EL VALOR MINIMO
                starting_run -= 1
                d1 = distance
                shortest_town = town
            # -------------------------------------------
            if distance < d1:
                d1 = distance
                shortest_town = town

    print(shortest_town)





shortest_beach('test5.txt')