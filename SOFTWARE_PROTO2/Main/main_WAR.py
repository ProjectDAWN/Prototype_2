#  Python 3.6
#  main_WAR.py
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

# Sensors : water level, pH, EC
#
# Actuactors :  ultrasonic mixt maker, agitateur solution nutritive,
#                        ventilateur waterproof
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
#print = partial(print,flush=True)



######################## Modules loops #######################################
sys.stdout = log_config.print_log_file
###Variable initialization
print("WAR module")
actuators = growth_config.actuators()
sensors = growth_config.sensors()
climate_recipe = growth_config.recipe()
date_ini = growth_config.date_ini()



def watering_loop(day,climate_recipe):
    """Control water_level, pH, EC, aeroponic system

    Arguments:
    day -- [int] current day of growth
    climate_recipe -- [Climate_recipe] class managing the current growth

    """
    time_pH = 0
    date_current = datetime.datetime.now()
    print(date_current)

    while True :
        #get pH value
        pH_value = sensors.read("pH")

        water_level = sensors.read("water_level")
        if water_level < 80:
            print("WARNING ! WATER LEVEL TOO LOW !!!!!!!!!!")

        #get EC value
        EC_value = sensors.read("conductivity")

        #pH regulation
        if pH_value > climate_recipe.pH_max():
            #think about arrange time regulation on pH diff
            time_pH = climate_recipe.time_pH_regulation()
            actuators.activate("NUT_Pump_pHDown")
            time.sleep(time_pH)
            actuators.desactivate("NUT_Pump_pHDown")

        #watering

        #break time with activation of the mixer
        actuators.activate("WAR_Mixer")
        time.sleep(climate_recipe.OFF_time(day) - time_pH)
        actuators.desactivate("WAR_Mixer")

        #vaporization time
        actuators.activate("WAR_MistMaker", "WAR_Ventilator")
        time.sleep(climate_recipe.ON_time(day))
        actuators.desactivate("WAR_MistMaker", "WAR_Ventilator")


####### End of growth

def end_loop():
    """Desactivate every WAR actuators"""
    actuators.desactivate("WAR_MistMaker",
                    "WAR_Mixer",
                    "WAR_Ventilator",
                    "NUT_Pump_pHDown")

######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
print(date_current)
watering_loop(diff.days,climate_recipe)
