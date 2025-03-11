import numpy as np
import matplotlib.pyplot as plt

xMin = -5
xMax = 5

xValues = np.linspace(xMin, xMax, 500)
yValues = []

for i in xValues:
    yValues.append(i**3)

plt.plot(xValues, yValues)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([min(xValues)-1, max(xValues)+1])
plt.ylim([min(yValues)-1, max(yValues)+1])
plt.grid()
plt.show()