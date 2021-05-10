
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.ones(shape=3)
np.ones(shape=(2,2))
np.ones(shape=(2, 2, 3))

a = np.ones((2, 2))
a
a[1,1]=18
a

np.sctypes

a = np.array([1, 100, 110], dtype=np.int8)

a

a.dtype

a.itemsize

a.nbytes

np.array([1, 45, 128], dtype=np.int8)

np.array([1, 45, 129], dtype=np.int8)

a = np.array([1, 2, np.nan])
a.dtype

# a = np.array([1, 2, np.nan], dtype= np.int32) # error

np.sctypes['others']

a = np.array(['spam', 'bean'], dtype=np.str)
a

a = np.array(['spam', 'beans'], dtype=np.str)
a

a = np.array(['spam', 'beans'], dtype=(np.str, 2))
a

np.sctypes['others']

# 1D

%matplotlib inline
plt.ion()
plt.show()
Y = np.cos(X)
plt.plot(X, Y)
plt.show()

Z = np.cos(X)**2 + np.sin(X)**2 + 3
plt.plot(X, Z);

@np.vectorize
def scalar_function(x):
    return x**2 + 2*x + (1 if x <=0 else 10)
X = np.linspace(-5, 5, 1000)
Y = scalar_function(X)
plt.plot(X, Y);
plt.show()
##
(elpy-use-ipython)
(setq python-shell-interpreter "python"
      python-shell-interpreter-args "-i")
(setq python-shell-interpreter "ipython"
      python-shell-interpreter-args "-i --simple-prompt")
##
