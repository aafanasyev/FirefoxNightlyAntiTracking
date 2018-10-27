#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Andrey Afanasyev"
__copyright__ = "Copyright 2018, FirefoxNightlyAntiTracking"
__license__ = "MIT"
__version__ = "0.0.2"
__email__ = "aafanasyev@os3.nl"
__status__ = "Prototype"

import os
import csv
import matplotlib as mpl
# to work around $DISPLAY error in terminal moder
#mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.ticker as tck
from matplotlib.ticker import FormatStrFormatter
import numpy as np

path_csv = 'results.csv'

x_axis_values = []
y_axis = []
csv_data =[]

with open(path_csv, 'r', encoding='utf-8') as results:
    reader = csv.reader(results, delimiter = ',')
    for row in enumerate(reader):
        if row[0] == 0:
            x_label = str(row[1][1])
            g_label = str(row[1][3])
            y_label = str(row[1][5])
        else:
            csv_data.append((row[1][1], row[1][3], row[1][5]))
print ("Group of usecases by x axis: {}".format(g_label))
print ("Browser versions by x axis: {}".format(x_label))
print ("Amount of cookies by y axis: {}".format(y_label))
#print (csv_data)

# separate group and sort items from first column (group label)
# ['TP', 'TP and CB', 'no TP']
usecases = list(sorted(set([rows[0] for rows in csv_data])))
# ['60.2.2', '62.0.3', '64.0a1']
browsers = list(sorted(set([rows[1] for rows in csv_data])))


#[[],[],[]] 
# data []
# data[usecases] = [[],[],[]]
# data[usecases [browsers]] = [[[],[],[]], [[],[],[]], [[],[],[]]]
data = [[[] for count in range(len(browsers))] for count in range(len(usecases))]

for rows in csv_data:
    data[usecases.index(rows[0])][browsers.index(rows[1])].append(int(rows[2]))


def set_box_color(bp, color, mediancolor):    
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['medians'], color=mediancolor)
    plt.setp(bp['fliers'], color=color)
    plt.setp(bp['means'], color=color)

plt.figure()

#using http://colorbrewer2.org

esr = [x[0] for x in data]
print(esr)
release = [x[1] for x in data]
print(release)
nightly = [x[2] for x in data]
print(nightly)


bp_0=plt.boxplot(esr, positions=[x*3 for x in range(len(esr))], sym='', widths=0.6)
set_box_color(bp_0, '#4daf4a', '#000000')

bp_1=plt.boxplot(release, positions=[x*3+1 for x in range(len(release))], sym='', widths=0.6)
set_box_color(bp_1, '#377eb8', '#000000')

bp_2=plt.boxplot(nightly, positions=[x*3+2 for x in range(len(nightly))], sym='', widths=0.6)
set_box_color(bp_2, '#e41a1c', '#000000')

#for group in data:
#    position=[x+3*int(data.index(group)) for x in range(len(group))]
#    plt.figure()
#    plt.boxplot(group, positions=position, sym='', widths=0.6)

# grid configuration and axes
#f = lambda x,pos: str(x).rstrip('0').rstrip('.')
plt.gca().yaxis.grid(color='b', linestyle='--', linewidth=1, alpha=0.1)
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(20))

#plt.errorbar([i+1 for i,e in enumerate(data)], np.mean(data, axis=0), yerr=np.std(data, axis=0), color='green', linestyle='-', linewidth=1, alpha=0.50)
plt.title('Effectiveness of Mozilla Firefox browsers anti-tracking approaches.\n Reserved page loading and pause between browsers sessions is 15 seconds \n Each page in each browser session was visited 100 times', 
            fontsize=10, fontweight='bold')

plt.plot([], c='#4daf4a', label='ESR 60.2.2')
plt.plot([], c='#377eb8', label='Release 62.0.3')
plt.plot([], c='#e41a1c', label='Nightly 64.0a1')
plt.legend()


print(usecases)

print(tuple([x+3 for x in range(len(usecases))]))

plt.xlabel(x_label, fontweight='bold')
plt.ylabel(y_label, fontweight='bold')

plt.xticks((1, 4, 7), usecases)
plt.xlim(-1, len(usecases)*4)

plt.savefig(str('results.png'), format='png', dpi=300)
plt.show()



