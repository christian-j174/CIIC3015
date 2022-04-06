fname = 'cities.txt'  # Use this file name
maxC = 0  # Farthest distance
minC = -1  # Closest
distance = 0  # track distance for every line
Mintown = ''  # Closest city
Maxtown = ''  # Farthest city
town = ''  # track town name

#_----------------------------------
fhandle = open( fname )
for line in fhandle:
    line = line.rstrip()
    x = line.find( ',' )
    distance = int( line[:x] )
    y = x + 1
    town = line[y::]

    if distance < minC or minC == -1:
        minC = distance
        Mintown = town

    if distance > maxC:
        maxC = distance
        Maxtown = town
fhandle.close()


print( f"Closest city is {Mintown}: {minC}" )
print( f"Farthest city is {Maxtown}: {maxC}" )

# Don't forget to close the file when you've finished