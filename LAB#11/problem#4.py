"""
Create a routine to sum the cost of the videogames that the user will buy consider a tax of 15%,
and ask at the user to enter the videogames prices,
and make this procedure while the variable is different from 1.
"""

TotalCost = 0
TAX = 0.85

#user_input = float(input("Add the new videogame if you don't add more videogames put 1: "))
user_input = ""

while user_input != 1:
    user_input = float(input("Add the new videogame if you don't add more videogames put 1: "))
    TotalCost += (user_input * TAX)

print(round(TotalCost, 2))



