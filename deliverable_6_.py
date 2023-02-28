import pandas as pd
import numpy as np
import seaborn as sns

iris = sns.load_dataset('iris')

iris = iris.drop('species', axis=1)

iris['sepal_sum'] = iris['sepal_length'] + iris['sepal_width']
iris['petal_sum'] = iris['petal_length'] + iris['petal_width']

summary_stats = pd.DataFrame({'mean': iris.mean(),'std': iris.std(),'min': iris.min(),'max': iris.max()})

summary_stats = summary_stats.T

print(summary_stats)
