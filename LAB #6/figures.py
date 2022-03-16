# triangle
try:
    lenght = int( input( 'Heihgt: ' ) )
    if lenght > 0:
        for i in range( 1, lenght + 1 ):
            print( '*' * i )
except:
    print( 'Error!' )

# Squares
try:
    height = int( input( 'Height: ' ) )
    width = height  # because all sides are the same distance
    for i in range( 1, height + 1 ):
        print( '*' * width )
except:
    print( 'Error!' )

# rectangles
try:
    height = int( input( 'Height: ' ) )
    width = int( input( 'Width: ' ) )
    for i in range( 1, height + 1 ):
        print( '*' * width )
except:
    print( 'Error!' )

l1 = [2, 3, 6]
l2 = [2, 4, 6, 8]
result = []
for i in l1:
    if i in l2:
        result.append( i )
print( result )
