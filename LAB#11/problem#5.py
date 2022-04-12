# Sample files are already stored in Moodle server
fname = input( "Enter file name: " )
fh = open( fname )
new_fh = open( "notabs.py", 'w' )

new_string = ''
for line in fh:
    new_fh.write( line.replace( '    ', '   ' ) )

# print( new_string )
fh.close()
new_fh.close()
