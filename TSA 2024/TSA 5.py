import math
print("Currency Conversion Menu:")
print("1. Convert from Euros to US Dollars (EUR to USD)")
print("2. Convert from Us Dollars to Euros (USD to EUR)")
option = int(input("Please select a conversion option (1/2): "))
USD = 118
EUR = 100
value = 0

def roundTo(num):
    toRound = num * 100
    toRetur = 0
    if (toRound % 1) < 0.5:
        toRetur = (math.floor(toRound) / 100)
    else:
        toRetur = (math.ceil(toRound) / 100)
    if str(toRetur)[-1] == "0" and str(toRetur)[-2] == ".":
        toRetur = str(toRetur) + "0"
    return toRetur

if option == 1:
    amount = input("Enter the amount in Euros (EUR): " )
    amount = int(float(amount)*100)/100

    print(roundTo(amount))
    value = (amount * USD)/100
    print(roundTo(value))
    
elif option == 2:
    amount = (input("Enter the amount in US Dollars (USD): " ))
    amount = int(float(amount)*100)/100
    print(roundTo(amount))
    value = (amount*100) / (USD)
    print(roundTo(value))

#no points because wrong output message but code works and calculates correctly