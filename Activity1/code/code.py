import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10*np.pi,10000)

f1 = 1
f2 = 3
A = 5
B = 5
deg = 0
ph = deg*np.pi/180

x = A*np.sin((2*np.pi*f1)*t + ph)
y = B*(np.sin((2*np.pi*f2)*t))

plt.grid()
plt.axis("equal")
plt.scatter(x,y,label = f"$f_1 = {f1}, f_2 = {f2}, \\phi = {deg}^\\circ$")
plt.legend(loc="best")
plt.savefig("../figs/fig9.png")
plt.show()