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
pin_file = "Files/Actuators.csv"
realMode = False
variety = "tomato"
date_file = open("Files/date_ini",'rb')
depickler = pickle.Unpickler(date_file)
date_ini = depickler.load()
actuators = GPIO_Actuators.GPIO_Actuators(pin_file,realMode)
sensors = GPIO_Sensors.GPIO_Sensors(realMode)
climate_recipe = Climate_recipe(variety)



def watering_loop(variety,climate_recipe):
    """water_loop control level_water, pH, EC, hydroponic system"""

    pH = sensors.read("pH")

    EC = sensors.read("conductivity")
    #pH regulation
    if pH < climate_recipe.caracteristics["pH_down"]:
        actuators.activate(NUT_Pump4)
        time.sleep(x) # find the right amount of time to reach the good value
        actuators.desactivate(NUT_Pump4)

    if pH > climate_recipe.caracteristics["pH_up"]:
        actuators.activate(WARpHup_pin)
        time.sleep(x) # find the right amount of time to reach the good value
        actuators.desactivate(WARpHup_pin)

    #watering
    if climate_recipe.watering_fistcycle(nbdays,variety):
        actuators.activate(WAR_MistMaker, WAR_Ventilator)
        time.sleep(climate_recipe.WAR_ON_FIRST(variety))
        actuators.desactivate(WAR_MistMaker, WAR_Ventilator)

        actuators.activate(WAR_Mixer)
        time.sleep(climate_recipe.WAR_OFF_FIRST(variety))
        actuators.desactivate(WAR_Mixer)

    if not climate_recipe.watering_fistcycle(nbdays,variety):
        actuators.activate(WAR_MistMaker, WAR_Ventilator)
        time.sleep(climate_recipe.WAR_OFN_SECOND(variety))
        actuators.desactivate(WAR_MistMaker, WAR_Ventilator)

        actuators.activate(WAR_Mixer)
        time.sleep(climate_recipe.WAR_OFF_SECOND(variety))
        actuators.desactivate(WAR_Mixer)

####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""

    actuators.desactivate(WAR_MistMaker,
                    WAR_Mixer,
                    WAR_Ventilator,
                    WARwatermevel_pin,
                    WARpHup_pin,
                    NUT_Pump4)

######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
watering_loop(date_current.hour,diff.days,climate_recipe)
