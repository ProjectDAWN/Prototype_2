#  Python 3.6
#  main_ATM.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
#
###############################################################################
#
#                       MAIN PROGRAM
#
###############################################################################
#
# This program collect all the data from the sensors print everything in a csv file
# any processing. All the time intervals are defined in ...
#
#
##################### Importation section   #################################
import sys
import datetime
import time


path = sys.path[0]+"/.."
sys.path.append(path)


from Raspberry_Interface import *
from config import growth_config, log_config
from Data_Managers.Reads_Writes import CSV_writer

######################## Module loop #######################################

sys.stdout = log_config.print_log_file
print("DATA module")
###Variable initialization

actuators = growth_config.actuators()
sensors = growth_config.sensors()
date_ini = growth_config.date_ini()


def data_loop():

    data_df = CSV_writer.CSV_writer()
    count = 0
    while count < 5:
        date_current = datetime.datetime.now()
        day = date_current.strftime("%Y-%m-%d")
        hour = date_current.strftime("%H-%M-%S")
        for sensor in sensors.class_dict.keys():
            value = sensors.read(sensor)
            id = sensors.get_id(sensor)
            module = sensors.get_module(sensor)
            value_column = sensor
            data_df.add({"day": day,
                         "hour": hour,
                         "id": id,
                         "module": module,
                         value_column: value})

        print("writing data")
        data_df.write("../Datas/ex.csv", 'a')
        data_df.clear_df()
        count = count+1
        time.sleep(1)


data_loop()
