for x in range(2,2 ** 31):
    prime = True
    for y in range(2,x):
        if x % y == 0:
            prime = False
    if prime:
        print(x, end=", ")
