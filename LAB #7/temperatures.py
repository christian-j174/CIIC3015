def celsius_to_fahrenheit(arg1):
    result = (temp * 9 / 5) + 32
    return round( result, 1 )


def fahrenheit_to_celsius(arg1):
    # C = 5/9 * (F - 32)
    result = (5 / 9) * (arg1 - 32)
    return round( result, 1 )


# Main program
temp = float( input( "Enter the temperature: " ) )
unit = input( "Enter the unit (C/F): " )

if unit == 'C':
    x = celsius_to_fahrenheit( temp )
    print( f"{temp} Celsius is equivalent to {x} Fahrenheit" )

elif unit == 'F':
    x = fahrenheit_to_celsius( temp )
    print( f"{temp} Fahrenheit is equivalent to {x} Celsius" )


