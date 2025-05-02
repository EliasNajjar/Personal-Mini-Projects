import matplotlib.pyplot as plt 
import numpy as np

nums = range(21)
sums = np.zeros(21)

for x in range(len(nums)):
    sum = nums[x]
    while sum > 9:
        sum = 0
        for y in str(x):
            sum += int(y)
    sums[x] = sum

plt.scatter(nums, sums)
plt.xlabel("Start")
plt.ylabel("Result")
plt.show()