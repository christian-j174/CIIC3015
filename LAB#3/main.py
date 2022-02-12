

#Problem #1
# a = "The cake was"
# b = 13.56
# c = "inches tall!"
#
#
# print(f'{a} {b} {c}')


#PROBLEM #2
# print("Who's making all that noise?")
# print("I'd like to order Rosie's special, the \"Grand Omelette\".")
# print("""Here's a list of utensils:
# Spoon
# Fork
# \"Spork\"
# Knife""")

#PROBLEM #3

# x = int(input('Enter a number of seconds: '))
# hour = None
# minutes = None
# seconds = None
# #----------------------------------------
# if x >= 3600:
#     if x % 3600 != 0:
#         hour = x // 3600
#         minutes = round(((x/3600) - (x // 3600)) * 60)
#
#         seconds = x % 60
#     else:
#         hour = x // 3600
#         minutes = 0
#         seconds = 0
# #----------------------------------------
# elif x >= 60:
#     hour = 0
#     minutes = x // 60
#     seconds = x % 60
# #----------------------------------------
# elif x < 60 and x > 0:
#     hour = 0
#     minutes = 0
#     seconds = x
# #----------------------------------------
#
# print("Time ",end='')
# print(str(hour), str(minutes), str(seconds), sep=':')

#PROBLEM 15
# Ask the user to enter an integer. If that integer is evenly divisible by 3, return the string "Fizz".
# If that integer is evenly divisible by 5, return the string "Buzz".
# And if the integer is evenly divisible by both 3 and 5, return the string "FizzBuzz". Otherwise, just return the integer.

# x = int( input( 'Enter an integer: ' ) )
#
# if x % 5 == 0 and x % 3 == 0:
#     print( "FizzBuzz" )
#
# elif x % 5 == 0:
#     print( 'Buzz' )
#
# elif x % 3 == 0:
#     print( 'Fizz' )
#
# else:
#     print( x )
#

#PROBLEM #16
# x = float(input('Enter the temperature value: '))
#
# if x > 38:
#     print("You have a fever")
# else:
#     print('You do not have a fever')

#PROBLEM #17
# number = int(input('Enter your number: '))
#
# if number % 2 == 0 and 20 <= number < 50:
#     print('Ok')
# elif number % 2 == 0 and 50 <= number < 70:
#     print('Good')
# elif number % 2 == 0 and 70 <= number < 100:
#     print('Great')
# elif number % 2 == 0 and number >= 100:
#     print('Awesome')
# elif number == 0:
#     print()
# else:
#     print('Bad')
