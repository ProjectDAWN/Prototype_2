#  Python 3.6
#  main_LIG.py
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
# This program aims to control the four modules of the box according to climate
# recipes. All the threshold are defined in climate_recipe.py and this code
# only control the automation between sensors, actuators and climate recipes.
#
# Actuactors : LED
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

WARwatermevel_pin=0



####### Atmospheric module
InOut = Raspberry_GPIO.Interface(pin_file,realMode)
climate_recipe = Climate_recipe(variety)
AM2315 = am2315.AM2315()

####### Lighting module
def lighting_loop(date_current,climate_recipe):
    """lighting_loop i a function that control Leds acoording to climate recipe"""

    if t(1) < climate_recipe.LEDupBoundary(t, variety) and InOut.input(LIG_Led): # end of the day for LEDs
        InOut.desactivate(LIG_Led)
    if t(1) > climate_recipe.LEDupBoundary(t,variety) and not InOut.input(LIG_Led):# beginning of the day for LEDs
        InOut.activate(LIG_Led)

####### Nutrients module

####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""
    InOut.desactivate(LIG_Led)


######################### Main loop ###########################################

date_current = datetime.datetime.now()
lighting_loop(date_current,climate_recipe)
