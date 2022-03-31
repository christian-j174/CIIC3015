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

def show_recipe(list):
    if list:
        print( 'Ingredients needed for selected recipe:' )
        yy = -1
        if yy < 5:
            yy += 1
        for i in range( 0, 8 ):

            if i == 7 or i == 2:
                print( f"{list[i]} {ingredients[i]}" )
            else:
                print( f"{list[i]} {units[i]} of {ingredients[i]}" )


show_recipe([3,4,5,6,7,8,9,10])