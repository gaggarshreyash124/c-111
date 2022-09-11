import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math_score"],show_hist = False)
fig.show()

mean = statistics.mean(data)
sd = statistics.stdev(data)
print(sd)
print(mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    meanlist.append(set_of_mean)

mean = statistics.mean(meanlist)
print(mean)

fig = ff.create_distplot([meanlist],["Math_score"],show_hist = False)
fig.show()