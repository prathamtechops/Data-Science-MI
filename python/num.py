import numpy as np
import time


SiZE = 10000000

l1 = range(SiZE)
l2 = range(SiZE)

a1 = np.arange(SiZE)
a2 = np.arange(SiZE)

start = time.time()

result = [(x, y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000)
start = time.time()
result = a1 + a2
print((time.time() - start) * 1000)
