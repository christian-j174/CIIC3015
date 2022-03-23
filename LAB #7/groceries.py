def groceries(items, budget, tax):
    """ Add the price, while the total is less than
    the budget"""
    total = 0.0
    acc = 0.0
    for item in items:
        if (total + item) <= budget:
            total += ((tax/100) * item) +item
    return total


# print(groceries([5.5,7,2.3],7,0))
print(groceries([15,7.5,1.5],35,1.5))