def Transpose(m):
    t = []
    result = []
    for i in range( len( m[0] ) ):
        for j in range( len( m ) ):
            t.append( m[j][i] )
        result.append( t )
        t = []
    return result




A = [[2, -9, 3], [13, 11, 17]]
print(Transpose(A))









