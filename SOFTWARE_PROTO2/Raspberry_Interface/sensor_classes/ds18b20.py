import os
import glob
import time

class DS18B20:
    """Class for the ds18b20 sensor: Get the temperature of the water"""

    def __init__(self):
        """Initialize the class & establish connection with the sensor"""
        os.system('modprobe w1-gpio') #enable the raspberry to use the sensor
        os.system('modprobe w1-therm') #enable the raspberry to use the sensor
        self.base_dir = '/sys/bus/w1/devices/' #go to the right directory 
        self.device_folder = glob.glob(self.base_dir + '28*')[0]
        self.device_file = self.device_folder + '/w1_slave'
        
    def read_temp_raw(self):
        """Read all the information from the sensor"""
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    def get(self):
        """Get the temperature, it's in Celsius""" 
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
        return temp_c

    def read(self):
        """Print the value in terminal"""
        print("La température de l'eau est " +str(self.get()) +" °C")