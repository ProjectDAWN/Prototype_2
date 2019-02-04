#  Python 2.7
#  main_program.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
#  Antoine PINAUD
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
# Modules : - Atmospherique
#           - Eclairage
#           - Nutriments
#           - Arrosage
#
# Sensors :
#          --> Atmospherique : Temperature, humidite (same probe)
#          --> Eclairage : /
#          --> Nutriments : /
#          --> Arrosage : water level, pH, EC
#
# Actuactors :
#          --> Atmosperique : ventilateur waterproof, mistmaker, rechauffeur
#                             electrique
#          --> Eclairage : LED de croissance
#          --> Nutriments : pompes peristatiques, ventilateurs melangeurs
#          --> Arrosage: ultrasonic mixt maker, agitateur solution nutritive,
#                        ventilateur waterproof
#
##################### Importation section   #################################
import sys
sys.path.append(sys.path[0] + '/..')
from out_in import Emulator
import datetime
from climate_recipe import climate_recipe
import time
from am2315 import *
from AtlasI2C import *
#add sensors' and actuators' classes here



######################## Modules loops #######################################

###Variable initialization

necessry_time=0
size_x_bac=0
size_y_bac=0

pH_I2C_address = 0
EC_I2C_address = 0

WARwatermevel_pin=0



####### Atmospheric module
InOut = Emulator.Interface()
AM2315 = am2315.AM2315()

def atmospheric_loop(t,nbdays,variety):
    """atmospheric_loop i a function that maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = AM2315.read_temperature() #get value of temperature
    if temperature < climate_recipe.threshold_temp_min(t,nbdays,variety)-1 and not InOut.input(ATM_Warmer): #too cold
        InOut.activate(ATM_Warmer, InOut.HIGH) #turn on electric warmer
    if temperature > climate_recipe.threshold_temp_max(t,nbdays,variety)+1:  #too warm
        InOut.desactivate(ATM_Warmer, InOut.LOW) #turn off electric warmer

    #humidity
    humidity = AM2315.read_humidity() #get value of humidity
    humidity_threshold = climate_recipe.thresholdd_humidity(t,variety) # get value of threshold from climate recipe
    if humidity < humidity_threshold*(1-0.005) and not InOut.input(ATM_MistMaker) and not InOut.input(ATM_Ventilator):
        # humidity is too low
        InOut.activate(ATM_MistMaker, ATM_Ventilator) # turn on mistmaker, ventilator
    if humidity < humidity_threshold*(1+0.005) : # humidity is too high
        InOut.desactivate(ATM_MistMaker) # turn off ATM_MistMaker
        time.sleep(necessry_time) # decide how many time it gets to homogenize
        InOut.desactivate(ATM_MistMaker) #turn off ventilator

####### Lighting module
def lighting_loop(t, variety):
    """lighting_loop i a function that control Leds acoording to climate recipe"""

    if t(1) < climate_recipe.LEDupBoundary(t, variety) and InOut.input(LIG_Led): # end of the day for LEDs
        InOut.desactivate(LIG_Led)
    if t(1) > climate_recipe.LEDupBoundary(t,variety) and not InOut.input(LIG_Led):# beginning of the day for LEDs
        InOut.activate(LIG_Led)

####### Nutrients module
def nutrients_loop(nbdays, variety,nutrient_week):
    """nutrients_loop is a function that control the release of nutrients according to climate recipe"""
    flow= 1.6 #pump's flow = 1.6ml.s-1
    water_level = 0 #Add the fonction
    volume = size_x_bac*size_y_bac*water_level
    coeff = volume/3.79
    i = nbdays//7 # week index
    if not nutrient_week[i]: # no nutrient for the current week
        nutrient_week[i]=True
        FloraMicro = climate_recipe.floraMicro(i, variety) #ml
        InOut.activate(NUT_Pump_pHDown)
        time.sleep(FloraMicro/flow*coeff)
        InOut.desactivate(NUT_Pump_pHDown)
        FloraGro = climate_recipe.floraGro(i, variety) #ml
        InOut.activate(NUT_Pump2)
        time.sleep(FloraGro/flow*coeff)
        InOut.desactivate(NUT_Pump2)
        FloraBloom = climate_recipe.floraBloop(i, variety) # ml
        InOut.activate(NUT_Pump3)
        time.sleep(FloraBloom/flow*coeff)
        InOut.desactivate(NUT_Pump3)



####### Watering module
def watering_loop(t, variety, nbdays):
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
    #ATM module
    InOut.desactivate(ATM_Ventilator,
                    ATM_MistMaker,
                    ATM_Warmer)
    #LIG module
    InOut.desactivate(LIG_Led)
    #NUT module
    InOut.desactivate(NUT_Pump_pHDown,
                    NUT_Pump2,
                    NUT_Pump3)
    #WAT module
    InOut.desactivate(WAR_MistMaker,
                    WAR_Mixer,
                    WAR_Ventilator,
                    WARwatermevel_pin,
                    WARpHup_pin,
                    NUT_Pump4)

######################### Main loop ###########################################

def growing_program(variety) :

    ###################### Initialisation ########################################

    #InOut.setmode(InOut.BOARD)

    ##### Global variables
    date_ini = datetime.datetime.now() # Get the value of time at the beginning of the growth
    T = climate_recipe.nb_days(variety) # Get the end value from climate_recipe (in matter of days)
    date_end = date_ini + datetime.timedelta(days = T)
    nbdays = 0
    nutrient_week = [False]*(T//7 + 1)
    date_current = datetime.datetime.now()

    while  date_current < date_end:  # loop until the current time reach T (in matter of days)

        ###### Time update
        #date = datetime.datetime.now()
        #month = monthini - date.month
        #day = monthini - date.day
        #hour = hourini - date.hour
        #minute = min_ini - date.minute
        #former_t = t
        #t = (month,day, hour, minute,second)

        ## calculate the current number of days
        #if t[1] != former_t(1):
        #    nbdays+=1

        ###### loop

        atmospheric_loop(diff,nbdays,variety)
        #Decide waiting time
        lighting_loop(diff,variety)
        #Decide wainting Time
        nutrients_loop(nbdays,variety,nutrient_week)
        #Decide waiting Time
        watering_loop(diff,variety)
        #Decide waiting time
        diff = datetime.datetime.now() - date_current

        if diff < datetime.timedelta(minutes=10):
            time.sleep((datetime.timedelta(minutes=10) - diff).total_seconds())
        date_current = datetime.datetime.now()

    ###### End of loop

    end_loop()
growing_program("tomates")
