#  Python 2.7
#  Raspberry_GPIO.py
#  SOFTWARE_PROTO2
#  V1.0
#  DAWN
import sys
sys.path.append(sys.path[0] + "/..")
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader
print = partial(print,flush=True)

class GPIO_Actuators :

    """Actuators manager class

    allow to activate/desactivate any actuator given its name,pin,gpio,relay number
    check if any problem can occur during these actions

    """

    def __init__(self,channel_file,inOut_mode,real_mode=True) :
        """Constructor of Actuator class

        Keyword Arguments:
        channel_file -- [string] name-chanel correspondance file to read
        inOut_mode -- [string] chanel mode used to communicate with the actuator
        real_mode -- [boolean] indicate if the code is executed on the Raspberry(True by default) or just for test on computer(False)

        """
        self.actuators = CSV_reader(channel_file) #instantiation of the actuators file reader class
        self.activated_channels = [] #list of channels which are activate (hardware ON)
        self.nb_channels = self.actuators.nb_index
        self.channels_dict = dict(zip(self.actuators.get_list(inOut_mode),
                                        [None] * self.nb_channels)) #dict of state by channel
        self.real_mode = real_mode
        self.inOut_mode = inOut_mode


    def verif_channel(self,channel,activate):
        """Check error on channel activation

        Keyword Arguments:
        channel -- [int] channel which is willing to be (des)activate
        activate -- [boolean] indicate if it is for an activation or not

        """

        if(channel not in self.channels_dict.keys()):
            print("{} {} doesn't exist".format(self.inOut_mode,channel))
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
        """Activate the given(s) actuators after verifications

        Arguments:
        actuators -- [string or int] actuator names or chanel to activate

        """
        for actuator in actuators: #actuators is a list of string representing actuators
            channel = actuator
            if(not isinstance(channel,int)):
                channel = int(self.actuators.get(channel,self.inOut_mode)) # allow to the user (main) to choose between channel or actuator name
            if self.verif_channel(channel,True):
                #self.activated_channels.append(channel)
                self.channels_dict[channel]=True
                print("activation {} : {}".format(actuator,channel))
                if(self.real_mode):
                    import RPi.GPIO as GPIO
                    print("real_mode true")
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(channel, GPIO.OUT)
                    GPIO.output(channel, GPIO.HIGH)

    def desactivate(self,*actuators):
        """Desactivate the given(s) actuators after verifications

        Arguments:
        actuators -- [string or int] actuator names or chanel to activate

        """
        for actuator in actuators: #actuators is a list of string representing actuators
            channel = actuator
            if(not isinstance(channel,int)):
                channel = int(self.actuators.get(actuator,self.inOut_mode)) # allow to the user (main) to choose between channel or actuator name
            if self.verif_channel(channel,False):
                #self.activated_channels.remove(channel)
                self.channels_dict[channel]=False
                print("desactivation {} : {}".format(actuator,channel))
                if(self.real_mode):
                    import RPi.GPIO as GPIO
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setup(channel, GPIO.OUT)
                    GPIO.cleanup(channel)


    def cleanup(self):
        """Desactivate every actuators without verification"""
        for actuator in self.actuators.get_list(self.inOut_mode):
            self.desactivate(actuator)

#In = GPIO_Actuators("../Files/Actuators.csv",False)
#In.activate("NUT_Mixer")

#In.activate(31)
#In.cleanup()
