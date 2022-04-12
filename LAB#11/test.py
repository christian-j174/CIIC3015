def NewLine(str):
    """ receives a string and returns a modified version
    where these commas, periods, colons and quotes have been removed.
    """
    listString = str.split()
    result = list()

    for word in listString:     #ELIMINA LAS COMAS Y PUNTOS
        rr = word.strip(',.":')
        result.append(rr.lower())

    return result

pp = """To be, or not to be.
That is the question."""

print(NewLine(pp))

# rr = NewLine('Chris, Javi:')
#
# print(rr[0].strip(',.":'))



# def NewLine(str):
#     """ receives a string and returns a modified version
#     where these commas, periods, colons and quotes have been removed.
#     """
#     str = str.lower().strip()
#     str = str.replace(',', '')
#     str = str.replace( '.', '' )
#     str = str.replace( ':', '' )
#     str = str.replace( "''", '' )
#     str = str.replace( '""', '' )