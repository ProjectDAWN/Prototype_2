
import sys
sys.path.append(sys.path[0]+"/..")
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
from sensor_classes import *

class GPIO_Sensors :

    def __init__(self,pin_file,realMode=True) :
        self.sensors = CSV_reader(pin_file) #instantiation of the actuators manager class
        self.nb_pins = self.actuators.nb_index
        self.pins_dict = dict(zip(self.sensors.get_list("pin"),[None]*self.nb_pins)) #dict of state by pin
        self.realMode = realMode
        if self.realMode:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)

    def verif_pin(self,pin,activate):
        """this function check error on pin activation
        take a pin and a bool indicating the info to communicate"""

        if(pin not in self.pins_dict.keys()):
            print("Pin {} doesn't exist".format(pin))
            return(False)
        else:
            return(True)

    def read(self,pin):
        """Given pins or sensor,
        check if the activation is possible and activate it"""
        for pin in actuators: #actuators is a list of string representing actuators
            if(not isinstance(pin,int)):
                pin = self.sensors.get(pin,"pin") # allow to the user (main) to choose between pin or actuator name
            if self.verif_pin(pin,True):
                self.pins_dict[pin]=-1
                if(self.realMode):
                    self.pins_dict[pin]=-1

In = GPIO_Sensors("../Files/Actuators.csv",False)
In.read("NUT_Mixer")

In.read(11)
In.cleanup()
