import numpy as np
import math


q = [1, -1.0024, -0.1871, -0.9067]
k = 1
x = [1, .6912, -.3007, .7215]
x2 = [1, -.2880, -1.3231, .5044]

sum = 0
for i in range(len(q)):
    sum += math.pow((q[i] - x2[i]), 2)

d = -1 * (np.sqrt(sum))

print(np.exp(d))
