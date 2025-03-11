import time

print("1\t0")
print("2\t1")
list = [0,1]
term = 2
goldenRatio = (1 + 5**0.5) / 2

while True:
    toAppend = list[term-2] + list[term-1]
    list.append(toAppend)
    print(str(term+1) + "\t" + str(list[term]) + "\t" + str(list[term] / list[term-1]) + "\t" + str(goldenRatio), end="\t")
    if list[term] / list[term-1] == goldenRatio:
        print("Exact")
    else:
        print()
    term += 1
    time.sleep(0.1)