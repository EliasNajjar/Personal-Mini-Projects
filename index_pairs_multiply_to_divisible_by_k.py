n = 15
k = 4
for i in range(n):
    for j in range(i + 1, n):
        if i * j % k == 0:
            print(i,j)
