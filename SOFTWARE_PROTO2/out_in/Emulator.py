#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
from reads import *
pin_list = (11,13,15,16,18,22,29,31,32,33,35,36,40)
# faire fichier pour dictionnaire pin-nomActionneur
nbPins = len(pin_list)

class Interface :

    pin_dict = read_pins_dict("../Files/pins.txt")

    def __init__(self) :
        self.activated_pins = [] #list of pins which are activate (hardware ON)
        self.pins = [False]*nbPins #list of state by pin

    def verif_pin(self,pin,activate):
        """this function check error on pin activation
        take a pin and a bool indicating the info to communicate"""
        if(pin not in pin_dict.values()):
            raise PinExeption("Pin {} doesn't exist".format(pin))
            return(false)
        elif(activate and pin in self.activated_pins):
            raise ActivateExeption("Pin {} already activated".format(pin))
            return(false)
        elif(not activate and pin not in self.activated_pins):
            raise ActivateExeption("Pin {} not activated".format(pin))
            return(false)
        else:
            return(True)

    def activate(self,*pins):
        for pin in pins:
            if verif_pin(pin,True):
                self.activated_pins.append(pin)
                self.pins[pin]=True

    def desactivate(self,*pins):
        for pin in pins:
            if verif_pin(pin,False):
                self.activated_pins.remove(pin)
                self.pins[pins]=False

    #def output(pin,val):
    #    if verif_pin(pin):
    #        self.pins[pin]=val

    def input(pin):
        return(12)

    def cleanup():
        for pin in activated_pins:
            desactivate(pin)
