import sys
path = sys.path[0]+"/../.."
sys.path.append(path)
from Raspberry_Interface.GPIO_Actuators import GPIO_Actuators
from Raspberry_Interface.GPIO_Sensors import GPIO_Sensors
pin_file = "../../Files/Actuators.csv"
InOutMode = "GPIO"
realMode = True
import time
InOut = GPIO_Actuators(pin_file,InOutMode,realMode)
sensors = GPIO_Sensors(InOutMode,realMode)

def test_pH():

	ph_value = sensors.read("pH")
	ph_max = 6.2
	count = 0
	temps = 0
	print("Début test pH")

	while ph_value > ph_max :

		print(ph_value,ph_max)

		InOut.activate("NUT_Pump_pHDown")
		print("pompe pH allumée")
		time.sleep(3)
		InOut.desactivate("NUT_Pump_pHDown")
		print("pompe pH éteinte")

		InOut.activate("WAR_Mixer")
		print("WAR_Mixer allumé")
		time.sleep(30)
		InOut.desactivate("NUT_Pump_pHDown")
		print("WAR_Mixer éteint")

		count = count + 1
		temps = count * 31
		print(temps)
	print (count)
	return count

test_pH()
