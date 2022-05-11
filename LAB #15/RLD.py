def RLD(l):
    if len(l) == 0:
        return ""
    else:
        return l[1]*int(l[0]) + RLD(l[2:])



print(RLD('57'))
