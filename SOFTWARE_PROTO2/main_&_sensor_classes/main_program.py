#  Python 2.7
#  main_program.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN ©
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
#          --> Atmospherique : Température, humidité (same probe)
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

import RPI.GPIO as GPIO
import datetime
import climate_recipe
import time
import am2315
import AtlasI2C
#add sensors' and actuators' classes here



######################## Modules loops #######################################


####### Atmospheric module

def atmospheric_loop(t,nbdays,variety):
    "atmospheric_loop i a function that maintain parameters (temperature, humidity) in a range define in climate recipe"

    #Temperature
    temperature = am2315.read_temperature() #get value of temperature
    if temperature < climate_recipe.threshold_temp_min(t,nbdays,variety)-1 and not GPIO.input(ATMelectricwarmer_pin)  : #too cold
        GPIO.output(ATMelectricwarmer_pin, GPIO.HIGH) #turn on electric warmer
    if temperature < climate_recipe.threshold_temp_max(t,nbdays,variety)+1:  #too warm
        GPIO.output(ATMelectricwarmer_pin, GPIO.LOW) #turn off electric warmer

    #humidity
    humidity = am2315.read_humidity() #get value of temperature
    humidity_threshold = climate_recipe.thresholdd_humidity(t,variety) # get value of threshold from climate recipe
    if humidity < humidity_threshold*(1-0.005) and not GPIO.input(ATMmistmaker_pin) and not GPIO.input(ATMventilator_pin)  :
        # humidity is too low
        GPIO.output(ATMmistmaker_pin, GPIO.HIGH) # turn on mistmaker
        GPIO.output(ATMventilator_pin, GPIO.HIGH) #turn on ventilator
    if humidity < humidity_threshold*(1+0.005) : # humidity is too high
        GPIO.output(ATMmistmaker_pin, GPIO.LOW) # turn off ATMmistmaker_pin
        time.sleep(necessry_time) # decide how many time it gets to homogenize
        GPIO.output(ATMmistmaker_pin, GPIO.LOW) #turn off ventilator

####### Lighting module
def lighting_loop(t, variety):
    "lighting_loop i a function that control Leds acoording to climate recipe"

    if t(1) < climate_recipe.LEDupBoundary(t, variety) and GPIO.input(LIGled_pi) # end of the day for LEDs
        GPIO.output(LIGled_pin, GPIO.LOW)
    if t(1) > climate_recipe.LEDupBoundary(t,variety) and not GPIO.input(LIGled_pi) # beginning of the day for LEDs
        GPIO.output(LIGled_pin, GPIO.HIGH)

####### Nutrients module
def nutrients_loop(nbdays, variety):
    "nutrients_loop is a function that control the release of nutrients according to climate recipe"
    nutrient_week=(False,False,False,False,False,False,False,False,False,False,False,False
    flow= 1.6 #pump's flow = 1.6ml.s-1
    water_level = ...
    volume = size_x_bac*size_y_bac*water_level
    coeff = volume/3.79
    i = floor(nbdays/7) +1 # week index
    if nutrient_week(i) == False : # no nutrient for the current week
        FloraMicro = climate_recipe.floraMicro(i, variety) #ml
        GPIO.output(NUTpump1_pin, GPIO.HIGH)
        time.sleep(FloraMicro/flow*coeff)
        GPIO.output(NUTpump1_pin, GPIO.LOW)

        FloraGro = climate_recipe.floraGro(i, variety) #ml
        GPIO.output(NUTpump2_pin, GPIO.HIGH)
        time.sleep(FloraGro/flow*coeff)
        GPIO.output(NUTpump2_pin, GPIO.LOW)

        FloraBloom = climate_recipe.floraBloop(i, variety) # ml
        GPIO.output(NUTpump3_pin, GPIO.HIGH)
        time.sleep(FloraBloom/flow*coeff)
        GPIO.output(NUTpump3_pin, GPIO.LOW)

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
        GPIO.output(WARpH_pin, GPIO.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        GPIO.output(WARpH_pin, GPIO.LOW)

    if pH > climate_recipe.pHtop(t, variety):
        GPIO.output(WARpHdown_pin, GPIO.HIGH)
        time.sleep(x) # find the right amount of time to reach the good value
        GPIO.output(WARpHdown_pin, GPIO.LOW)

    #watering
    if climate_recipe.watering_fistcycle(nbdays,variety):
        GPIO.output(WARultrasonicmistmaker_pin, GPIO.HIGH)
        GPIO.output(WARventilator_pin, GPIO.HIGH)
        time.sleep(climate_recipe.WAR_ON_FIRST(variety))
        GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
        GPIO.output(WARventilator_pin, GPIO.LOW)

        GPIO.output(WARmixer_pi, GPIO.HIGH)
        time.sleep(climate_recipe.WAR_OFF_FIRST(variety))
        GPIO.output(WARmixer_pi, GPIO.LOW)

    if not climate_recipe.watering_fistcycle(nbdays,variety):
        GPIO.output(WARultrasonicmistmaker_pin, GPIO.HIGH)
        GPIO.output(WARventilator_pin, GPIO.HIGH)
        time.sleep(climate_recipe.WAR_OFN_SECOND(variety))
        GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
        GPIO.output(WARventilator_pin, GPIO.LOW)

        GPIO.output(WARmixer_pi, GPIO.HIGH)
        time.sleep(climate_recipe.WAR_OFF_SECOND(variety))
        GPIO.output(WARmixer_pi, GPIO.LOW)

####### End of growth

def end_loop():
    "put all the GPIO pins at LOW value"
    #ATM module
    GPIO.output(ATMventilator_pin, GPIO.LOW)
    GPIO.output(ATMmistmaker_pin, GPIO.LOW)
    GPIO.output(ATMelectricwarmer_pin, GPIO.LOW)
    #LIG module
    GPIO.output(LIGled_pin, GPIO.LOW)
    #NUT module
    GPIO.output(NUTpump1_pin, GPIO.LOW)
    GPIO.output(NUTpump2_pin, GPIO.LOW)
    GPIO.output(NUTpump3_pin, GPIO.LOW)
    #WAT module
    GPIO.output(WARultrasonicmistmaker_pin, GPIO.LOW)
    GPIO.output(WARmixer_pin, GPIO.LOW)
    GPIO.output(WARventilator_pin, GPIO.LOW)
    GPIO.output(WARwatermevel_pin, GPIO.LOW)
    GPIO.output(WARpHup_pin, GPIO.LOW)
    GPIO.output(WARpHdown_pin, GPIO.LOW)

######################### Main loop ###########################################

def growing_program(variety) :

    ###################### Initialisation ########################################

    GPIO.setmode(GPIO.BOARD)

    ####### Atmospheric module (ATM)
    ATMventilator_pin =  ...
    GPIO.setup(ATMventilator_pin, GPIO.OUT, initial = GPIO.LOW)
    ATMmistmaker_pin = ...
    GPIO.setup(ATMmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
    ATMelectricwarmer_pin = ...
    GPIO.setup(ATMelectricwarmer_pin, GPIO.OUT, initial = GPIO.LOW)

    ####### Lighting module (LIG)
    LIGled_pin = ...
    GPIO.setup(LIGled_pin, GPIO.OUT, initial = GPIO.LOW)
    ####### Nutrients module (NUT)
    NUTpump1_pin = ...                     #Flora Micro/Mato
    GPIO.setup(NUTpump1_pin, GPIO.OUT, initial = GPIO.LOW)
    NUTpump2_pin = ...                     #FloraGro
    GPIO.setup(NUTpump2_pin, GPIO.OUT, initial = GPIO.LOW)
    NUTpump3_pin = ...                     #FloraBloom
    GPIO.setup(NUTpump3_pin, GPIO.OUT, initial = GPIO.LOW)
    size_x_bac = ...
    size_y_bac ...
    ####### Watering module (WAT)
    WARultrasonicmistmaker_pin = ...
    GPIO.setup(WARultrasonicmistmaker_pin, GPIO.OUT, initial = GPIO.LOW)
    WARmixer_pin = ...
    GPIO.setup(WARmixer_pin, GPIO.OUT, initial = GPIO.LOW)
    WARventilator_pin = ...
    GPIO.setup(WARventilator_pin, GPIO.OUT, initial = GPIO.LOW)
    WARwaterlevel_pin = ...
    WARpHup_pin = ...
    GPIO.setup(WARpHup_pin, GPIO.OUT, initial = GPIO.LOW)
    WARpHdown_pin = ...
    GPIO.setup(WARpHdown_pin, GPIO.OUT, initial = GPIO.LOW)
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
