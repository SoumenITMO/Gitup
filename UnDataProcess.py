__author__ = 'Soumen'

import os
import zipfile as z
import  csv

def CompareUNdata():

    skipline = 0
    push_UN_data = []
    sum =0
    arr = []
    final_output_array = []
    year = "2013"
    fname = "UN ANALYSIS"

    with open("UN_Data\\UNdata_Export_20161220_181205327.csv", "rb") as undata:
        data = undata.readlines()
        for g in data:
            if skipline >= 5:
                data = g.replace("\n","")
                data = data.replace('"',"")
                data = data.split(",")
                push_UN_data.append([data[0], data[1], data[3]])
                #print(push_UN_data)
            skipline += 1

    push_UN_data_cus = ['Bulgaria','Ukraine','United States','Jordan','Russian Federation', 'Kazakhstan']
    count = 0

    for getUNdata in push_UN_data_cus:
        #comp_country = getUNdata[0]
        #comp_country = push_UN_data[count]
        for getUNdata_ in push_UN_data:
            #print(getUNdata)
            if getUNdata_[0] == getUNdata:
                sum += int(getUNdata_[2])
        arr.append([getUNdata, sum])
        sum = 0
        count+=1

    #print(arr)
    #arr = []

    for extract_arr in arr:
            dirs = os.listdir("Gdelt_Files__\\year-"+year)
            counter = 0
            for fetch_files in dirs:
                with z.ZipFile("Gdelt_Files__\\Year-"+year+"\\"+fetch_files, "r") as zf:
                            filename = list(zf.namelist())[0]
                            print(filename)
                            with zf.open(filename,"r") as fo:
                                datt = fo.readlines()
                                for row in datt:
                                    row = list(row.split("\t"))
                                    if "SYR" in row and "REF" in row and extract_arr[0] in row:
                                        if row[36] != "" and row[43] != "":
                                            print(row)
                                            counter += 1
            final_output_array.append([extract_arr[0], extract_arr[1], counter])
            counter = 0

    with open("CSV_OUTPUT\\Filter_Duplicate\\"+year+"-half-1-filter\\"+year+"-"+fname+"-UN-filter.csv", "w") as ccsv:
        CSV_fieldnames = ['UN Country', 'UN Count']
        writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
        writer.writeheader()
        for extract_final_arr in final_output_array:
            writer.writerow({
                                 "UN Country": extract_final_arr[0],
                                 "UN Count": extract_final_arr[1],
                                 #GDELT COUNT": extract_final_arr[2]
            })

    with open("CSV_OUTPUT\\Filter_Duplicate\\"+year+"-half-1-filter\\"+year+"-"+fname+"-GDELT-filter.csv", "w") as ccsv:
        CSV_fieldnames = ['UN Country', 'GDELT COUNT']
        writer = csv.DictWriter(ccsv, delimiter=",", lineterminator='\n', fieldnames=CSV_fieldnames)
        writer.writeheader()
        for extract_final_arr in final_output_array:
            writer.writerow({
                                 "UN Country": extract_final_arr[0],
                                 #"UN Count": extract_final_arr[1],
                                 "GDELT COUNT": extract_final_arr[2]
            })
