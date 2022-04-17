# def NewLine(str):
#     """ receives a string and returns a modified version
#     where these commas, periods, colons and quotes have been removed.
#     """
#     listString = str.split()
#     result = list()
#
#     for word in listString:     #ELIMINA LAS COMAS Y PUNTOS
#         rr = word.strip(',.":')
#         result.append(rr.lower())
#
#     return result
#
# track_words = []
# diff_words = 0
# total_words = 0
#
# fname = input( "Enter file name: " )
# fh = open( fname, 'r' )
#
# for line in fh:
#     line = NewLine( line )
#
#     for i in line:
#         if i not in track_words:  # Llevar el conteo sobre las palabras unicas
#             diff_words += 1
#             total_words += 1
#             track_words.append( i )
#         else:  # Llevar el conteo de cantidad de palabras por lines
#             total_words += 1
# fh.close()
#
# # Don't forget to close the file when you've finished
# print( f"Different words: {diff_words}" )
# print( f"Total words: {total_words}" )
#





fname = input( "Enter file name: " )

fh = open( fname, 'r' )
read_data = fh.read()
read_data = read_data.lower()
qq = read_data.split()
newList = []

for word in qq:
    rr = word.strip( ',.":' )
    newList.append( rr)

unique_words = 0
unique_wordsV1 = []

for word in newList:
    if word not in unique_wordsV1:
        unique_words += 1
        unique_wordsV1.append(word)


print( "Different words:", unique_words )
print( "Total words:", len( qq ) )