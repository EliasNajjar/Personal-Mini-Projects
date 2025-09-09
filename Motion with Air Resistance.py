import matplotlib.pyplot as plt 
import numpy as np
from time import sleep

# air resistance constants
P = 2 # density of air
A = 1 # area
C_D = 1 # drag coefficient

F_G = -10 # gravity
F_a = 0 # air resitance
v = 0 # velocity
x = 0 # position

t = 0 # time
MAX_TIME = 5 # stop time
DT = .01 # time interval

tValues = np.linspace(0, MAX_TIME, int(MAX_TIME / DT)) # 0 to MAX_TIME on intervals of DT
F_aValues = []
vValues = []
xValues = []

for i in tValues:
    F_a = v * v * P * A * C_D / 2
    v += (F_a + F_G) * DT # dv = a * dt
    x += v * DT # dx = v * dt
    F_aValues.append(F_a)
    vValues.append(v)
    xValues.append(x)

plt.plot(tValues, [F_G] * len(tValues), label="Gravity")
plt.plot(tValues, F_aValues, label="Air Resistance")
plt.plot(tValues, vValues, label="Velocity")
plt.plot(tValues, xValues, label="Position")
plt.xlabel("time")
plt.grid()
plt.legend()
plt.show()