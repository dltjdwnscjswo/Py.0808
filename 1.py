import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
header = ['preg','plas','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)
data.describe().to_csv('./results/pima_describe.csv')
corr = data.corr(method ='pearson')

#data.corr(method='pearson').to_scv('./results/corr.csv')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm',vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticks(header)
ax.set_xticklebls(header)
ax.set_yticklebls(header)
plt.show()
#plt.savefig('./results/corr.png')