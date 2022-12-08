import random
import matplotlib.pyplot as plt
import numpy as np

N = 1000
x = np.zeros(N)
y = np.zeros(N)

#dice =rndom()
for i in range(N-1):
    dice = random.random()
    dicey = random.random()
    if dice > 0.5:
         x[i+1] = x[i]+1
    else:
        x[i+1] = x[i]-1
    if dicey > 0.5:
        y[i+1] = y[i]+1
    else:
        y[i+1] = y[i]-1
plt.plot(y,x)
plt.show()
