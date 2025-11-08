num = input("Enter hexadecimal number: ")
list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

sum = 0
for x in range(len(num)):
    for y in range(len(list)):
        if num[x] == list[y]:
            sum += 16 ** (len(num) - x - 1) * y

print(sum)