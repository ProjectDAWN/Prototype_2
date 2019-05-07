import pickle
import sys
path = sys.path[0]+"/.."
sys.path.append(path)

from Raspberry_Interface import GPIO_Actuators, GPIO_Sensors
from climate_recipe.Climate_recipe import Climate_recipe

# config variables

chanel_file = "Files/Actuators.csv"
date_file_path = "Files/date_ini"
realMode = False
variety = "tomato"
InOutMode = "GPIO"
model = "Prototype_2"
nut_list = ("Micro","BioBloom","BioGro","Mato")


# access functions

def date_ini():
    """return the initial date of growth"""
    date_file = open(sys.path[0] + "/../" + date_file_path,'rb')
    date = pickle.Unpickler(date_file).load()
    date_file.close()
    return(date)


def recipe():
    """return climate recipe class"""
    return(Climate_recipe(variety,model))


def sensors():
    """return sensor class"""
    return(GPIO_Sensors.GPIO_Sensors(InOutMode,realMode))


def actuators():
    """return actuator class"""
    return(GPIO_Actuators.GPIO_Actuators(chanel_file,InOutMode,realMode))


def set_date_ini(date):
    date_file = open(sys.path[0] + "/" + date_file_path,'wb')
    pickler = pickle.Pickler(date_file)
    pickler.dump(date)
    date_file.close()
