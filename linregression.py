%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

X = range(10)
y = range(11,21)

sns.stripplot(X,y)
path = '/home/baks/MidSummer/data1.txt'

data = pd.read_csv(path, delimiter=None, header=None, names=['Population', 'Profit'])

print(data.describe())


data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))


