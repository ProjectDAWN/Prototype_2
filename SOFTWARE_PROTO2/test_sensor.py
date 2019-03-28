import sys
from Raspberry_Interface.GPIO_Sensors import GPIO_Sensors
realMode = False
sensors = GPIO_Sensors(realMode)

def test(sensor):
	sensors.read(sensor)