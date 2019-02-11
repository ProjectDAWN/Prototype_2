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
#                      - lettuce
#



###############################################################################
from CSV_reader import CSV_reader
class Climate_recipe:

    CR_folder = "Files/climate_recipes/"

    __init__(self,variety):
        self.caracteristics = CSV_reader(Climate_recipe.CR_folder+"caracteristics.csv").get_infos(variety)
        self.recipe = CSV_reader(Climate_recipe.CR_folder+ variety +".csv")
        self.variety = variety

    def threshold_temp_min(t):
        "return the min acceptable value at t"
        nb_days = self.caracteristics["nb_days"]
        if self.variety == "tomato":
            if nb_days <= 7 : # "germination" time
                x = 28
            elif nb_days > 7 and t <= 21 : # "croissance" time
                if t(2)<23 and t(2)>5 : #day
                    x = 26
                else : # night
                    x = 19
            elif nb_days > 21 and t <= 51:# "floraison" Time
                if t(2)<19 and t(2)>7 : #day
                    x = 26
                else : # night
                    x = 19
            elif nb_days > 51 : # "fructification" time
                if t(2)<19 and t(2)>7 : #day
                    x = 26
                else : # night
                    x = 19
        else:        #limit case (no climate recipe)
            x = -1
        return x

    def threshold_temp_max(t):
        """return the max acceptable value at t"""
        nb_days = self.caracteristics["nb_days"]
        if self.variety == "tomato":
            if nbdys <= 7 : # "germination" time
               x = 28
            elif nb_days > 7 and t <= 21 : # "croissance" time
                if t(2)<23 and t(2)>5 : #day
                    x = 26
                else : # night
                    x = 19
            elif nb_days > 21 and t <= 51: # "floraison" Time
                if t(2)<19 and t(2)>7 : #day
                    x = 26
                else : # night
                    x = 19
            elif nb_days > 51 : # "fructification" time
                if t(2)<19 and t(2)>7 : #day
                    x = 26
                else : # night
                    x = 19
        else :         #limit case (no climate recipe)
            x = -1
        return x


    def thresholdd_humidity(t):
        """return the average value needed at t"""
        if self.variety == "tomato":
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

    def LEDupBoundary(t):
        #return the hour when LEDs should be turned off
        if self.variety == "tomato":
            if t <= 21 : # "growth" time
                x = 23
            elif t > 21 : # "bloom" time
                x = 19
        else :         #limit case (no climate recipe)
            x = -1
        return x

    def LEDdownBoundary(t):
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

    def floraMicro(i):
        """return the number of ml of this nutrient for week i according to climate recipe"""


    def floraGro(i):
        """return the number of ml of this nutrient for week i according to climate recipe"""

    def floraBloom(i):
        """return the number of ml of this nutrient for week i according to climate recipe"""



    ########## Watering Module #########################

    def watering_first_cycle(t):

        nb_days = self.caracteristics["nb_days"]

        if nb_days <= 21 :
            #bool = lectrique
            bool = True
        elif nb_days > 21 :
            bool = False
        return bool

    def WAR_ON_FIRST():
        return 0.75

    def WAR_OFF_FIRST():
        return 52.5

    def WAR_ON_SECOND():
        return 1.5

    def WAR_OFF_SECOND():
        return 50
