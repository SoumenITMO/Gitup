__author__ = 'SOUMEN'
import csv

class process_Cameocode:
    skip_first_line = 0
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
        with open("CAMEO_DataFiles\\CAMEO.eventcodes.txt","r") as rcameo:
                    for k in rcameo.readlines():
                        if cls.skip_first_line > 1:
                            if k != "":
                                if cameo_code == k.split("\t")[0]:
                                    return k.split("\t")[1]
                        cls.skip_first_line += 1
        cls.skip_first_line = 0
    def country_lookup(cls, fips_country_code):
        cameo_country_lookupfile = "FIPS_Code\\FIPS.country.txt"
        country_name = ""
        with open(cameo_country_lookupfile, "r") as cfips:
            data = cfips.readlines()
            for fips_data_code in data:
                if fips_country_code == fips_data_code.split("\t")[0]:
                    country_name = fips_data_code.split("\t")[1]
                    break;
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
