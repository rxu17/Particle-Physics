import matplotlib.pyplot as plt
#import plotly.plotly as plt
#import plotly.graph_objs as go
#import matplotlib.mlab as mlab
import numpy as np
import math 

#np.random.seed(0) #keeps same numbers for random generator

gluon_energy = np.random.uniform(0.25, 0.75, size = 600) 
#

num_bins = 50 

n, bins, patches = plt.hist(gluon_energy, num_bins, normed=1)

plt.title("Gluon energy Distribution")
plt.xlabel("Percentage of total energy")
plt.ylabel("Frequency")

plt.show() #displays the histogram

gluon_angle = np.random.uniform(0, (math.pi)/2, size = 600)

count = 0
theta = []
gauss_func = (1/ math.sqrt(2 * math.pi)) 
while(count < 500):
    num1 = np.random.uniform(low = 0, high = 1, size = None)
    num2 = np.random.uniform(low = 0, high = 1, size = None)
    norm1 = math.sqrt(-2* math.log(num1)) * math.cos(2* math.pi *num2)
    count += 1
    theta.append(norm1)
    
num_bins = 25

plt.hist(theta, num_bins, normed=1)
plt.title("Gluon angle Distribution")
plt.xlabel("Angle of Gluon")
plt.ylabel("Frequency")

plt.show()
