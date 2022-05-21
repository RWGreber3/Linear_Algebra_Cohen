import random
import numpy as np
import matplotlib.pyplot as plt

scalars = []
scaled_vectors = []
for i in range(0,10):
    scalars.append(random.gauss(1, 1))

a = random.randint(0, 100)
b = random.randint(0, 100)
v = np.array([a , b])
scaled_vectors.append(v)
for scalar in scalars:
    scaled_vectors.append(scalar * v)

for i in scaled_vectors:
    plt.plot([0, i[0]], [0,i[1]])
print(scaled_vectors)
# plt.axis([-20, 20, -20, 20])
plt.show()
