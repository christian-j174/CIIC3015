def Checkout(items, order):
    total = 0  # tracks the balance
    for key in order:
        if key in items:
            total += order[key]  * items[key]
    return total



price = {'spam':9.00,'eggs':3.00,'bacon':5.00,'sausage':4.50}
order = {'spam':100,'chocolate':3,'eggs':1}


print(Checkout(price,order))