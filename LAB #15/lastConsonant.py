def LastConsonant(string, result=None):
    cons = 'qwrtypsdfghjklzxcvbnm'

    if len( string ) == 0:
        return result
    else:
        if string[0].lower() in cons:
            return LastConsonant( string[1:], string[0] )
        else:
            return LastConsonant( string[1:], result )



print(LastConsonant('!@#$%^&*()Z_:; <>a{}[]'))
