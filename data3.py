import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math_score"],show_hist = False)
fig.show()

mean = statistics.mean(data)
sd = statistics.stdev(data)
print(sd)
print(mean)