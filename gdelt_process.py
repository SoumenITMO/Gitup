__author__ = 'Soumen'

import os
import zipfile as z
import csv
import CAMEO_PROCESS as cam
import re
import map_analysis_plott as map


# import pandas as pd
import keyword_filter as kf
import gdelt_event_downloader as ged
import buildMap as map__

#................................. START CRAWLING ................................................... #

def crawl():
    # " https://plot.ly/python/lines-on-maps/ PLOTLY EXAMPLE"
    pc = cam.process_Cameocode()  # INITILIZATION OF CAMEO CLASS
    year = "2011"
    dirs = os.listdir("Gdelt_Files__\\year-"+year)

    cities = []
    map_data_latt = []
    map_data_long = []
    #days = 364
    days = 58
    count_month = 0
    coords = []

    main_analysis_data = []
    main_analysis_data_1 = []
    file_processed = 1
    Quad_data = ""
    month = 0
    Origin = []
    Destination = []

    event_file_event_arr = []

    with open("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1ee.csv", "w") as ccsv:
            CSV_fieldnames = ['Event_COLOR_CODE','Event_COLOR_ROOT_CODE', 'Actor1Geo_CountryCode', 'Actor2Geo_CountryCode',
                              'ActionGeo_CountryCode','Event Code', "RootEventCode", "MainReason", "Reason", "AC1_lat",
                              "AC1_lon", "AC2_lat", "AC2_lon", "AC_lat", "AC_lon", "Source Url", "Source City",
                              "Destination City", "Keyword", "GeoMove"]

            writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
            writer.writeheader()

            for file in dirs:
                event_code_arr = []
                with z.ZipFile("Gdelt_Files__\\Year-"+year+"\\"+file, "r") as zf:
                    filename = list(zf.namelist())[0]
                    with zf.open(filename,"r") as fo:
                        datt = fo.readlines()

                        if year == "2011" or year == "2012" or year == "2013":
                            month = filename[:6:].split(".")[0]
                            month = int(month[4:])

                        else:
                            month = filename[:6:].split(".")[0]
                            month = int(month[4:])
                            #print(month)
                            #return 0

                for row in datt:
                    row = list(row.split("\t"))
                    try:
                        Url = row[57]
                    except:
                        Url = "--"
                    record_date = row[1]
                    EventCode = row[26]
                    EventBaseCode = row[27]
                    EventRootCode = row[28]
                    QuadClass = row[29]             # QUAD CLASS
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
                    Geo_Action = row[42]
                    DOR = row[56]

                    # print(Geo_Action, Actor2Geo_FullName)
                    # Continent = row[5]
                    # Capital_City = row[6]
                    # City_Code_Source = row[50]
                    # Location_Code = row[38]
                    # Source_place = row[52]
                    # Country = pc.country_lookup(Actor1Geo_CountryCode)

                    City_Code_Destination = row[36]

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

                    if "SYR" in row and "REF" in row and row[7] != "" \
                            and row[17] != "" and row[6]!="" and row[16]!="" \
                            and Actor1Geo_Lat != 0 and Actor1Geo_Long != 0 \
                            and Actor2Geo_Lat != 0 and Actor2Geo_Long != 0:

                        #print(row)
                        # return 0
                ############################## FOR D3 PLOTTING ########################################


                        if row[7] == "":
                            Origin.append([row[17], row[6], Actor1Geo_Lat, Actor1Geo_Long])  ## WHEN SOURCE AND DESTINATION IS SAME
                            main_analysis_data_1.append([row[17], row[17]])
                        if row[17] == "":
                            Destination.append([row[7], row[16], ActionGeo_Lat, ActionGeo_Long])  ## WHEN SOURCE AND DESTINATION IS SAME
                            main_analysis_data_1.append([row[7], row[7]])
                        else:

                            main_analysis_data_1.append([row[7], row[17]])
                            Origin.append([row[7], Actor1Geo_Lat, Actor1Geo_Long, row[6], Actor1Geo_FullName])
                            Destination.append([row[17], ActionGeo_Lat, ActionGeo_Long, row[16], Actor2Geo_FullName])  ## WHEN SOURCE AND DESTINATION IS SAME
                ############################## ################### ######################################

                        """
                        cities.append(City_Code_Destination)
                        map_data_latt.append(ActionGeo_Lat)
                        map_data_long.append(ActionGeo_Long)
                        """

                        # print(EventBaseCode, EventRootCode, EventCode)
                        # return 0
                        event_code_arr.append(pc.cameo([EventCode, EventBaseCode, EventRootCode,
                                                        Quad_data, Country, record_date],
                                                        [Actor1Geo_Lat, Actor1Geo_Long,
                                                        Actor2Geo_Lat, Actor2Geo_Long,
                                                        ActionGeo_Lat, ActionGeo_Long,
                                                        Actor1Geo_CountryCode,
                                                        Actor2Geo_CountryCode,
                                                        ActionGeo_CountryCode, Url,
                                                        Actor1Geo_FullName,
                                                        Actor2Geo_FullName, Geo_Action, DOR]))
                arr_event_code = []
                cameo_code = []
                coordinate = []
                # event_file_event_arr = []


                for event_code in event_code_arr:
                    ####################################  CSV FIELD VARIABLES
                    color_code = event_code[0][8][0]
                    color_code_root = event_code[0][8][1]
                    Actor1Geo_CountryCode_csv = event_code[0][0]
                    Actor2Geo_CountryCode_csv = event_code[0][1]
                    ActionGeo_CountryCode_csv = event_code[0][2]
                    EventCode = event_code[0][3]
                    RootEventCode = event_code[0][4]
                    Quad_text = event_code[0][5]
                    CountryCode = event_code[0][0]
                    MainReason = event_code[0][9][2][0]
                    Reason = event_code[0][9][0][0] #+ event_code[0][5] + event_code[6]
                    AC1_lat = event_code[0][10]
                    AC1_lon = event_code[0][11]
                    AC2_lat = event_code[0][12]
                    AC2_lon = event_code[0][13]
                    AC_lat = event_code [0][14]
                    AC_lon = event_code[0][15]
                    extract_Url = event_code[0][16]
                    source_city = event_code[0][17]
                    destination_city = event_code[0][18]
                    geomove = event_code[0][19]

                    #if kf.search_word(extract_Url) != "" or kf.search_word(extract_Url) == "":

                    writer.writerow({
                                     "Event_COLOR_CODE": color_code,
                                     "Event_COLOR_ROOT_CODE":color_code_root,
                                     "Actor1Geo_CountryCode":Actor1Geo_CountryCode_csv,
                                     "Actor2Geo_CountryCode":Actor2Geo_CountryCode_csv,
                                     "ActionGeo_CountryCode":ActionGeo_CountryCode_csv,
                                     "Event Code":EventCode,
                                     "RootEventCode":RootEventCode,
                                     "MainReason" : MainReason,
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
                                     #"Keyword" : kf.search_word(extract_Url)
                                     "Keyword" : "",
                                     "GeoMove" : geomove
                                   })

                    event_file_event_arr.append(event_code[0])
                    event_dat = event_code[0]
                    cameo_code.append(event_code[0][0])
                    arr_event_code.append(event_dat)
                    coordinate.append([event_code[0][2], event_code[0][3], event_code[0][4], event_code[0][5],
                                       event_code[0][6]])


                print("FILE PROCESSED ---------------------------------------------------------------------------"
                      "----> " + file + " MONTH --> " + str(month) + "FILE COUNT --> "+ str(file_processed))

                # os.remove("Gdelt_Files__\\year-"+year+"\\"+file)
                arr_event_code = []
                cameo_code = []
                coordinate = []

                """
                if year == "2011" or year == "2012" or year == "2013":
                    if month == 6:
                        file_processed = 0
                        ccsv.close()
                        os.rename("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1.csv", "CSV_OUTPUT\\"+year+"-half-1\\half-1.csv")
                        break

                if year == "2011" or year == "2012" or year == "2013":
                    if month == 12:
                        file_processed = 0
                        ccsv.close()
                        os.rename("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1.csv", "CSV_OUTPUT\\"+year+"-half-1\\half-2.csv")
                        break

                else:
                    if month == 6:
                        file_processed = 0
                        ccsv.close()
                        os.rename("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1.csv", "CSV_OUTPUT\\"+year+"-half-1\\half-1.csv")
                        break
                    if month == 12:
                        file_processed = 0
                        ccsv.close()
                        os.rename("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1.csv", "CSV_OUTPUT\\"+year+"-half-1\\half-2.csv")
                        break
                file_processed += 1
                """
                """
                else:
                    break
                file_processed += 1
                days -= 1
                """
            #ccsv.close()
            #os.rename("CSV_OUTPUT\\"+year+"-half-1\\"+year+"-half-1ee.csv", "CSV_OUTPUT\\"+year+"-half-1\\half-2new.csv")
            # print(pc.build_d3_data_file(main_analysis_data_1, Origin, Destination))
            main_analysis_data.append(pc.analysis(event_file_event_arr))


    with open("CSV_OUTPUT\\Analysis\\main__analysis-2new-"+year+".csv", "w") as ccsv_1:
        fieldnames_1 = ["Root Event Color Code", "Root Event Code",
                        "Root Event Name",
                        "Total Count Root Event",
                        "Event Code",
                        "Event Code Name",
                        "Number of Event Code"]

        temp_analysis = []
        for main_analysis_data_extract in main_analysis_data:
            for h in main_analysis_data_extract:
                if [h[1], h[2], h[3], h[9], h[5], h[6]] not in temp_analysis:
                    temp_analysis.append([h[1], h[2], h[3], h[9], h[5], h[6]])

        """
        writer_1 = csv.DictWriter(ccsv_1, delimiter=',', lineterminator='\n', fieldnames=fieldnames_1)
        writer_1.writeheader()
        a = ({  "Root Event Color Code": h[0],
                "Root Event Code":h[1],
                "Root Event Name":h[3],
                "Total Count Root Event":h[2],
                "Event Code":h[4],
                "Event Code Name":h[5],
                "Number of Event Code":h[6]
            })
        #print(a)
        # writer_1.writerow(a)
        """

        print(temp_analysis)

    #............................................................................................................... #

#map.plot_analysis_data()
crawl()
#ap__.csv_fiter()
#map__.map()
#ged.gdeltDownloader()
