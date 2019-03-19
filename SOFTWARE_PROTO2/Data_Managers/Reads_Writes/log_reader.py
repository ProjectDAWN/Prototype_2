import datetime
import re
import sys
import matplotlib
import matplotlib.pyplot as plt
log_file = sys.path[0]+ "/../../Files/logs/prints.txt"
format = '%Y-%m-%d %H:%M:%S.%f'
file = open(log_file,'r')
sensors = ["pH","conductivity","water_level","water_temperature","temperature","humidity"]
X_dict = dict(zip(sensors,[[]]*len(sensors)))
Y_dict = dict(zip(sensors,[[]]*len(sensors)))
for line in file.readlines():
    line = line.strip()
    if re.search(r"^2019-",line):
        date = datetime.datetime.strptime(line, format)
    else:
        list = line.split(' ')
        if list[0] in sensors:
            X_dict[list[0]].append(date)
            Y_dict[list[0]].append(list[1])
for sensor in sensors:
    figure = plt.figure()
    axes = plt.axes()
    dates = matplotlib.dates.date2num(X_dict[sensor])
    print(X_dict[sensor])
    plt.plot(dates,Y_dict[sensor])
    axes.set(xlabel ="time")
    plt.savefig(sensor+".pdf")
