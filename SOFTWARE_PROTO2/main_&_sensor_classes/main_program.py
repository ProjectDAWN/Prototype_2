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
#          --> Atmospherique : Temperature, humidité (same probe)
#          --> Eclairage : /
#          --> Nutriments : /
#          --> Arrosage : water level, pH, EC
#
# Actuactors :
#          --> Atmosperique : ventilateur waterproof, mistmaker, réchauffeur
#                             électrique
#          --> Eclairage : LED de croissance
#          --> Nutriments : pompes peristatiques, ventilateurs mélangeurs
#          --> Arrosage: ultrasonic mixt maker, agitateur solution nutritive,
#                        ventilateur waterproof
#
##################### Importation section   #################################

from Emulator import Interface
import datetime
import climate_recipe
import time
import am2315
import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################


####### Atmospheric module

InOut = Interface()

def atmospheric_loop(t,nbdays,variety):
    "atmospheric_loop i a function that maintain parameters (temperature, humidity) in a range define in climate recipe"

    #Temperature
    temperature = am2315.read_temperature() #get value of temperature
    if temperature < climate_recipe.threshold_temp_min(t,nbdays,variety)-1 and not InOut.input(ATMelectricwarmer_pin)  : #too cold
        InOut.output(ATMelectricwarmer_pin, InOut.HIGH) #turn on electric warmer
    if temperature < climate_recipe.threshold_temp_max(t,nbdays,variety)+1:  #too warm
        InOut.output(ATMelectricwarmer_pin, InOut.LOW) #turn off electric warmer

    #humidity
    humidity = am2315.read_humidity() #get value of temperature
    humidity_threshold = climate_recipe.thresholdd_humidity(t,variety) # get value of threshold from climate recipe
    if humidity < humidity_threshold*(1-0.005) and not InOut.input(ATMmistmaker_pin) and not InOut.input(ATMventilator_pin)  :
        # humidity is too low
        InOut.output(ATMmistmaker_pin, InOut.HIGH) # turn on mistmaker
        InOut.output(ATMventilator_pin, InOut.HIGH) #turn on ventilator
    if humidity < humidity_threshold*(1+0.005) : # humidity is too high
        InOut.output(ATMmistmaker_pin, InOut.LOW) # turn off ATMmistmaker_pin
        time.sleep(necessry_time) # decide how many time it gets to homogenize
        InOut.output(ATMmistmaker_pin, InOut.LOW) #turn off ventilator

####### Lighting module
def lighting_loop(t, variety):
    "lighting_loop i a function that control Leds acoording to climate recipe"

    if t(1) < climate_recipe.LEDupBoundary(t, variety) and InOut.input(LIGled_pi): # end of the day for LEDs
        InOut.output(LIGled_pin, InOut.LOW)
    if t(1) > climate_recipe.LEDupBoundary(t,variety) and not InOut.input(LIGled_pi): # beginning of the day for LEDs
        InOut.output(LIGled_pin, InOut.HIGH)

####### Nutrients module
def nutrients_loop(nbdays, variety):
    "nutrients_loop is a function that control the release of nutrients according to climate recipe"
    nutrient_week=[False]*(nb_days/7)
    flow= 1.6 #pump's flow = 1.6ml.s-1
    water_level = ...
    volume = size_x_bac*size_y_bac*water_level
    coeff = volume/3.79
    i = floor(nbdays/7) +1 # week index
    if nutrient_week[i] == False : # no nutrient for the current week
        FloraMicro = climate_recipe.floraMicro(i, variety) #ml
        InOut.output(NUTpump1_pin, InOut.HIGH)
        time.sleep(FloraMicro/flow*coeff)
        InOut.output(NUTpump1_pin, InOut.LOW)

        FloraGro = climate_recipe.floraGro(i, variety) #ml
        InOut.output(NUTpump2_pin, InOut.HIGH)
        time.sleep(FloraGro/flow*coeff)
        InOut.output(NUTpump2_pin, InOut.LOW)

        FloraBloom = climate_recipe.floraBloop(i, variety) # ml
        InOut.output(NUTpump3_pin, InOut.HIGH)
        time.sleep(FloraBloom/flow*coeff)
        InOut.output(NUTpump3_pin, InOut.LOW)

        nutrient_week(i) = True

####### Watering module
def watering_loop(t, variety):
    "water_loop control level_water, pH, EC, hydroponic system"

    #get pH value
    device = AtlasI2C(pH_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
    pH = info = string.split(device.query("I"), ",")[1]

    #get EC value
    device = AtlasI2C(EC_I2C_address)     # creates the I2C port object, specify the address or bus if necessary
    EC = info = string.split(device.query("I"), ",")[1]

    #pH regulation
    if pH < climate_recipe.pHlow(t, variety):
        InOut.output(WARpH_pin, InOut.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.output(WARpH_pin, InOut.LOW)

    if pH > climate_recipe.pHtop(t, variety):
        InOut.output(WARpHdown_pin, InOut.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        InOut.output(WARpHdown_pin, InOut.LOW)

    #watering
    if climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.output(WARultrasonicmistmaker_pin, InOut.HIGH)
        InOut.output(WARventilator_pin, InOut.HIGH)
        time.sleep(climate_recipe.WAR_ON_FIRST(variety))
        InOut.output(WARultrasonicmistmaker_pin, InOut.LOW)
        InOut.output(WARventilator_pin, InOut.LOW)

        InOut.output(WARmixer_pi, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFF_FIRST(variety))
        InOut.output(WARmixer_pi, InOut.LOW)

    if not climate_recipe.watering_fistcycle(nbdays,variety):
        InOut.output(WARultrasonicmistmaker_pin, InOut.HIGH)
        InOut.output(WARventilator_pin, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFN_SECOND(variety))
        InOut.output(WARultrasonicmistmaker_pin, InOut.LOW)
        InOut.output(WARventilator_pin, InOut.LOW)

        InOut.output(WARmixer_pi, InOut.HIGH)
        time.sleep(climate_recipe.WAR_OFF_SECOND(variety))
        InOut.output(WARmixer_pi, InOut.LOW)

####### End of growth

def end_loop():
    "put all the InOut pins at LOW value"
    #ATM module
    InOut.output(ATMventilator_pin, InOut.LOW)
    InOut.output(ATMmistmaker_pin, InOut.LOW)
    InOut.output(ATMelectricwarmer_pin, InOut.LOW)
    #LIG module
    InOut.output(LIGled_pin, InOut.LOW)
    #NUT module
    InOut.output(NUTpump1_pin, InOut.LOW)
    InOut.output(NUTpump2_pin, InOut.LOW)
    InOut.output(NUTpump3_pin, InOut.LOW)
    #WAT module
    InOut.output(WARultrasonicmistmaker_pin, InOut.LOW)
    InOut.output(WARmixer_pin, InOut.LOW)
    InOut.output(WARventilator_pin, InOut.LOW)
    InOut.output(WARwatermevel_pin, InOut.LOW)
    InOut.output(WARpHup_pin, InOut.LOW)
    InOut.output(WARpHdown_pin, InOut.LOW)

######################### Main loop ###########################################

def growing_program(variety) :

    ###################### Initialisation ########################################

    InOut.setmode(InOut.BOARD)

    ####### Atmospheric module (ATM)
    ATMventilator_pin =  ...
    InOut.setup(ATMventilator_pin, InOut.OUT, initial = InOut.LOW)
    ATMmistmaker_pin = ...
    InOut.setup(ATMmistmaker_pin, InOut.OUT, initial = InOut.LOW)
    ATMelectricwarmer_pin = ...
    InOut.setup(ATMelectricwarmer_pin, InOut.OUT, initial = InOut.LOW)

    ####### Lighting module (LIG)
    LIGled_pin = ...
    InOut.setup(LIGled_pin, InOut.OUT, initial = InOut.LOW)
    ####### Nutrients module (NUT)
    NUTpump1_pin = ...                     #Flora Micro/Mato
    InOut.setup(NUTpump1_pin, InOut.OUT, initial = InOut.LOW)
    NUTpump2_pin = ...                     #FloraGro
    InOut.setup(NUTpump2_pin, InOut.OUT, initial = InOut.LOW)
    NUTpump3_pin = ...                     #FloraBloom
    InOut.setup(NUTpump3_pin, InOut.OUT, initial = InOut.LOW)
    size_x_bac = ...
    size_y_bac ...
    ####### Watering module (WAT)
    WARultrasonicmistmaker_pin = ...
    InOut.setup(WARultrasonicmistmaker_pin, InOut.OUT, initial = InOut.LOW)
    WARmixer_pin = ...
    InOut.setup(WARmixer_pin, InOut.OUT, initial = InOut.LOW)
    WARventilator_pin = ...
    InOut.setup(WARventilator_pin, InOut.OUT, initial = InOut.LOW)
    WARwaterlevel_pin = ...
    WARpHup_pin = ...
    InOut.setup(WARpHup_pin, InOut.OUT, initial = InOut.LOW)
    WARpHdown_pin = ...
    InOut.setup(WARpHdown_pin, InOut.OUT, initial = InOut.LOW)
    pH_I2C_adress = ...
    EC_I2C_address = ...

    ####### Global variables
    t = (0,0,0,0,0) # current value of Time
    T = (0,0,0,0,0) # value of the end of production

    ##### Global variables
    dateini = datetime.datetime.now()
    monthini = dateini.month
    dayini = dateini.day
    Tini = (monthini,dayini,0,0,0) # Get the value of time at the beginning of the growth
    T = climate_recipe.nb_days(variety) # Get the end value from climate_recipe (in matter of days)
    nbdays= 0

    while t(2) < T :  # loop until the current time reach T (in matter of days)

        ###### Time update
        date = datetime.datetime.now()
        month = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date. second
        former_t = t
        t = (month,day, hour, minute,second)

        ## calculate the current number of days
        if t(1) != former_t(1):
            nbdays+=1

        ###### loop

        atmospheric_loop(t,nbdays,variety)
        #Decide waiting time
        lighting_loop(t,variety)
        #Decide wainting Time
        nutrients_loop(nbdays,variety)
        #Decide waiting Time
        watering_loop(t,variety)
        #Decide waiting time

    ###### End of loop

    end_loop()
