#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import sys
sys.path.append(sys.path[0]+"/..")
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
import RPi.GPIO as GPIO

class GPIO_Actuators :


    def __init__(self,chanel_file,InOutMode,realMode=True) :
        self.actuators = CSV_reader(chanel_file) #instantiation of the actuators manager class
        self.activated_chanels = [] #list of chanels which are activate (hardware ON)
        self.nb_chanels = self.actuators.nb_index
        self.chanels_dict = dict(zip(self.actuators.get_list("GPIO"),[None]*self.nb_chanels)) #dict of state by chanel
        self.realMode = realMode
        self.InOutMode = InOutMode
        if realMode:
            GPIO.setmode(GPIO.BCM)
            print("GPIO imported")

    def verif_chanel(self,chanel,activate):
        """this function check error on chanel activation
        take a chanel and a bool indicating the info to communicate"""

        if(chanel not in self.chanels_dict.keys()):
            print("Pin {} doesn't exist".format(chanel))
            return(False)
        elif(activate and chanel in self.activated_chanels):
            print("Pin {} already activated".format(chanel))
            return(False)
        elif(not activate and chanel not in self.activated_chanels):
            print("Pin {} not activated".format(chanel))
            return(False)
        else:
            return(True)

    def activate(self,*actuators):
        """Given chanels or actuators,
        check if the activation is possible and activate it"""
        for chanel in actuators: #actuators is a list of string representing actuators
            if(not isinstance(chanel,int)):
                chanel = int(self.actuators.get(chanel,self.InOutMode)) # allow to the user (main) to choose between chanel or actuator name
            if self.verif_chanel(chanel,True):
                self.activated_chanels.append(chanel)
                self.chanels_dict[chanel]=True
                print("activation {}".format(chanel))
                if(self.realMode):
                    GPIO.setup(chanel, GPIO.OUT)
                    GPIO.output(chanel, GPIO.HIGH)

    def desactivate(self,*actuators):
        """Given chanels or actuators,
        check if the desactivation is possible and desactivate it"""
        for chanel in actuators: #actuators is a list of string representing actuators
            if(not isinstance(chanel,int)):
                chanel = int(self.actuators.get(chanel,self.InOutMode)) # allow to the user (main) to choose between chanel or actuator name
            if self.verif_chanel(chanel,False):
                self.activated_chanels.remove(chanel)
                self.chanels_dict[chanel]=False
                print("desactivation {}".format(chanel))
                if(self.realMode):
                    GPIO.setup(chanel, GPIO.OUT)
                    GPIO.cleanup(chanel)


    def cleanup(self):
        for chanel in self.activated_chanels:
            self.desactivate(chanel)

#In = GPIO_Actuators("../Files/Actuators.csv",False)
#In.activate("NUT_Mixer")

#In.activate(31)
#In.cleanup()
