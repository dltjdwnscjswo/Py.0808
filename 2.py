import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
header = ['preg','plas','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

plt.clf()

pd.plotting.scatter_matrix(data)
plt.savefig('./results/scatter.png')

# data.plot(kind='density',figsize=(12,10),subplots=True,layout=(3,3),sharex=False)
# plt.savefig('./results/desity.png')

# data.plot(kind="box", subplots=True, figsize=(12,10), layout=(3,3),sharex=False, sharey=False)
# plt.savefig("./results/voxplot.png")

# data.hist(figsize=(12,10),bins=5)
# plt.tight_layout()
# plt.savefig("./results/histogram.png")
