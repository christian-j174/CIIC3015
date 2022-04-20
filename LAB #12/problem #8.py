def calc_pay(dict1, dict2):
    """
    The first dictionary has the hours worked by employees at a company
    and second has the employees' hourly rate, with the same employee IDs as keys.
    """
    result = dict()
    empleados_id = list()
    horas_trabajadas = list()
    dict1 = dict1.items()
    dict2 = dict2.items()

    for i in range(0,len(dict1)):     #iterate over the worked hours
        print(dict1)
        #result[i] = dict1[i+1] * dict2[i +1]
# print(calc_pay({123456: 40, 987654: 30}, {123456: 7.25, 987654: 11.50}))


calc_pay({123456: 40, 987654: 30}, {123456: 7.25, 987654: 11.50})
