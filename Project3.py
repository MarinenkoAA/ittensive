import pandas as pd
a = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
a["dole"]=a["UnemployedDisabled"]/a["UnemployedTotal"]*100
a=a[a["dole"] < 2]
a.set_index("Year")
a.sort_index()
print(a["Year"][0:1])