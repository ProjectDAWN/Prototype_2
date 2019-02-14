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
# This program aims to control the module ATM of the box according to climate
# recipes. All the threshold are defined in climate_recipe.py and this code
# only control the automation between sensors, actuators and climate recipes.
#
# Sensors : Temperature, humidity (same probe)
#
# Actuactors : waterproof ventilator, mistmaker, electrical warmer
#
##################### Importation section   #################################
import sys
import Raspberry_Interface
import datetime
import pickle
from climate_recipe.Climate_recipe import Climate_recipe
import time
from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
from Raspberry_Interface.sensor_classes import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization
chanel_file = "Files/Actuators.csv"
realMode = False
variety = "tomato"
InOutMode = "GPIO"
date_file = open("Files/date_ini",'rb')
depickler = pickle.Unpickler(date_file)
date_ini = depickler.load()
actuators = GPIO_Actuators.GPIO_Actuators(chanel_file,InOutMode,realMode)
sensors = GPIO_Sensors.GPIO_Sensors(InOutMode,realMode)
climate_recipe = Climate_recipe(variety)

def atmospheric_loop(hour,day,climate_recipe):
    """maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = sensors.read("temperature")
    if temperature < climate_recipe.threshold_temp(hour, day)-1 : #too cold
        actuators.activate("ATM_Warmer")
    if temperature > climate_recipe.threshold_temp(hour, day)+1:  #too warm
        actuators.desactivate("ATM_Warmer")

    #humidity
    humidity = sensors.read("humidity")
    humidity_threshold = climate_recipe.thresholdd_humidity(date_current.hour,date_current.day)
    if humidity < humidity_threshold*(1-0.005):
        # humidity is too low
        actuators.activate("ATM_MistMaker", "ATM_Ventilator")
    if humidity > humidity_threshold*(1+0.005) : # humidity is too high
        actuators.desactivate("ATM_MistMaker")


####### End of growth

def end_loop():
    """put all the actuators chanels at LOW value"""
    actuators.desactivate("ATM_Ventilator",
                    "ATM_MistMaker",
                    "ATM_Warmer")

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
atmospheric_loop(date_current.hour,diff.days,climate_recipe)
time.sleep(10)
end_loop()
