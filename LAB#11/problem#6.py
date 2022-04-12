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

track_words = []
diff_words = 0
total_words = 0

fname = input( "Enter file name: " )
fh = open( fname, 'r' )

for line in fh:
    line = NewLine( line )

    for i in line:
        if i not in track_words:  # Llevar el conteo sobre las palabras unicas
            diff_words += 1
            total_words += 1
            track_words.append( i )
        else:  # Llevar el conteo de cantidad de palabras por lines
            total_words += 1
fh.close()

# Don't forget to close the file when you've finished
print( f"Different words: {diff_words}" )
print( f"Total words: {total_words}" )