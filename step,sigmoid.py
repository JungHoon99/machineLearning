import numpy as np
import matplotlib.pylab as plt

def step(x):
    return np.array(x>0,dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))


x=np.arange(-5.0,5.0,0.1)
y=sigmoid(x)
z=step(x)
plt.plot(x,y,label="sigmoid")
plt.plot(x,z,linestyle="--",label="step")
plt.legend()
plt.show()
