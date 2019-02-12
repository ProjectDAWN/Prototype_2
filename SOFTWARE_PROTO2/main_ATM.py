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
from climate_recipe.Climate_recipe import Climate_recipe
import time
from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
from Raspberry_Interface.sensor_classes import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization
pin_file = "Files/Actuators.csv"
realMode = False
variety = "tomato"
necessry_time=0
size_x_bac=0
size_y_bac=0

pH_I2C_address = 0
EC_I2C_address = 0

InOut = GPIO_Actuators.GPIO_Actuators(pin_file,realMode)
climate_recipe = Climate_recipe(variety)

def atmospheric_loop(date_current,climate_recipe):
    """maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = 12#AM2315.read_temperature()
    if temperature < climate_recipe.threshold_temp_min(date_current)-1 and not InOut.input(ATM_Warmer): #too cold
        InOut.activate(ATM_Warmer)
    if temperature > climate_recipe.threshold_temp_max(date_current)+1:  #too warm
        InOut.desactivate(ATM_Warmer)

    #humidity
    humidity = 12#AM2315.read_humidity()
    humidity_threshold = climate_recipe.thresholdd_humidity(date_current.hours,date_current.days)
    if humidity < humidity_threshold*(1-0.005):
        # humidity is too low
        InOut.activate(ATM_MistMaker, ATM_Ventilator)
    if humidity > humidity_threshold*(1+0.005) : # humidity is too high
        InOut.desactivate(ATM_MistMaker)


####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""
    InOut.desactivate(ATM_Ventilator,
                    ATM_MistMaker,
                    ATM_Warmer)

date_current = datetime.datetime.now()
atmospheric_loop(date_current,climate_recipe)
