from bokeh.plotting import figure, show, output_notebook
from bokeh.models import Legend
from pykalman import KalmanFilter
import numpy as np
from scipy import stats
import statistics

x_dat = []
x_dat_1 = []
y_dat = []
y_dat_1 = []

tmp_kal_val__ = []
counter = 0
kalman_data__ = []

index_number = 2
country_type = "destinatnion"

"""
date__3 = ["15-Jan FO", "15-Feb F", "15-Feb S", "15-Feb T", "15-Feb FO", "15-Mar F",
           "15-Mar S", "15-Mar T", "15-Mar FO", "15-Apr F", "15-Apr S", "15-Apr T",
           "15-Apr FO", "15-May F", "15-May S", "15-May T", "15-May FO", "15-Jun F",
           "15-Jun S", "15-Jun T", "15-Jun FO", "15-Jul F", "15-Jul S", "15-Jul T",
           "15-Jul FO", "15-Aug F", "15-Aug S", "15-Aug T", "15-Aug FO", "15-Sep F",
           "15-Sep S", "15-Sep T", "15-Sep FO", "15-Oct F", "15-Oct S", "15-Oct T",
           "15-Oct FO", "15-Nov F", "15-Nov S", "15-Nov T", "15-Nov FO", "15-Dec F",
           "15-Dec S"]
"""
date__2 = ["14-Jan FO", "14-Feb F", "14-Feb S", "14-Feb T", "14-Feb FO",
          "14-Mar F", "14-Mar S", "14-Mar T", "14-Mar FO",
          "14-Apr F", "14-Apr S", "14-Apr T", "14-Apr FO",
          "14-May F", "14-May S", "14-May T", "14-May FO",
          "14-Jun F", "14-Jun S", "14-Jun T", "14-Jun FO",
          "14-Jul F", "14-Jul S", "14-Jul T", "14-Jul FO",
          "14-Aug F", "14-Aug S", "14-Aug T", "14-Aug FO",
          "14-Sep F", "14-Sep S", "14-Sep T", "14-Sep FO",
          "14-Oct F", "14-Oct S", "14-Oct T", "14-Oct FO",
          "14-Nov F", "14-Nov S", "14-Nov T", "14-Nov FO",
          "14-Dec F", "14-Dec S"]


"""
date__3 = ["15-Feb", "1", "2", "3", "15-Mar", "4", "5", "6", "15-Apr", "7", "8", "9", "15-May",
           "10", "11", "12", "15-Jun", "13", "14", "15", "15-Jul", "16", "17", "18", "15-Aug",
           "19", "20", "21", "15-Sep", "22", "23", "24", "15-Oct", "25", "26", "27", "15-Nov", "28", "29", "30",
           "15-Dec", "31", "32", "33"]


date__3 = ["15-Feb F", "", "", "", "15-Mar F", " ", " ", " ", "15-Apr F", " ", " ", "", "15-May F", "", "", "",
           "15-Jun F", "", "", "", "15-Jul F", "", "", "", "15-Aug F", "", "", "", "15-Sep F", "", "", "",
           "15-Oct F", "", "", "", "15-Nov F", "", "", "", "15-Dec F", ""]
"""

date__3 = ["14-Feb F", "", "", "", "14-Mar F", " ", " ", " ", "14-Apr F", " ", " ", "", "14-May F", "", "", "",
           "14-Jun F", "", "", "", "14-Jul F", "", "", "", "14-Aug F", "", "", "", "14-Sep F", "", "", "",
           "14-Oct F", "", "", "", "14-Nov F", "", "", "", "14-Dec F", ""]

#date__3 = ["15-Feb", "1", "2", "15-May"] #,
           #"g", "g", "g", "15-Jun", "g", "g", "g", "15-Jul", "g", "g", "g", "15-Aug", "g", "g", "g", "15-Sep",
           #"g", "g", "g", "15-Oct", "g", "g", "g", "15-Nov", "g", "g", "g", "15-Dec", "g", ""]


t_s__  = []

def analysis_Kalman(countries_num, type):

    with open("D3-data-file-refugee-1.csv") as csvfile:
        reader = csvfile.readlines()
        skipline = 0
        line_ = 0
        country_name = ""
        date_limit = 0
        c = 0
        delta = 1e-5
        trans_cov = delta / (1 - delta) * np.eye(2)

        for row in reader:
            if skipline > 1:
                if date_limit < 20:
                    ""
                x_dat.append(row.split("\t")[0])
                t_s__.append(c)
                tmp_kal_val__.append(int(row.split("\t")[index_number]))
                y_dat.append(int(row.split("\t")[index_number]))
                c += 1

                """
                if date_limit > 20 and date_limit <= 40:
                    x_dat_1.append(row.split("\t")[0])
                    tmp_kal_val__.append(int(row.split("\t")[index_number]))
                    y_dat_1.append(int(row.split("\t")[index_number]))
                """
            else:
                try:
                    country_name = row.split("\t")[1].split(",")[index_number - 1]
                except:
                    ""
            skipline += 1
            date_limit += 1

    kf = KalmanFilter(transition_matrices=[1],
                      observation_matrices=[1],
                      initial_state_mean=y_dat[0],
                      initial_state_covariance=1,
                      observation_covariance=1,
                      random_state=0)

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    times = range(y_dat[index_number])
    p = figure(plot_width=1000, toolbar_location="right", y_axis_label = "Refuges",
              x_axis_label = "Weekly")

    #state_means, _ = kf.em(np.asarray(y_dat)).smooth(np.asarray(y_dat)) #.filter(y_dat)
    #state_means = state_means.flatten()

    state_means1, _ = kf.filter(np.asarray(y_dat))
    state_means1 = state_means1.flatten()

    #MSE = stats.linregress(t_s__, state_means)
    #MSE1 = stats.linregress(t_s__, state_means1)
    #print(MSE, MSE1)
    #print(state_means)
    #np.savetxt("trained_dataset_Syria_15.txt", state_means, delimiter=',')
    #print(len(x_dat), len(state_means))


    data_1 = []
    data_2 = []
    tmp_cov = []
    tmp_cov_1 = []


    with open("trained_dataset_Syria_15.txt")as train_data:
        data__ex = train_data.readlines()
        for j in data__ex:
            tmp_cov.append(j)

    with open("trained_dataset_Syria_14.txt")as train_data:
        data__ex = train_data.readlines()
        for j in data__ex:
            tmp_cov_1.append(j)

    index_ = 0
    for kk in tmp_cov:
        data_1.append(kk)
        data_2.append(tmp_cov_1[index_])
        index_ += 1

    #slope, intercept, rvalue, pvalue, stderr = stats.linregress(np.array(data_1).astype(np.float), np.array(data_2).astype(np.float))
    #print (stderr)

    p = figure(x_range = x_dat, plot_width=1000, toolbar_location="right",y_axis_label = "Refuges moving through "+country_type +" country("+ country_name +")",
              x_axis_label = "Weeks")
    #p.line(x_dat, state_means, line_width=1, line_color = 'blue', legend="Kalman filter 0")
    p.line(x_dat, y_dat, line_width=1, line_color = 'green', legend="Refuge from Syria to destination country ")
    p.line(x_dat, state_means1, line_width=1, line_color = 'red', legend="Kalman filter 1")
    #slope, intercept, rvalue, pvalue, stderr = stats.linregress(np.array(y_dat).astype(np.float), np.array(state_means1).astype(np.float))
    slope, intercept, rvalue, pvalue, stderr = stats.linregress(t_s__, np.array(state_means1).astype(np.float))

    print(stderr)
    print statistics.pvariance(state_means1)
    #show(p)

    """
    state_means,_ = kf.filter(y_dat_1)
    state_means = state_means.flatten()
    p1 = figure(x_range = x_dat_1, plot_width=1000, toolbar_location="right",y_axis_label = "Refuges moving through "+country_type +" country("+ country_name +")",
              x_axis_label = "Weeks")
    p1.line(x_dat_1, state_means, line_width=1, line_color = 'blue', legend="Kalman filter 1")
    p1.line(x_dat_1, y_dat_1, line_width=1, line_color = 'green', legend="Refuge from Syria to destination cdqwdountry ")
    show(p1)
    """


analysis_Kalman(index_number, country_type)

while(index_number == 1):
    analysis_Kalman(index_number, country_type)
    x_dat = []
    y_dat = []
    tmp_kal_val__ = []
    counter = 0
    kalman_data__ = []
    c = 0
    index_number -= 1

