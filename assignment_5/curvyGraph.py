from numpy import random as rd
import numpy as np
from matplotlib import pyplot as pt

x = np.array([1, 2, 3, 4, 5, 6])
y = rd.randint(1, 7, size=100)
y1 = rd.randint(1, 7, size=100)

occurrences = [0, 0, 0, 0, 0, 0]
occurrences1 = [0, 0, 0, 0, 0, 0]

for i in range(100):
    occurrences[y[i] - 1] += 1
    occurrences1[y1[i] - 1] += 1

pt.bar(x, occurrences, color='y', alpha=0.7, label='y')
pt.bar(x, occurrences1, color='g', alpha=0.7, label='y1')

pt.xlabel("Numbers")
pt.ylabel("Occurrence")
pt.title("Graph Members Vs. Occurrence")
pt.legend()
pt.show()
