__author__ = 'Soumen'
#import pandas as pd
import plotly as plt
import csv
from plotly import session as sess
from plotly import graph_objs as go
import plotly.plotly as py

username = "scottt1987"
API_key = "ytAwGhmFGgzFGDH0axco"

#######################################################################
sess.sign_in(username,API_key)
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


# ////  CODE TO VISUALIzE data FILE ON MAP
fname = "CSV_OUTPUT\\data_file.csv"
skip_header_lin = 0
file_records_count = 0
df_airports = []
latt = []
long = []
flight_paths = []
city = []
temp_data = []
temp_data__ = []
map_data__ = []

def map():

    year = "2014"
    part = "2"
    all_lattitudes = []
    all_longitudes = []
    map_data__ = []
    cities = []
    skip_header_lin = 0
    count = 0
    map_year_time_span = ""
    legend_boolean = False
    duplicate_legend_data = []

    with open("CSV_OUTPUT\\Filter_Duplicate\\"+year+"-half-1-filter\\"+year+"-half-"+part+"-filter.csv", 'rb') as csvfile:
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

                if k[5] not in duplicate_legend_data:
                    legend_boolean = True
                    duplicate_legend_data.append(k[5])
                else :
                    legend_boolean = False
                tx = str(k[7].replace('\n','')) + "-" + str(k[8].replace('\n',''))[:16]+"..."

                map_data__.append(
                                 dict(
                                        type = 'scattergeo',
                                        #locationmode = 'USA-states',
                                        lon = [ k[10], k[12] ],
                                        lat = [ k[9], k[11] ],
                                        mode = 'lines',
                                        hoverinfo = 'text',
                                        name = tx ,
                                        showlegend=legend_boolean,
                                        line = dict(
                                            width = 2,
                                            color = "#"+k[0].split("\n")[0],
                                        ),
                                        #opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
                                        opacity = float(0.39)
                                    )
                )

            if skip_header_lin >= 5000:
                break
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
                        width=800,
                        height=600,
                        showlegend = True,
                        margin=go.Margin(
                            l=50,
                            r=50,
                            b=100,
                            t=100,
                            pad=1
                        ),
                        paper_bgcolor='white',
                        plot_bgcolor='white'
    )

    fig = dict( data=map_data__ + map_markers__, layout=layout )
    if part == "1":
        map_year_time_span = "Jan "+year+" - Jun "+year
    if part == "2":
        map_year_time_span = "Jul "+year+" - Dec "+year
    plt.plotly.plot(fig, filename=map_year_time_span+'Syria-Refugee' )

def csv_fiter():
    ct = 0
    data = ""
    duplicat_count = 0

    skip_header = 0
    temp_data__ = []
    fname = "half-1"
    year = "2015"

    with open("CSV_OUTPUT\\"+year+"-half-1\\"+fname+".csv", 'rb') as map_data:
        file_records_count = 0
        data = csv.reader(map_data)
        for j in data:
            if skip_header == 1:
                temp_data.append(j)
                file_records_count += 1
            skip_header = 1

    with open("CSV_OUTPUT\\"+year+"-half-1\\"+fname+".csv", 'rb') as map_data_1:
        dup = []
        data = csv.reader(map_data_1)
        skip_header = 0
        for ds in data:
            duplicat_count = 0
            if skip_header == 1:
                for ds1 in temp_data:
                    if ds1 == ds:
                        ## ... WRITE HERE NLTK CHECKING SYSTEM ... ##
                        if ds not in temp_data__:
                            temp_data__.append(ds)
                        else:
                            dup.append([ds, duplicat_count])
                        duplicat_count += 1
                #map_data__.append([temp_data__, duplicat_count])
                #temp_data__ = []
            skip_header = 1


    with open("CSV_OUTPUT\\Filter_Duplicate\\"+year+"-half-1-filter\\"+year+"-"+fname+"-filter.csv", "w") as ccsv:
        CSV_fieldnames = ['Event_COLOR_CODE', 'Event_ROOT_COLOR_CODE', 'Actor1Geo_CountryCode', 'Actor2Geo_CountryCode',
                          'ActionGeo_CountryCode', 'Event Code', 'Root Event Code', 'Main Reason', 'Reason', 'AC1_lat',
                          'AC1_lon', 'AC2_lat', 'AC2_lon', 'AC_lat', 'AC_lon', 'Source Url', 'Source City',
                          'Destination City', 'Keyword', 'Duplicate Entry']

        writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
        writer.writeheader()

        counter_to_extract_duplicate_data = 0
        duplicate_record_number = 0

        for extract_original_map_data in temp_data__:
            for extract_duplicate_data in dup:
                if extract_original_map_data == extract_duplicate_data[0]:
                    duplicate_record_number = extract_duplicate_data[1]

            writer.writerow({
                                         "Event_COLOR_CODE": extract_original_map_data[0],
                                         "Event_ROOT_COLOR_CODE": extract_original_map_data[1],

                                         "Actor1Geo_CountryCode": extract_original_map_data[2],
                                         "Actor2Geo_CountryCode": extract_original_map_data[3],
                                         "ActionGeo_CountryCode": extract_original_map_data[4],

                                         "Event Code": extract_original_map_data[5],
                                         "Root Event Code": extract_original_map_data[6],
                                         "Main Reason":extract_original_map_data[7],
                                         "Reason": extract_original_map_data[8],

                                         "AC1_lat": extract_original_map_data[9],
                                         "AC1_lon": extract_original_map_data[10],
                                         "AC2_lat": extract_original_map_data[11],
                                         "AC2_lon": extract_original_map_data[12],
                                         "AC_lat": extract_original_map_data[13],
                                         "AC_lon": extract_original_map_data[14],

                                         "Source Url" : extract_original_map_data[15],
                                         "Source City": extract_original_map_data[16],
                                         "Destination City" : extract_original_map_data[17],
                                         "Keyword" : extract_original_map_data[18],
                                         "Duplicate Entry": duplicate_record_number
                             })
            counter_to_extract_duplicate_data += 1
"""
def lets_stream():
    s = py.Stream(stream_id='ipn5a4kaxn')
    s.open()
    airports = dframe.sample(4)[['lat', 'long', 'airport']]
    depart = airports.iloc[0]
    arrive = airports.iloc[1]
    num_steps = 20

    while True:
        count = 0
        lats = np.linspace(depart['lat'], arrive['lat'], num_steps)
        lons = np.linspace(depart['long'], arrive['long'], num_steps)

        for i, j in zip(lats, lons):
            # added pts for the departure and arrival airports!!!
            s.write(dict(lon=[depart['long'], j, arrive['long']],
                         lat=[
                             depart['lat'], i, arrive['lat']], type='scattergeo',
                         marker={'size': [5, 7 + 0.2 * count, 5], 'sizemode': 'area',
                                 'color': ["green", "blue", "red"],
                                 'symbol': ["circle", "star", "x-open"]},
                         text=[depart['airport'],
                               '{},{}'.format(count, datetime.datetime.now()),
                               arrive['airport']]))
            count += 1
            stall = np.random.normal(10, 3)
            time.sleep(int((abs(stall) + 0.01) / 2.0))
            s.heartbeat()
            time.sleep(int((abs(stall) + 0.01) / 2.0))
        depart = arrive
        arrive = dframe.sample(1)[['lat', 'long', 'airport']].iloc[0]

    while True:
        try:
            lets_stream()
        except Exception as e:
            with open('log.txt', 'a+') as f:
                f.write(str(e))
            print(str(e))
            s.close()
"""
