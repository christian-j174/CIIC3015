# def count_words(str):
#     count_words = 1
#     for i in str:
#         if i == ' ':
#             count_words += 1
#     return count_words
#
#
# print('TEST FOR THIS PROBLEM')
# print(f"input: 'chris javi qqq', expected output: 3 | {count_words('chris javi qqq')}")
# print(f"input: 'hola', expected output: 1 | {count_words('hola')}")
# print(f"input: 'real hasta la muertx', expected output: 4 | {count_words('real hasta la muertx')}")

#COUNT HOW MANY TIMES APPEARS A VOWEL
# def vowel_count(str):
#     rr = 0
#     for i in str:
#         if i in 'aeiou':
#             rr += 1
#     return rr
# def first_occurrence(x, str):
#     for i in range(0, len(str)):
#         if x == str[i]:
#             return i
#     return -1
#
# def contains_twice(string, char):
#     """Return True if char occurs two or more times in the string"""
#     times = 0
#     for characters in string:
#         if characters == char:
#             times += 1
#         if times > 1:
#             return True
#     return False
#
#
# print(contains_twice('Tokyo', 'o'))

# def last_first(name):
#     Initial = name[0]
#     last_name = name[name.find( ' ' ) + 1::]
#     return f"{last_name}, {Initial}."
#
#
# print(last_first("Marla Singer"))

'hola  chris tian'
#
# def count_words(string):
#     string = string.strip()
#     counter = 0
#     track_whitespace = ''
#     for i in string:
#         print(i)
#     #     if i == ' ' and track_whitespace != ' ':
#     #         counter += 1
#     #     track_whitespace = i
#     # return counter
# def count_words(string):
#     string = string.strip()
#     counter_whitespaces = 0
#     new_string = ''
#     track = None
#     for i in range(len(string)):
#         if i == ' ' and i != track:
#             new_string += ' '
#         else:
#             new_string += string[i]
#         track = i
#     for i in new_string:
#         if i == ' ':
#             counter_whitespaces += 1
#
#     if counter_whitespaces > 0:
#         return counter_whitespaces + 1
#
#     else:
#         return counter_whitespaces
#
#
#
#
# print(count_words("hi chris      ss ss    "))

# def first_medium_last(name):
#     Initial = name[name.find( ' ' ) + 1]
#     x = Initial.find(' ') + 1
#     print(f'{x}')
#     first_name = name[0:(name.find( ' ' )) ]
#     last_name = name[x::]
#     return f"{first_name} {Initial}. {last_name}"
#
#
#
# print(first_medium_last('Christian J Naza'))
#

#PROBLEM #7
# def first_medium_last(name):
#     white1 =  name.find(' ')   #finde the first whitespace
#     first = name[:white1]
#     namev2 = name[white1 + 1::]
#     white2 = namev2.find(' ')    #find the second whitespace
#     medium = namev2[0]
#     index3 = name
#     last = namev2[white2+1:]
#     return f"{first} {medium}. {last}"


def count_words(str):
    result = ""
    lista = []
    for i in str:
        if i == " ":
            if len( result ) != 0:
                lista.append( result )
                result = ""
        else:
            i.isalpha()
            result += i
    if len( result ) != 0:
        lista.append( result )
    return len( lista )


print(count_words("  this  string     has  wide   spaces "))

















