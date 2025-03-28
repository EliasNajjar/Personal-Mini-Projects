import time

maxExponent = 10000000

def setValue(val,exps):
    while val > 10:
        val /= 10
        exps[-1] += 1
        if exps[-1] > maxExponent:
            exps.append(exps[-1]-maxExponent)
            exps[-2] = maxExponent
    return val


def printValue(val,exps):
    print(val,end="")
    for x in exps:
        print(" * 10^" + str(x),end="")
    print()

step = 1
value = 1
exponents = [0]
while True:
    value *= step
    value = setValue(value,exponents)
    print(str(step) + ": ",end="")
    printValue(value,exponents)
    step += 1
    #time.sleep(.05)
