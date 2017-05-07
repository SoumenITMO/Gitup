__author__ = 'Soumen'

import matplotlib.pyplot as plt
import numpy as np

def assignIDs(list):
    '''Take a list of strings, and for each unique value assign a number.
    Returns a map for "unique-val"->id.
    '''
    sortedList = sorted(list)

    #taken from
    #http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order/480227#480227
    seen = set()
    seen_add = seen.add
    uniqueList =  [ x for x in sortedList if x not in seen and not seen_add(x)]

    return  dict(zip(uniqueList,range(len(uniqueList))))

def plotData(inData,color):
    x,y = zip(*inData)

    xMap = assignIDs(x)
    xAsInts = np.array([xMap[i] for i in x])

    pearR = np.corrcoef(xAsInts,y)[1,0]
    # least squares from:
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
    A = np.vstack([xAsInts,np.ones(len(xAsInts))]).T
    m,c = np.linalg.lstsq(A,np.array(y))[0]

    plt.scatter(xAsInts,y,label='Data '+color,color=color)
    plt.plot(xAsInts,xAsInts*m+c,color=color,
             label="Fit %6s, r = %6.2e"%(color,pearR))
    plt.xticks(xMap.values(),xMap.keys())
    plt.legend(loc=3)


x_dat = []
y_dat = []
y_dat_1 = []

counter = 0

with open("D3-data-file-refugee-1.csv") as csvfile:
    reader = csvfile.readlines()
    skipline = 0
    for row in reader:

        if skipline >= 1 and skipline < 20:
            x_dat.append(row.split("\t")[0])
            y_dat.append([row.split("\t")[0], int(row.split("\t")[8])])  # FOR RUSSIA
            counter += 1

        if skipline > 14 and skipline < 42:
            x_dat.append(row.split("\t")[0])
            y_dat_1.append([row.split("\t")[0], int(row.split("\t")[8])])  # FOR RUSSIA
            counter += 1

        skipline += 1


DATA = [['a', 47], ['b', 55], ['c', 5], ['d', 42], ['e', 21], ['f', 5]]

DATA2 = [['a', 323], ['b', 442], ['c', 411], ['d', 342], ['e', 11], ['f', 4], ['a', 524], ['b', 712], ['c', 74],
         ['d', 6], ['e', 4], ['f', 7]]

plotData(y_dat, 'blue')
plotData(y_dat_1, 'red')
plt.show()
#plt.gcf().savefig("correlation.png")