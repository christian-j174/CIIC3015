
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

def SumOfDigits(n):
    nn = str(n)
    accumulator = 0
    for i in nn:
        accumulator += int(i)
    return accumulator

print(SumOfDigits(827104))