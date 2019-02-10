#  Python 2.7
#  climate_recipe.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
#
###############################################################################
#
#                       CLIMATE RECIPE
#
###############################################################################

# This function aims to return all the threshold that the main_loops need to insure the growth
# It takes as parameters the variety and the current time
#
#
# Possible varieties : - tomato
#                       - lettuce
#



###############################################################################
import numpy as np
import pandas as pd
class Climate_recipe:

    CR_folder = "Files/climate_recipes/"

    __init__(self,variety):
        self.df = pd.read_csv(Climate_recipe.CR_folder+"caracteristics.csv",index_col=0).variety
        self.variety = variety
        self.nb_days = self.df["nb_days"] #number of days needed for the entire growth
        self.pH_down = self.df["pH_down"]
        self.pH_up = self.df["pH_up"]
        self.recipe = pd.read_csv(CR_folder+ variety +".csv",index_col=0)

###################################

####### Functions for Atmospheric module #########################

def threshold_temp_min(t,nbdays,variety):
    "return the min acceptable value at t"

    if variety == "tomato":
        if nbdays <= 7 : # "germination" time
            x = 28
        elif nbdays > 7 and t <= 21 : # "croissance" time
            if t(2)<23 and t(2)>5 : #day
                x = 26
            else : # night
                x = 19
        elif nbdays > 21 and t <= 51:# "floraison" Time
            if t(2)<19 and t(2)>7 : #day
                x = 26
            else : # night
                x = 19
        elif nbdays > 51 : # "fructification" time
            if t(2)<19 and t(2)>7 : #day
                x = 26
            else : # night
                x = 19
    else:        #limit case (no climate recipe)
        x = -1
    return x

def threshold_temp_max(t,nbdays,variety):
    """return the max acceptable value at t"""
    if variety == "tomato":
        if nbdys <= 7 : # "germination" time
                x = 28
        elif nbdays > 7 and t <= 21 : # "croissance" time
            if t(2)<23 and t(2)>5 : #day
                x = 26
            else : # night
                x = 19
        elif nbdays > 21 and t <= 51: # "floraison" Time
            if t(2)<19 and t(2)>7 : #day
                x = 26
            else : # night
                x = 19
        elif nbdays > 51 : # "fructification" time
            if t(2)<19 and t(2)>7 : #day
                x = 26
            else : # night
                x = 19
    else :         #limit case (no climate recipe)
        x = -1
    return x


def thresholdd_humidity(t,variety):
    """return the average value needed at t"""
    if variety == "tomato":
        if t <= 7 : # "germination" time
            x = 85
        elif t > 7 and t <= 21 : # "croissance" time
            x = 75
        elif t > 21 and t <= 51: # "floraison" Time
            x = 70
        elif t > 51 : # "fructification" time
            x = 70
    else :         #limit case (no climate recipe)
        x = -1
    return x    # x is an %


####### Functions for Lighting module ##########################

def LEDupBoundary(t,variety):
    #return the hour when LEDs should be turned off
    if variety == "tomato":
        if t <= 21 : # "growth" time
            x = 23
        elif t > 21 : # "bloom" time
            x = 19
    else :         #limit case (no climate recipe)
        x = -1
    return x

def LEDdownBoundary(t,variety):
    #return the hour when LEDs should be turned on
    if variety == "tomato":
        if t <= 21 : # "growth" time
            x = 5
        elif t > 21 : # "bloom" time
            x = 7
    else :         #limit case (no climate recipe)
        x = -1
    return x


############### Functions for Nutrients Module ######################

def floraMicro(i, variety):
    "return the number of ml of this nutrient for week i according to climate recipe"
    if variety == "tomato":
        if i == 1 :
            x = 2.5
        elif i == 2 :
            x = 7.5
        elif i == 3 :
            x = 10
        elif i == 4 :
            x = 7.5
        elif i == 5 :
            x = 7.5
        elif i == 6 :
            x = 7.5
        elif i == 7 :
            x = 7.5
        elif i == 8 :
            x = 7.5
        elif i == 9 :
            x = 7.5
        elif i == 10 :
            x = 7.5
        elif i == 11 :
            x = 5
        elif i == 12 :
            x = 0
        else :         #limit case (no climate recipe)
            x = 0
    return x

def floraGro(i, variety):
    "return that return the number of ml of this nutrient for week i according to climate recipe"
    if variety == "tomato":
        if i == 1 :
            x = 2.5
        elif i == 2 :
            x = 10
        elif i == 3 :
            x = 10
        elif i == 4 :
            x = 7.5
        elif i == 5 :
            x = 2.5
        elif i == 6 :
            x = 2.5
        elif i == 7 :
            x = 2.5
        elif i == 8 :
            x = 2.5
        elif i == 9 :
            x = 0
        elif i == 10 :
            x = 0
        elif i == 11 :
            x = 0
        elif i == 12 :
            x = 0
    else :         #limit case (no climate recipe)
        x = 0
    return x
def floraBloom(i, variety):
    "return that return the number of ml of this nutrient for week i according to climate recipe"
    if variety == "tomato":
        if i == 1 :
            x = 2.5
        elif i == 2 :
            x = 7.5
        elif i == 3 :
            x = 10
        elif i == 4 :
            x = 7.5
        elif i == 5 :
            x = 7.5
        elif i == 6 :
            x = 7.5
        elif i == 7 :
            x = 7.5
        elif i == 8 :
            x = 7.5
        elif i == 9 :
            x = 7.5
        elif i == 10 :
            x = 7.5
        elif i == 11 :
            x = 5
        elif i == 12 :
            x = 0
    else :         #limit case (no climate recipe)
        x = 0
    return x


########## Watering Module ###########################

def pHlow(t,variety):
    return 5.8
def pHup(t,variety):
    return 6.2

def watering_first_cycle(t, variety,nbdays):
    if nbdays <= 21 :
        #bool = lectrique
        bool = True
    elif nbdays > 21 :
        bool = False
    return bool

def WAR_ON_FIRST(variety):
    return 0.75

def WAR_OFF_FIRST(variety):
    return 52.5

def WAR_ON_SECOND(variety):
    return 1.5

def WAR_OFF_SECOND(variety):
    return 50
