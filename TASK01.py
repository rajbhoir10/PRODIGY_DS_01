import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
ages = np.random.randint(18, 70, size=100)

plt.hist(ages, bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a Population')
plt.show()