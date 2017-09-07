import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as stat

incomes = np.random.normal(27000, 15000, 10000)
print("Mean:", np.mean(incomes))
print("Median:",  np.median(incomes))

plt.hist(incomes, 50)
plt.show()

# Mode
ages = np.random.randint(17, high=90, size=500)
print(ages)

print(stat.mode(ages))