__author__ = 'SOUMEN'

from collections import Counter
from collections import OrderedDict
import csv

class process_Cameocode:

    def cameo(cls, cameo_data, coordinate_data):  #NOTE : 0 -> EventCode, 1-> EventBaseCode, 2-> EventRootCode

        skip_first_line = 0
        cameo_file = "CAMEO_DataFiles\\CAMEO.eventcodes.txt"
        event_information = []
        old_event_data = 0;
        for extract_cameo_data in cameo_data:
            with open(cameo_file) as f:
                for line in f:
                    skip_first_line += 1
                    if skip_first_line > 1:
                        if extract_cameo_data == line.split("\t")[0]:

                            cameo_data_code = line.split("\t")[0]
                            cameo_data_text = line.split("\t")[1]
                            break


                event_information.append([coordinate_data[6],
                                          coordinate_data[7],
                                          coordinate_data[8],
                                          cameo_data[0], cameo_data[2],
                                          cameo_data[3],
                                          cameo_data[4],
                                          cameo_data[5],
                                          cls.get_Colorcode(cameo_data[2]),
                                          cameo_data_text,
                                          coordinate_data[0],
                                          coordinate_data[1],
                                          coordinate_data[2],
                                          coordinate_data[3],
                                          coordinate_data[4],
                                          coordinate_data[5],
                                          coordinate_data[9],
                                          coordinate_data[10],
                                          coordinate_data[11]])


        return event_information
    skip_first_line = 0

    def analysis(cls, data):

        cameo_file = "CAMEO_DataFiles\\CAMEO.eventcodes.txt"
        event_count = []
        temp = []
        c = 0
        c0 = 0

        try:
            for extract_data in data:
                for cameo_code in data:
                    if cameo_code[4] == extract_data[4]:
                        c+=1
                    if cameo_code[3] == extract_data[3]:
                        c0+=1
                temp = [extract_data[4], c, cls.cameo_text_generator(extract_data[4]),
                        extract_data[3], cls.cameo_text_generator(extract_data[3]), c0]
                if temp not in  event_count:
                    event_count.append(temp)
                c = 0
                c0 = 0
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
    def get_Colorcode(cls, event_code):
        cameo_colourcode_lookupfile = "CAMEO_DataFiles\\CAMEO.eventcolor_code.txt"
        color_code = ""
        skipline = 0
        with open(cameo_colourcode_lookupfile, "r") as cfips:
            data = cfips.readlines()

            for fips_data_code in data:
                if skipline == 1:
                    data = fips_data_code.split("#")
                    if str(data[0]) == event_code:
                        return data[1]
                skipline = 1

