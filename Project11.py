import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("https://video.ittensive.com/python-advanced/rts-index.csv")
data["Date"] = pd.to_datetime(data["Date"], dayfirst=True)
dates = pd.date_range(min(data["Date"]), max(data["Date"]))
data = data.set_index("Date")
data = data.reindex(dates).ffill()
data["Day"] = pd.to_datetime(data.index).dayofyear
data.index.name = "Date"
data = data.sort_index()
data3 = data.loc["2019"].reset_index().set_index("Day")
data1 = data.loc["2017"].reset_index().set_index("Day")["Max"].ewm(span=20).mean()
fig = plt.figure(figsize=(12,8))
area = fig.add_subplot(1, 1, 1)
data3["Close"].plot(ax=area, color="red", label="2019", lw=3)
data1.plot(ax=area, color="orange", label="Exp.2017", lw=3)
data.loc["2017"].reset_index().set_index("Day")["Close"].plot.area(ax=area, color=".5", label="2017")
data.loc["2018"].reset_index().set_index("Day")["Close"].plot(ax=area, color="blue", label="2018", lw=3)
plt.legend()
plt.show()
data_fall = data3[data3["Close"] < data1[0:len(data3)]]
data_fall.set_index("Date", inplace=True)
data_fall = data_fall.sort_index(ascending=False)
print (data_fall.head(1).index)