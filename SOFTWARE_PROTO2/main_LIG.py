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
import Raspberry_Interface
import datetime
import time

from Raspberry_Interface.sensor_classes import AtlasI2C
from config import read_config
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization

actuators = read_config.actuators()
sensors = read_config.sensors()
climate_recipe = read_config.recipe()
date_ini = read_config.date_ini()

def lighting_loop(hour,day,climate_recipe):
    """lighting_loop i a function that control Leds acoording to climate recipe"""

    if(hour<climate_recipe.LEDupBoundary(day)) and (hour>=climate_recipe.LEDdownBoundary(day)):
        actuators.desactivate("LIG_Led")
    else:
        actuators.activate("LIG_Led")

####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""
    actuators.activate("LIG_Led")


######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
lighting_loop(date_current.hour,diff.days,climate_recipe)
