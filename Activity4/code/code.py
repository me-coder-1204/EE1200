import matplotlib.pyplot as plt
import numpy as np


R =  233
L = 2.2e-3 * 0.9
C = 1e-9 

omN = 1/np.sqrt(L*C)
alp = R/(2*L)
om = np.sqrt(omN**2 - alp**2)

v0 = 5

x = np.linspace(0,60e-6,10000)

y = -v0/2 +(v0 * np.exp(-alp*x)*(-alp*np.sin(om*x)+om*np.cos(om*x)))/om
print(om, omN)
plt.plot(x, y, label='a')
# plt.axis("equal") 
plt.grid()
plt.show()
 