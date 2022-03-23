# def factorial(num):
#     if num<-1:
#         return('Invalid input!')
#     if num==0:
#         return 1
#     if num>0:
#         return num*factorial(num-1)
#
# num=int(input('Enter a non-negative integer: '))
#
# if num<0:
#     print(factorial(num))
# else:
#     print(str(num)+'! = '+ str(factorial(num)))


temp = float( input( "Enter the temperature: " ) )
unit = input( "Enter the unit (C/F): " )


def celsius_to_fahrenheit(temp):
    F = float( round( 9 / 5 * temp + 32, 2 ) )
    return round(F, 1)

def fahrenheit_to_celsius(temp):
    C = float( round( 5 / 9 * (temp - 32), 2 ) )
    return round(C,1)


if unit == 'C':
    # celsius_to_fahrenheit(temp)
    print( str( temp ) + ' Celsius is equivalent to ' + str( celsius_to_fahrenheit( temp ) ) + ' Fahrenheit' )

if unit == 'F':
    print( str( temp ) + ' Fahrenheit is equivalent to ' + str( fahrenheit_to_celsius( temp ) ) + ' Celsius' )

# string = 'aaOOee'
#
# def remove_duplicates(string):
#     track = ''
#     r = ''
#     for i in string:
#         if i != track:
#             r = r + i
#             track = i
#         else:
#             track = i
#     return  r
#
#
#
#
#
# print(remove_duplicates('s'))