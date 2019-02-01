#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
pin_list = (11,13,15,16,18,22,29,31,32,33,35,36,40)
# faire fichier pour dictionnaire pin-nomActionneur
nbPins = len(pin_list)

class Interface :

    def __init__(self) :
        self.activated_pins = [] #list of pins which are activate (hardware ON)
        self.pins = [None]*nbPins #list of state by pin

    def verif_pin(pin):
        return(pin in pin_list)

    def activate(self,*pins,init=None):
        for pin in pins:
            if verif_pin(pin):
                if pin not in self.activated_pins:
                    self.activated_pins.append(pin)
                    self.pins[pin]=init
                else:
                    raise ActivateExeption("Pin {} already activated".format(pin))
            else:
                raise PinExeption("Pin {} doesn't exist".format(pin))

    def desactivate(pin):
        if verif_pin(pin):
            self.pins[pins]=None
            self.activated_pins.remove(pin)

    def output(pin,val):
        if verif_pin(pin):
            self.pins[pin]=val

    def input(pin):
        return(12)

    def cleanup():
        for pin in activated_pins:
            desactivate(pin)
