__author__ = 'Soumen'
import  csv
store_Data = []

with open("test11.csv", "r")as fp:

    datas__ = fp.readlines()
    c = 0
    for extract_data in datas__:
        if c >= 3:
            print(extract_data.split(",")[7], c)
        c += 1


        """
        if extract_data != "" and extract_data != []:
            store_Data.append(extract_data.split(","))
        """
"""
for extract_spl_data in store_Data:
    if extract_spl_data != "":
        for filter_out in extract_spl_data:
            if filter_out != "" and filter_out != "\n":
                print(filter_out)
"""