import matplotlib.pyplot as plt 
import nummpy as np
import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
from Raspberry_Interface.GPIO_Sensors import GPIO_Sensors
pin_file = path + "/Files/Actuators.csv"
InOutMode = "GPIO"
realMode = True
import time
InOut = GPIO_Actuators(pin_file,InOutMode,realMode)
sensors = GPIO_Sensors(InOutMode,realMode)

def test(actuator):
	values=[]

	t = time.time()
	t_empty = t + 60

	print("Test sans actionneurs")
	while time.time() < t_empty :
		values.append(sensors.read("temperature"))
		time.sleep(1)

	InOut.activate(actuator)
	print("Allumé")

	t_fin = time.time() + 180
	print("Test avec actionneurs")
	while time.time() < t_fin :
		values.append(sensors.read("temperature"))
		time.sleep(1)

	InOut.desactivate(actuator)
	print("Eteint")

	ti = np.linspace(0,len(values),len(values))
	plt.grid()
	plt.plot(ti,values)
	plt.show()

test("ATM_Warmer")
