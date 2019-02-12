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
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
class Climate_recipe:

    CR_folder = "Files/climate_recipes/"

    def __init__(self,variety):
        self.caracteristics = CSV_reader(Climate_recipe.CR_folder+"caracteristics.csv").get_infos(variety)
        self.thresholds = CSV_reader(Climate_recipe.CR_folder +variety+ "/" +"thresholds.csv")
        self.nutrients = CSV_reader(Climate_recipe.CR_folder +variety+ "/" +"nutrients.csv")
        self.variety = variety

    def get_period(self,day):
        """return current period according to day"""
        period = "germination"
        for p in list("growth","flowering","fructification"):
            if self.caracteristic[p]<=day:
                period = p
            else:
                break

    def get_cycle(self,hour,day):
        """return day or night according to hour"""
        period = self.get_period(day)
        if hour >= self.thresholds.get(period+"_day","hour") and hour <= self.thresholds.get(period+"_day","hour"):
             return("day")
        else:
            return("night")

    def threshold_temp_min(self,hour,day):
        """return the min acceptable value at t"""
        period = self.get_period(day) + "_" + self.get_cycle(hour)
        return(self.thresholds.get(period,"temp"))


    def threshold_temp_max(self):
        """return the max acceptable value at t"""
        return(12)


    def thresholdd_humidity(self,hour,day):
        """return the average value needed at t"""
        period = self.get_period(day) + "_" + self.get_cycle(hour)
        return(self.thresholds.get(period,"humidity"))



    ####### Functions for Lighting module ##########################

    def LEDupBoundary(self):
        """return the hour when LEDs should be turned off"""
        return(self.caracteristics["hour_day"])

    def LEDdownBoundary(t):
        """return the hour when LEDs should be turned on"""
        return(self.caracteristics["hour_night"])


    ############### Functions for Nutrients Module ######################

    def floraMicro(i):
        """return the quantity in ml of this nutrient for week i according to climate recipe"""
        return(self.nutrients.get(i,"micro"))

    def floraGro(i):
        """return the number of ml of this nutrient for week i according to climate recipe"""
        return(self.nutrients.get(i,"gro"))

    def floraBloom(i):
        """return the number of ml of this nutrient for week i according to climate recipe"""
        return(self.nutrients.get(i,"bloom"))



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
