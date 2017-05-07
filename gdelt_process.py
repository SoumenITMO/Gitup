__author__ = 'Soumen'

import os
import zipfile as z
import csv
import CAMEO_PROCESS as cam
import re
#................................. START CRAWLING ................................................... #

def crawl():
    # " https://plot.ly/python/lines-on-maps/ PLOTLY EXAMPLE"
    pc = cam.process_Cameocode()  # INITILIZATION OF CAMEO CLASS
    year__ = "2015"
    year = ""
    dirs = os.listdir("Gdelt_Files__\\year-"+year__)
    fcount = 0
    main_analysis_data = []
    event_file_event_arr = []
    CountArray = []
    CountArray_1 = []

    filename = ""
    stage_1 = 0
    stage_2 = 0
    stage_3 = 0
    stage_4 = 0


    with open("CSV_OUTPUT\\"+year__+"-half-1\\"+year__+"-half-1test.csv", "w") as ccsv:
            CSV_fieldnames = ['Event_COLOR_CODE','Event_COLOR_ROOT_CODE', 'Actor1Geo_CountryCode', 'Actor2Geo_CountryCode',
                              'ActionGeo_CountryCode','Event Code', "RootEventCode", "MainReason", "Reason", "AC1_lat",
                              "AC1_lon", "AC2_lat", "AC2_lon", "AC_lat", "AC_lon", "Source Url", "Source City",
                              "Destination City", "Keyword", "GeoMove"]
            writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
            writer.writeheader()

            for file in dirs:
                Gdeltmonth_ = ""
                event_code_arr = []
                with z.ZipFile("Gdelt_Files__\\Year-"+str(year__)+"\\"+file, "r") as zf:
                    filename = list(zf.namelist())[0]
                    with zf.open(filename, "r") as fo:
                        datt = fo.readlines()
                        #Gdeltmonth_ = int(filename.split

                for row in datt:
                    row = list(row.split("\t"))
                    Gdeltmonth_ = int(row[2][4:])
                    year = row[3]
                    day__ = int(row[1][6:])

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

                            CountArray.append([Gdeltmonth_, date_to_sentence(Gdeltmonth_, year),
                                              [pc.country_lookup(Actor1Geo_CountryCode)],
                                              [pc.country_lookup(Actor2Geo_CountryCode)],
                                              [pc.country_lookup(ActionGeo_CountryCode),
                                              [EventCode, EventBaseCode,
                                              pc.country_lookup(Actor2Geo_CountryCode),
                                              pc.country_lookup(ActionGeo_CountryCode)]]])

                            CountArray_1.append([Gdeltmonth_, date_to_sentence(Gdeltmonth_, year),
                                              [pc.country_lookup(Actor1Geo_CountryCode)],
                                              [pc.country_lookup(Actor2Geo_CountryCode)],
                                              [pc.country_lookup(ActionGeo_CountryCode),
                                              [EventCode, EventBaseCode,
                                              pc.country_lookup(Actor2Geo_CountryCode),
                                              pc.country_lookup(ActionGeo_CountryCode)]]])



                    """
                    if day__ == 8 and stage_1 == 0:
                        point = 1
                        pc.buildCounterTable(point, CountArray, fcount, filename)
                        CountArray = []
                        stage_1 = 1

                    if day__ == 15 and stage_2 == 0:
                        point = 1
                        pc.buildCounterTable(point, CountArray, fcount, filename)
                        stage_2 = 1
                        CountArray = []



                    if day__ == 22 and stage_3 == 0:
                        point = 1
                        pc.buildCounterTable(point, CountArray, fcount, filename)
                        CountArray = []
                        stage_3 = 1

                    else:
                        if stage_3 == 1:
                            point = 1
                            pc.buildCounterTable(point, CountArray, fcount, filename)
                            CountArray = []
                    """
            print(filename)
            point = 1
            pc.buildCounterTable(point, CountArray_1, fcount, filename)
            CountArray_1 = []
            fcount += 1
            stage_1 = 0
            stage_2 = 0
            stage_3 = 0
            ccsv.close()
def data_analysis():

    all_country = []
    store_all_data = []
    skip_header = 0
    raw_processed_data = []


    date__1 = [["13-Apr F" , "13-Apr-Data-1"],["13-Apr S","13-Apr-Data-2"],["13-Apr T","13-Apr-Data-3"],
            ["13-Apr FO","13-Apr-Data-4"],["13-May F","13-May-Data-1"],["13-May S","13-May-Data-2"],
            ["13-May T","13-May-Data-3"],["13-May FO","13-May-Data-4"],["13-Jun F","13-Jun-Data-1"],
            ["13-Jun S","13-Jun-Data-2"],["13-Jun T","13-Jun-Data-3"],["13-Jun FO","13-Jun-Data-4"],
            ["13-July F","13-July-Data-1"],["13-July S","13-July-Data-2"],["13-July T","13-July-Data-3"],
            ["13-July FO","13-July-Data-4"],["13-Aug F","13-Aug-Data-1"],["13-Aug S","13-Aug-Data-2"],
            ["13-Aug T","13-Aug-Data-3"],["13-Aug FO","13-Aug-Data-4"],["13-Sep F","13-Sep-Data-1"],
            ["13-Sep S","13-Sep-Data-2"],["13-Sep T","13-Sep-Data-3"],["13-Sep FO","13-Sep-Data-4"],
            ["13-Oct F","13-Oct-Data-1"],["13-Oct S","13-Oct-Data-2"],["13-Oct T","13-Oct-Data-3"],
            ["13-Oct FO","13-Oct-Data-4"],["13-Nov F","13-Nov-Data-1"],["13-Nov S","13-Nov-Data-2"],
            ["13-Nov T","13-Nov-Data-3"],["13-Nov FO","13-Nov-Data-4"],["13-Dec F","13-Dec-Data-1"],
            ["13-Dec S","13-Dec-Data-2"],["13-Dec T","13-Dec-Data-3"],["13-Dec FO","13-Dec-Data-4"]]

    """
    date__2 = [["14-Jan F","14-Jan-Data-1"],["14-Jan S","14-Jan-Data-2"],["14-Jan T","14-Jan-Data-3"],
               ["14-Jan FO","14-Jan-Data-4"],["14-Feb F","14-Feb-Data-1"],["14-Feb S","14-Feb-Data-2"],
               ["14-Feb T","14-Feb-Data-3"],["14-Feb FO","14-Feb-Data-4"],["14-Mar F","14-Mar-Data-1"],
               ["14-Mar S","14-Mar-Data-2"],["14-Mar T","14-Mar-Data-3"],["14-Mar FO","14-Mar-Data-4"],
               ["14-Apr F","14-Apr-Data-1"],["14-Apr S","14-Apr-Data-2"],["14-Apr T","14-Apr-Data-3"],
               ["14-Apr FO","14-Apr-Data-4"],["14-May F","14-May-Data-1"],["14-May S","14-May-Data-2"],
               ["14-May T","14-May-Data-3"],["14-May FO","14-May-Data-4"],["14-Jun F","14-Jun-Data-1"],
               ["14-Jun S","14-Jun-Data-2"],["14-Jun T","14-Jun-Data-3"],["14-Jun FO","14-Jun-Data-4"],
               ["14-Jul F","14-Jul-Data-1"],["14-Jul S","14-Jul-Data-2"],["14-Jul T","14-Jul-Data-3"],
               ["14-Jul FO","14-Jul-Data-4"],["14-Aug F","14-Aug-Data-1"],["14-Aug S","14-Aug-Data-2"],
               ["14-Aug T","14-Aug-Data-3"],["14-Aug FO","14-Aug-Data-4"],["14-Sep F","14-Sep-Data-1"],
               ["14-Sep S","14-Sep-Data-2"],["14-Sep T","14-Sep-Data-3"],["14-Sep FO","14-Sep-Data-4"],
               ["14-Oct F","14-Oct-Data-1"],["14-Oct S","14-Oct-Data-2"],["14-Oct T","14-Oct-Data-3"],
               ["14-Oct FO","14-Oct-Data-4"],["14-Nov F","14-Nov-Data-1"],["14-Nov S","14-Nov-Data-2"],
               ["14-Nov T","14-Nov-Data-3"],["14-Nov FO","14-Nov-Data-4"],["14-Dec F","14-Dec-Data-1"],
               ["14-Dec S","14-Dec-Data-2"],["14-Dec T","14-Dec-Data-3"],["14-Dec FO","14-Dec-Data-4"]] """

    date__2 = [["14-Jan FO","14-Jan-Data-4"],["14-Feb F","14-Feb-Data-1"],["14-Feb S","14-Feb-Data-2"],
               ["14-Feb T","14-Feb-Data-3"],["14-Feb FO","14-Feb-Data-4"],["14-Mar F","14-Mar-Data-1"],
               ["14-Mar S","14-Mar-Data-2"],["14-Mar T","14-Mar-Data-3"],["14-Mar FO","14-Mar-Data-4"],
               ["14-Apr F","14-Apr-Data-1"],["14-Apr S","14-Apr-Data-2"],["14-Apr T","14-Apr-Data-3"],
               ["14-Apr FO","14-Apr-Data-4"],["14-May F","14-May-Data-1"],["14-May S","14-May-Data-2"],
               ["14-May T","14-May-Data-3"],["14-May FO","14-May-Data-4"],["14-Jun F","14-Jun-Data-1"],
               ["14-Jun S","14-Jun-Data-2"],["14-Jun T","14-Jun-Data-3"],["14-Jun FO","14-Jun-Data-4"],
               ["14-Jul F","14-Jul-Data-1"],["14-Jul S","14-Jul-Data-2"],["14-Jul T","14-Jul-Data-3"],
               ["14-Jul FO","14-Jul-Data-4"],["14-Aug F","14-Aug-Data-1"],["14-Aug S","14-Aug-Data-2"],
               ["14-Aug T","14-Aug-Data-3"],["14-Aug FO","14-Aug-Data-4"],["14-Sep F","14-Sep-Data-1"],
               ["14-Sep S","14-Sep-Data-2"],["14-Sep T","14-Sep-Data-3"],["14-Sep FO","14-Sep-Data-4"],
               ["14-Oct F","14-Oct-Data-1"],["14-Oct S","14-Oct-Data-2"],["14-Oct T","14-Oct-Data-3"],
               ["14-Oct FO","14-Oct-Data-4"],["14-Nov F","14-Nov-Data-1"],["14-Nov S","14-Nov-Data-2"],
               ["14-Nov T","14-Nov-Data-3"],["14-Nov FO","14-Nov-Data-4"],["14-Dec F","14-Dec-Data-1"],
               ["14-Dec S","14-Dec-Data-2"]]


    date__3 = [["15-Jan FO","15-Jan-Data-4"],["15-Feb F","15-Feb-Data-1"],["15-Feb S","15-Feb-Data-2"],
            ["15-Feb T","15-Feb-Data-3"],["15-Feb FO","15-Feb-Data-4"],["15-Mar F","15-Mar-Data-1"],
            ["15-Mar S","15-Mar-Data-2"],["15-Mar T","15-Mar-Data-3"],["15-Mar FO","15-Mar-Data-4"],
            ["15-Apr F","15-Apr-Data-1"],["15-Apr S","15-Apr-Data-2"],["15-Apr T","15-Apr-Data-3"],
            ["15-Apr FO","15-Apr-Data-4"],["15-May F","15-May-Data-1"],["15-May S","15-May-Data-2"],
            ["15-May T","15-May-Data-3"],["15-May FO","15-May-Data-4"],["15-Jun F","15-Jun-Data-1"],
            ["15-Jun S","15-Jun-Data-2"],["15-Jun T","15-Jun-Data-3"],["15-Jun FO","15-Jun-Data-4"],
            ["15-Jul F","15-Jul-Data-1"],["15-Jul S","15-Jul-Data-2"],["15-Jul T","15-Jul-Data-3"],
            ["15-Jul FO","15-Jul-Data-4"],["15-Aug F","15-Aug-Data-1","15-Aug S","15-Aug-Data-2"],
            ["15-Aug T","15-Aug-Data-3"],["15-Aug FO","15-Aug-Data-4"],["15-Sep F","15-Sep-Data-1"],
            ["15-Sep S","15-Sep-Data-2"],["15-Sep T","15-Sep-Data-3"],["15-Sep FO","15-Sep-Data-4"],
            ["15-Oct F","15-Oct-Data-1"],["15-Oct S","15-Oct-Data-2"],["15-Oct T","15-Oct-Data-3"],
            ["15-Oct FO","15-Oct-Data-4"],["15-Nov F","15-Nov-Data-1"],["15-Nov S","15-Nov-Data-2"],
            ["15-Nov T","15-Nov-Data-3"],["15-Nov FO","15-Nov-Data-4"],["15-Dec F","15-Dec-Data-1"],
            ["15-Dec S","15-Dec-Data-2"]]





    date__ = [["13-Apr F", "13-Apr-Data-1"], ["13-Apr S", "13-Apr-Data-2"], ["13-Apr T", "13-Apr-Data-3"],
              ["13-Apr FO", "13-Apr-Data-4"], ["13-May F", "13-May-Data-1"], ["13-May S", "13-May-Data-2"],
              ["13-May T", "13-May-Data-3"], ["13-May FO", "13-May-Data-4"], ["13-Jun F","13-Jun-Data-1"],
            ["13-Jun S","13-Jun-Data-2"],["13-Jun T","13-Jun-Data-3"],["13-Jun FO","13-Jun-Data-4"],
            ["13-July F","13-July-Data-1"],["13-July S","13-July-Data-2"],["13-July T","13-July-Data-3"],
            ["13-July FO","13-July-Data-4"],["13-Aug F","13-Aug-Data-1"],["13-Aug S","13-Aug-Data-2"],
            ["13-Aug T", "13-Aug-Data-3"], ["13-Aug FO", "13-Aug-Data-4"]]

    country_count = 9

    date__ = date__2

    with open("midpoint-refugee-counter-7.csv", "r")as fo:
    #with open("finalpoint-refugee-counter.csv", "r")as fo:
        data = fo.readlines()
        for read_all in data:
            if read_all not in store_all_data:
                store_all_data.append(read_all)
            if skip_header > 0:
                for extacrt_all in read_all.split(","):
                    if extacrt_all != "" and extacrt_all != "\n":
                        if RepresentsInt(extacrt_all) == False:
                            if extacrt_all not in all_country:
                                if country_count > 0:
                                    all_country.append(extacrt_all)
                                    country_count -= 1
            skip_header += 1

    all_country = ["Algeria", "Syria", "France", "Somalia", "Tunisia"]  # FOR TESTING PURPOSE

    #all_country = ["Syria", "Russia"]  # FOR TESTING PURPOSE
    all_country = ["Algeria", "Syria", "Lebanon", "Somalia", "Israel", "Turkey", "France", "Greece", "United Kingdom"]#, "Germany"]  # FOR TESTING PURPOSE
    all_country___ = ["", "", "", "", "", "", "", "", ""]  # FOR TESTING PURPOSE



    with open("finalpoint-refugee-counter.csv", "r") as fo1:
        csv_dict_data = csv.DictReader(fo1)
        for extract_csv_data in csv_dict_data:
            for extract_country in all_country:
                for extract_date in date__:
                    if extract_csv_data[extract_date[0]] != "":
                        if extract_country in extract_csv_data[extract_date[0]]:
                            raw_processed_data.append([extract_country, extract_date[0],
                                                       extract_csv_data[extract_date[1]]])

    build_country_data = []
    build_tmp_refugee_counter = []
    build_refugee_counter = []
    count_num_cuntry = 0
    single_time_series = []
    _time_series = []

    for k in all_country:
        for extract_raw_data in raw_processed_data:
            if extract_raw_data[0] == k:
                if k not in build_country_data:
                    build_country_data.append(k)
                    count_num_cuntry += 1
                build_tmp_refugee_counter.append([extract_raw_data[2], extract_raw_data[1]])
        build_refugee_counter.append(build_tmp_refugee_counter)
        build_tmp_refugee_counter = []

    for ext_date in date__:
        single_time_series.append(ext_date[0])
    while count_num_cuntry > 0:
        _time_series.append(single_time_series)
        count_num_cuntry -= 1


    ###############  DATA ARRANGER ##############################
    sd__ = []
    sd__0 = []
    sd__tmp = []

    for extract_inner_refugee_counter in build_refugee_counter:
        for extract__date_ in _time_series:
            for inner_extract_date_ in extract__date_:
                for extract_inner_0_refugee_counter in extract_inner_refugee_counter:
                    if extract_inner_0_refugee_counter not in sd__:
                        sd__.append(extract_inner_0_refugee_counter)
                    if inner_extract_date_ == extract_inner_0_refugee_counter[1]:
                        if extract_inner_0_refugee_counter not in sd__0:
                            sd__0.append(extract_inner_0_refugee_counter)
        if sd__0 != []:
            sd__tmp.append(sd__0)
        sd__0 = []
    build_refugee_counter = sd__tmp
    ##################################################################


    t0_ = []
    for ex_single_time in _time_series:
        for g in build_refugee_counter:
            if [g, ex_single_time] not in t0_:
                t0_.append([g, ex_single_time])
    difference = 0
    c_difference = 0
    t1_ = []
    temp_final = []

    for k in t0_:
        if len(k[1]) > len(k[0]):
            difference = len(k[1]) - len(k[0])
            for kk in k[1]:
                for ex_k_0 in k[0]:
                    if kk not in ex_k_0:
                        if difference > c_difference:
                            t1_.append(['0', kk])
                            c_difference += 1
                    else:
                        t1_.append([ex_k_0[0], ex_k_0[1]])
            temp_final.append(t1_)
            t1_ = []
            c_difference = 0
        else:
            temp_final.append(k[0])

    tmp_ref_count_arr = []
    final_ref_count_arr = []
    plt_color_set = []
    color_counter = 0

    for ex_tmp_final in temp_final:
        for ex_tmp_inner_val in ex_tmp_final:
            tmp_ref_count_arr.append(ex_tmp_inner_val[0])
        final_ref_count_arr.append(tmp_ref_count_arr)
        #plt_color_set.append("rgba(67,67,"+str(67 + color_counter * 2)+"," + str(color_counter + 60 * 0.2) + ")")
        plt_color_set.append("red")

        tmp_ref_count_arr = []
        color_counter += 1

    print(_time_series)
    print(final_ref_count_arr)

    #print(all_country)
    #print(_time_series)
    #print(plt_color_set)

    #plt_color_set = ["#fae583", "#31471c", "#f26544", "#7b7b7b", "#7f2221", "#7e816e", "#9c9c9c", "#ff4500", "#CD5C5C"]
    #fp.plot(_time_series, final_ref_count_arr, plt_color_set, all_country, all_country___, 7, len(all_country), "Refugee Flow destination country")

    #print(single_time_series)
    #print(final_ref_count_arr)
    #print(all_count
    data_string__  = ""




    with open("D3-data-file-refugee-1.csv", "w")as fw:
        data_string__ += "iteration" + "\t"
        for extract_country_plt in all_country:
            data_string__ += extract_country_plt + ","
        fw.writelines(data_string__)
        fw.writelines("\n")
        hold_data = []
        tmp_hold_data = []
        count__ = 0

        for da in date__:
            for t in final_ref_count_arr:
                tmp_hold_data.append(t[count__])
            count__ += 1
            hold_data.append(tmp_hold_data)
            tmp_hold_data = []
            if count__ == 5:
                ""
            #count__ = 0

        array_index = 0
        hold_data_1 = []
        tmp_hold_data = ""
        date_flag = 0
        data_date_str__ = ""
        fw.close()

    with open("D3-data-file-refugee-1.csv", "a")as fw1:
        for k in hold_data:
            for ex_int in k:
                if date_flag == 0:
                    data_date_str__ = date__[array_index][0] + "\t" + ex_int + "\t"
                    #data_date_str__ = data_date_str__ + "\t" +ex_int + "\t"
                    date_flag = 1
                else:
                    data_date_str__ += ex_int + "\t"

            date_flag = 0
            fw1.writelines(data_date_str__)
            fw1.writelines("\n")
            array_index += 1
            data_date_str__ = ""
            #data_date_str__ = 0
        fw1.close()

def RepresentsInt(s):
    return re.match(r"[-+]?\d+$", s) is not None
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


#crawl()
#gd.gdeltDownloader()
data_analysis()
#fp.plot()