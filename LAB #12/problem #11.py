def Inventory(file):
    fh = open(file)
    result = dict()
    for line in fh:
        line = line.strip('\n')
        if line not in result:
            result[line] = 1
        else:
            result[line] += 1
    fh.close()
    return result




"""
Sudoku is a solitaire game in which you try to fill a 9x9 grid with numbers from 1 through 9
such that each number appears exactly once in each row, in each column, and in each of the nine 3x3 subgrids.
"""

def checkSum(array):
    """Verify if the sum of all numbers is 45, and returns True"""
    TotalSum = 0
    for i in array:
        TotalSum += int(i)
    if TotalSum == 45:
        return True
    return False


def DoIWin(file):
    fh = open(file)
    rows = []
    columns = []
#------------------------------------------------------------------------------------
#ITERA POR CADA LINEA Y ANADELAS A ROWS COMO LISTA, ENTONCES TENEMEOS UNA LISTA DE LISTAS
    for line in fh:
        if line.startswith('\n'):       #REMUEVE LOS NEWLINES
            continue
        else:
            line = line.strip('\n')             #REMUEVE LOS NEWLINES
            line = line.replace(' ', '')       #REMUEVE LOS ESPACIOS ENTRE LOS NUEMROS
            rows.append(line)                   #ANADE ESA LINEA A ROWS
    for k in rows:
        if checkSum(k) == False:
            return False
#-------------------------------------------------------------------------------------
#ITERA POR CADA LINEA Y ANADELAS A COLUMNS COMO LISTA,
    column = ''
    acc = 0
    for k in range(9):
        for i in range(9):
            x = rows[i]  # itera por cada row, es un string
            x1 = x[k]  # coge el row index 0
            column += (x1)
        column += ' '
    columns.append( column )
    columns = columns[0].split()
    for z in columns:
        if checkSum(z) == False:
            return False
#-----------------------------------------------------------
#CREA UNA LISTA EN ORDEN DE TODOS LOS NUMEROS, PARA LOS GRUPOS 3X3
    TotalNumbers = ''
    for k in rows:
        TotalNumbers += k
#----------------------------------------------------------------
#GRUPOS 3X3
    group0 = [0,1,2,27,28,29,54,55,56]
    group1 = [3,4,5,30,31,32,57,58,59]
    group2 = [6,7,8,33,34,35,60,61,62]
    group3 = [9,10,11,36,37,38,63,64,65]
    group4 = [12,13,14,39,40,41,66,67,68]
    group5 = [15,16,17,42,43,44,69,70,71]
    group6 = [18,19,20,45,46,47,72,73,74]
    group7 = [21,22,23,48,49,50,75,76,77]
    group8 = [24,25,26,51,52,53,78,79,80]
    SUBGROUPS = [group0, group1, group2, group3, group4, group5, group6, group7, group8]
#----------------------------------------------------------------------------------------
    checkGroup = []
    s = None
    for q in SUBGROUPS:
        for index in q:
            s = int(TotalNumbers[index])       #itera por cada numero
            checkGroup.append(s)
            s = None
    if sum(checkGroup) == 405:
        return True
    else:
        return False







print(DoIWin('test6.txt'))
#print(checkRow([1,2,3,4,5,6,7,8,9]))



