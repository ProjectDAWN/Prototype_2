#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
nbPins = 30

class Interface :

    def __init__(self) :
        self.activated_pins = []
        self.pins = [None]*nbPins

    def verif_pin(pin):

    def activate(self,pin,init=None):
        if pin>=0 and pin<nbPins:
            if pin not in self.activated_pins:
                self.activated_pins.append(pin)
                self.pins[pin]=init
                
            else:
                raise ActivateExeption("Pin {} already activated".format(pin))
        else:
            raise PinExeption("Pin {} doesn't exist".format(pin))
methClasse = classmethod(methClass)




def desactivate(pin):





def input(pin):
    return()

def cleanup():
    for pin in activated_pins:
        desactivate(pin)
