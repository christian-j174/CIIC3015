
# INICIALIZAR VARIABLES
cook = True
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '']
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'fruits']
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 5]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 1.5]
menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]
recipe = []
pantry = []



def pantry_update():
    """Un for loop, """
    pantry_updateV2()
    if verify_pantry():  # VAMOS A RESTAR RECIPE
        resultado = 0
        for i in range (0 , 8):
            pantry[i] -= recipe[i]
        print( "Great choice. That was delicious!" )
    # else:
    #     print('Not enough ingredients!')

def verify_pantry():
    """ Return True if there are enough ingredients in the pantry """
    # acc = pantry.copy()
    for i in range (0, 8):
        if pantry[i] < recipe[i]:
            # print('No hay suficientes ingrdientes')
            return False
    return True


def show_pantry():
    # write the body of the function that allow to print the content of the pantry
    for i in range( 0, 8 ):
        if i == 7 or i == 2:
            print( f"{pantry[i]} {ingredients[i]}" )
        else:
            print( f"{pantry[i]} {units[i]} of {ingredients[i]}" )


def pantry_ingredients(units, ingredients):  # PIDE LOS INGREDIENTES AL USUARIO
    for i in range( len( units ) ):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input( 'How many ' + str( unit ) + str( ingredient ) + ' do you have? ' )
        pantry.append( float( item ) )


def recipe_menu():
    print( "What would you like to cook? Here's the recipe book:" )
    for i in range( len( menu_list ) ):
        print( i + 1, ". ", menu_list[i], sep="" )

    print( i + 2, ". Nevermind, I don't want to cook anything (Exit).", sep="" )
    run = True
    # ---------------------
    while run:
        option = None
        if type( option ) == int:
            run = False
        else:
            try:
                option = int( input( "Select an option by typing its number here:" ) )
                if option >= 1:
                    run = False
            except:
                print( 'Try again' )
    # -----------------------------------------------
    return option


def valid_option(option):
    if option == 1:
        # banana_pancake
        return [1, 2, 1, 1, 3, 2, 0, 2]

    elif option == 2:
        # peach_crepe
        return [1, 0, 1, 1, 2, 0, 0, 3]

    elif option == 3:
        # apple_pie
        return [2, 4, 2, 0.5, 1, 1, 0, 5]

    elif option == 4:
        # french_toast
        return [0.5, 3, 3, 0.5, 2, 0, 8, 0]

    elif option == 5:
        # scrambled_eggs
        return [0, 0, 4, 0.5, 0, 0, 2, 1.5]

    elif option == 6:
        cook = False
        return [0,0,0,0,0,0,0,0]


def show_recipe(option):
    banana_pancake_recipe
    if option == 1:
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):
            if i == 7 or i == 2:
                print( f"{banana_pancake_recipe[i]} {ingredients[i]}" )
            else:
                print( f"{banana_pancake_recipe[i]} {units[i]} of {ingredients[i]}" )
    elif option == 2:
        # peach_crepe_recipe
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):
            if i == 7 or i == 2:
                print( f"{peach_crepe_recipe[i]} {ingredients[i]}" )
            else:
                print( f"{peach_crepe_recipe[i]} {units[i]} of {ingredients[i]}" )
    elif option == 3:
        # apple_pie_recipe
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):
            if i == 7 or i == 2:
                print( f"{apple_pie_recipe[i]} {ingredients[i]}" )
            else:
                print( f"{apple_pie_recipe[i]} {units[i]} of {ingredients[i]}" )
    elif option == 4:
        # french_toast_recipe
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):
            if i == 7 or i == 2:
                print( f"{french_toast_recipe[i]} {ingredients[i]}" )
            else:
                print( f"{french_toast_recipe[i]} {units[i]} of {ingredients[i]}" )
    elif option == 5:
        # scrambled_eggs
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):
            if i == 7 or i == 2:
                print( f"{scrambled_eggs[i]} {ingredients[i]}" )
            else:
                print( f"{scrambled_eggs[i]} {units[i]} of {ingredients[i]}" )


def pantry_updateV2():
    index_track = list()
    for i in range( 0, 8 ):
        if pantry[i] < recipe[i]:
            index_track.append( i )
    # ----------------------------------
    for index in index_track:
        print( "Not enough ingredients! Let's update it." )
        if index == 7 or index == 2:
            user = float( input( f"How many {ingredients[index]} do you have? " ) )
            pantry[index] = user
        else:
            user = float( input( f"How many {units[index]} of {ingredients[index]} do you have? " ) )
            pantry[index] = user


def servings(recipe):
    serving = float( input( "How many servings? " ) )
    result = []
    for element in recipe:
        result.append( serving * element )
    recipe = result.copy()
    return recipe


# ---------------------------------------------------------------------------------------


pantry_ingredients( units, ingredients )

# option = recipe_menu()
# print( 'You selected option', option )
# recetas = valid_option( option )
# print(recetas, option)

while cook:
    # Ask user what they'd like to make (from options)
    option = recipe_menu()      #EL INPUT DEL USUARIO DE LO QUE QUIERE HACER
    recetas = valid_option( option )    #CREA LA LISTA DE RECETAS
    recetas = servings( recetas )

    print( 'You selected option', option )

    if recetas[0] == 0:             #ESTE ES LA OPCION #6
        print( "See you later!" )
        break

    show_recipe( option )
    print( "Here's what's left in the pantry: " )
    show_pantry()
    # if recetas == False:
    #     print( "See you later!" )
    #     break
    pantry_update()

    print( "Here's what's left in the pantry: " )
    show_pantry()