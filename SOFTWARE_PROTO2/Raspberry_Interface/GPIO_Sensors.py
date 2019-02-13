
import sys
sys.path.append(sys.path[0]+"/..")
sys.path.append(sys.path[0]+"/Raspberry_Interface")
from Data_Managers.Reads_Writes.CSV_reader import CSV_reader


class GPIO_Sensors :

    class_dict = dict.fromkeys(["pH","conductivity","waterlevel","water_temperature","temperature","humidity"])

    def __init__(self,InOutMode,realMode=True) :
        self.realMode = realMode
        if self.realMode:
            import RPi.GPIO as GPIO
            from sensor_classes.pH import pH
            from sensor_classes.EC import EC
            from sensor_classes.mcp3008 import MCP3008
            from sensor_classes.ds18b20 import DS18B20
            from sensor_classes.am2320_Humidity import AM2320_Humidity
            from sensor_classes.am2320_Temperature import AM2320_Temperature
            GPIO_Sensors.class_dict = {"pH" : pH(), "conductivity" : EC(), "waterlevel" : MCP3008(), "water_temperature" : DS18B20(),
            "temperature" : AM2320_Temperature(), "humidity" : AM2320_Temperature()}

            GPIO.setmode(GPIO.BCM)

    def verif_sensor(self,name):
        """this function check if the name exists
        take a name (str)"""

        if(name not in GPIO_Sensors.class_dict.keys()):
            print("sensor {} doesn't exist".format(name))
            return(False)
        else:
            return(True)

    def read(self,name_sensor):
        """Given name_sensor
        check if the reading is possible and get the value"""
        if self.verif_sensor(name_sensor):
            output = -1
            print("lecture {}".format(name_sensor))
            if(self.realMode):
                sensor_class = GPIO_Sensors.class_dict[name_sensor]
                output = sensor_class.read()

        return output

    def print(self,name_sensor):
        """Given name_sensor
        check if the reading is possible and print the value"""
        if self.verif_sensor(name_sensor):
            output =  -1
            print("lecture {}".format(name_sensor))
            if(self.realMode):
                sensor_class = GPIO_Sensors.class_dict[name_sensor]
                output = sensor_class.get()
                sensor_class.print()

        return output


#In = GPIO_Sensors("../Files/Actuators.csv",False)
#In.read("NUT_Mixer")

#In.read(11)
#In.cleanup()
