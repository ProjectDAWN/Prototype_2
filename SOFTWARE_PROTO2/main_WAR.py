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

InOut = Raspberry_GPIO.Interface(pin_file,realMode)
climate_recipe = Climate_recipe(variety)
AM2315 = am2315.AM2315()


def watering_loop(variety,climate_recipe):
    """water_loop control level_water, pH, EC, hydroponic system"""

    #get pH value
    device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
    pH = string.split(device.query("I"), ",")[1]

    #get EC value
    device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
    EC = string.split(device.query("I"), ",")[1]

    #pH regulation
    if pH < climate_recipe.pHlow(t, variety):
        InOut.activate(NUT_Pump4)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.desactivate(NUT_Pump4)

    if pH > climate_recipe.pHtop(t, variety):
        InOut.activate(WARpHup_pin)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.desactivate(WARpHup_pin)

    #watering
    if climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.activate(WAR_MistMaker, WAR_Ventilator)
        time.sleep(climate_recipe.WAR_ON_FIRST(variety))
        InOut.desactivate(WAR_MistMaker, WAR_Ventilator)

        InOut.activate(WAR_Mixer)
        time.sleep(climate_recipe.WAR_OFF_FIRST(variety))
        InOut.desactivate(WAR_Mixer)

    if not climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.activate(WAR_MistMaker, WAR_Ventilator)
        time.sleep(climate_recipe.WAR_OFN_SECOND(variety))
        InOut.desactivate(WAR_MistMaker, WAR_Ventilator)

        InOut.activate(WAR_Mixer)
        time.sleep(climate_recipe.WAR_OFF_SECOND(variety))
        InOut.desactivate(WAR_Mixer)

####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""

    InOut.desactivate(WAR_MistMaker,
                    WAR_Mixer,
                    WAR_Ventilator,
                    WARwatermevel_pin,
                    WARpHup_pin,
                    NUT_Pump4)

######################### Main loop ###########################################


date_current = datetime.datetime.now()
water_loop(date_current,climate_recipe)
