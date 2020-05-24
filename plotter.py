import matplotlib.pyplot as py
import pandas as pd
fig, ax = py.subplots()
df=pd.read_csv("gdp2.csv")
df["rate"].plot(kind="line",color='green',ax=ax)
df2=pd.read_csv("sensex.csv")
df2['rate'].plot(kind="line",color='blue',ax=ax)
py.ylabel("rate")
ax.legend(["Gdp rate", "Sensex rate"]);
ax.set_xticklabels(list(range(2000,2019,2)))
py.show()