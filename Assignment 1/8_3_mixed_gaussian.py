import matplotlib.pyplot as plt
import numpy as np

pi = [0.3, 0.7]
num_samples = 100
mean = [[1, 0], [-1, 0]]
cov = [[[1, 0.2], [0.2, 1]], [[1, -0.2], [-0.2, 1]]]
pi_samples = np.random.choice([0, 1], num_samples, p=pi)
X = []
Y = []
for i in range(0, num_samples):
    x, y = np.random.multivariate_normal(mean[pi_samples[i]], cov[pi_samples[i]]).T
    X.append(x)
    Y.append(y)
plt.plot(X, Y, 'x')
plt.axis([-5, 5, -5, 5])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
