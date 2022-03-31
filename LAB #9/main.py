
#Problem 1
# mystr = 'yes'
# mystr += 'no'
# mystr += 'yes'
# print(mystr)

#problem #2
# mystr = 'abc' * 3
# print(mystr)

#problem #3
# mystring = 'abcdefg'
# print(mystring[2:5])

#problem #4
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# print(numbers[4:6])

#problem #5
# name = 'joe'
# print(name.lower(), name.upper(), name)

#problem #6
# my_string = 'I love programming'
#
# print(my_string[-1])

#problem #7
# ll = ['cookies', 'milk', 'fudge', 'cake', 'ice cream']
# mystring = 'cookies>milk>fudge>cake>ice cream'
# if mystring.split('>') == ll:
#     print('yes')
# # print(mystring.split('>'))

#problem #10
#
# def SumOfDigits(n):
#     nn = str(n)
#     accumulator = 0
#     for i in nn:
#         accumulator += int(i)
#     return accumulator
#
# print(SumOfDigits(827104))


#PROBLEM #11
# def split_string(split_str, sub_str, index):
#     result = split_str.split( sub_str )
#     return result[index]
#
#
# print(split_string("CIIC 3015"," ",0))
#
# """
# El primer arg es el string, el segundo es el sub-string or character used for
# spitting the string, and the third parameter is the position
#
# """

#PROBLEM 12

# def print_pyramid(n):
#     for number in range( 1, n+1 ):  # range(n,0,-1) creates a decreasing sequence from n to 1
#         line = ''
#         for k in range( 1, number +1 ):
#             line = line + '*'
#         print( line )

#PROBLEM 13
# def number_diagonal(n):
#     for number in range( 1, n+1 ):  # range(n,0,-1) creates a decreasing sequence from n to 1
#         line = ''
#         for k in range( 1, number +1 ):
#             if k == number:
#                 line = line + f"{k}"
#             else:
#                 line = line + ' '
#         print( line )


#PROBLEM #20

#
# def translate():
#     result =''
#     for i in user:
#         print(type(i )
#         # if i == '-':
#         #     pass
#         # elif i == 'A' or i == 'B' or i == 'C':
#         #     print(i)
#         #     # result += str(i)
#     print(result)
#
# user = input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")
#
# translate()