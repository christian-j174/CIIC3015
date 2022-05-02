# THE FOLLOWING LIST CONTAINS THE UNITS OF THE INGREDIENTS
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']

# THE FOLLOWING LIST CONTAINS THE NAMES OF THE INGREDIENTS
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

#THE FOLLOWING ARE EXAMPLES OF RECIPES - OBSERVE THE ORDER OF THE INGREDIENTS IS THE SAME THAN THE ORDER OF THE PANTRY
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]

pantry = [10,10,10,10,10,10,10,10,10]
# Task 1: define function below

"""
primero el menu list, imprimo el element,

luego un print de qty y su respectiva unidad 

"""

def create_recipes():
    fh = open('recipes.txt', 'w')
    for i in range(0,5):
        fh.write(menu_list[i] + '\n')
        track = menu[i]     #LISTA DE CANTIDADES
        for i in range(0,10):
            if i == 2 or i == 7 or i == 8 or i == 9:
                fh.write(f"{track[i]} {units[i]} {ingredients[i]}" + '\n')
            else:
                fh.write(f"{track[i]} {units[i]} of {ingredients[i]}" + '\n')



create_recipes()
