import matplotlib.pyplot as plt
import numpy as np

l_x = np.linspace(1, 5, 1000)
l_xP = 2 * np.pi * np.power(10, l_x)

R = 1000
C = 1*10**-7

l_y = 20*(np.atan(-R * C * l_xP))
# l_y2 = 40*(np.atan(-R * C * np.power(10,l_x)* 2 * np.pi))
l_y2 = (20*(np.atan((-(3*l_xP*R*C)/(1 - (l_xP * R *C)**2)))))
l_y3 = 20*(np.atan(-(l_xP*R*C)*((6-(l_xP*R*C)**2))/(1-5*(l_xP*R*C)**2)))
dx = (np.array([10,50,100,500,1000,5000,10000,50000,100000]))

# dy = np.array([1.5e-3,200e-6,200e-6,140e-6,120e-6,47.5e-6,])
dy = np.array([1.4e-3,320e-6,120e-6,104e-6,62e-6,30.4e-6,5.6e-6,3.8e-6,880e-9])
dy1 = np.array([5.6e-3,560e-6,300e-6,116e-6,96e-6,31.2e-6,18.4e-6,4.48e-6,2.2e-6])
dy2 = np.array([5.2e-3,520e-6,320e-6,216e-6,184e-6,68e-6, 40e-6,10.8e-6,0])
# dy2 = np.array([1e-3,500e-6,500e-6,105e-6,90e-6,39e-6,22.5e-6,4.6e-6,2.4e-6])
dy3 = np.array([1.6e-3,200e-6,220e-6,200e-6,176e-6,0,0,0,0])

for i in range(len(dx)):
    dy[i] = dy[i] * 2 * np.pi * dx[i]
    dy1[i] = dy1[i] * 2 * np.pi * dx[i]
    dy2[i] = dy2[i] * 2 * np.pi * dx[i]
    dy3[i] = dy3[i] * 2 * np.pi * dx[i]

# dy3[4] -= np.pi

# dy2[5] -= np.pi 
for i in range(len(dy2[5:])):
    dy2[5+i] -=np.pi

plt.plot(l_x, l_y, label = "u")
# plt.scatter(np.log10(dx),-20*dy)
print(dy2)
# print(dy2-2*np.pi)
plt.scatter(np.log10(dx),-20*(dy1), color='orange')
# plt.scatter(np.log10(dx),-20*dy1)
plt.savefig('../figs/Pfig1.png')
plt.show()
