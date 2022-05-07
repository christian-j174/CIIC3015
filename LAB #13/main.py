def min_max(l1):
    return (min( l1 ), max( l1 ))


theList = [2, 5, 3.14, -6, 1]
theCopy = [2, 5, 3.14, -6, 1]

print(min_max(theList))
print(theList == theCopy) # Make sure list hasn't changed