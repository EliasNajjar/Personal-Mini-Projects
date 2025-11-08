num1 = int(input("Please enter the first positive integer: "))
num2 = int(input("Please enter the second positive integer: "))

smaller = num1
if num2 < num1:
    smaller = num2

GCF = 0
x = smaller

while x > 0 and GCF == 0:
    if num1 % x == 0 and num2 % x == 0:
        GCF = x
    x -= 1

print("The Greatest Common Factor (GCF) of " + str(num1) + " and " + str(num2) + " is: " + str(GCF))