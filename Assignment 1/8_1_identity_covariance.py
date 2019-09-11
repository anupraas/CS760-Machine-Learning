import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 0], [0, 1]]
# cov1 = [[2, 0], [0, 2]]
# mean1 = [1, -1]
# c = np.add(cov, cov1)
# c = np.multiply(2, cov)
# print(c)
x, y = np.random.multivariate_normal(mean, cov, 100).T
plt.plot(x, y, 'x')
plt.axis([-5, 5, -5, 5])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
