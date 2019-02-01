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

import Emulator
import datetime
import climate_recipe
import time
import am2315
import AtlasI2C
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

def atmospheric_loop(t,nbdays,variety):
    """atmospheric_loop i a function that maintain parameters (temperature, humidity) in a range define in climate recipe"""

    #Temperature
    temperature = am2315.read_temperature() #get value of temperature
    if temperature < climate_recipe.threshold_temp_min(t,nbdays,variety)-1 and not InOut.input(ATM_Warmer): #too cold
        InOut.output(ATM_Warmer, InOut.HIGH) #turn on electric warmer
    if temperature > climate_recipe.threshold_temp_max(t,nbdays,variety)+1:  #too warm
        InOut.output(ATM_Warmer, InOut.LOW) #turn off electric warmer

    #humidity
    humidity = am2315.read_humidity() #get value of humidity
    humidity_threshold = climate_recipe.thresholdd_humidity(t,variety) # get value of threshold from climate recipe
    if humidity < humidity_threshold*(1-0.005) and not InOut.input(ATM_MistMaker) and not InOut.input(ATM_Ventilator):
        # humidity is too low
        InOut.output(ATM_MistMaker, InOut.HIGH) # turn on mistmaker
        InOut.output(ATM_Ventilator, InOut.HIGH) #turn on ventilator
    if humidity < humidity_threshold*(1+0.005) : # humidity is too high
        InOut.output(ATM_MistMaker, InOut.LOW) # turn off ATM_MistMaker
        time.sleep(necessry_time) # decide how many time it gets to homogenize
        InOut.output(ATM_MistMaker, InOut.LOW) #turn off ventilator

####### Lighting module
def lighting_loop(t, variety):
    """lighting_loop i a function that control Leds acoording to climate recipe"""

    if t(1) < climate_recipe.LEDupBoundary(t, variety) and InOut.input(LIG_Led): # end of the day for LEDs
        InOut.output(LIG_Led, InOut.LOW)
    if t(1) > climate_recipe.LEDupBoundary(t,variety) and not InOut.input(LIG_Led):# beginning of the day for LEDs
        InOut.output(LIG_Led, InOut.HIGH)

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
        InOut.output(NUT_Pump_pHDown, InOut.HIGH)
        time.sleep(FloraMicro/flow*coeff)
        InOut.output(NUT_Pump_pHDown, InOut.LOW)
        FloraGro = climate_recipe.floraGro(i, variety) #ml
        InOut.output(NUT_Pump2, InOut.HIGH)
        time.sleep(FloraGro/flow*coeff)
        InOut.output(NUT_Pump2, InOut.LOW)
        FloraBloom = climate_recipe.floraBloop(i, variety) # ml
        InOut.output(NUT_Pump3, InOut.HIGH)
        time.sleep(FloraBloom/flow*coeff)
        InOut.output(NUT_Pump3, InOut.LOW)



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
        InOut.output(NUT_Pump4, InOut.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.output(NUT_Pump4, InOut.LOW)

    if pH > climate_recipe.pHtop(t, variety):
        InOut.output(WARpHup_pin, InOut.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.output(WARpHup_pin, InOut.LOW)

    #watering
    if climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.output(WAR_MistMaker, InOut.HIGH)
        InOut.output(WAR_Ventilator, InOut.HIGH)
        time.sleep(climate_recipe.WAR_ON_FIRST(variety))
        InOut.output(WAR_MistMaker, InOut.LOW)
        InOut.output(WAR_Ventilator, InOut.LOW)

        InOut.output(WAR_Mixer, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFF_FIRST(variety))
        InOut.output(WAR_Mixer, InOut.LOW)

    if not climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.output(WAR_MistMaker, InOut.HIGH)
        InOut.output(WAR_Ventilator, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFN_SECOND(variety))
        InOut.output(WAR_MistMaker, InOut.LOW)
        InOut.output(WAR_Ventilator, InOut.LOW)

        InOut.output(WAR_Mixer, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFF_SECOND(variety))
        InOut.output(WAR_Mixer, InOut.LOW)

####### End of growth

def end_loop():
    """put all the InOut pins at LOW value"""
    #ATM module
    InOut.output(ATM_Ventilator, InOut.LOW)
    InOut.output(ATM_MistMaker, InOut.LOW)
    InOut.output(ATM_Warmer, InOut.LOW)
    #LIG module
    InOut.output(LIG_Led, InOut.LOW)
    #NUT module
    InOut.output(NUT_Pump_pHDown, InOut.LOW)
    InOut.output(NUT_Pump2, InOut.LOW)
    InOut.output(NUT_Pump3, InOut.LOW)
    #WAT module
    InOut.output(WAR_MistMaker, InOut.LOW)
    InOut.output(WAR_Mixer, InOut.LOW)
    InOut.output(WAR_Ventilator, InOut.LOW)
    InOut.output(WARwatermevel_pin, InOut.LOW)
    InOut.output(WARpHup_pin, InOut.LOW)
    InOut.output(NUT_Pump4, InOut.LOW)

######################### Main loop ###########################################

def growing_program(variety) :

    ###################### Initialisation ########################################

    InOut.setmode(InOut.BOARD)

    ####### Atmospheric module (ATM)
    InOut.setup(ATM_Ventilator, InOut.OUT, initial = InOut.LOW)
    InOut.setup(ATM_MistMaker, InOut.OUT, initial = InOut.LOW)
    InOut.setup(ATM_Warmer, InOut.OUT, initial = InOut.LOW)

    ####### Lighting module (LIG)
    InOut.setup(LIG_Led, InOut.OUT, initial = InOut.LOW)
    ####### Nutrients module (NUT)
    InOut.setup(NUT_Pump_pHDown, InOut.OUT, initial = InOut.LOW) #Flora Micro/Mato
    InOut.setup(NUT_Pump2, InOut.OUT, initial = InOut.LOW)  #FloraGro
    InOut.setup(NUT_Pump3, InOut.OUT, initial = InOut.LOW) #FloraBloom
    ####### Watering module (WAT)
    InOut.setup(WAR_MistMaker, InOut.OUT, initial = InOut.LOW)
    InOut.setup(WAR_Mixer, InOut.OUT, initial = InOut.LOW)
    InOut.setup(WAR_Ventilator, InOut.OUT, initial = InOut.LOW)
    InOut.setup(WARpHup_pin, InOut.OUT, initial = InOut.LOW)
    InOut.setup(NUT_Pump4, InOut.OUT, initial = InOut.LOW)

    ####### Global variables
    t = (0,0,0,0,0) # current value of Time
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

        atmospheric_loop(t,nbdays,variety)
        #Decide waiting time
        lighting_loop(t,variety)
        #Decide wainting Time
        nutrients_loop(nbdays,variety,nutrient_week)
        #Decide waiting Time
        watering_loop(t,variety)
        #Decide waiting time
        diff = datetime.datetime.now() - date_current

        if diff < datetime.timedelta(minutes=10):
            time.sleep(datetime.timedelta(minutes=10) - diff.total_seconds())
        date_current = datetime.datetime.now()

    ###### End of loop

    end_loop()
