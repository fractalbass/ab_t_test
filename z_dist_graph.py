import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))
plt.title("Normal Distribution One Tail p=0.05")
plt.plot([1.65, 1.65], [0, 1], color='k', linestyle='-', linewidth=1)
plt.plot([-3.5, 3.5], [0, 0], color='k', linestyle='-', linewidth=1)
plt.plot([3.18, 3.18], [0, 1], color='r', linestyle='-', linewidth=1)
plt.show()