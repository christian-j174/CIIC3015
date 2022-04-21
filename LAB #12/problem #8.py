def calc_pay(dict1, dict2):
    result = dict()
    for key in dict1:
        result[key] = dict1[key] * dict2[key]
    return result


print(calc_pay({123456: 40, 987654: 30}, {123456: 7.25, 987654: 11.50}))
