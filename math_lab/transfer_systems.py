n = 0
f = 1 # number of flat transfer systems is the sum of the previous Catalan numbers
t = 1 # number of transfer systems is Catalan of n+1
while True:
    #print(f"n: {n}\tt: {t}\tf: {f}\tf/t: {f/t}")
    print(f/t)
    n += 1
    f += t # current number of transfer systems is added to the number of flats of next n
    t = t * (2 * n + 2) * (2 * n + 1) // ((n + 2) * (n + 1)) # equation for Catalan of n is (2n)!/(n+1)!n!