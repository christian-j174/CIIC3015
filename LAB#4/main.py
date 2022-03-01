color = input('Enter the color of the star: ')
temperature = float(input('Enter the temperature of the star: '))




















# run = True
# while run:
#     user = None
#     try:
#         user = int(input("Please enter the fruits servings: "))
#     except:
#         print("Is not a valid number to servings.")
#         break
#
#     label = str(input('Enter the fruit label: ' ))
#     result = 0
#
#     if label == 'apple':
#         result = int( user * 2 )
#         print(f'The recommended servings are: {result}')
#         run = False
#     elif label == 'pear':
#         result = int( user * 3 )
#         print(f'The recommended servings are: {result}')
#         run = False
#     else:
#         print('You need to include fruits in your diet')
#         run = False

# PROBLEM 8
# k_value = 0
# accumulator = 0
# planet_id = int( input( 'Enter a number between 0 to 3 estimate the distance from the Sun to the planets: ' ) )
# x = planet_id
# distance = None
#
# while x != -1:
#     k_value = 2 ** accumulator
#     distance = 0.4 + (0.3 * k_value)
#     print( f'The distance for planet is {distance}' )
#     x -= 1
#     accumulator += 1
# ########################
# k_value = 0
# accumulator = 0
# planet_id = int( input( 'Enter a number between 0 to 3 estimate the distance from the Sun to the planets: ' ) )
# x = planet_id
# distance = None
# run = True
#
# while run:
#     if planet_id == 0:
#         print( 'The distance for planet is Mercury:  0.4' )
#         run = False
#     if planet_id == 1:
#         print( 'The distance for planet is Venus:  0.7' )
#         planet_id -= 1
#
#     if planet_id == 2:
#         print( 'The distance for planet is Earth:  1.0' )
#
#     if planet_id == 3:
#         print( 'The distance for planet is Mars:  1.6' )

# while x != -1:
#     k_value = 2 ** accumulator
#     distance = 0.4 + (0.3 * k_value)
#     print( f'The distance for planet is {distance}' )
#     x -= 1
#     accumulator += 1

# PROBLEM 6
# try:
#     int1 = int(input('Enter a number: '))
#     int2 = int(input('Enter a number: '))
#     result = round((int1/ int2), 2)
#     print('Result:', str(result))
# except:
#     print('Result:','Error!')

# PROBLEM 4
# accumulator = 0  # compares its value to the temperature
# kelvin = float(input('Enter the temperature value in Kelvin: '))
# celsius = kelvin - 273
# while accumulator <= celsius:
#     accumulator += (5 * celsius)
#
# print(f'The temperature value in Celsius after the accumulator is: {accumulator}')


# PROBLEM 5
# num_employees = int(input('Enter the number of employees: '))
# accumulator = 0
# x = num_employees
# while x > 0:
#     y = float(input('Enter the salary of employee: $ '))
#     accumulator += y
#     x-= 1
# avg = accumulator / num_employees
#
# if accumulator >= 2500 * num_employees:
#     print('You exceeded the limit for salaries.')
# else:
#     print(f'Average salary of the employees: $ {avg}' )
#
#


# PROBLEM #6

# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a number: "))
# result = None
# try:
#     result = num1 / num2
#     print(f'Result: {result}')
# except:
#     print(' Error!')

# try:
#     int1 = int(input('Enter a number: '))
#     int2 = int(input('Enter a number: '))
#     result = round((int1/ int2), 2)
#     print('Result:', str(result))
# except:
#     print('Result:','Error!')

# PROBLEM

# user = input('Enter the product classification: ')
# qty = int(input('Enter the quantity of the products: '))
# result = qty
# accumulator = 0
# iterations = qty
#
# while iterations >= 0:
#     if user == 'carbs':
#         accumulator += 0.25
#         result += (accumulator * qty)
#         iterations -= 1
#     elif user == 'vegetables':
#         pass
#     elif user == 'fruits':
#         pass
#     else:
#         print('your product is not in any of the categories')
#
#
# print(result)
#
