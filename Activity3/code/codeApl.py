import numpy as np
import matplotlib.pyplot as plt

from math import *

res = 1000
l_x = np.linspace(1,6,res)
l_xP = np.power(10, l_x)*2*np.pi

R = 10**(3)
C = 10**(-7)

dx = np.log10(np.array([10,50,100,500,1000,5000,10000,50000,100000,500000,1000000]))

# dy = 20*np.log10(np.array([4.801,4.801,5.001,4.801,4.601,1.601,0.880,0.2,0.156,0.11,0.108])/5)
# dy2 = 20*np.log10(np.array([4.801,5.201,5.401,4.801,4.401,1.481,0.780,0.160,0.084,0.016,0.008])/5)
# dy3 = 20*np.log10(np.array([5.001,4.801,4.801,4.401,4,1.24,0.6,0.05,0.012,0.002,0.0001])/5)

dy1 = 20*np.log10(np.array([5.001,5.001,5.001,4.401,3.201,1.441,0.880,0.200,0.104,0.030,0.016])/5)
dy2 = 20*np.log10(np.array([5.001,5.001,5.001,4.401,3.001,0.580,0.184,0.016,])/5)
dy3 = 20*np.log10(np.array([5.001,4.801,4.801,4.401,4.201,1.521,0.030,0.0005])/5)
# dy3 = 20*np.log10(np.array([4.8,5.2,5.2,4.8,4,1.24,0.6,0.05,0.12,0.02,0])/5)
x1 = np.linspace(1,-np.log10(R*C), 3)
y1 = np.zeros(3)

x2 = np.linspace(-np.log10(R*C),6,100)
y2 = -20*(np.log10(R*C)+(x2))
y22 = -40*(np.log10(R*C)+(x2))
# y23 = -60
# l_y = np.zeros(res)

l_y1  = -10*np.log10(1 + R**2 * C**2 * l_xP**2)
l_y2 = -10*np.log10((1-(l_xP*R*C)**2)**2+(3*l_xP*R*C)**2)
l_y3 = -10*np.log10((1-5*(l_xP*R*C)**2)**2+(6*l_xP*R*C - (l_xP*R*C)**3)**2)

# plt.plot(l_x,l_y,label="u")
plt.plot(l_x, l_y1,label='G')
plt.scatter(dx, dy1, color = 'orange')
plt.savefig('../figs/Afig1.png')
plt.show()
