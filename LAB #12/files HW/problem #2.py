# def Gimme(file_name):
#     fh = open(file_name)
#     return fh.read()

def Gimme(file_name):
    fh = open(file_name)
    x = fh.read()
    fh.close()
    return x


print(Gimme('chris.txt'))
