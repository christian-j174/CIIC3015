# By Christian J. Rodriguez Nazario
# 28 february 2022

"""
Create a program that calculates the increment in salary for an employee.
You should ask the user to input the number of days they were a star seller and their salary (see examples).
Then, your program must calculate the increment of the salary for each day by using the following formula,
and add the result to the initial value of the salary to update it:

increment = day*0.05*salary

At the end of your program you should print a message indicating the final calculation.
"""

days = int(input("Enter the number of days you were a star seller: "))
salary = int(input("Enter your salary: "))


for day in range(1, days+1):
    increment = day * 0.05 * salary
    salary += increment


print(f'The final calculation of your salary:  {salary}')