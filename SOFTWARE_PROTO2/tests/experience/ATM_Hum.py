import matplotlib.pyplot
import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
from Raspberry_Interface.GPIO_Actuators import GPIO_Sensors
pin_file = path + "/Files/Actuators.csv"
realMode = False
import time
InOut = GPIO_Actuators(pin_file,realMode)

def test(actuator1, actuator2):
	values=[]
	time = [xfor x in range(0,180,10)]
	InOut.activate(actuator1)
	InOut.activate(actuator2)
	print("Allumé")

	t = time.time()
	t_fin = time.time + 180

	while time.time() < t_fin :
		values.append(GPIO_Sensors.read("humidity"))
		time.sleep(10)

	InOut.desactivate(actuator1)
	InOut.desactivate(actuator1)
	print("Eteint")

	plot(Values, time)

test("ATM_MistMaker","ATM_Ventilator")
