import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
data = pd.DataFrame({"Box1": np.random.rand(10), "Box2": np.random.rand(10)})
data.boxplot()
for i, d in enumerate(data):
   y = data[d]
   x = np.random.normal(i + 1, 0.04, len(y))
   plt.scatter(x, y)
plt.show()