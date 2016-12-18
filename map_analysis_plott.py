__author__ = 'Soumen'

import plotly as plt
import csv
from plotly import graph_objs as go
import random
import plotly.plotly as py

import csv as cs
from plotly import session as sess
from numpy import *

username = "scottt1987"
API_key = "ytAwGhmFGgzFGDH0axco"
sess.sign_in(username,API_key)

def plot_analysis_data():
    """
    N = 30.     # Number of boxes
    # generate an array of rainbow colors by fixing the saturation and lightness of the HSL representation of colour
    # and marching around the hue.
    # Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.

    c = ['hsl('+str(h)+',50%'+',50%)' for h in linspace(0, 360, N)]
    # Each box is represented by a dict that contains the data, the type, and the colour.
    # Use list comprehension to describe N boxes, each with a different colour and with different randomly generated data:

    data = []
    count = 0
    h = [11.993142123, 99.4154234]
    for i in h:
        data.append(
                      dict({
                                'y': h * random.rand(2),
                                'type':'box',
                                'marker':{'color': c[count]}
                      })
                   )
        count += 1
    # format the layout
    layout = {'xaxis': {'showgrid':False,'zeroline':False, 'tickangle':60,'showticklabels':False},
              'yaxis': {'zeroline':False,'gridcolor':'white'},
              'paper_bgcolor': 'rgb(233,233,233)',
              'plot_bgcolor': 'rgb(233,233,233)',
              }
    py.plot(data, validate=True, layout = layout)
    """

    fname = "1"
    year = "2011"
    tmp = []
    skip_first = 0

    dat = []
    skip_first1 = 0

    with open("CSV_OUTPUT\\Analysis\\main__analysis-"+fname+"-"+year+".csv", "rb") as csvfile:
        spamreader = cs.reader(csvfile)
        for row in spamreader:
            k = list(row)
            if skip_first == 1:
                strr = k[2].replace("\r\n","")
                if strr not in tmp:
                    tmp.append(strr)
            skip_first = 1

    with open("CSV_OUTPUT\\Analysis\\main__analysis-"+fname+"-"+year+".csv", "rb") as csvfile:
        spamreader1 = cs.reader(csvfile)
        listdata = list(spamreader1)

        skip_first1 = 0
        aggregate_analysis = []
        sum = 0

        for extracttmp in tmp:
            for listdata_extract in listdata:
                if skip_first1 == 1:
                    string_stp = listdata_extract[2].replace("\r\n","")
                    if extracttmp == string_stp:
                       sum += int(listdata_extract[3])
                skip_first1 = 1
            aggregate_analysis.append([extracttmp, sum])

    #with open("CSV_OUTPUT\\Analysis\\FinalAnalysis\\final_analysis-"+fname+"-"+year+".csv", "rb") as csvfile: