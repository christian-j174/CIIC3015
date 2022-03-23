
def factorial(arg1):
    #Manage the user input and converted to int
    try:
        arg1 = int(arg1)
    except:
        arg1 = str(arg1)
    #------------------------------
    accumulator = 1
    try:
        if (arg1) > -1 and type(arg1) == int:
            arg1 = int(arg1)
            for n in range(1,  arg1):
                #print(f'{n}   times {accumulator}')
                accumulator += (accumulator * n)
            print(f"{arg1}! = {accumulator}")
        else:
            print( "Invalid input!" )

    except TypeError:
        print("Invalid input!")




number = input("Enter a non-negative integer: ")

factorial(number)