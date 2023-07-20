import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import scipy.stats
data = pd.read_csv("https://video.ittensive.com/python-advanced/marathon-data.csv", delimiter=",")
data["split"]=data["split"].apply(lambda x: int(x.split(":")[0])*3600+int(x.split(":")[1])*60+int(x.split(":")[2]))
data["final"]=data["final"].apply(lambda x: int(x.split(":")[0])*3600+int(x.split(":")[1])*60+int(x.split(":")[2]))
sns.set_context("paper", font_scale=2)
sns.pairplot(data, hue="age", height=6)
plt.show()
sns.jointplot(data=data, x="split", y="final", height=12, kind="kde")
plt.show()
print(scipy.stats.pearsonr(data["split"], data["final"])[0])
