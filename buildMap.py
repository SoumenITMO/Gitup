__author__ = 'Soumen'
import plotly as plt
import csv
from plotly import session as sess
from plotly import graph_objs as go
import pandas as pd
#######################################################################
sess.sign_in("scottt1987","xxb6xdrboe")

"""
df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()
df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()
airports = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_airports['long'],
        lat = df_airports['lat'],
        hoverinfo = 'text',
        text = df_airports['airport'],
        mode = 'markers',
        marker = dict(
            size=2,
            color='rgb(255, 0, 0)',
            line = dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
flight_paths = []
for i in range( len( df_flight_paths ) ):
    flight_paths.append(
        dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
            lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
            opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
        )
    )
layout = dict(
        title = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
        showlegend = False,
        geo = dict(
            scope='north america',
            projection=dict( type='azimuthal equal area' ),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )
fig = dict( data=flight_paths + airports, layout=layout )
plt.plotly.iplot( fig, filename='d3-flight-paths' )
"""
############################################################################


# ////  CODE TO VISUALIZE data FILE ON MAP
fname = "CSV_OUTPUT\\data_file.csv"
skip_header_lin = 0

df_airports = []

latt = []
long = []
flight_paths = []
city = []


def map():

    all_lattitudes = []
    all_longitudes = []
    map_data__ = []
    cities = []
    skip_header_lin = 0

    with open("CSV_OUTPUT\\data_file_2014.csv", 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        color = 'red'
        for row in spamreader:
            k = list(row)
            if skip_header_lin >= 1:

                all_lattitudes.append(k[6])
                all_lattitudes.append(k[8])
                all_longitudes.append(k[7])
                all_longitudes.append(k[9])
                cities.append(k[13])
                cities.append(k[14])

                if (skip_header_lin < 5):
                    color = 'red'
                else:
                    color = 'green'

                map_data__.append(
                                    dict(
                                        type = 'scattergeo',
                                        #locationmode = 'USA-states',
                                        lon = [ k[7], k[9] ],
                                        lat = [ k[6], k[8] ],
                                        mode = 'lines',
                                        line = dict(
                                            width = 2,
                                            color = "#"+k[0].split("\n")[0],
                                        ),
                                        #opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
                                        opacity = float(0.39)
                                    )
                )
            skip_header_lin += 1


    map_markers__ = [ dict(
                            type = 'scattergeo',
                            #locationmode = 'USA-states',
                            lon = all_longitudes,
                            lat = all_lattitudes,
                            hoverinfo = 'text',
                            text = cities,
                            mode = 'markers',
                            marker = dict(
                                            size=2,
                                            color='rgb(255, 0, 0)',
                                            line = dict(
                                                            width=3,
                                                            color='rgba(68, 68, 68, 0)'
                                                       )
                                    )
                        )
                    ]


    layout = go.Layout(
                        autosize=False,
                        width=500,
                        height=500,
                        showlegend = False,
                        margin=go.Margin(
                            l=50,
                            r=50,
                            b=100,
                            t=100,
                            pad=4
                        ),
                        paper_bgcolor='#7f7f7f',
                        plot_bgcolor='#c7c7c7'
    )

    fig = dict( data=map_data__ + map_markers__, layout=layout )
    plt.plotly.plot(fig, filename='Syria-Refugee' )