import matplotlib.pyplot
import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
from Raspberry_Interface.GPIO_Sensors import GPIO_Sensors
pin_file = path + "/Files/Actuators.csv"
InOutMode = "GPIO"
realMode = False
import time
InOut = GPIO_Actuators(pin_file,InOutMode,realMode)
sensors = GPIO_Sensors(InOutMode,realMode)

def test(actuator):
	values=[]
	ti = [x for x in range(0,180,10)]
	InOut.activate(actuator)
	print("Allumé")

	t = time.time()
	t_fin = t + 180

	while time.time() < t_fin :
		values.append(sensors.read("pH"))
		time.sleep(10)

	InOut.desactivate(actuator)
	print("Eteint")

	plot(Values, ti)

test("ATM_Warmer")