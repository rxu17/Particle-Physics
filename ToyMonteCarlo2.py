import random
import math
import numpy as np
import matplotlib.pyplot as plt

data2 = []    
data4 = []
dataA = []
dataAd = []
g = 0
for i in range(1000):
    data4.append(random.random()*(math.pi/4.00) + (math.pi/2.00))

while len(dataA) != 1000:
    data2.append(random.random()*0.5 + 0.25)
    
    x = random.random()*(math.pi/4.00) + math.pi/2.00
    y = random.random()
    # gaussian function with mean of 5 and standard deviation of 1
    g = math.exp((-(x-(math.pi/4.00))**2)/4)/(2*math.sqrt(2*math.pi))
    
    if g >= y:
        dataA.append(x)
    
plt.hist(dataA, bins = 20, normed = True)
plt.hist(data2, bins = 20, normed = True)
plt.show()


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos = dataA
ypos = np.ones(len(dataA))
zpos = np.zeros(len(dataA))
dx = np.ones(len(dataA))
dy = np.ones(len(dataA))
dz = np.ones(len(dataA))
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()

