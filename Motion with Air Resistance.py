import matplotlib.pyplot as plt 
import numpy as np
import math

# air resistance constants
P = 2 # density of air
A = 1 # area
C_D = 1 # drag coefficient
K = P * A * C_D / 2 # constants together

F_G = 10 # gravity
F_a = 0 # air resitance
v = 0 # velocity
x = 0 # position

MAX_TIME = 5 # stop time
DT = .001 # time interval

tValues = np.linspace(0, MAX_TIME, int(MAX_TIME / DT)) # 0 to MAX_TIME on intervals of DT
F_aValues = []
vValues = []
vProj = []
xValues = []
xProj = []

for i in tValues:
    F_a = v * v * K
    v += (F_a - F_G) * DT # dv = a * dt
    x += v * DT # dx = v * dt
    F_aValues.append(F_a)
    vValues.append(v)
    vProj.append(F_G ** .5 * (1 - math.e ** ((F_G * K) ** .5 * 2 * i)) / K ** .5 / (1 + math.e ** ((F_G * K) ** .5 * 2 * i))) # found using differential equations
    xValues.append(x)
    xProj.append(((F_G * K) ** .5 * i + math.log(2 / (math.e ** ((F_G * K) ** .5 * 2 * i) + 1))) / K) # integral of velocity proj

plt.plot(tValues, [-F_G] * len(tValues), label="Gravity")
plt.plot(tValues, F_aValues, label="Air Resistance")
plt.plot(tValues, vValues, label="Velocity")
plt.plot(tValues, vProj, label="Velocity Projection")
plt.plot(tValues, xValues, label="Position")
plt.plot(tValues, xProj, label="Position Projection")
plt.xlabel("time")
plt.grid()
plt.legend()
plt.show()