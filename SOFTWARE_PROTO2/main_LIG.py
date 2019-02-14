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
import pickle
from climate_recipe.Climate_recipe import Climate_recipe
import time
from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
from Raspberry_Interface.sensor_classes import AtlasI2C
#add sensors' and actuators' classes here





######################## Modules loops #######################################

###Variable initialization
pin_file = "Files/Actuators.csv"
realMode = True
variety = "tomato"
InOutMode = "GPIO"
date_file = open("Files/date_ini",'rb')
depickler = pickle.Unpickler(date_file)
date_ini = depickler.load()
actuators = GPIO_Actuators.GPIO_Actuators(pin_file,InOutMode,realMode)
sensors = GPIO_Sensors.GPIO_Sensors(InOutMode,realMode)
climate_recipe = Climate_recipe(variety)


def lighting_loop(hour,day,climate_recipe):
    """lighting_loop i a function that control Leds acoording to climate recipe"""

    if(hour<climate_recipe.LEDupBoundary(day)) and (hour>=climate_recipe.LEDdownBoundary(day)):
        actuators.activate("LIG_Led")
    else:
        actuators.desactivate("LIG_Led")

####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""
    actuators.desactivate("LIG_Led")


######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
lighting_loop(date_current.hour,diff.days,climate_recipe)
time.sleep(25)
end_loop()
