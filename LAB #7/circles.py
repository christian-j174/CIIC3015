def pi():
    """Only returns the value of Pi """
    return (3.141592653589793)

def circumference(radius):
    """Returns the circumference of the circle """
    return (pi() * radius * 2)

def area(radius):
    """Returns the area of the circle """
    return (pi() * (radius ** 2))

# Main program
radius = int(input("Enter the radius of a circle: "))
print("The circumference of the circle is:", circumference(radius))
print("The area of the circle is:", area(radius))