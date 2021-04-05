from random import gauss
from matplotlib import pyplot as plt
import numpy as np
r = 1
s = 0.5
tau = 1/255
print(f"Exponential Martingale, {r=}, {s=}, {tau=}")
Nc = 1000
Ni = int(2/tau)
X = np.zeros((Nc, Ni))
for i in range(Nc):
    x = 1
    for j in range(Ni):
        x = x + x*(r*tau + s*gauss(0, tau))
        X[i][j] = x

times = np.array(range(Ni))
plt.plot(times*tau, X.T)
plt.xlabel('Timestep (year)')
plt.ylabel('Stock value')
plt.plot(times*tau, np.sum(X,0)/Nc, color='red', linewidth=3)
plt.show()
