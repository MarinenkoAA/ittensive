import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
a = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
a = a.drop(columns = "Period")
a["Delta"] = 100 * a["UnemployedDisabled"] / a["UnemployedTotal"]
a_data = a.groupby("Year").filter(lambda x: x["Delta"].count() > 5)
a_data = a_data.groupby("Year").mean()
x = np.array(a_data.index).reshape(len(a_data.index), 1)
y = np.array(a_data["Delta"]).reshape(len(a_data["Delta"]), 1)
model = LinearRegression()
model.fit(x, y)
print(np.around(model.predict(np.array(2020).reshape(1, 1)), 2))
