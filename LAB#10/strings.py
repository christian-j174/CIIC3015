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
def first_occurrence(x, str):
    for i in range(0, len(str)):
        if x == str[i]:
            return i
    return -1