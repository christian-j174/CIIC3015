#
# cars = open ('cars.txt', 'a')
# cars.write ('MY FAVORITE CAR IS THE FORD MUSTANG ')
#
# #print(cars.read())
# cars.close()


# # This program writes three lines of data to a file.
# def main():
#     # Open a file named ff.txt.
#     outfile = open( 'ff.txt', 'w' )
#     # Write the names of three philosphers to the file.
#     outfile.write( 'John Locke\n' )
#     outfile.write( 'David Hume\n' )
#     outfile.write( 'Edmund Burke\n' )
#     # Close the file.
#     outfile.close()
#
#     outfile = open('ff.txt', 'r')
#     print(outfile.readline())
#     # Call the main function.
#
#
# main()





fhand = open('ff.txt')
x = 0
for line in fhand :
    x = x + 1
print(x)