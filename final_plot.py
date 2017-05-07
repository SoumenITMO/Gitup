__author__ = 'Soumen'
from plotly import session as se
import plotly.graph_objs as go
import plotly.plotly as py
import csv
from numpy import arange,array,ones
from scipy import stats
import pandas
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from pykalman import KalmanFilter

def plot(x_data, y_data, colors, other_lables, labels, nodes, segment, title):
    se.sign_in("scottt1987", "T7ztp3BTkd0kFqeqilZX")   # Do Not Share It
    mode_size = [8, 8, 12, 8]
    line_size = [2, 2, 4, 2]

    traces = []
    for i in range(0, segment):
        #print(y_data[i],  y_data[i])


        traces.append(go.Scatter(
            x=x_data[i],
            y=y_data[i],
            mode='lines',
            name=other_lables[i],
            line=dict(color=colors[i], width=2),
            connectgaps=True,
        ))

        traces.append(go.Scatter(
            x=[x_data[i][0], x_data[i][nodes]],
            y=[y_data[i][0], y_data[i][nodes]],
            name = "",
            mode='markers',
            marker=dict(color=colors[i], size=1)
        ))


    layout = go.Layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            autotick=False,
            ticks='outside',
            tickcolor='rgb(204, 204, 204)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=True,
    )

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                      xanchor='right', yanchor='middle',
                                      text=label + ' {}%'.format(y_trace[0]),
                                      font=dict(family='Arial',
                                                size=16,
                                                color=colors,),
                                      showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[nodes],
                                      xanchor='left', yanchor='middle',
                                      text='{}%'.format(y_trace[nodes]),
                                      font=dict(family='Arial',
                                                size=16,
                                                color=colors,),
                                      showarrow=False))
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                  xanchor='left', yanchor='bottom',
                                  text=title,
                                  font=dict(family='Arial',
                                            size=30,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                  xanchor='center', yanchor='top',
                                  text='Source: PewResearch Center & ' +
                                       'Storytelling with data',
                                  font=dict(family='Arial',
                                            size=12,
                                            color='rgb(150,150,150)'),
                                  showarrow=False))

    layout['annotations'] = annotations

    fig = go.Figure(data=traces, layout=layout)
    py.plot(fig, filename='news-source')


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

#se.sign_in("scottt1987", "T7ztp3BTkd0kFqeqilZX")   # Do Not Share It
se.sign_in("mark99", "4F7tE4Uo3aKnQNEziTO6")   # Do Not Share It
xi = []

#data = pandas.read_csv("D3-data-file-refugee-main.csv", delimiter='\t')
#print(data['Syria'])

x_dat = []
y_dat = []
counter = 0
with open("D3-data-file-refugee.csv") as csvfile:
    reader = csvfile.readlines()
    skipline = 0
    for row in reader:
        if skipline > 1 and skipline < 40:
            xi.append(counter)
            x_dat.append(row.split("\t")[0])
            y_dat.append(int(row.split("\t")[1]))  # FOR RUSSIA
            counter += 1
        skipline += 1


kf = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
measurements = [[y_dat[0]], [y_dat[1]], [y_dat[2]]]
print(kf.em(measurements).smooth([[y_dat[3]], [y_dat[4]], [y_dat[5]]])[0])

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y_dat)
line = slope*xi+intercept

# Creating the dataset, and generating the plot
trace1 = go.Scatter(
                  x=x_dat,
                  y=y_dat,
                  mode='markers',
                  marker=go.Marker(color='rgb(255, 187, 19)'),
                  name='Data'
                  )

trace2 = go.Scatter(
                  x=x_dat,
                  y=line,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Fit'
                  )

annotation = go.Annotation(
                  x=3.5,
                  y=23.5,
                  text='$R^2 = '+str(float(std_err)),
                  showarrow=False,
                  font=go.Font(size=16)
                  )
layout = go.Layout(
                title='Linear Regression on Lebanon Refugee',
                plot_bgcolor='rgb(229, 229, 229)',
                  xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  annotations=[annotation]
                )

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Refugee Liner Refression')
