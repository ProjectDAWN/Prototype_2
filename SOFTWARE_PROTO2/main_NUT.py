#  Python 3.6
#  main_NUT.py
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

# Actuactors : pompes peristatiques, ventilateurs melangeurs
#
##################### Importation section   #################################
import sys
import Raspberry_Interface
import datetime
import time

from Raspberry_Interface.sensor_classes import AtlasI2C
from config import growth_config,log_config
#add sensors' and actuators' classes here



######################## Modules loops #######################################
sys.stdout = log_config.print_log_file
###Variable initialization
print("NUT module")

actuators = growth_config.actuators()
sensors = growth_config.sensors()
climate_recipe = growth_config.recipe()
date_ini = growth_config.date_ini()
nut_list = growth_config.nut_list

####### Nutrients module
def nutrients_loop(day,climate_recipe):
    """nutrients_loop is a function that control the release of nutrients according to climate recipe"""
    water_level = sensors.read("water_level")
    for nutrient in nut_list:
        nut_time = climate_recipe.pump_nut_time(nutrient,day,water_level) #second
        actuators.activate("NUT_Pump_"+nutrient)
        time.sleep(nut_time)
        actuators.desactivate("NUT_Pump_"+nutrient)


####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""
    actuators.desactivate("NUT_Pump_BioGro",
                    "NUT_Pump_Micro",
                    "NUT_Pump_BioBloom")

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
print(date_current)
nutrients_loop(diff.days,climate_recipe)
