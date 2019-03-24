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
import sys

class Climate_recipe:

    """climate recipe manager

    Access to the system datas and calculate the values needed
    to run the main programs
    """

    CR_folder = "Files/climate_recipes/"

    def __init__(self,variety,model):
        """Constructor of Climate_recipe class

        Keyword Arguments:
        variety -- [string] name of the variety to grow
        model -- [string] version of the greenhouse used

        """
        self.caracteristics = CSV_reader(Climate_recipe.CR_folder + \
                                        "caracteristics.csv").get_infos(variety) # dict of caracteristics
        self.thresholds = CSV_reader(Climate_recipe.CR_folder + \
                                    variety + "/thresholds.csv")
        self.nutrients = CSV_reader(Climate_recipe.CR_folder + \
                                    variety + "/nutrients.csv")
        self.system = CSV_reader("Files/system.csv").get_infos(model)

    def get_period(self,day):
        """Return current period according to day

        Keyword Arguments:
        day -- [int] current day of growth

        """
        period = "germination"
        for p in ["growth","flowering","fructification"]:
            if self.caracteristics[p] <= day:
                period = p
            else:
                break
        return(period)

    def get_cycle(self,hour,day):
        """Return "day" or "night" according to hour

        Keyword Arguments:
        hour -- [int] current hour of the day
        day -- [int] current day of growth

        """
        period = self.get_period(day)
        if hour >= self.thresholds.get(period + "_day","hour") and hour <= self.thresholds.get(period + "_day","hour"):
             return("day")
        else:
            return("night")

    def threshold_temp(self,hour,day):
        """Return the acceptable value of temperature

        Keyword Arguments:
        hour -- [int] current hour of the day
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_" + self.get_cycle(hour,day)
        return(self.thresholds.get(period,"temp"))

    def thresholdd_humidity(self,hour,day):
        """Return the acceptable value of humidity

        Keyword Arguments:
        hour -- [int] current hour of the day
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_" + self.get_cycle(hour,day)
        return(self.thresholds.get(period,"humidity"))



    ####### Functions for Lighting module ##########################

    def LEDupBoundary(self,day):
        """Return the hour when LEDs should be turned off

        Arguments:
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_night"
        return(self.thresholds.get(period,"hour"))

    def LEDdownBoundary(self,day):
        """Return the hour when LEDs should be turned on

        Arguments:
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_day"
        return(self.thresholds.get(period,"hour"))


    ############### Functions for Nutrients Module ######################
    def flow_coef(self,pump,water_level):
        """Return the coef in s/ml of a pump

        Arguments:
        pump -- [string] name of the pump
        water_level -- [int] water level in the big box (in mm)

        """
        size_tank_x = self.system["size_tank_x"]
        size_tank_y = self.system["size_tank_y"] #cm
        flow = self.system["flux_NUT_Pump_" + pump] #pump's flow ml/s
        volume = size_tank_x * size_tank_y * water_level / 10000
        coef = volume / flow
        return(coef)

    def pump_nut_time(self,nutrient,day,water_level):
        """return the time (in s) that a pump need to be activated

        Arguments:
        nutrient -- [string] nutrient to dispense
        day -- [int] current day of growth
        water_level -- [int] water level in the big box (in mm)

        """
        week = day // 7 + 1
        quantity = self.nutrients.get(week,nutrient)
        coef = self.flow_coef(nutrient,water_level)
        time = quantity * coef
        return(min(25,time))
    ########## Functions for Watering Module #########################

    def pH_max(self):
        """Returns the the maximum acceptable pH value"""
        return(self.caracteristics.get("pH_up"))


    def ON_time(self,day):
        """Return the time of

        Arguments:
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_day"
        return(self.thresholds.get(period,"ON"))


    def OFF_time(self,day):
        """Return the time of

        Arguments:
        day -- [int] current day of growth

        """
        period = self.get_period(day) + "_day"
        return(self.thresholds.get(period,"OFF"))

    def time_pH_regulation(self):
        """Return the time that pH pump is activated to regulate
        pH discretely """
        return(self.system["time_pH_regulation"])

    def time_temp_regulation(self):
        """Return the time that ATM system is activated to regulate
        temperature discretely """
        return(self.system[time_temp_regulation])
