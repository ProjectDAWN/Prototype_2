import sys
path = sys.path[0]+"/.."
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
	time.sleep(2)
	InOut.desactivate(actuator)
	print("Eteint")

test("NUT_Pump_Mato")
test("NUT_Pump_pHDown")
test("NUT_Pump_BioGro")
test("NUT_Pump_BioBloom")
test("NUT_Pump_Micro")
