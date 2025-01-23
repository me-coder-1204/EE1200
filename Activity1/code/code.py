import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10*np.pi,10000)

f1 = 4
f2 = 12
A = 5
B = 5
ph = 90*np.pi/180

x = A*np.sin((2*np.pi/f1)*t + ph)
y = B*(np.sin((2*np.pi/f2)*t))

plt.grid()
plt.axis("equal")
plt.scatter(y,x)
plt.savefig("../figs/fig4.png")
plt.show()