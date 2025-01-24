import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

n = 10**3
h = 1/10**10
p = 10


T = n*h

t = np.linspace(0,p*T,p*n)

T = 2

R = 1000
C = 1/10**6
Ce = 10**-3
V0 = 5


sq = V0*signal.square(2*np.pi*t/T)

Vr = np.zeros((p*n))
Vc = np.zeros((p*n))
Vr[0] = V0


s = 0
for i in range(1,p*n):
    if i%n < n/2: s = 1
    else: s = -1
    if not i%(n/2):
        # print(i)
        Vc[i] = 0
        if i%(n):
            # Vr[i]-=V0+Vr[i-1]
            Vr[i]-=2*V0
        else:
            # Vr[i]-=-V0+Vr[i-1]
            Vr[i]+=2*V0
    Vr[i]+=(Vr[i-1] - (h*(Vr[i-1]))/(R*C))
    Vc[i] = s*V0 - Vr[i]*(1+Ce/R)
# plt.plot(t,sq,label='p',color= 'red')

f = 5*np.exp(-t/(R*C))
# plt.plot(t, Vr, label='r')
plt.plot(t,Vc, color='r')
# plt.plot(t,f,label='l')
plt.grid()
plt.show()
