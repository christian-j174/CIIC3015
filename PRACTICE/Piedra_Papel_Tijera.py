# PIEDRA PAPEL Y TIJERA

def DoIWin(me,you):
    R,P,S = 'rock', 'paper', 'scissors'
    me, you = me.lower(), you.lower()
    if R in me and S in you: # the keyword 'in' works similary to '==' and returns a bool
        return True
    if P in me and R in you:
        return True
    if S in me and P in you:
        return True
    return False

print('TEST#1')
print(DoIWin('rock','paper'))
print('TEST #2')
print(DoIWin('scissors','paper'))

#ALTERNATIVE SOLUTION

def DoIWin(me,you):
    R,P,S = 'rock', 'paper', 'scissors'
    me, you = me.lower(), you.lower()
    if me.find(R) > -1:
        return you.find(S) > -1
    if me.find(P) > -1:
        return you.find(R) > -1
    return you.find(P) > -1

print('--------------------------------+')
print('TEST#1')
print(DoIWin('rock','paper'))
print('TEST #2')
print(DoIWin('scissors','paper'))