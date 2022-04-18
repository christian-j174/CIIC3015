# def interlace(l1, l2):
#     """ """
#     result = list()
#     if len(l1) == len(l2):   #  VERIFICA SI TIENEN EL MISMO LEN
#         same_len = len(l1)
#         for i in range(0, same_len):
#             result.append(l1[i])
#             result.append(l2[i])
#         return result
#
#     else:
#         diff = abs(len(l1) - len(l2))   #diferencia entre los arrays
#
# #--------------------------------------------       #VARIABLES PARA LOS FOR LOOPS
#         Lista_menor = None
#         Lista_mayor = None
#         validateV1 = None
# #--------------------------------------------
#         if len(l1) > len(l2):       #IDENTIFICAR EL ARRAY MAS PEQUENO
#             Lista_menor = len(l2)
#             Lista_mayor = len(l1)
#             validateV1 = l1
#         else:
#             Lista_menor = len(l1)
#             Lista_mayor = len(l2)
#             validateV1 = l2
# #--------------------------------------------
#         for i in range(0, Lista_menor):     #add the same elements to the list
#             result.append(l1[i])
#             result.append(l2[i])
#
#         for k in range(Lista_menor, Lista_mayor):     #add the last elements
#             result.append(validateV1[k])
#
#         return result
#
#
#
# print(interlace([0, 2, 4], [1, 3, 5, 6, 8]))
#
# print(interlace(['a','b','c'],[1,2,3]))
#

def is_perfect_number(num):
    acc = 0
    for i in range( 1, num ):
        if num % i == 0:  # if divisible, adds up
            acc += i
    if acc == num:
        return True
    else:
        return False


print(is_perfect_number(3))






