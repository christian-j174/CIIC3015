pantry = [0,5,0,5,5,5,5,5]
#PANCAKES
recipe = [1, 2, 1, 1, 3, 2, 0, 2]


def pantry_update():
    """Un for loop, """
    pantry_updateV2()
    if verify_pantry():     #VAMOS A RESTAR RECIPE
        # resultado = 0
        for i in range(0,8):
            pantry[i] -= recipe[i]
        print( "Great choice. That was delicious!" )
    else:
        print("Not enough ingredients! Let's update it.")
		#PERO AQUI VA UN TALVEZ UN FOR LOOP
		#pantry.append(track)



def verify_pantry():
    """ Return True if there are enough ingredients in the pantry """
    # acc = pantry.copy()
    for i in range(0, 8):
        if pantry[i] < recipe[i]:
            # print('No hay suficientes ingrdientes')
            return False
    return True

def pantry_updateV2():
	index_track = list()
	for i in range(0,8):
		if pantry[i] < recipe[i]:
			index_track.append(i)
	#----------------------------------
	for index in index_track:
		user = float(input(f"How many {ingredients[index]} do you have?"))
		pantry[index] += user






pantry_update()

