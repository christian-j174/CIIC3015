# line = "29,Barceloneta"
# maxC = 0  # Farthest distance
# minC = 0  # Closest
# distance = 0  # track distance for every line
#
# x = line.find( ',' )
#
# print(x)
#
# distance = int( line[:x] )
# y = x + 1
# town = line[y::]
# print(town)

ccity = ""
cdist = -1
fcity = ""
fdist = -1
fh = open(cities.txt)
for line in fh:
    line = line.rstrip()
