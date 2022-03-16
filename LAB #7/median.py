
def median_of_3(arg1, arg2, arg3):
    """return the median  """
    array = [arg1, arg2, arg3]
    array = sorted(array)
    return array[1]


# Main program
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
print("The median is", median_of_3(first, second, third))
