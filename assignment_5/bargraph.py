import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

l = []
print("Enter 10 elements: ")
for i in range(10):
    o = int(input(""))
    l.append(o)

mean = np.mean(l)
med = np.median(l)
mod = stats.mode(l)
x = np.arange(3)
k = [mean, med, mod.mode[0] if mod.count[0] > 1 else None]

lab = ["Mean", "Median", "Mode"]
plt.bar(x, k, tick_label=lab)
plt.show()
