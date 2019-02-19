import sys
path = sys.path[0]+"/.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Sensors import GPIO_Sensors
realMode = False
sensors = GPIO_Sensors(realMode)

def test(sensor):
	sensors.read(sensor)