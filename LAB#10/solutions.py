# print("~"*50)
# print('''Question 16:
# Palindromes
# Background
# A palindrome is a string that contains exactly the same sequence of characters forwards as backwards. For example, "madam" or "racecar" are palindromes. For the purpose of this exercise, spaces, punctuation, and any other character should be treated the same as letters, so strings such as "dog god" and "123 $$ 321" would also be considered palindromes (as would the empty string "").
#
# Task
# Write a program that prompts the user for a string and determines whether that string is a palindrome.
#
# Your program must include a function named is_palindrome that receives a string as a parameter and returns True if that string is a palindrome, or False otherwise.
# Your program must invoke the is_palindrome function you create and use the user's input as argument.
# Your program must output a message indicating whether the input is a palindrome (see sample output further below).
# Hint: Use indices to compare corresponding characters. For example, if a string has 6 characters, compare index 0 with index 5, index 1 with index 4, and index 2 with index 3.''')
# print("~"*50)
#
# # Solution
# def is_palindrome(s):
#     lenS = len(s)
#     for i in range(len(s) // 2):
#         if s[i] != s[lenS - 1 - i]:
#             return False
#     return True
#
# inputStr = input("Enter a string: ")
# if is_palindrome(inputStr):
#     print("The string", inputStr, "is a palindrome")
# else:
#     print("The string", inputStr, "is not a palindrome")

print("~"*50)
print('''Question 17:
More palindromes
Task
Modify your program from the previous exercise as follows:

Make the program case insensitive.
Only consider letters (ignore spaces, punctuation, and numbers).  Create a function named keep_letters that receives a string and returns a modified version of that string where only the letters remain.
Add quotes around the input string when displayed in the output.
Hint: Within the is_palindrome function first convert the input to lower case and invoke the keep_letters function, then proceed with the original code.  How to determine whether a character is a letter? Remember that strings are comparable, and think of where a character would be found within the ASCII table to be considered a letter...''')
print("~"*50)

# Solution
# def keep_letters(s):
#     result = ""
#     for c in s:
#         if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
#             result += c
#     return result
#
# def is_palindrome(s):
#     s = keep_letters(s.lower())
#     lenS = len(s)
#     for i in range(len(s) // 2):
#         if s[i] != s[lenS - 1 - i]:
#             return False
#     return True
#
# inputStr = input("Enter a string: ")
# if is_palindrome(inputStr):
#     print("The string \"" + inputStr + "\" is a palindrome")
# else:
#     print('The string "' + inputStr + '" is not a palindrome')


print("~"*50)
print('''Question 18:
Many companies use telephone numbers like 555-GET-FOOD, so the number is easier for their customers to remember. On a standard telephone, the alphabetic letters are mapped to numbers in the following fashion:

A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6 
P, Q, R, and S = 7 
T, U, and V = 8
W, X, Y, and Z = 9

Write a program that asks the user to enter a 10-character telephone number in the format XXX- XXX-XXXX. The application should display the telephone number with any alphabetic characters in the original translated to their numeric equivalent. For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.

Define the function translator to perform the required task. You can assume the user will only input numbers, letters, or "-".

In your code you ned to call (invoke) the function to obtain the expected output. 

Hint: the function implementation don't requiere to receive parameters.

''')
print("~"*50)

# Solution
# def telephone_translator():
# 	tel = input("Enter a 10-character telephone number in the format XXX-XXX-XXXX: ")
# 	translator(tel)
#
# def translator(tel):
# 	new_tel = ""
# 	for t in tel:
# 		if t.upper()=="A" or t.upper()=="B" or t.upper()=="C":
# 			new_tel = new_tel + "2"
# 		elif t.upper()=="D" or t.upper()=="E" or t.upper()=="F":
# 			new_tel = new_tel + "3"
# 		elif t.upper()=="G" or t.upper()=="H" or t.upper()=="I":
# 			new_tel = new_tel + "4"
# 		elif t.upper()=="J" or t.upper()=="K" or t.upper()=="L":
# 			new_tel = new_tel + "5"
# 		elif t.upper()=="M" or t.upper()=="N" or t.upper()=="O":
# 			new_tel = new_tel + "6"
# 		elif t.upper()=="P" or t.upper()=="Q" or t.upper()=="R" or t.upper()=="S":
# 			new_tel = new_tel + "7"
# 		elif t.upper()=="T" or t.upper()=="U" or t.upper()=="V":
# 			new_tel = new_tel + "8"
# 		elif t.upper()=="W" or t.upper()=="X" or t.upper()=="Y" or t.upper()=="Z":
# 			new_tel = new_tel + "9"
# 		else:
# 			new_tel = new_tel + t
#
# 	print(f"The number is {new_tel}")
# # 	print(new_tel)
#
#
# telephone_translator()


# print("~"*50)
# print('''Question 14:
# Write a function named number_triangle that accepts an integer parameter and prints a number triangle based on the integer.
#
# Hints:
#
# You will need to write a loop within a loop to print the pattern
# To print something without adding a new line at the end, use print(var, end = ''). See the official python doc for more details: https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function''')
# print("~"*50)
#
# # Solution
# def number_triangle(n):
#     # row keeps track of the number
#     # of rows to be printed
#     for row in range(1, n + 1):
#         # count keeps a track of the
#         # number of times the the
#         # current number of the row
#         # will be printed
#         for count in range(1, row + 1):
#             # This is how to print without
#             # adding a new line at the end
#             print(row, end = '')
#         # Simply print a new line between
#         # rows
#         print()