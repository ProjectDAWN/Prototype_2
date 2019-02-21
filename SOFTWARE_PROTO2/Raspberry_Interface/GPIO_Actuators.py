#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import sys
sys.path.append(sys.path[0]+"/..")
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader

class GPIO_Actuators :


    def __init__(self,channel_file,InOutMode,realMode=True) :
        self.actuators = CSV_reader(channel_file) #instantiation of the actuators manager class
        self.activated_channels = [] #list of channels which are activate (hardware ON)
        self.nb_channels = self.actuators.nb_index
        self.channels_dict = dict(zip(self.actuators.get_list(InOutMode),[None]*self.nb_channels)) #dict of state by channel
        self.realMode = realMode
        self.InOutMode = InOutMode #determine which kind of channel the interface use


    def verif_channel(self,channel,activate):
        """this function check error on channel activation
        take a channel and a bool indicating the info to communicate"""

        if(channel not in self.channels_dict.keys()):
            print("{} {} doesn't exist".format(self.InOutMode,channel))
            return(False)
        #elif(activate and channel in self.activated_channels):
        #    print("Pin {} already activated".format(channel))
        #    return(False)
        #elif(not activate and channel not in self.activated_channels):
        #    print("Pin {} not activated".format(channel))
        #    return(False)
        else:
            return(True)

    def activate(self,*actuators):
        """Given channels or actuators,
        check if the activation is possible and activate it"""
        for actuator in actuators: #actuators is a list of string representing actuators
            channel = actuator
            if(not isinstance(channel,int)):
                channel = int(self.actuators.get(channel,self.InOutMode)) # allow to the user (main) to choose between channel or actuator name
            if self.verif_channel(channel,True):
                self.activated_channels.append(channel)
                self.channels_dict[channel]=True
                print("activation {} : {}".format(actuator,channel))
                if(self.realMode):
                    import RPi.GPIO as GPIO
                    print("realMode true")
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(channel, GPIO.OUT)
                    GPIO.output(channel, GPIO.HIGH)

    def desactivate(self,*actuators):
        """Given channels or actuators,
        check if the desactivation is possible and desactivate it"""
        for actuator in actuators: #actuators is a list of string representing actuators
            channel = actuator
            if(not isinstance(channel,int)):
                channel = int(self.actuators.get(actuator,self.InOutMode)) # allow to the user (main) to choose between channel or actuator name
            if self.verif_channel(channel,False):
                #self.activated_channels.remove(channel)
                self.channels_dict[channel]=False
                print("desactivation {} : {}".format(actuator,channel))
                if(self.realMode):
                    import RPi.GPIO as GPIO
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(channel, GPIO.OUT)
                    GPIO.cleanup(channel)


    def cleanup(self):
        for actuator in self.actuators.get_list(self.InOutMode):
            self.desactivate(actuator)

#In = GPIO_Actuators("../Files/Actuators.csv",False)
#In.activate("NUT_Mixer")

#In.activate(31)
#In.cleanup()
