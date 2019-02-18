import matplotlib.pyplot as plt
import numpy as np
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

#def test(actuator1, actuator2):
	#values=[]

	#t = time.time()
	#t_empty = t + 60

	#print("Test sans actionneurs")
	#while time.time() < t_empty :
		#values.append(sensors.read("humidity"))
		#time.sleep(1)

	#InOut.activate(actuator1)
	#InOut.activate(actuator2)
	#print("Allumé")

	#t_act = time.time() + 600
	#print("Test avec actionneurs")
	#while time.time() < t_act :
		#values.append(sensors.read("humidity"))
		#time.sleep(1)

	#InOut.desactivate(actuator1)
	#InOut.desactivate(actuator2)
	#print("Eteint")

	#t_fin = time.time() + 1800
	#print("Test sans actionneurs")
	#while time.time() < t_fin :
		#values.append(sensors.read("humidity"))
		#time.sleep(1)

	#ti = np.linspace(0,len(values),len(values))
	#plt.figure()
	#plt.plot(ti,values,"k-")
	#plt.title("Evolution de l'humidité de l'air en fonction du temps")
	#plt.xlabel("Temps en seconde")
	#plt.ylabel("Humidité de l'air en %")
	#plt.grid()
	#plt.show()

#test("ATM_MistMaker","ATM_Ventilator")



def test(actuator1, actuator2):
	values=[]

# On commence à 62% d'humidité. D'après nos données,le module humidité fait +3%/min. 
# On veut donc arriver à 70% puis fluctuer autour de cette valeur.
# On allume donc 7min = 420.
	
	
	InOut.activate(actuator1)
	InOut.activate(actuator2)
	t_reach = time.time() + 200
	print("Test atteindre valeur")
	while time.time() < t_reach :
		values.append(sensors.read("humidity"))
		time.sleep(1)
		
		
	InOut.desactivate(actuator1)
	InOut.desactivate(actuator2)
	print("Eteint")
	t = time.time()
	t_OFF_1 = t + 120
	print("Test sans actionneurs")
	while time.time() < t_OFF_1 :
		values.append(sensors.read("humidity"))
		time.sleep(1)

		
	InOut.activate(actuator1)
	InOut.activate(actuator2)
	print("Allumé")
	t_ON_1 = time.time() + 10
	print("Test avec actionneurs")
	while time.time() < t_ON_1 :
		values.append(sensors.read("humidity"))
		time.sleep(1)

		
	InOut.desactivate(actuator1)
	InOut.desactivate(actuator2)
	print("Eteint")
	t = time.time()
	t_OFF_2 = t + 120
	print("Test sans actionneurs")
	while time.time() < t_OFF_2 :
		values.append(sensors.read("humidity"))
		time.sleep(1)

		
	InOut.activate(actuator1)
	InOut.activate(actuator2)
	print("Allumé")
	t_ON_2 = time.time() + 10
	print("Test avec actionneurs")
	while time.time() < t_ON_2 :
		values.append(sensors.read("humidity"))
		time.sleep(1)
		
		
	InOut.desactivate(actuator1)
	InOut.desactivate(actuator2)
	print("Eteint")	
	t = time.time()
	t_OFF_3 = t + 120
	print("Test sans actionneurs")
	while time.time() < t_OFF_3 :
		values.append(sensors.read("humidity"))
		time.sleep(1)

		
	InOut.activate(actuator1)
	InOut.activate(actuator2)
	print("Allumé")
	t_ON_3 = time.time() + 10
	print("Test avec actionneurs")
	while time.time() < t_ON_3 :
		values.append(sensors.read("humidity"))
		time.sleep(1)
		
		
	InOut.desactivate(actuator1)
	InOut.desactivate(actuator2)
	print("Eteint")
	t_fin = time.time() + 120
	print("Test sans actionneurs")
	while time.time() < t_fin :
		values.append(sensors.read("humidity"))
		time.sleep(1)

		
	ti = np.linspace(0,len(values),len(values))
	plt.figure()
	plt.plot(ti,values,"k-")
	plt.title("Evolution de l'humidité de l'air en fonction du temps")
	plt.xlabel("Temps en seconde")
	plt.ylabel("Humidité de l'air en %")
	plt.grid()
	plt.show()

test("ATM_MistMaker","ATM_Ventilator")

