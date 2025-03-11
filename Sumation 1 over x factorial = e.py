import math

total = 0
x = 0
while True:
    total += 1/(math.factorial(x))
    print(x,end="\t")
    print(total)
    x += 1