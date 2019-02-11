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
import out_in
import datetime
from climate_recipe import climate_recipe
import time
from out_in import Raspberry_GPIO
from out_in.sensor_classes import am2315
from out_in.sensor_classes import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization
pin_file = "Files/Actuators.csv"
realMode = False
necessry_time=0
size_x_bac=0
size_y_bac=0

pH_I2C_address = 0
EC_I2C_address = 0

WARwatermevel_pin=0

InOut = Raspberry_GPIO.Interface(pin_file,realMode)
AM2315 = am2315.AM2315()

def atmospheric_loop(t,nbdays,variety):
    """maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = 12#AM2315.read_temperature()
    if temperature < climate_recipe.threshold_temp_min(t,nbdays,variety)-1 and not InOut.input(ATM_Warmer): #too cold
        InOut.activate(ATM_Warmer)
    if temperature > climate_recipe.threshold_temp_max(t,nbdays,variety)+1:  #too warm
        InOut.desactivate(ATM_Warmer)

    #humidity
    humidity = 12#AM2315.read_humidity()
    humidity_threshold = climate_recipe.thresholdd_humidity(t,variety)
    if humidity < humidity_threshold*(1-0.005) and not InOut.input(ATM_MistMaker) and not InOut.input(ATM_Ventilator):
        # humidity is too low
        InOut.activate(ATM_MistMaker, ATM_Ventilator)
    if humidity < humidity_threshold*(1+0.005) : # humidity is too high
        InOut.desactivate(ATM_MistMaker)
        time.sleep(necessry_time) # decide how many time it gets to homogenize
        InOut.desactivate(ATM_MistMaker)

####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""
    InOut.desactivate(ATM_Ventilator,
                    ATM_MistMaker,
                    ATM_Warmer)


growing_program("tomato")