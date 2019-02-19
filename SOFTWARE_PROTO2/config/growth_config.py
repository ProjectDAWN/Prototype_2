import pickle
import os
from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
from climate_recipe.Climate_recipe import Climate_recipe

### config variables

chanel_file = "Files/Actuators.csv"
date_file_name = "Files/date_ini"
realMode = False
variety = "tomato"
InOutMode = "GPIO"
model = "Prototype_2"
nut_list = ("Micro","BioBloom","BioGro","Mato")

### access function
def date_ini():
    """return the initial date of growth"""
    date_file = open(os.getcwd()+"/"+date_file_name,'rb')
    depickler = pickle.Unpickler(date_file)
    return(depickler.load())

def recipe():
    """return climate recipe class"""
    return(Climate_recipe(variety,model))

def sensors():
    """return sensor class"""
    return(GPIO_Sensors.GPIO_Sensors(InOutMode,realMode))

def actuators():
    """return actuator class"""
    return(GPIO_Actuators.GPIO_Actuators(chanel_file,InOutMode,realMode))
