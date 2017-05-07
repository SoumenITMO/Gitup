__author__ = 'Soumen'

from plotly import graph_objs as go
import csv as cs
import plotly.plotly as py
from numpy import *

def plot_analysis_data():
    fname = "2"
    year = "2015"

    X_Data = []
    Y_Data = []

    """
    data_X = [20, 14, 23, 300]
    data_Y = ['giraffes', 'orangutans', 'monkeys', 'dog']

    data = [go.Bar(
            x=data_X,
            y=data_Y,
            orientation = 'h'
    )]
    py.plot(data, filename='horizontal-bar')
    """

    with open("CSV_OUTPUT\\Analysis\\FinalAnalysis\\final_analysis-"+fname+"-"+year+".csv", "rb") as csvfile:
        spamreader = csvfile.readlines()
        for row in spamreader:
           string_row = row.replace("\n","")
           string_row = string_row.split(",")
           X_Data.append(string_row[0])
           Y_Data.append(int(string_row[1]) / 100)

    data = [go.Bar(
            x=X_Data,
            y=Y_Data,
            orientation = 'h'
    )]
    py.plot(data, filename='horizontal-bar')
def generateFinalDataAnalysis():
    fname = "2"
    year = "2015"
    tmp = []
    skip_first = 0

    dat = []
    skip_first1 = 0

    with open("CSV_OUTPUT\\Analysis\\main__analysis-"+fname+"-"+year+".csv", "rb") as csvfile:
        spamreader = cs.reader(csvfile)
        for row in spamreader:
            k = list(row)
            if skip_first == 1:
                strr = k[2].replace("\r\n","")
                if strr not in tmp:
                    tmp.append(strr)
            skip_first = 1

    with open("CSV_OUTPUT\\Analysis\\main__analysis-"+fname+"-"+year+".csv", "rb") as csvfile:
        spamreader1 = cs.reader(csvfile)
        listdata = list(spamreader1)
        skip_first1 = 0
        aggregate_analysis = []
        sum = 0

        for extracttmp in tmp:
            for listdata_extract in listdata:
                if skip_first1 == 1:
                    string_stp = listdata_extract[2].replace("\r\n","")
                    if extracttmp == string_stp:
                       sum += int(listdata_extract[3])
                skip_first1 = 1
            aggregate_analysis.append([extracttmp, sum])
            sum = 0
    with open("CSV_OUTPUT\\Analysis\\FinalAnalysis\\final_analysis-"+fname+"-"+year+".csv", "wb") as csvfile:
        csvfile.writelines(str("name,value")+"\n")
        for extract_analysis_data in aggregate_analysis:
            str_write = extract_analysis_data[0]+","+str(extract_analysis_data[1])
            csvfile.writelines(str_write+"\n")
            str_write =""
        csvfile.close()
