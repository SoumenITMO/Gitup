__author__ = 'Soumen'

import os
import zipfile as z
import csv
import CAMEO_PROCESS as cam
import keyword_filter as kf
import re
import buildMap as map__

import gdelt_event_downloader as ged
# ... SET DEFAULT ENCODING ... #
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
# ............................ #


#................................. START CRAWLING ................................................... #

def crawl():

    # " https://plot.ly/python/lines-on-maps/ PLOTLY EXAMPLE"

    pc = cam.process_Cameocode()  # INITILIZATION OF CAMEO CLASS
    year = "2014"
    dirs = os.listdir("Gdelt_Files__\\year-"+year)
    cities = []
    map_data_latt = []
    map_data_long = []

    #days = 364
    days = 58
    main_analysis_data = []
    file_processed = 0
    Quad_data = ""


    with open("CSV_OUTPUT\\data_file_"+year+".csv", "w") as ccsv:
            CSV_fieldnames = ['Event_COLOR_CODE','Actor1Geo_CountryCode', 'Actor2Geo_CountryCode', 'ActionGeo_CountryCode','Event Code',
                          "Reason", "AC1_lat", "AC1_lon", "AC2_lat", "AC2_lon", "AC_lat", "AC_lon", "Source Url",
                          "Source City", "Destination City", "Keyword"]

            writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
            writer.writeheader()
            for file in dirs:
                event_code_arr = []
                zf = z.ZipFile("Gdelt_Files__\\Year-"+year+"\\" + file)

                with z.ZipFile("Gdelt_Files__\\Year-"+year+"\\"+file, "r") as zf:
                    filename = list(zf.namelist())[0]
                    print(filename)
                    with zf.open(filename, "r") as f:
                        csvreader = csv.reader(f, dialect = "excel", delimiter = "\t")
                        data = list(csvreader)

                for row in data:
                    record_date = row[1]
                    City_Code_Destination = row[36]
                    EventCode = row[26]
                    EventBaseCode = row[27]
                    EventRootCode = row[28]
                    QuadClass = row[29]             # QUAD CLASS
                    Url = row[57]                   # Source URL
                    Actor1Geo_FullName = row[36]    # SOURCE CITY
                    Actor1Geo_CountryCode = row[37] # SOURCE COUNTRY
                    Actor1Geo_Lat = row[39]         # CENTROID MAPPING
                    Actor1Geo_Long = row[40]
                    ActionGeo_CountryCode = row[51] # COUNTRY TO MOVE
                    ActionGeo_FullName  = row[50]   # CITY TO MOVE
                    ActionGeo_Lat = row[53]
                    ActionGeo_Long = row[54]
                    Actor2Geo_CountryCode = row[44]
                    Actor2Geo_FullName = row[43]
                    Actor2Geo_Lat = row[46]
                    Actor2Geo_Long = row[47]
                    Geo_Action = row[49]

                    Continent = row[5]
                    Capital_City = row[6]
                    City_Code_Source = row[50]
                    Location_Code = row[38]
                    Source_place = row[52]
                    DOR = row[56]
                    Country = pc.country_lookup(Actor1Geo_CountryCode)

                    Country = ""
                    if QuadClass == "1":
                        Quad_data = "Verbal Cooperation"
                    if QuadClass == "2":
                        Quad_data = "Material Cooperation"
                    if QuadClass == "3":
                        Quad_data = "Verbal Conflict"
                    if QuadClass == "4":
                        Quad_data = "Material Conflict"
                    if QuadClass == "":
                        Quad_data = ""

                    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                      Url)

                    if "SYR" in row and "REF" in row and Actor2Geo_Lat != '' and Actor1Geo_Lat != '' \
                            and Actor2Geo_Long != '' and  urls != [] and kf.search_word(Url) != "":

                        #print(row)
                        cities.append(City_Code_Destination)
                        map_data_latt.append(ActionGeo_Lat)
                        map_data_long.append(ActionGeo_Long)

                        event_code_arr.append(pc.cameo([EventCode, EventBaseCode, EventRootCode,
                                                        Quad_data, Country, record_date],
                                                        [Actor1Geo_Lat, Actor1Geo_Long,
                                                        Actor2Geo_Lat, Actor2Geo_Long,
                                                        ActionGeo_Lat, ActionGeo_Long,
                                                        Actor1Geo_CountryCode,
                                                        Actor2Geo_CountryCode,
                                                        ActionGeo_CountryCode, Url,
                                                        Actor1Geo_FullName,
                                                        Actor2Geo_FullName]))

                arr_event_code = []
                cameo_code = []
                coordinate = []
                event_file_event_arr = []

                for event_code in event_code_arr:
                    ####################################  CSV FIELD VARIABLES

                    color_code = event_code[0][8]
                    print(event_code)
                    Actor1Geo_CountryCode_csv = event_code[0][0]
                    Actor2Geo_CountryCode_csv = event_code[0][1]
                    ActionGeo_CountryCode_csv = event_code[0][2]
                    EventCode = event_code[0][3]
                    Quad_text = event_code[0][5]
                    CountryCode = event_code[0][0]


                    Reason = event_code[0][9]   #+ event_code[0][5] + event_code[6]
                    AC1_lat = event_code[0][10]
                    AC1_lon = event_code[0][11]
                    AC2_lat = event_code[0][12]
                    AC2_lon = event_code[0][13]
                    AC_lat = event_code [0][14]
                    AC_lon = event_code[0][15]

                    extract_Url = event_code[0][16]
                    source_city = event_code[0][17]
                    destination_city = event_code[0][18]

                    if kf.search_word(extract_Url) != "" or kf.search_word(extract_Url) == "":
                        writer.writerow({
                                         "Event_COLOR_CODE": color_code,
                                         "Actor1Geo_CountryCode":Actor1Geo_CountryCode_csv,
                                         "Actor2Geo_CountryCode":Actor2Geo_CountryCode_csv,
                                         "ActionGeo_CountryCode":ActionGeo_CountryCode_csv,
                                         "Event Code":EventCode,
                                         "Reason":Reason,
                                         "AC1_lat":AC1_lat,
                                         "AC1_lon":AC1_lon,
                                         "AC2_lat":AC2_lat,
                                         "AC2_lon":AC2_lon,
                                         "AC_lat":AC_lat,
                                         "AC_lon":AC_lon,
                                         "Source Url" : extract_Url,
                                         "Source City": source_city,
                                         "Destination City" : destination_city,
                                         "Keyword" : kf.search_word(extract_Url)
                                       })

                    event_file_event_arr.append(event_code[0])
                    event_dat = event_code[0]
                    cameo_code.append(event_code[0][0])
                    arr_event_code.append(event_dat)
                    coordinate.append([event_code[0][2], event_code[0][3], event_code[0][4], event_code[0][5],
                                       event_code[0][6]])

                print("FILE PROCESSED ---------------------------------------------------------------------------"
                      "----> " + file)
                file_processed += 1
                main_analysis_data.append(pc.analysis(event_file_event_arr))

                if file_processed >= 1:
                    ""
                """
                else:
                    break
                file_processed += 1
                days -= 1
                main_analysis_data.append(pc.analysis(event_file_event_arr))
                """
    analysis_data = []


    with open("CSV_OUTPUT\\main__analysis.csv", "w") as ccsv_1:
        fieldnames_1 = ["Root Event Code",
                        "Root Event Name",
                        "Total Count Root Event",
                        "Event Code",
                        "Event Code Name",
                        "Number of Event Code"]

        writer_1 = csv.DictWriter(ccsv_1, delimiter=',', lineterminator='\n', fieldnames=fieldnames_1)
        writer_1.writeheader()

        for hj in main_analysis_data:
            for h in hj:
                a = ({
                        "Root Event Code":h[0],
                        "Root Event Name":h[2],
                        "Total Count Root Event":h[1],
                        "Event Code":h[3],
                        "Event Code Name":h[4],
                        "Number of Event Code":h[5]
                    })
                writer_1.writerow(a)
    #............................................................................................................... #

crawl()
#map__.map()
#ged.gdeltDownloader()
