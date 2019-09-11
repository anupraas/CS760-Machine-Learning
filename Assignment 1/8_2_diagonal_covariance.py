import matplotlib.pyplot as plt
import numpy as np

mean = [1, -1]
cov = [[2, 0], [0, 2]]
x, y = np.random.multivariate_normal(mean, cov, 100).T
plt.plot(x, y, 'x')
plt.axis([-5, 5, -5, 5])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
