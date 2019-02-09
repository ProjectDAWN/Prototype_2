#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
from . import Reads

class Interface :


    def __init__(self,pin_file,realMode=True) :
        self.actuators = Reads.Actuators(pin_file) #instantiation of the actuators manager class
        self.activated_pins = [] #list of pins which are activate (hardware ON)
        self.pins_dict = dict(zip(self.actuators.get_pin_list(),[None]*self.actuators.nbPins)) #dict of state by pin
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
        elif(activate and pin in self.activated_pins):
            print("Pin {} already activated".format(pin))
            return(False)
        elif(not activate and pin not in self.activated_pins):
            print("Pin {} not activated".format(pin))
            return(False)
        else:
            return(True)

    def activate(self,*actuators):
        """Given pins or actuators,
        check if the activation is possible and activate it"""
        for pin in actuators: #actuators is a list of string representing actuators
            if(not isinstance(pin,int)):
                pin = self.actuators.get_pin(pin) # allow to the user (main) to choose between pin or actuator name
            if self.verif_pin(pin,True):
                self.activated_pins.append(pin)
                self.pins_dict[pin]=True
                if(self.realMode):
                    GPIO.setup(pin, GPIO.OUT)
                    GPIO.output(pin, GPIO.HIGH)

    def desactivate(self,*actuators):
        """Given pins or actuators,
        check if the desactivation is possible and desactivate it"""
        for pin in actuators: #actuators is a list of string representing actuators
            if(not isinstance(pin,int)):
                pin = self.actuators.get_pin(pin) # allow to the user (main) to choose between pin or actuator name
            if self.verif_pin(pin,False):
                self.activated_pins.remove(pin)
                self.pins_dict[pin]=False
                if(self.realMode):
                    GPIO.cleanup(pin)

    def input(pin):
        return(12)

    def cleanup(self):
        for pin in self.activated_pins:
            self.desactivate(pin)

#In = Interface("../Files/Actuators.csv",False)
#In.activate("NUT_Mixer")

#In.activate(31)
#In.cleanup()
