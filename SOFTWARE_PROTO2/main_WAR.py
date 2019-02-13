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
from Raspberry_Interface.sensor_classes import pH
from Raspberry_Interface.sensor_classes import EC


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



def watering_loop(day,climate_recipe):
    """water_loop control level_water, pH, EC, hydroponic system"""
    count = 0
    bool = True
    
    while bool=True :
        #get pH value
        pH_value = pH.read()

        #get EC value
        EC_value = EC.read()

        #pH regulation
        if pH_value > climate_recipe.pH_max():
            actuators.activate("NUT_Pump_pHDown")
            time.sleep(5) # find the right amount of time to reach the good value
            actuators.desactivate("NUT_Pump_pHDown")

        #watering

        #break time with activation of the mixer
        actuators.activate("WAR_Mixer")
        time.sleep(climate_recipe.OFF_time(day)-5)
        actuators.desactivate("WAR_Mixer")

        #vaporization time
        actuators.activate(WAR_MistMaker, WAR_Ventilator)
        time.sleep(climate_recipe.ON_time(day))
        actuators.desactivate(WAR_MistMaker, WAR_Ventilator)

        count+=1
        if count = 5 :
            bool = False

####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""

    actuators.desactivate(WAR_MistMaker,
                    WAR_Mixer,
                    WAR_Ventilator,
                    NUT_Pump_pHDown)

######################### Main loop ###########################################

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
watering_loop(diff.days,climate_recipe)
