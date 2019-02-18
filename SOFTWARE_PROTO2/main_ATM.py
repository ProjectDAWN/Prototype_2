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
import time

from Raspberry_Interface.sensor_classes import AtlasI2C
from config import growth_config,log_config
#add sensors' and actuators' classes here



######################## Modules loops #######################################
sys.stdout = log_config.print_log_file
###Variable initialization
print("ATM module")

actuators = growth_config.actuators()
sensors = growth_config.sensors()
climate_recipe = growth_config.recipe()
date_ini = growth_config.date_ini()



def atmospheric_loop(hour,day,climate_recipe):
    """maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = sensors.read("temperature")
    if temperature < climate_recipe.threshold_temp(hour, day)-1 : #too cold
        #actuators.activate("ATM_Warmer")
        #sleep(climate_recipe.system[time_temp_regulation])
        #actuator.desactivate("ATM_Warmer")
        pass
    if temperature > climate_recipe.threshold_temp(hour, day)+1:  #too warm
        #actuators.activate("ATM_Cooler")
        pass

    #humidity
    humidity = sensors.read("humidity")
    humidity_threshold = climate_recipe.thresholdd_humidity(date_current.hour,date_current.day)
    if humidity < humidity_threshold*(1-0.005):
        # humidity is too low
        actuators.activate("ATM_MistMaker", "ATM_Ventilator")
        sleep(climate_recipe.system[time_hum_regulation])
        actuators.desactivate("ATM_MistMaker", "ATM_Ventilator")
    if humidity > humidity_threshold*(1+0.005) : # humidity is too high
        #actuators.desactivate("ATM_MistMaker")
        pass


####### End of growth

def end_loop():
    """desactivate every actuators"""
    actuators.desactivate("ATM_Ventilator",
                    "ATM_MistMaker",
                    "ATM_Warmer")

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
print(date_current)
atmospheric_loop(date_current.hour,diff.days,climate_recipe)
