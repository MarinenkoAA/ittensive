import pandas as pd
a = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";", index_col=["Year", "Period"])
b= pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";", index_col=["AdmArea", "Year", "Month"])
b=b.loc["Центральный административный округ"]
b.index.names = ["Year", "Period"]
data=pd.merge(a,b, right_index=True, left_index=True)
data=data.reset_index()
data=data.set_index("Calls").sort_index()
print(data["UnemployedMen"][0:1])