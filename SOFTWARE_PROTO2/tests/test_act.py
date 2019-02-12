import sys
path = sys.path[0]+"/.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
pin_file = path + "/Files/Actuators.csv"
realMode = False
import time 
InOut = GPIO_Actuators(pin_file,realMode)

def test(actuator):
	InOut.activate(actuator)
	print("Allumé")
	time.sleep(5)
	InOut.desactivate(actuator)
	print("Eteint")