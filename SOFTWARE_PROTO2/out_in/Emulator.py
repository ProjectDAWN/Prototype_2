#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import Reads
pin_list = (11,13,15,16,18,22,29,31,32,33,35,36,40)

# faire fichier pour dictionnaire pin-nomActionneur
nbPins = len(pin_list)

class Interface :

    Actuactors = Reads.Actuactors("../Files/Actuactors.csv")

    def __init__(self) :
        self.activated_pins = [] #list of pins which are activate (hardware ON)
        self.pins = [False]*nbPins #list of state by pin

    def verif_pin(self,pin,activate):
        """this function check error on pin activation
        take a pin and a bool indicating the info to communicate"""
        if(pin not in pin_list):
            raise PinExeption("Pin {} doesn't exist".format(pin))
            return(False)
        elif(activate and pin in self.activated_pins):
            raise ActivateExeption("Pin {} already activated".format(pin))
            return(False)
        elif(not activate and pin not in self.activated_pins):
            raise ActivateExeption("Pin {} not activated".format(pin))
            return(False)
        else:
            return(True)

    def activate(self,*actuators):
        for act in actuators:
            pin = Actuactors.pin(act)
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
