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
import out_in
import datetime
from climate_recipe import climate_recipe
import time
from out_in import Raspberry_GPIO
from out_in.sensor_classes import am2315
from out_in.sensor_classes import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization
pin_file = "Files/Actuators.csv"
realMode = False
variety = "tomato"
necessry_time=0
size_x_bac=0
size_y_bac=0

pH_I2C_address = 0
EC_I2C_address = 0

InOut = Raspberry_GPIO.Interface(pin_file,realMode)
climate_recipe = Climate_recipe(variety)
AM2315 = am2315.AM2315()

####### Atmospheric module
InOut = Raspberry_GPIO.Interface(pin_file,realMode)
AM2315 = am2315.AM2315()



####### Nutrients module
def nutrients_loop(date_current,climate_recipe):
    """nutrients_loop is a function that control the release of nutrients according to climate recipe"""
    flow= 1.6 #pump's flow = 1.6ml.s-1
    water_level = 0 #Add the fonction
    volume = size_x_bac*size_y_bac*water_level
    coeff = volume/3.79
    i = nbdays//7 # week index
    if not nutrient_week[i]: # no nutrient for the current week
        nutrient_week[i]=True
        FloraMicro = climate_recipe.floraMicro(i, variety) #ml
        InOut.activate("NUT_Pump_pHDown")
        time.sleep(FloraMicro/flow*coeff)
        InOut.desactivate("NUT_Pump_pHDown")
        FloraGro = climate_recipe.floraGro(i, variety) #ml
        InOut.activate(NUT_Pump2)
        time.sleep(FloraGro/flow*coeff)
        InOut.desactivate(NUT_Pump2)
        FloraBloom = climate_recipe.floraBloop(i, variety) # ml
        InOut.activate(NUT_Pump3)
        time.sleep(FloraBloom/flow*coeff)
        InOut.desactivate(NUT_Pump3)

####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""

    InOut.desactivate(NUT_Pump_pHDown,
                    NUT_Pump2,
                    NUT_Pump3)


date_current = datetime.datetime.now()
atmospheric_loop(date_current,climate_recipe)
