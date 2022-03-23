# def SumOfDigits(number):
#     ss = str(number)
#     rr = 0
#     for i in ss:
#         rr += int(i)
#     return int(rr)
#
#
# print(SumOfDigits(827104))

def Summation(m, n):
    acc = 0
    for i in range(m, n+1):
        acc += i
    return acc



print(Summation(10,13))