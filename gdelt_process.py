__author__ = 'Soumen'

import os
import zipfile as z
import csv
import CAMEO_PROCESS as cam
import re
import numpy as np
import gdelt_event_downloader as gd
#................................. START CRAWLING ................................................... #

def crawl():
    # " https://plot.ly/python/lines-on-maps/ PLOTLY EXAMPLE"
    pc = cam.process_Cameocode()  # INITILIZATION OF CAMEO CLASS
    year__ = "2011"
    month_ = ""
    year = ""
    dirs = os.listdir("Gdelt_Files__\\year-"+year__)
    fcount = 0
    main_analysis_data = []
    event_file_event_arr = []
    CountArray = []
    filename = ""

    with open("CSV_OUTPUT\\"+year__+"-half-1\\"+year__+"-half-1test.csv", "w") as ccsv:
            CSV_fieldnames = ['Event_COLOR_CODE','Event_COLOR_ROOT_CODE', 'Actor1Geo_CountryCode', 'Actor2Geo_CountryCode',
                              'ActionGeo_CountryCode','Event Code', "RootEventCode", "MainReason", "Reason", "AC1_lat",
                              "AC1_lon", "AC2_lat", "AC2_lon", "AC_lat", "AC_lon", "Source Url", "Source City",
                              "Destination City", "Keyword", "GeoMove"]

            writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
            writer.writeheader()


            for file in dirs:
                event_code_arr = []
                with z.ZipFile("Gdelt_Files__\\Year-"+str(year__)+"\\"+file, "r") as zf:
                    filename = list(zf.namelist())[0]

                    with zf.open(filename, "r") as fo:
                        datt = fo.readlines()

                for row in datt:
                    row = list(row.split("\t"))
                    month_ = int(row[2][4:])
                    year = row[3]
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
                    Actor2Geo_CountryCode = row[44] # MIDDLE COUNTRY or VIA
                    ActionGeo_CountryCode = row[51] # COUNTRY TO MOVE
                    Actor1Geo_Lat = row[39]         # CENTROID MAPPING
                    Actor1Geo_Long = row[40]
                    ActionGeo_FullName  = row[50]   # CITY TO MOVE
                    ActionGeo_Lat = row[53]
                    ActionGeo_Long = row[54]
                    Actor2Geo_FullName = row[43]
                    Actor2Geo_Lat = row[46]
                    Actor2Geo_Long = row[47]
                    Geo_Action = row[42]
                    DOR = row[56]

                    #print(Actor1Geo_FullName, Actor2Geo_FullName, ActionGeo_FullName)
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
                            and row[17] != "" and row[6]!="" and row[16] != "" \
                            and Actor1Geo_Lat != 0 and Actor1Geo_Long != 0 \
                            and Actor2Geo_Lat != 0 and Actor2Geo_Long != 0:


                            CountArray.append([month_, date_to_sentence(month_, year),
                                              [pc.country_lookup(Actor1Geo_CountryCode)],
                                              [pc.country_lookup(Actor2Geo_CountryCode)],
                                              [pc.country_lookup(ActionGeo_CountryCode),
                                              [EventCode, EventBaseCode,
                                              pc.country_lookup(Actor2Geo_CountryCode),
                                              pc.country_lookup(ActionGeo_CountryCode)]]])

                pc.buildCounterTable(CountArray, fcount, filename)
                CountArray = []
                #print(EventCode, EventBaseCode, EventRootCode)

                #pc.buildCounterTable(CountArray, fcount, filename)

                fcount += 1
            
            ccsv.close()

def date_to_sentence(month_code, year):
    if month_code == 1:
        return "January " + str(year)
    if month_code == 2:
        return "February " + str(year)
    if month_code == 3:
        return "March " + str(year)
    if month_code == 4:
        return "April " + str(year)
    if month_code == 5:
        return "May " + str(year)
    if month_code == 6:
        return "June " + str(year)
    if month_code == 7:
        return "July " + str(year)
    if month_code == 8:
        return "Auguest " + str(year)
    if month_code == 9:
        return "September " + str(year)
    if month_code == 10:
        return "October " + str(year)
    if month_code == 11:
        return "November " + str(year)
    if month_code == 12:
        return "December " + str(year)
def test_fun():
    data = [[1, 'January 2011', ['Lebanon'], ['Syria'], ['Syria']], [1, 'January 2011', ['Lebanon'], ['Syria'],
            ['Syria']], [1, 'January 2011', ['Lebanon'], ['Syria'], ['Syria']], [1, 'January 2011', ['Syria'],
            ['Syria'], ['Syria']], [1, 'January 2011', ['Syria'], ['Syria'], ['Syria']],
            [1, 'January 2011', ['Iraq'], ['Syria'], ['Syria']], [1, 'January 2011', ['Syria'], ['Syria'],
            ['Australia']], [1, 'January 2011', ['Syria'], ['Australia'], ['Australia']],
            [1, 'January 2011', ['Iraq'], ['Syria'], ['Australia']], [1, 'January 2011', ['Iraq'], ['Syria'],
            ['Syria']], [1, 'January 2011', ['Iraq'], ['Syria'], ['Syria']], [1, 'January 2011', ['Syria'],
            ['Iraq'], ['Syria']], [1, 'January 2011', ['Iraq'], ['Iraq'], ['Iraq']], [1, 'January 2011', ['Israel'],
            ['Israel'], ['Israel']], [1, 'January 2011', ['Israel'], ['Israel'], ['Israel']]]


    count__ = 0
    month__ = 1
    # cls.temp.append(table_data[0][0])
    processed = []
    lock = 0
    header__ = ""
    fcount = 0
    #######

    skip_first_line = 0
    dest = []
    destination_ = 0
    temp = []
    temp_ = []
    count_country = []

    headers = []
    csv_data = []
    tmp = []
    tmp_arr = []
    tmp_arr0 = []
    main_ = []
    temp_data_holder = []

    line_0_prev = 0
    line_0_current = 0
    first_ = 0
    position = 0
    position_1 = 0
    headers_written = 0
    i = 1
    k = 0
    j = 0
    second_data_header = ""
    uu = 0
    inuu = 0
    uucounter = 0
    header__ = ""
    parts = 0
    second_data_header__ = ""
    count_parts = 0
    tmp_data_part = ""
    main_data_part = []


    for extract_data_ in data:
        for h in data:
            if extract_data_[2] == h[2]:
                count__ += 1
        temp.append([extract_data_[1], count__, extract_data_[2]])
        count__ = 0


    for k in temp:
        if k not in count_country:
            count_country.append(k)


    if fcount == 0 and not os.path.exists("file__.csv"):
        with open("file__.csv", "w") as ccsv:
            for k in count_country:
                if position == 0:
                    CSV_fieldnames = [k[0]]
                    writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
                    writer.writeheader()

                    CSV_fieldnames = ["  ", " "]
                    writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
                    writer.writeheader()

                    writer.writerow({
                               "  ": k[2][0],
                               " ": k[1],
                    })

                """
                if position == 1:
                    CSV_fieldnames = ["  ", " "]
                    writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
                    writer.writeheader()
                """

                if position > 0:
                        writer.writerow({
                               "  ": k[2][0],
                               " ": k[1],
                   })
                position += 1
        ccsv.close()
        lock += 1

"""
if column == 0:
                                try:
                                    tempstring = extract_data[i]
                                except:
                                    tempstring = ",,"
                            if column == 1:
                                for jj in extract_data[i]:
                                    if k == 0:
                                        internal_str += str(jj)+","
                                    else:
                                        if i == 0:
                                            internal_str = internal_str+"\t\t" + str(jj)
                                        else:
                                            internal_str += str(jj)+"\n"
                                    k += 1
                                if i == 0:
                                    internal_str += "\n"
                                    d = tempstring.replace("\n", "")
                                    d += "," + "\t\t"
                                else:
                                    d = tempstring.replace("\n", "")

                                hold_data.append(d+","+internal_str)
                                k = 0
                                internal_str = ""
                                tempstring = ""
                            column += 1
                        tempstring = ""
                        column = 0
                        i += 1
                print(hold_data)
"""

#map.generateFinalDataAnalysis()
crawl()
#map__.csv_fiter()
#map__.map()
#gd.gdeltDownloader()
#udp.CompareUNdata()
#test_fun()
