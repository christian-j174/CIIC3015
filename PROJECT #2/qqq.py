def translator():
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    n = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

    num = input( 'Enter phone number in format of XXX-XXX-XXXX: ' ).upper()

    index = 0
    x = ''

    for index in range( len( num ) ):

        if num[index].isalpha():

            x += str( n[alpha.index( num[index] )] )

        else:
            continue
            x += num[index]

    ss = x[0:2] + '-' + x[5:7] + '-' + x[9:12]

    return f"The number is {x}"


print(translator())

