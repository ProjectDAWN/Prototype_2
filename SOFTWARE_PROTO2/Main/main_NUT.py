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
import datetime
import time
path = sys.path[0]+"/.."
sys.path.append(path)

import Raspberry_Interface
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
    """Control the release of nutrients according to climate recipe

    Arguments:
    day -- [int] current day of growth
    climate_recipe -- [Climate_recipe] class managing the current growth

    """
    water_level = 15 #sensors.read("water_level")
    actuators.activate("NUT_Mixer")
    time.sleep(60)
    actuators.desactivate("NUT_Mixer")
    for nutrient in nut_list:
        nut_time = climate_recipe.pump_nut_time(nutrient,day,water_level) #second
        actuators.activate("NUT_Pump_" + nutrient)
        time.sleep(nut_time)
        actuators.desactivate("NUT_Pump_" + nutrient)


####### End of growth

def end_loop():
    """Desactivate every NUT actuators"""
    actuators.desactivate("NUT_Pump_BioGro",
                        "NUT_Pump_Micro",
                        "NUT_Pump_BioBloom",
                        "NUT_Pump_Mato"
                        "NUT_Mixer")

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
print(date_current)
nutrients_loop(diff.days,climate_recipe)
