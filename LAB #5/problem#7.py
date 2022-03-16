"""
creates a program that asks the user to enter how many
vegetables you need to buy and the total amount of the purchase.

discount = amount * 0.05 * total

You will repeat this for the total amount of vegetables,
and have to update the total amount of the purchase after
applying the discount for each vegetable. The formula


"""

x = int(input('Enter how many vegetables you need to buy: '))
amount = float(input('Enter total amount of your purchase: '))
for i in range(1, x+1):
    f = i * amount * 0.05
    amount -= f


print(f"The total amount of your discounted purchase is:  {amount}")
