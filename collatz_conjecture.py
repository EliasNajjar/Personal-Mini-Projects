numToTest = 1000
for i in range(1,numToTest):
    c = i
    count = 1
    while c > 1:
        if c % 2 == 0:
            c /= 2
        else:
            c = 3 * c + 1
        count += 1
    print(f"{i}: {count}")