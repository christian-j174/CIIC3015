# posible solution
# for every multiple add + the number

multiples = int( input( 'Enter the number to calculates its multiples: ' ) )
amount_multiples = int( input( 'Enter how many multiples you want to calculate: ' ) )

list1 = [0]
track = 0

for number in range( 1, amount_multiples + 1 ):  # add the sequence of multiples
    track += multiples
    list1.append( track )

print( f'The multiples of {multiples} are:' )

for i in (list1):  # looping to prints elements from list
    print( i )