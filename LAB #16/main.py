

class Pet:
    def __init__(self):
        self.__name = None
        self.__animal_type  = None
        self.__age = None

    def set_name(self):
        self.__name = input("What's your pet's name? ")

    def set_animal_type(self):
        self.__animal_type  = input("What type of animal is your pet? ")

    def set_age(self):
        self.__age = int(input("How old is your pet? "))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


"""
Once you have written the class, write a program that asks the user how many pets they have, then, the program prompts the user to enter the name, type, 
and age t and and creates an object of the class Pet for each pet the user enters. This data should be stored as  the object’s attributes.
"""

db = []
jj = int(input("How many pets do you have? "))

for j in range(1, jj+1):
    print(f"Pet #{j}")
    object = Pet()
    object.set_name()
    object.set_animal_type()
    object.set_age()
    db.append(object)
    print(object)



for k in db:
    k.get_name()
