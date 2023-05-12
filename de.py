import numpy as np

data = np.loadtxt('data/minutes_n_ingredients.csv', dtype=np.int32, delimiter=',', skiprows=1)
print(data[:5])