import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
pin_file = path + "/Files/Actuators.csv"
InOutMode = "GPIO"
realMode = True
import time
InOut = GPIO_Actuators(pin_file,InOutMode,realMode)

def test(actuator):
	InOut.activate(actuator)
	print("Allumé")
	time.sleep(12)
	InOut.desactivate(actuator)
	print("Eteint")

test("NUT_Pump_BioGro")
