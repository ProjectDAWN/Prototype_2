#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import Reads

# faire fichier pour dictionnaire pin-nomActionneur

class Interface :

    Actuators = Reads.Actuators("../Files/Actuators.csv") #instantiation of the actuators manager class
    def __init__(self) :
        self.activated_pins = [] #list of pins which are activate (hardware ON)
        self.pins_dict = dict(zip(Interface.Actuators.get_pin_list(),[None]*Interface.Actuators.nbPins)) #dict of state by pin

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
        for pin in actuators: #actuators is a list of string representing actuators
            if(not isinstance(pin,int)):
                pin = Interface.Actuators.get_pin(act)
            if self.verif_pin(pin,True):
                self.activated_pins.append(pin)
                self.pins_dict[pin]=True

    def desactivate(self,*actuators):
        for pin in actuators: #actuators is a list of string representing actuators
            if(not isinstance(pin,int)):
                pin = Interface.Actuators.get_pin(pin)
            if self.verif_pin(pin,False):
                self.activated_pins.remove(pin)
                self.pins_dict[pin]=False

    #def output(pin,val):
    #    if verif_pin(pin):
    #        self.pins[pin]=val

    def input(pin):
        return(12)

    def cleanup(self):
        for pin in self.activated_pins:
            self.desactivate(pin)

In = Interface()
In.activate("NUT_Mixer")

In.activate("NUT_Pump_pHDown")
In.cleanup()
