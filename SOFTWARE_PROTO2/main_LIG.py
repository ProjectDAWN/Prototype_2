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
import datetime
import time

import Raspberry_Interface
from Raspberry_Interface.sensor_classes import AtlasI2C
from config import growth_config,log_config
#add sensors' and actuators' classes here



######################## Modules loops #######################################
sys.stdout = log_config.print_log_file
###Variable initialization
print("LIG module")
actuators = growth_config.actuators()
sensors = growth_config.sensors()
climate_recipe = growth_config.recipe()
date_ini = growth_config.date_ini()

def lighting_loop(hour,day,climate_recipe):
    """(des)Activate acoording to climate recipe

    Arguments:
    hour -- [int] current hour of the day
    day -- [int] current day of growth
    climate_recipe -- [Climate_recipe] class managing the current growth

    """

    if(hour < climate_recipe.LEDupBoundary(day)) and
      (hour >= climate_recipe.LEDdownBoundary(day)):
        actuators.desactivate("LIG_Led")
    else:
        actuators.activate("LIG_Led")

####### End of growth

def end_loop():
    """Desactivate every LIG actuators"""
    actuators.activate("LIG_Led")


######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
print(date_current)
lighting_loop(date_current.hour,diff.days,climate_recipe)
