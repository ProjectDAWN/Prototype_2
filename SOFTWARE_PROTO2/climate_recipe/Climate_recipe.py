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
        for p in ["growth","flowering","fructification"]:
            if self.caracteristics[p]<=day:
                period = p
            else:
                break
        return(period)

    def get_cycle(self,hour,day):
        """return day or night according to hour"""
        period = self.get_period(day)
        if hour >= self.thresholds.get(period+"_day","hour") and hour <= self.thresholds.get(period+"_day","hour"):
             return("day")
        else:
            return("night")

    def threshold_temp(self,hour,day):
        """return the acceptable value at t"""
        period = self.get_period(day) + "_" + self.get_cycle(hour,day)
        return(self.thresholds.get(period,"temp"))

    def thresholdd_humidity(self,hour,day):
        """return the average value needed at t"""
        period = self.get_period(day) + "_" + self.get_cycle(hour,day)
        return(self.thresholds.get(period,"humidity"))



    ####### Functions for Lighting module ##########################

    def LEDupBoundary(self,day):
        """return the hour when LEDs should be turned off"""
        period = self.get_period(day) + "_night"
        return(self.thresholds.get(period,"hour"))

    def LEDdownBoundary(self,day):
        """return the hour when LEDs should be turned on"""
        period = self.get_period(day)+"_day"
        return(self.thresholds.get(period,"hour"))


    ############### Functions for Nutrients Module ######################

    def floraMicro(self,day):
        """return the quantity in ml of this nutrient according to climate recipe"""
        week = day//7+1
        return(self.nutrients.get(week,"micro"))

    def floraGro(self,day):
        """return the number of ml of this nutrient according to climate recipe"""
        week = day//7+1
        return(self.nutrients.get(week,"gro"))

    def floraBloom(self,day):
        """return the number of ml of this nutrient according to climate recipe"""
        week = day//7+1
        return(self.nutrients.get(week,"bloom"))


    ########## Functions for Watering Module #########################

    def pH_max(self):
        "returns the value of the minimumu value for pH"
        return(self.caracteristics.get("pH_up"))


    def ON_time(self,day):
        period = self.get_period(day) + "_day"
        return(self.thresholds.get(period,"ON"))


    def OFF_time(self,day):
        period = self.get_period(day) + "_day"
        return(self.thresholds.get(period,"OFF"))
