# THE FOLLOWING LIST CONTAINS THE UNITS OF THE INGREDIENTS
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']

# THE FOLLOWING LIST CONTAINS THE NAMES OF THE INGREDIENTS
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

# THE FOLLOWING ARE EXAMPLES OF RECIPES - OBSERVE THE ORDER OF THE INGREDIENTS IS THE SAME THAN THE ORDER OF THE PANTRY
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]


# def create_recipes():
#     fh = open( 'recipe.txt', 'w' )
#     for i in range( 0, 5 ):
#         fh.write( menu_list[i] + '\n' )
#         track = menu[i]  # LISTA DE CANTIDADES
#         for i in range( 0, 10 ):
#             if i == 2 or i == 7 or i == 8 or i == 9:
#                 fh.write( f"{track[i]} {ingredients[i]}" + '\n' )
#             else:
#                 fh.write( f"{track[i]} {units[i]} of {ingredients[i]}" + '\n' )
#     fh.close()

# create_recipes()
# ------------------------------------------------------------------------------

def read_recipes():
    fh = open( 'recipe.txt' )
    menu = []
    menu_list = ['banana pancake', 'peach crepe', 'apple pie', 'french toast', 'scrambled eggs with toast and fruits']
    tmp_index = -1
    qty = ''
    ingredient = ''
    local_dic = ''
    for line in fh:
        line = line.strip( '\n' )
        if line in menu_list:
            tmp_index += 1
            menu.append( {} )
        else:
            qty = line[:line.find( ' ' )]
            ingredient = line[line.find( ' ' ) + 1:]
            local_dic = menu[tmp_index]
            local_dic[ingredient] = float( qty )
    return menu, menu_list


menu1, menu_list1 = read_recipes()


# ---------------------------------------------------------------------------------------


def add_new_recipe():
    recipe_name = input( "Name of the new recipe: " )
    menu_list1.append( recipe_name )
    new_recipe = {}

    for i in range( len( units ) ):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = float( input( 'How many ' + str( unit ) + str( ingredient ) + ' are required? ' ) )
        new_recipe[f"{unit}{ingredient}"] = float( item )

    menu1.append( new_recipe )
    return menu1, menu_list1


# ------------------------------------------------------------------------------------------------------


def add_new_recipe_to_file():
    menu2, menu_list2 = add_new_recipe()
    fh = open( 'recipe_updated.txt', 'w' )
    track_last_dic = len( menu_list2 ) - 1
    x = track_last_dic

    for i in range( len( menu2 ) ):
        fh.write( menu_list2[i] + '\n' )
        track = menu2[i]  # LISTA DE DICCIONARIOS
        for key, value in track.items():
            if '' in key:
                fh.write( f"{value} {key}" + '\n' )
            else:
                fh.write( f"{key} of {value}" + '\n' )
    fh.close()




add_new_recipe_to_file()
