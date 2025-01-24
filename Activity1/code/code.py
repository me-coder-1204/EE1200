import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10*np.pi,10000)

f1 = 5
f2 = 6
A = 5
B = 5
deg = 0
ph = deg*np.pi/180

x = A*np.sin((2*np.pi/f1)*t + ph)
y = B*(np.sin((2*np.pi/f2)*t))

plt.grid()
plt.axis("equal")
plt.scatter(y,x,label = f"$f_1 = {f1}, f_2 = {f2}, \\phi = {deg}^\\circ$")
plt.legend(loc="best")
plt.savefig("../figs/fig8.png")
plt.show()