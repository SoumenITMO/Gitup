__author__ = 'SOUMEN'
import csv
import os

class process_Cameocode:

    def cameo(cls, cameo_data, coordinate_data):  #NOTE : 0 -> EventCode, 1-> EventBaseCode, 2-> EventRootCode

        skip_first_line = 0
        cameo_file = "CAMEO_DataFiles\\CAMEO.eventcodes.txt"
        event_information = []
        cameo_data_text = []
        old_event_data = 0

        for extract_cameo_data in cameo_data:
            with open(cameo_file) as f:
                for line in f:
                    skip_first_line += 1
                    if skip_first_line > 1:
                        if extract_cameo_data == line.split("\t")[0]:
                            # cameo_data_code = line.split("\t")[0]
                            cameo_data_text.append([line.split("\t")[1]])
                            break

                event_information.append([coordinate_data[6],
                                          coordinate_data[7],
                                          coordinate_data[8],
                                          cameo_data[0], cameo_data[2],
                                          cameo_data[3],
                                          cameo_data[4],
                                          cameo_data[5],
                                          cls.get_Colorcode(cameo_data[2], cameo_data[1]),
                                          cameo_data_text,
                                          coordinate_data[0],
                                          coordinate_data[1],
                                          coordinate_data[2],
                                          coordinate_data[3],
                                          coordinate_data[4],
                                          coordinate_data[5],
                                          coordinate_data[9],
                                          coordinate_data[10],
                                          coordinate_data[11],
                                          coordinate_data[12],
                                          coordinate_data[13]])
        cameo_data_text = []
        return event_information
    def analysis(cls, data):
        cameo_file = "CAMEO_DataFiles\\CAMEO.eventcodes.txt"

        event_count = []
        event_calculation = []
        Urls = []
        temp = []

        c = 0
        c0 = 0
        try:
            for extract_data in data:
                for cameo_code in data:
                    if cameo_code[4] == extract_data[4]:
                        if extract_data[16] not in Urls:
                            Urls.append(extract_data[16])
                        c+=1
                    if cameo_code[3] == extract_data[3]:
                        if extract_data[16] not in Urls:
                            Urls.append(extract_data[16])
                        c0+=1
                temp = [extract_data[8],
                        extract_data[4],
                        c,
                        cls.cameo_text_generator(extract_data[4]),
                        extract_data[3],
                        cls.cameo_text_generator(extract_data[3]),
                        c0,
                        extract_data[17],
                        extract_data[18],
                        Urls]
                c = 0
                c0 = 0
                Urls = []

                if temp not in  event_count:
                    event_count.append(temp)
            return event_count
        except IndexError:
            ""
    def cameo_text_generator(cls, cameo_code):
        skip_first_line_ = 0
        with open("CAMEO_DataFiles\\CAMEO.eventcodes.txt","r") as rcameo:
                    for k in rcameo.readlines():
                        if skip_first_line_ > 1:
                            if k != "":
                                if cameo_code == k.split("\t")[0]:
                                    return k.split("\t")[1]
                        skip_first_line_ += 1
        cls.skip_first_line = 0
    def country_lookup(cls, fips_country_code):
        cameo_country_lookupfile = "FIPS_Code\\FIPS.country.txt"
        country_name = ""
        with open(cameo_country_lookupfile, "r") as cfips:
            data = cfips.readlines()
            for fips_data_code in data:
                if fips_country_code == fips_data_code.split("\t")[0]:
                    country_name = fips_data_code.split("\t")[1]
                    country_name = country_name.split("\n")[0]
                    break
        return country_name
    def build_d3_data_file(cls, data, data_origin, data_destination):
        counter = 0
        tmp_result_analysis = []
        main_d3_analysis = []
        final_origin_data = []
        final_destination_data = []

        """
        for hh in data:
            for hh1 in data:
                if hh == hh1:
                    counter+=1
            tmp_result_analysis.append([counter, hh])
            counter = 0
        for extract_dat in tmp_result_analysis:
            if extract_dat not in main_d3_analysis:
                main_d3_analysis.append(extract_dat)
        """



        counter = 0

        for extract_data_origin in data_origin:

            if [extract_data_origin[0],extract_data_origin[1], extract_data_origin[2], extract_data_origin[3],
                extract_data_origin[4]]  not in final_origin_data:
                final_origin_data.append([extract_data_origin[0], extract_data_origin[1], extract_data_origin[2],
                           extract_data_origin[3], extract_data_origin[4]])

            if counter >= 30:
                break
            counter += 1

        for extract_data_destination in data_destination:
            if [extract_data_destination[0],extract_data_destination[1], extract_data_destination[2],
                extract_data_destination[3], extract_data_destination[4]]  not in final_destination_data:

                final_destination_data.append([extract_data_destination[0], extract_data_destination[1],
                                               extract_data_destination[2], extract_data_destination[3],
                                               extract_data_destination[4]])
            if counter >= 30:
                break
            counter += 1



        with open("CSV_OUTPUT\\lll.csv", "w") as ccsv:
            CSV_fieldnames = ["Code", "Lat", "Lon", "region1", "region2"]
            writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
            writer.writeheader()

            for extract_data_origin in final_origin_data:

                writer.writerow({
                                         "Code":extract_data_origin[0],
                                         "Lat" :extract_data_origin[1],
                                         "Lon":extract_data_origin[2],
                                         "region1":extract_data_origin[3],
                                         "region2":extract_data_origin[4],
                                })

            for extract_data_destination in final_destination_data:
                writer.writerow({
                                         "Code":extract_data_destination[0],
                                         "Lat" :extract_data_destination[1],
                                         "Lon":extract_data_destination[2],
                                         "region1":extract_data_destination[3],
                                         "region2":extract_data_destination[4],
                                })

        return  0
    def get_Colorcode(cls, event_root_code, event_base_code):
        cameo_colourcode_lookupfile = "CAMEO_DataFiles\\CAMEO.eventcolor_code.txt"
        color_code = ""
        skipline = 0
        with open(cameo_colourcode_lookupfile, "r") as cfips:
            data = cfips.readlines()
            base_color_code_number = int(event_base_code[0]) + int(event_base_code[1]) + int(event_base_code[2])
            for fips_data_code in data:
                if skipline == 1:
                    data = fips_data_code.split("#")
                    if str(data[0]) == event_root_code:
                        code_hex = data[1].replace('\n','')
                        code_hex = "0x"+code_hex
                        hh = str(hex(int(code_hex, 16) + base_color_code_number)[2:]) # 0xcd4
                        # print(base_color_code_number)
                        return [data[1], hh]
                skipline = 1
    def buildCounterTable(cls, point, table_data, fcount, fname):

        hold_tmp_event_data = []
        other_data = []
        other_data_tmp = []
        counter = 0
        mergefinaldata = []
        savemaindata = []
        save_cameocode = []

        if table_data != []:

            for table_data_Ex in table_data:
                hold_tmp_event_data.append(table_data_Ex[4][1])

            for kk in hold_tmp_event_data:
                for kk1 in hold_tmp_event_data:
                    if point == 0:                    # GET ONLY MIDPOINT
                        if kk[2] == kk1[2]:
                            if kk[0] not in other_data_tmp:
                                other_data_tmp.append(kk[0])
                            counter += 1
                    if point == 1:                    # GET ONLY FINALPOINT
                        if kk[3] == kk1[3]:
                            if kk[0] not in other_data_tmp:
                                other_data_tmp.append(kk[0])
                            counter += 1
                if other_data_tmp != [] and point == 0:
                    other_data.append([counter, kk[2], other_data_tmp[0]])
                if other_data_tmp != [] and point == 1:
                    other_data.append([counter, kk[3], other_data_tmp[0]])
                other_data_tmp = []
                counter = 0
            other_data_tmp = []
            country_data = []
            counter = 0
            event_arr = []

            for ex_other_data in other_data:
                for ex_other_data_ in other_data:
                    if ex_other_data_[1] == ex_other_data[1]:
                        if ex_other_data_[1] not in country_data:
                            country_data.append(ex_other_data_[1])
                            country_data.append(ex_other_data_[0])
                        if ex_other_data[2] not in event_arr:
                            event_arr.append(ex_other_data[2])
                        counter += 1
                other_data_tmp.append([country_data, event_arr])
                country_data = []
                event_arr = []
                counter = 0

            for extract_main_data in other_data_tmp:
                mergefinaldata.append([extract_main_data[0][0], extract_main_data[0][1],
                      cls.cameo_text_generator(extract_main_data[1][0]).replace("\n", "").replace(",", " ")])
            for data in mergefinaldata:
                for internaldata in mergefinaldata:
                    if data[0] == internaldata[0]:
                        save_cameocode.append(internaldata[2])
                if [data[0], data[1], save_cameocode] not in savemaindata:
                    savemaindata.append([data[0], data[1], save_cameocode])
                save_cameocode = []

            first_header = ""
            second_header = ""
            line_index = 0
            merge_cameo_text = ""

            array_lengths = []
            i = 0
            j = 0
            lock = 0
            ex_str = ""
            main_header_flag = 0
            counter_data = ""
            holdprevdata = ""

            for extract_final_data in savemaindata:
                first_header += str(extract_final_data[0])+"\t,"+str(extract_final_data[1]) + "\t,"
                counter_data += str(extract_final_data[0])+","+str(extract_final_data[1]) + "\n"
            first_header += "\n"

            if not os.path.exists("final-counter-data7.csv"):
                with open("final-counter-data7.csv", "w")as outf:

                    outf.writelines(table_data[1][1]+"\n")
                    outf.writelines(counter_data)
            else:
                with open("final-counter-data7.csv", "a")as inf:
                    inf.writelines(table_data[1][1]+"\n")
                    inf.writelines(counter_data)
                    inf.close()

                    """
                    index = 0
                    holdprevdata = inf.readlines()

                    print(savemaindata[0][0], savemaindata[0][1])

                    for extract_prevdata in holdprevdata:
                        if index > 0:
                            dataprev = extract_prevdata.replace("\n", "")
                            print(dataprev)
                        index += 1
                    #os.remove("counter-data.csv")
                    #os.rename("counter-data-1.csv", "counter-data.csv")
                    """

            cameo_file_name = "Cameo-Details"
            if point == 0:
                cameo_file_name = cameo_file_name+"-Midpoint"+".csv"
            else:
                cameo_file_name = cameo_file_name+"-Finalpoint"+".csv"


            if not os.path.exists(cameo_file_name):
                with open(cameo_file_name, "w") as rdata:
                    rdata.writelines("\t,\t,\t,\t,\t," + table_data[0][1]+",\n")
                    rdata.writelines("\n\n")
                    rdata.writelines(first_header)
                    for extract_final_data in savemaindata:
                        array_lengths.append(len(extract_final_data[2]))
                    while max(array_lengths) > i:
                        for extract_final_data in savemaindata:
                            try:
                                ex_str += extract_final_data[2][i]+",,"
                            except:
                                ex_str += ",,"
                        rdata.writelines(ex_str + "\n")
                        i += 1
                        lock += 1
                        ex_str = ""
                    rdata.writelines("\n\n")
                    rdata.close()
                rdata.close()

            else:
                with open(cameo_file_name, "a") as rdata:
                    rdata.writelines("\t,\t,\t,\t,\t," + table_data[0][1]+",\n")
                    rdata.writelines(first_header)
                    for extract_final_data in savemaindata:
                        array_lengths.append(len(extract_final_data[2]))
                    while max(array_lengths) > i:
                        for extract_final_data in savemaindata:
                            try:
                                ex_str += extract_final_data[2][i]+",,"
                            except:
                                ex_str += ",,"
                        rdata.writelines(ex_str + "\n")
                        i += 1
                        lock += 1
                        ex_str = ""
                    rdata.writelines("\n\n")
                    rdata.close()
                rdata.close()



