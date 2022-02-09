# TASK #1


# INICIAR LAS VARIABLES

dollars = 100  # d  TRACK
quaters = 25  # q  TRACK
dimes = 10  # d  TRACK
nickles = 5  # n  TRACK
pennies = 1  # p  TRACK

# test input 0.13

d, q, n, p, dd = 0, 0, 0, 0, 0

test = int( float( input( "Enter an amount: " ) ) * 100 )

for i in range( 25 ):

    if test >= dollars:
        # print('dollars')
        dd += 1
        test -= dollars

    elif test >= quaters:
        q += 1
        test -= quaters
    # print('1')

    elif test >= dimes:
        d += 1
        test -= dimes
    # print('2')

    elif test >= nickles:
        # print('3')
        n += 1
        test -= nickles

    elif test >= pennies:
        # print('4')
        p += 1
        test -= pennies

print( f'dollars: {dd}' )
print( f'quarters: {q}' )
print( f'dimes: {d}' )
print( f'nickels: {n}' )
print( f'pennies: {p}' )
