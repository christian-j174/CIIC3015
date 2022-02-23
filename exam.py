"""  Set P equal  to 10

            Set N equal to 2

            total=1

Repeat while N<= P

     Set P equal to P+P

     N=N*total

    total=total+1

  Print total
"""
# 1
# p = 10
# n = 2
# total = 1
# while n <= p:
#     p = p + p
#     n = n * total
#     total += 1
#
# print(total)


#2
# x = int(input('Age in years? '))
# if x >= 21:
#     print('OK')
# if x < 21:
#     print(f"{21 - x} years left")


# number_students = int(input("number of students? "))
# number_groups = int(input("Groups? "))
# print(f"{number_students % number_groups}")
#

# x = int(input("Enter an integer: "))
# sing = None
# status = None
# if x < 0:
#     sing = 'Negative'
# elif x > 0:
#     sing = 'Positive'
# else:
#     sing = ''
#
#
# if x % 2 == 0:
#     status = 'Even'
# else:
#     status = 'Odd'
#
# print(f"{status} {sing}")
#

# player1 = str(input("Player 1 move: "))
# player2 = str(input("Player 2 move: "))
#
# r,p,s = 'rock', 'paper', 'scissors'
#
# if r in player1 and s in player2:
#     print('Player 1 won') # true
# elif p in player1 and r in player2:
#     print('Player 1 won') # true
# elif s in player1 and p in player2:
#     print('Player 1 won') # true
# else:
#     print('Player 1 did not win') # lose

    # R,P,S = 'rock', 'paper', 'scissors'
    # me, you = me.lower(), you.lower()
    # if R in me and S in you: # the keyword 'in' works similary to '==' and returns a bool
    #     return True
    # if P in me and R in you:
    #     return True
    # if S in me and P in you:
    #     return True
    # return False
    #
    #


# x = int(input('Age? '))
# if x <= 10:
#     print('$5')
#
# elif x > 10 and x <= 60:
#     print('$8')
# elif x> 60:
#     print('$2')


# x = int(input('Enter age: '))
#
# if x <= 1: # 1 year or less
#     print('Infant')
#
# elif x > 1 and x < 13:
#     print('Child')
#
# elif x >= 13 and x < 20:
#     print('Teenager')
#
# else:
#     print('Adult')

# try:
#     x = float(input('Enter number? '))
#     print(f"The number is {x}")
# except:
#     print('No bueno!')



# x = float(input('Number1? '))
# y = float(input('Number2? '))
# z = float(input('Number3? '))
#
# if (x == y) or (x == z) or (z ==y ):
#     print('Duplicates')
#
# if (x < y) and (x < z):
#     print(x)
#
# if (y < x) and (y < z):
#     print(y)
#
# if (z < x) and (z < y):
#     print(z)


x = int(input('Enter a number: '))

counter = x
n = 1
# sequence to 1 to n

while counter != 0:
    n += 1
    counter -= 1
    if n % 5 == 0:
        print(n)







































