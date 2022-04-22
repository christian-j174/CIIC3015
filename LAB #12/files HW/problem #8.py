# def solve(num):
#     res = ""
#     table = [
#         (1000, "M"),
#         (900, "CM"),
#         (500, "D"),
#         (400, "CD"),
#         (100, "C"),
#         (90, "XC"),
#         (50, "L"),
#         (40, "XL"),
#         (10, "X"),
#         (9, "IX"),
#         (5, "V"),
#         (4, "IV"),
#         (1, "I"),
#     ]
#     for cap, roman in table:
#         d, m = divmod( num, cap )
#         res += roman * d
#         num = m
#
#     return res
#
#
# def FileToRoman(input, output):
#     fh1 = open(input)
#     fh2 = open(output, 'w')
#     for number in fh1:
#         number = number.strip('\n')
#         number = int( number )
#         fh2.write(str(solve(number)) + '\n')
#     fh2.close()
#
# FileToRoman('test#8.txt', 'result.txt')


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len( s ):
        if i + 1 < len( s ) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman[s[i]]
            i += 1
    return num


def FileToRoman(input, output):
    fh1 = open(input)
    fh2 = open(output, 'w')
    for number in fh1:
        number = number.strip('\n')
        fh2.write(str(romanToInt(number)) + '\n')
    fh2.close()



