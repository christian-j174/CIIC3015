




amount = int( input( 'Enter how many vegetables you need to buy: ' ) )
total = int( input( 'Enter total amount of your purchase: ' ) )

for i in range( 1, amount + 1 ):
    discount = amount * 0.05 * total
    total -= discount

print( total )


