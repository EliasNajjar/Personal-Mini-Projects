import math

amount = float(input("Enter the total amount of change in dollars and cents: "))
amount *= 100

print("Dollars: " + str(int(amount // 100)))
amount -= 100 * (amount // 100)
print("Quarters: " + str(int(amount // 25)))
amount -= 25 * (amount // 25)
print("Dimes: " + str(int(amount // 10)))
amount -= 10 * (amount // 10)
print("Nickels: " + str(int(amount // 5)))
amount -= 5 * (amount // 5)
print("Pennies: " + str(int(amount // 1)))
amount -= 1 * (amount // 1)