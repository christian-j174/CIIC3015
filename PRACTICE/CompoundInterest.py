"""
When a bank account pays compound interest, it pays interest not only on the principal
amount that was deposited into the account, but also on the interest that has accumulated
over time. Suppose you want to deposit some money into a savings account, and let the
account earn compound interest for a certain number of years. The formula for calculating
the balance of the account after a specified number of years is:
"""

# AMOUNT(TIME) = PRINCIPAL( 1 + (RATE)/ (N-TERMS))^(N-TERMS)(TIME)


print("""A: is amount of money in the Account after the specified number of years.
P: is the principal amount originally deposited into the account.
R: is the anual interest rate.
N: is the number of times per year the interest is compounded.
T: is the specified number of years.
""")
# TEST:
#THE AMOUNT OF PRINCIPAL ORIGINALLY DEPOSITED INTO THE ACCOUNT
#THE ANNUAL INTEREST RATE PAID BY THE ACCOUNT.

p = float(input("THE AMOUNT OF PRINCIPAL ORIGINALLY DEPOSITED INTO THE ACCOUNT: "))
r = (int(input("THE ANNUAL INTEREST RATE(%) PAID BY THE ACCOUNT: "))) / 100  # AND CONVERTED TO DECIMAL
n = int(input("The number of times per year that the interest is compounded: "))
t = int(input("THE NUMBER OF YEAR THE ACCOUNT WILL BE LEFT TO EARN INTEREST: "))
a = round(p * (1 + (r/n)) ** (n * t), 2)

print(f'The final result is ${a}')

