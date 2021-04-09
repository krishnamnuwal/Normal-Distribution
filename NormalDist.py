import plotly.figure_factory as ff
import csv
import plotly
import pandas as pd 

file=pd.read_csv("data.csv")
figure=ff.create_distplot([file["Height(Inches)"].tolist()],["Height"],hist_color='red')
plotly.offline.plot(figure)