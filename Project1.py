import pandas as pd
import numpy as np
a=pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
print (np.mean(a["Calls"]).round())