from matplotlib import pyplot as plt
import numpy as np
Ni = 1000
X = np.zeros((2, Ni))
bandwidth = (np.array(range(Ni))+Ni/5)/Ni*10**7
print(bandwidth)
X[0] = 1000*8/bandwidth
print (X[1])
X[1] = np.ones(Ni)*0.0011
print (X[1])
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(bandwidth/10**6, X[1]*1000, 'k:', label='Durée de la compression', color = 'red')
ax.plot(bandwidth/10**6, X[0]*1000, 'k--', label='Durée de la tranmission', color = 'blue')
plt.xlabel('Débit (Mb/s)')
plt.title('Intérêt de la compression en fonction du débit')
plt.ylabel('Temps (ms)')
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large', labelcolor='orange')
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C2')
plt.show()
