# initialize variables

set1 = []
user = None


def div2(arg1):
    if arg1 % 2 == 0:
        return True
    else:
        return False


run = True
# Main Loop
while run:
    try:
        user = input( 'Number? ' )
        if user == 'done':

            if len( set1 ) < 1:
                print( 'Need at least 1 value' )
                continue

            elif len( set1 ) == 1:
                # print(set1[0])
                run = False
                continue

            else:
                run = False
                continue

        log_user = float( user )  # if this returns an error go to except
        set1.append( log_user )  # Append element to set

    except:
        print( 'Please enter a number, or "done"' )

array = sorted( set1 )  # Reoder list
p = len( array )  # To identify the index of the elements

########################################################

#####################################################


if div2( len( set1 ) ):  # In case the list is even
    x1 = float( ((p / 2) - 1) )
    x2 = float( ((p / 2) - 1) + 1 )
    x1, x2 = int( x1 ), int( x2 )
    rr = (int( array[x1] ) + int( array[x2] )) / 2
    print( rr )

elif len( set1 ) == 1:
    print( f"{set1[0]}" )

elif len( set1 ) > 1:
    if len( set1 ) == 1:
        array = [1, 2, 3, 4, 5]
    x3 = p - 1
    x4 = int( x3 / 2 )  # find the half
    print( f'{array[x4]}' )


