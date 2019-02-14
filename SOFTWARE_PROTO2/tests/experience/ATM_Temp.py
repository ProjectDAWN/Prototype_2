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

def test(actuator):
	values=[]
	time = [xfor x in range(0,180,10)]
	InOut.activate(actuator)
	print("Allumé")

	t = time.time()
	t_fin = time.time + 180

	while time.time() < t_fin :
		values.append(GPIO_Sensors.read("pH"))
		time.sleep(10)

	InOut.desactivate(actuator)
	print("Eteint")

	plot(Values, time)

test("ATM_Warmer")
