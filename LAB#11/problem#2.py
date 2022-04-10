import math
# HYPOTHENUSE OF A RECTANG;E TRIANGLE


def pithagoras():
    adjacent = float(input("Enter the adjacent side: "))
    opposite = float(input("Enter the opposite side: "))
    hypotenuse = math.sqrt (adjacent ** 2 + opposite ** 2)
    hypotenuse = round(hypotenuse, 2)

    fhandle = open('file_pitagoras.txt', 'a')
    fhandle.write( str( adjacent ) )
    fhandle.write( str( opposite ) )
    fhandle.write(str(hypotenuse))
    fhandle.close()
    print(f'The hypotenuse:  {hypotenuse}')



pithagoras()