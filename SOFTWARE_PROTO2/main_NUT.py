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

size_x_bac = 80 #cm
size_y_bac = 50 #cm
flow= 1.6 #pump's flow = 1.6ml.s-1
water_level = sensors.read("waterlevel")
volume = size_x_bac*size_y_bac*water_level/1000
coef = volume/flow
print(coef)


####### Nutrients module
def nutrients_loop(day,climate_recipe):
    """nutrients_loop is a function that control the release of nutrients according to climate recipe"""
    FloraMicro = climate_recipe.floraMicro(day) #ml
    print("FloraMicro : {}".format(FloraMicro))
    actuators.activate("NUT_Pump_Micro")
    time.sleep(FloraMicro*coef)
    print(FloraMicro*coef)
    actuators.desactivate("NUT_Pump_Micro")
    FloraGro = climate_recipe.floraGro(day) #ml
    actuators.activate("NUT_Pump_BioGro")
    time.sleep(FloraGro*coef)
    actuators.desactivate("NUT_Pump_BioGro")
    FloraBloom = climate_recipe.floraBloom(day) # ml
    actuators.activate("NUT_Pump_BioBloom")
    time.sleep(FloraBloom*coef)
    actuators.desactivate("NUT_Pump_BioBloom")

####### End of growth

def end_loop():
    """put all the actuators pins at LOW value"""
    actuators.desactivate("NUT_Pump_BioGro",
                    "NUT_Pump_Micro",
                    "NUT_Pump_BioBloom")

date_current = datetime.datetime.now()
diff = datetime.datetime.now() - date_ini
end_loop()
#nutrients_loop(diff.days,climate_recipe)
