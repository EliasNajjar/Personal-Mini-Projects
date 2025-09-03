num = 4294967295
print(num)

names = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

num = str(num)
for x in range(len(num)):
    print(names[int(num[x])], end=" ")